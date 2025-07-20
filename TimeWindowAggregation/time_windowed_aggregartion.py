"""
1. convert to pandas
2. sort by time
3. for each patient, keep the first scan result within each 5-minutes window
"""
import json
from typing import List
import pandas as pd


def load_json_file(filepath: str):
    with open(filepath, "r", encoding='utf-8') as f:
        return json.load(f)


def windowed_aggregate(data_list: List[dict]):
    # convert to dataframe
    df = pd.DataFrame(data_list)

    # convert to datetime and sort by scan_time
    df['scan_time'] = pd.to_datetime(df['scan_time'])
    df = df.sort_values(by=['patient_id', 'scan_time'])

    # create 5-minute bins per patient
    df['window_start'] = df.groupby('patient_id')['scan_time'].transform(lambda x: x.dt.floor('5min'))

    # keep only the first scan per window
    rslts = df.groupby(['patient_id', 'window_start'], as_index=False).first()

    # remove helper column
    rslts = rslts.drop(columns='window_start')

    return rslts


if __name__ == '__main__':
    # data = [
    #     {"patient_id": 1, "scan_time": "2025-07-13T10:00:00Z", "ai_score": 0.95},
    #     {"patient_id": 1, "scan_time": "2025-07-13T10:02:00Z", "ai_score": 0.93},
    #     {"patient_id": 1, "scan_time": "2025-07-13T10:06:00Z", "ai_score": 0.80},
    #     {"patient_id": 2, "scan_time": "2025-07-13T10:01:00Z", "ai_score": 0.91},
    #     {"patient_id": 2, "scan_time": "2025-07-13T10:07:00Z", "ai_score": 0.89},
    # ]

    JSON_DATA_FILEPATH = 'patient_scan_records_constrained_1000.json'
    data = load_json_file(JSON_DATA_FILEPATH)
    results = windowed_aggregate(data)
    print(results)
