# Daily Summary Generator

<i>Given a CSV of scan results:</i>
```
patient_id,scan_time,ai_score
A1,2025-07-12T10:00:00Z,0.94
A2,2025-07-12T12:01:00Z,0.88
...
```

Write code to:
* Compute daily average ai_score
* Output result as a new CSV: day,avg_score