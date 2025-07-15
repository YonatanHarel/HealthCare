# Patient Scan Frequency Tracker
### Prompt:
You receive logs of:

```python
[{"patient_id": "P1", "scan_time": "2025-07-13T10:00:00Z"}, ...]
```

Write a function to:
* Return the top 3 patients with the most scans
* Output scan frequency per patient as {id: count}