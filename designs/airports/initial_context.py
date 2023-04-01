from nautobot.tenancy.models import Tenant

from design_builder.context import Context, context_file

from os import path
import csv
import string

def printable(value):
    return "".join(filter(lambda x: x in string.printable, value))

def read_csv(filename):
        with open(path.join(path.dirname(__file__), "data", filename)) as file:
            reader = csv.DictReader(file)
            for row in reader:
                yield row

def countries():
    countries = {}
    for row in read_csv("iso_countries.csv"):
        countries[row["alpha-2"]] = printable(row["name"])
    return countries

def regions():
    regions = {}
    for row in read_csv("iso_regions.csv"):
        regions[row["code"]] = printable(row["name"])
    return regions

@context_file("initial_context.yaml")
class InitialDesignContext(Context):
    """Render context for basic design"""

    country : str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.continents = {}
        self.sites = {}
        self._region_names = {}

        self.iso_countries = countries()
        self.iso_regions = regions()

        self.tenant_group_map = {}
        for group_slug, tenant_group in self["tenant_groups"]["airports"]["children"].items():
            for tenant_slug in tenant_group["tenants"].keys():
                tenant_slug = tenant_slug.replace("-", "_")
                self.tenant_group_map[tenant_slug] = group_slug
        
        for row in read_csv("airport-codes.csv"):
            if row['iso_country'] == self.country:
                if row['continent'] == "AS":
                    continue
                self.add_airport(row)
        


    def add_airport(self, row):
        path = ["continent", "iso_country", "iso_region", "ident"]
        for p in path:
            if not row[p]:
                return
        
        self.add_continent(row)
    
    def add_continent(self, row):
        name = self.continent_names[row["continent"]]
        slug = f"continent-{row['continent'].lower()}"
        if slug not in self.continents:
            if name in self._region_names:
                return
            self._region_names[name] = "continent"
            self.continents[slug] = {
                "name": name,
                "slug": slug,
                "countries": {}
            }
        self.add_country(self.continents[slug], row)

    def add_country(self, continent, row):
        name = self.iso_countries.get(row["iso_country"], None)
        slug = f"country-{row['iso_country'].lower()}"

        if name is None:
            return
        
        if slug not in continent["countries"]:
            if name in self._region_names:
                return

            self._region_names[name] = "country"
            continent["countries"][slug] = {
                "name": name,
                "slug": slug,
                "regions": {},
            }
        self.add_region(continent["countries"][slug], row)

    def add_region(self, country, row):
        name = self.iso_regions.get(row["iso_region"], None)
        slug = f"region-{row['iso_region'].lower()}"

        if name is None:
            return
        
        if slug not in country["regions"]:
            if name in self._region_names:
                typ = self._region_names[name]
                return

            self._region_names[name] = "region"
            country["regions"][slug] = {
                "name": name,
                "slug": slug,
                "sites": {},
            }
        self.add_site(country["regions"][slug], row)

    def add_site(self, region, row):
        name = f"{row['ident']} - {printable(row['name'])}"
        slug = printable(row["ident"]).lower()

        if slug not in region["sites"]:
            if slug in self.sites:
                return
            
            region["sites"][slug] = {
                "name": name,
                "slug": slug,
                "tenant__slug": self.tenant_group_map[row["type"]],
                "region__slug": region["slug"]
            }
            self.sites[slug] = region["sites"][slug]

class TenantFilterContext(InitialDesignContext):
    tenant : Tenant
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sites = {k: v for k,v in self.sites.items() if v["tenant__slug"] == self.tenant.slug}
