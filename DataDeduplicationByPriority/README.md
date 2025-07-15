# Data Deduplication by Priority


<i>You’re given incoming scan alerts for the same patient (can be duplicate due to retries):</i>
```
[
  {"patient_id": "A1", "scan_id": "S1", "priority": 3},
  {"patient_id": "A1", "scan_id": "S1", "priority": 1},
  {"patient_id": "A1", "scan_id": "S2", "priority": 2}
]
```
Write code to:
* Remove duplicate scan_id entries per patient
* Keep the one with highest priority (1 = highest)