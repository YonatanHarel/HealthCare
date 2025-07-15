import statistics
from collections import deque


class AnomalyDetector:
    def __init__(self, window_size=20, threshold=2):
        self.window_size = window_size
        self.threshold = threshold
        self.history = deque(maxlen=window_size)

    def add_score(self, new_score: float):
        is_anomamly = False
        mean, std = None, None

        if len(self.history) >= 2:
            mean = statistics.mean(self.history)
            std = statistics.stdev(self.history)

            if std > 0 and abs(new_score - mean) > self.threshold * std:
                is_anomamly = True

        self.history.append(new_score)

        return {
            "new_score": new_score,
            "mean": mean,
            "std_dev": std,
            "is_anomaly": is_anomamly,
            "window": list(self.history)
        }


if __name__ == "__main__":
    detector = AnomalyDetector(window_size=5)
    stream = [0.80, 0.82, 0.79, 0.81, 0.83, 0.95, 0.84]

    for score in stream:
        result = detector.add_score(score)
        print(result)
