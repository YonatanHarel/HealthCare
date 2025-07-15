# Secure Logging Wrapper

### Create a Python decorator that wraps any data function and:

* Logs input/output
* Masks patient_id and scan_id values to just the last 4 characters

### Examples:
#### Logs input/output
```json
Input: {'patient_id': '1234567890', 'scan_id': 'ABCD123456'}
Output: {'result': 'something'}
```

#### Mask ```patient_id``` and ```scan_id```
Before logging the input/output, you must anonymize sensitive values.
Specifically:
* For 'patient_id': '1234567890', only show the last 4 digits → 'patient_id': '****7890'
* For 'scan_id': 'ABCD123456', → 'scan_id': '****3456'

The goal is to preserve privacy by masking all but the last 4 characters.