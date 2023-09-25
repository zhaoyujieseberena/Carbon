# %%
import csv
import json

def run_csv():
    csv_file = './res/papers.csv'  
    json_file = './res/papers.json'  

    data = []

    with open(csv_file, 'r', encoding='utf-8') as csvfile:

        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)


    json_data = json.dumps(data, ensure_ascii=False, indent=4)


    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json_data)

    csv_file = './res/metrics.csv'  
    json_file = './res/metrics.json'  

    data = []

    with open(csv_file, 'r', encoding='utf-8') as csvfile:

        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)


    json_data = json.dumps(data, ensure_ascii=False, indent=4)


    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json_data)
    csv_file = './res/datasets.csv'  
    json_file = './res/datasets.json'  

    data = []

    with open(csv_file, 'r', encoding='utf-8') as csvfile:

        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)


    json_data = json.dumps(data, ensure_ascii=False, indent=4)


    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json_data)




    csv_file = './res/tools.csv'  
    json_file = './res/tools.json'  

    data = []

    with open(csv_file, 'r', encoding='utf-8') as csvfile:

        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)


    json_data = json.dumps(data, ensure_ascii=False, indent=4)


    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(json_data)

    # %%



