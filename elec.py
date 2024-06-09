import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from matplotlib.ticker import MaxNLocator

def load_data():
    data = pd.read_csv(전력 revenge3.csv)
    data.set_index('date', inplace=True)
    return data

def analyze_year(data, year):
    data_year = data[data.index.year == year]
    
    # 기본적인 전력 수요 그래프
    plt.figure(figsize=(15, 6))
    plt.plot(data_year.index, data_year['Electricity demand'], label='Electricity demand', color='blue')
    plt.title(f'{year}년 전력 수요')
    plt.xlabel('Date')
    plt.ylabel('Electricity Demand')
    plt.legend()
    plt.show()

    # 스페셜데이 평균 전력 수요 계산 및 비교
    special_day_mean = data_year[data_year['Special day'] == True]['Electricity demand'].mean()
    non_special_day_mean = data_year[data_year['Special day'] == False]['Electricity demand'].mean()

    mean_values = pd.DataFrame({
        'Day Type': ['평일', '주말'],
        'Electricity Demand': [non_special_day_mean, special_day_mean]
    })

    plt.figure(figsize=(8, 6))
    plt.bar(mean_values['Day Type'], mean_values['Electricity Demand'], color=['blue', 'red'])
    plt.title(f'{year}년 평균 전력 수요 비교 (주말과 평일)')
    plt.ylabel('평균 전력 수요')
    plt.show()

    # 계절별 평균 전력 수요
    data_year['season'] = data_year.index.month.map(lambda x: season(x))
    seasonal_means = data_year.groupby('season')['Electricity demand'].mean()
    seasonal_means = seasonal_means.reindex(['봄', '여름', '가을', '겨울'])

    plt.figure(figsize=(10, 6))
    plt.ylim(1200, 1500)
    ax = seasonal_means.plot(kind='bar', color=['green', 'red', 'orange', 'blue'])
    plt.title(f'{year}년 계절별 평균 전력 수요')
    plt.xlabel('계절')
    plt.ylabel('평균 전력 수요')
    plt.xticks(rotation=0)
    plt.show()

def season(month):
    if month in [12, 1, 2]:
        return '겨울'
    elif month in [3, 4, 5]:
        return '봄'
    elif month in [6, 7, 8]:
        return '여름'
    elif month in [9, 10, 11]:
        return '가을'

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        year = int(sys.argv[1])
        data = load_data('전력 revenge3.csv')
        analyze_year(data, year)
    else:
        print("Please provide a year as an argument.")
