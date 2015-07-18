import os

basepath = os.path.abspath(os.path.dirname(__file__) + "/..")
json_path = basepath + "/fixtures/initial_data.json"

with open(json_path, "w") as json_file:
    json_file.replace('crn', 'CRN')
    json_file.replace('"note":null', '"note":""') # not sure about this one
    json_file.replace('"graduate_level":null', '"graduate_level": False')
    json_file.replace('"graduate_level":"Y"', '"graduate_level": True') # this should be the other one
    json_file.replace('"year_long":"N', '"year_long": False')
    json_file.replace('"year_long":"Y', '"year_long": True')


