import csv
import json
CSV_ADS = "datasets/ads.csv"
JSON_ADS = "datasets/ads.json"
CSV_CATEGORIES = "datasets/categories.csv"
JSON_CATEGORIES = "datasets/categories.json"
def convert_file(csv_file, model_name, json_file) -> None:
    result = []
    with open(csv_file, encoding='utf-8') as csv_file:
        if csv_file.name == "datasets/ads.csv":
            for row in csv.DictReader(csv_file):
                to_add = {"model": model_name, "pk": int(row["Id"]), "fields": row}
                del row["Id"]
                row["price"] = int(row["price"])
                if row["is_published"] == 'TRUE':
                    row["is_published"] = True
                else:
                    row["is_published"] = False
                result.append(to_add)
        elif csv_file.name == CSV_CATEGORIES:
            for row in csv.DictReader(csv_file):
                to_add = {"model": model_name, "pk": int(row["id"]), "fields": row}
                del row["id"]
                result.append(to_add)
    with open(json_file, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, indent=2, ensure_ascii=False)

print(convert_file(CSV_ADS, "ads.ad", JSON_ADS))
print(convert_file(CSV_CATEGORIES, "ads.categorie", JSON_CATEGORIES))