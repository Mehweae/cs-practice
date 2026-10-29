import csv
import json

def csv_to_records(text):
    reader = csv.reader(text.splitlines(), delimiter=',')
    return [dict(s) for s in reader]

