import csv
import string
from os import path

from design_builder.context import Context, context_file


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
