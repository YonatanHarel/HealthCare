import pandas as pd


def daily_summary_generator(filepath: str):
    df = pd.read_csv(filepath)
    # convert timestamps to datetime
    df['scan_time'] = pd.to_datetime(df['scan_time'])

    # calculate daily average
    daily_avg = df.groupby(df['scan_time'].dt.date)['ai_score'].mean()

    # export results to new CSV file
    pd.DataFrame(daily_avg).to_csv("daily_avg.csv")


if __name__ == '__main__':
    csv_data_filepath = 'sample_scan_data.csv'
    daily_summary_generator(csv_data_filepath)
