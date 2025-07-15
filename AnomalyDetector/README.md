# Anomaly Detector
### Prompt:
You get a stream of ai_score values. Write a function that:
* Tracks a rolling mean and std dev
* Flags any new value as an anomaly if it's more than 2 std dev away from the mean

</br>

# FAQ
## "Tracks a rolling mean and std dev"
### This means:
* You don’t compute the mean (average) and standard deviation (how spread out values are) on the whole history of data.
* Instead, you compute them on the last N values (e.g., last 20 or 50 scores).
* This rolling window slides forward as new values come in — just like how a moving average works.
* 
📦 Think of it like:
“From the most recent 20 scores, what's the average and standard deviation?”


## "Flags any new value as an anomaly if it's more than 2 std dev away from the mean"
### This means:
* You compare the new incoming score to the current rolling mean and standard deviation
* If it’s too far from the center, it’s considered unusual (an anomaly)

### 📏 Mathematically:
A value x is flagged if:
```python
abs(x - rolling_mean) > 2 * rolling_std
```
This uses a classic statistical rule (the 68–95–99.7 rule):
* In a normal distribution:
* ~68% of values fall within ±1 std dev
* ~95% within ±2 std dev
* ~99.7% within ±3 std dev

So, by using 2 std devs as a threshold, we flag things that are very rare under normal conditions.

## 📊 Example
Last 20 ai_score values:

```python
[0.8, 0.82, 0.79, ..., 0.81]
```
* Rolling mean = 0.81
* Rolling std dev = 0.01

* Now a new score comes in:

```python
0.95
```

Check:
```python
abs(0.95 - 0.81) = 0.14
0.14 > 2 * 0.01 = 0.02 → ✅ anomaly
```

