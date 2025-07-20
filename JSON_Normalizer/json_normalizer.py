import json
from pydantic import ValidationError
from JSON_Normalizer.models import ScanEntry


def load_json_from_file(filepath):
    with open(filepath, "r", encoding='utf-8') as f:
        return json.load(f)


def json_normalizer(data):
    # entries = [ScanEntry(**record) for record in data]
    # flattened = [flatten_entry(entry) for entry in entries]
    #
    # return flattened

    valid_entries_list = []
    errors_list = []

    for idx, item in enumerate(data):
        try:
            entry = ScanEntry(**item)
            valid_entries_list.append(flatten_entry(entry))
        except ValidationError as e:
            errors_list.append({
                "index": idx,
                "error": e.errors(),  # detailed error list
                "raw_data": item  # optional: include offending record
            })

    return valid_entries_list, errors_list


def flatten_entry(entry: ScanEntry) -> dict:
    return {
        "patient_id": entry.data.patient_id,
        "scan_id": entry.data.scan.scan_id,
        "score": entry.data.scan.ai_result.score,
        "label": entry.data.scan.ai_result.label
    }


if __name__ == '__main__':
    FILEPATH = 'expanded_nested_scans.json'
    data = load_json_from_file(FILEPATH)
    valid_entries, errors = json_normalizer(data)
    print(f"we have {len(valid_entries)} valid entries")
    print(f"we have {len(errors)} invalid entries")
