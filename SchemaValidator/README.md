# Schema Validator

<i>Write a Python function that validates each row in a list of JSON scan results to:</i>

* Ensure patient_id is not null

* scan_time is in ISO format

* ai_score is between 0 and 1

Result: </br>
Raise an error if any row is invalid and print its index + error reason.