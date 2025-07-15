import json
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, ValidationError, field_validator
from pydantic_core._pydantic_core import PydanticCustomError


class DataSchema(BaseModel):
    patient_id: str = Field(..., min_length=1)
    scan_id: str = Field(..., min_length=1)
    scan_time: datetime
    ai_score: float = Field(..., gte=0, lt=1)

    # @field_validator('ai_score')
    # @classmethod
    # def validate_ai_score(cls, value: float) -> float:
    #     if value > 1:
    #         raise PydanticCustomError('ai score should be between 0 to 1.',
    #                                   f'current score is {value}')
    #     return value


def load_json_file(filepath: str):
    with open(filepath, "r", encoding='utf-8') as f:
        return json.load(f)


def schema_validator(events_json: List[dict]):
    valid_entries = []
    errors = []

    for key, value in enumerate(events_json):
        try:
            model = DataSchema(**value)
            valid_entries.append(model)
        except ValidationError as e:
            errors.append({
                "index": key,
                "record": value,
                "errors": e.errors()
            })
    return valid_entries, errors


if __name__ == '__main__':
    filepath = "patient_scan_records_constrained_1000.json"
    data = load_json_file(filepath)

    if not isinstance(data, list):
        raise ValueError("Input must be list of records")
    else:
        valid, invalid = schema_validator(data)

        print(f'valid records: {len(valid)}')
        print(f'invalid records: {len(invalid)}')

        if invalid:
            print("\n⚠️ Errors:")
            for err in invalid:
                print(f"\nRecord #{err['index']}:")
                print(json.dumps(err["errors"], indent=2, ensure_ascii=False))
