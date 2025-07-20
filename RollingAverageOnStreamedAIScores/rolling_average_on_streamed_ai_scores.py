import random
import time
from collections import defaultdict, deque

patient_scores = defaultdict(lambda: deque(maxlen=5))

patient_ids = ["P1", "P2", "P3", "P4"]


def update_score(patient_id: str, new_score: float) -> float:
    patient_scores[patient_id].append(new_score)
    return sum(patient_scores[patient_id]) / len(patient_scores[patient_id])


def simulate_stream(iterations=20, delay=1.0):
    for _ in range(iterations):
        patient_id = random.choice(patient_ids)
        new_score = round(random.uniform(0.1, 0.99), 2)

        avg = update_score(patient_id, new_score)
        print(f"patient ID {patient_id} | new score: {new_score} | Rolling average (last 5) : {avg:.2f}")
        time.sleep(delay)


if __name__ == '__main__':
    simulate_stream()
