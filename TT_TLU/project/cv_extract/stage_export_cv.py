import json
import csv
import os


def export_results(results):
    out_folder = "./output"
    os.makedirs(out_folder, exist_ok=True)

    # JSON
    json_path = os.path.join(out_folder, "cv_extracted.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    # CSV
    csv_path = os.path.join(out_folder, "cv_extracted.csv")
    keys = results[0].keys() if results else []

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(keys))
        writer.writeheader()
        writer.writerows(results)
