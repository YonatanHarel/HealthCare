from collections import Counter


def get_scan_frequency(logs):
    counter = Counter(log["patient_id"] for log in logs)
    top_3 = counter.most_common(3)

    return {
        "frequencies": dict(counter),
        "top_3": dict(top_3)
    }


if __name__ == '__main__':
    logs = [
        {"patient_id": "P1", "scan_time": "2025-07-13T10:00:00Z"},
        {"patient_id": "P2", "scan_time": "2025-07-13T10:05:00Z"},
        {"patient_id": "P1", "scan_time": "2025-07-13T10:15:00Z"},
        {"patient_id": "P3", "scan_time": "2025-07-13T10:30:00Z"},
        {"patient_id": "P2", "scan_time": "2025-07-13T10:35:00Z"},
        {"patient_id": "P1", "scan_time": "2025-07-13T10:45:00Z"},
        {"patient_id": "P4", "scan_time": "2025-07-13T10:30:00Z"},
        {"patient_id": "P5", "scan_time": "2025-07-13T10:35:00Z"},
        {"patient_id": "P4", "scan_time": "2025-07-13T10:45:00Z"},
    ]

    result = get_scan_frequency(logs)
    print(result)