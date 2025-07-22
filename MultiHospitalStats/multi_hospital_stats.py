import pandas as pd


def calculate_average_per_hospital(data):
    """
    calculates the average score per hospital and return results by score descending
    """
    df = pd.DataFrame.from_records(data)

    grouped_hospitals_avg = df.groupby(df['hospital'])['score'].mean().reset_index()
    avg_hospitals_sorted = grouped_hospitals_avg.sort_values(by='score', ascending=False)
    return avg_hospitals_sorted.set_index('hospital').to_dict(orient='index')


if __name__ == '__main__':
    INPUT = [
        {"hospital": "General Hospital", "score": 0.85},
        {"hospital": "Saint Mary", "score": 0.78},
        {"hospital": "General Hospital", "score": 0.90},
        {"hospital": "City Medical Center", "score": 0.72},
        {"hospital": "General Hospital", "score": 0.80},
        {"hospital": "Saint Mary", "score": 0.88},
        {"hospital": "City Medical Center", "score": 0.76},
        {"hospital": "Eastside Clinic", "score": 0.95},
        {"hospital": "Eastside Clinic", "score": 0.91},
        {"hospital": "General Hospital", "score": 0.78},
        {"hospital": "Saint Mary", "score": 0.82},
        {"hospital": "City Medical Center", "score": 0.70},
        {"hospital": "Eastside Clinic", "score": 0.87},
        {"hospital": "General Hospital", "score": 0.84}
    ]

    result = calculate_average_per_hospital(INPUT)
    print(result)

