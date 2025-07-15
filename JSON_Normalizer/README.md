# JSON Normalizer

You get nested scan results from an AI model:

``` json
{
  "meta": {"model_version": "v1.3", "received_at": "..."},
  "data": {
    "patient_id": "P123",
    "scan": {
      "scan_id": "S100",
      "ai_result": {
        "score": 0.87,
        "label": "lvo_detected"
      }
    }
  }
}
```
Write Python code to flatten this into:
```json
{
  "patient_id": "P123",
  "scan_id": "S100",
  "score": 0.87,
  "label": "lvo_detected"
}
```


