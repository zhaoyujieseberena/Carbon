# %%
import csv
import json

csv_file = './res/papers.csv'  # 替换为您的CSV文件路径
json_file = './res/papers.json'  # 替换为您想要生成的JSON文件路径

data = []

with open(csv_file, 'r', encoding='utf-8') as csvfile:

    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        data.append(row)

# 3. 创建JSON对象
json_data = json.dumps(data, ensure_ascii=False, indent=4)

# 4. 将JSON对象写入文件
with open(json_file, 'w', encoding='utf-8') as jsonfile:
    jsonfile.write(json_data)



# %%


