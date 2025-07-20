import json
from datetime import datetime
from typing import List
from pydantic import BaseModel, ValidationError


class Record(BaseModel):
    patient_id: str
    scan_id: str
    scan_time: datetime
    ai_score: float


def load_json_file(filepath: str):
    with open(filepath, "r", encoding='utf-8') as f:
        return json.load(f)


def deduplicate(data_dict: List[dict]) -> List[dict]:
    deduplicated_dict = {}
    for _, record in enumerate(data_dict):
        try:
            model = Record(**record)
            exist_record = deduplicated_dict.get(model.patient_id, None)
            patiant_id = model.patient_id
            # compare scan_id
            if exist_record:
                new_patient_id_suffix = int(model.scan_id.split("_")[1])
                exist_patient_id_suffix = int(exist_record.scan_id.split("_")[1])
                if new_patient_id_suffix > exist_patient_id_suffix:
                    print(f"replacing patiant_id {patiant_id} with scan_id {exist_patient_id_suffix} to scan_id {new_patient_id_suffix}")
                    deduplicated_dict[patiant_id] = model
            # add new record
            else:
                deduplicated_dict[patiant_id] = model
        except ValidationError as e:
            print(f'Error handling patient_id {patiant_id}. \n error: {e}')

    return deduplicated_dict


if __name__ == '__main__':
    FILEPATH = "patient_scan_10.json"
    data = load_json_file(FILEPATH)

    if not isinstance(data, list):
        raise ValueError("Input must be list of records")
    deduplicated_result = deduplicate(data)
