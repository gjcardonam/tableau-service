import csv
import json


def CSV_to_JSON(CSV_file):
    json_Dict = []

    # read csv file
    with open(CSV_file, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            json_Dict.append(row)

        JSON_file = json.dumps(json_Dict)

    return JSON_file
