# Time-Windowed Aggregation

<i>You’re given a list of scan results:</i>

```
[
    {"patient_id": 1, "scan_time": "2025-07-13T10:00:00Z", "ai_score": 0.95},
    {"patient_id": 1, "scan_time": "2025-07-13T10:02:00Z", "ai_score": 0.93},
    ...
]
```

Write Python code (using pandas) to:</br>
* Convert to DataFrame
* Sort by time
* For each patient, keep only the <b>first scan result within each 5-minute window</b>

Follow-up: What if this needs to work as a stream?