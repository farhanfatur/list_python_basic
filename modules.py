# default module
# fdd quotation list
# fdd purchase to patyment fdd
###############################
# import datetime
from datetime import date
from time import time
import json
# take module from pip(package manager)
###############################
from camelcase import CamelCase
# use custom module
from validator import validate_email
# today = datetime.date.today()


today = date.today()
timestamp = time()

c = CamelCase()


if validate_email("farhanail.com"):
    print("Email is valid")
else:
    print("Email is bad")

# print(today)
# print(timestamp)
# print(c.hump("Farhan Fatur Rozzi"))