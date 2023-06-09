import csv
import json

CSV_ADS = "datasets/ad.csv"
JSON_ADS = "datasets/ad.json"
CSV_CATEGORIES = "datasets/category.csv"
JSON_CATEGORIES = "datasets/category.json"
CSV_LOCATION = 'datasets/location.csv'
JSON_LOCATION = 'datasets/location.json'
CSV_USER = "datasets/user.csv"
JSON_USER = 'datasets/user.json'


def convert_file(csv_file, model_name, json_file) -> None:
    result = []
    with open(csv_file, encoding='utf-8') as csv_file:
        if csv_file.name == CSV_ADS:
            for row in csv.DictReader(csv_file):
                to_add = {"model": model_name, "pk": int(row["Id"]), "fields": row}
                del row["Id"]
                row["price"] = int(row["price"])
                if row["is_published"] == 'TRUE':
                    row["is_published"] = True
                else:
                    row["is_published"] = False
                result.append(to_add)
            with open(json_file, 'w', encoding='utf-8') as json_file:
                json.dump(result, json_file, indent=2, ensure_ascii=False)
        elif csv_file.name == CSV_CATEGORIES:
            for row in csv.DictReader(csv_file):
                to_add = {"model": model_name, "pk": int(row["id"]), "fields": row}
                del row["id"]
                result.append(to_add)
            with open(json_file, 'w', encoding='utf-8') as json_file:
                json.dump(result, json_file, indent=2, ensure_ascii=False)
        elif csv_file.name == CSV_LOCATION:
            for row in csv.DictReader(csv_file):
                to_add = {
                    "model": model_name,
                    "pk": int(row["id"]),
                    "fields": row
                }
                row["lat"] = float(row["lat"])
                row["lng"] = float(row["lng"])
                del row["id"]
                result.append(to_add)
            with open(json_file, 'w', encoding='utf-8') as json_file:
                json.dump(result, json_file, indent=2, ensure_ascii=False)
        elif csv_file.name == CSV_USER:
            for row in csv.DictReader(csv_file):
                to_add = {
                    "model": model_name,
                    "pk": int(row["id"]),
                    "fields": row
                }
                row["age"] = int(row["age"])
                row["location_id"] = int(row["location_id"])
                del row["id"]
                result.append(to_add)
            with open(json_file, 'w', encoding='utf-8') as json_file:
                json.dump(result, json_file, indent=2, ensure_ascii=False)


print(convert_file(CSV_ADS, "ads.ad", JSON_ADS))
print(convert_file(CSV_CATEGORIES, "ads.category", JSON_CATEGORIES))
print(convert_file(CSV_LOCATION, "users.location", JSON_LOCATION))
print(convert_file(CSV_USER, "users.user", JSON_USER))
