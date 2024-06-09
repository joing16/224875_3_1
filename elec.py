{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN1qus1RkClZ43qmFgOBApM",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/joing16/224875_3_1/blob/main/elec.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "-19jSmBk8vb4"
      },
      "outputs": [],
      "source": [
        "data_2014 = data[data.index.year == 2014]\n",
        "data_2014\n",
        "\n",
        "plt.figure(figsize=(15, 6))\n",
        "plt.plot(data_2014.index, data_2014['Electricity demand'], label='Electricity demand', color='blue')\n",
        "\n",
        "special_day_mean = data_2014[data_2014['Special day'] == True]['Electricity demand'].mean()\n",
        "non_special_day_mean = data_2014[data_2014['Special day'] == False]['Electricity demand'].mean()\n",
        "\n",
        "\n",
        "mean_values = pd.DataFrame({\n",
        "    'Day Type': ['평일', '주말'],\n",
        "    'Electricity Demand': [non_special_day_mean, special_day_mean]\n",
        "})\n",
        "\n",
        "\n",
        "plt.figure(figsize=(8, 6))\n",
        "plt.bar(mean_values['Day Type'], mean_values['Electricity Demand'], color=['blue', 'red'])\n",
        "plt.title('2014년 평균 전력 수요 비교 (주말과 평일)')\n",
        "plt.ylabel('평균 전력 수요')\n",
        "plt.show()\n",
        "\n",
        "def season(month):\n",
        "    if month in [12, 1, 2]:\n",
        "        return '겨울'\n",
        "    elif month in [3, 4, 5]:\n",
        "        return '봄'\n",
        "    elif month in [6, 7, 8]:\n",
        "        return '여름'\n",
        "    elif month in [9, 10, 11]:\n",
        "        return '가을'\n",
        "\n",
        "\n",
        "data_2014['season'] = data_2014.index.month.map(season)\n",
        "seasonal_means = data_2014.groupby('season')['Electricity demand'].mean()\n",
        "seasonal_means = seasonal_means.reindex(['봄', '여름', '가을','겨울'])\n",
        "\n",
        "\n",
        "plt.figure(figsize=(10, 6))\n",
        "plt.ylim(1200, 1500)\n",
        "ax = seasonal_means.plot(kind='bar', color=['green', 'red', 'orange', 'blue'])\n",
        "plt.title('2014년 계절별 평균 전력 수요')\n",
        "plt.xlabel('계절')\n",
        "plt.ylabel('평균 전력 수요')\n",
        "plt.xticks(rotation=0)\n",
        "plt.show()\n",
        "\n",
        "monthly_means = data_2014.groupby('month')['Electricity demand'].mean()\n",
        "\n",
        "monthly_means.index = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']\n",
        "\n",
        "plt.figure(figsize=(12, 6))\n",
        "plt.ylim(1200, 1550)\n",
        "ax = monthly_means.plot(kind='bar', color='skyblue')\n",
        "plt.title('2014년 월별 평균 전력 수요')\n",
        "plt.xlabel('월')\n",
        "plt.ylabel('평균 전력 수요')\n",
        "plt.xticks(rotation=0)\n",
        "plt.grid(axis='y')\n",
        "plt.show()\n",
        "\n",
        "temperature_means = data_2014[['Seoul','Gwang ju','Busan']].mean(axis=1)\n",
        "\n",
        "plt.figure(figsize=(15, 6))\n",
        "plt.plot(data_2014.index,temperature_means, color='red')\n",
        "\n",
        "plt.figure(figsize=(15, 6))\n",
        "plt.subplot(211)\n",
        "plt.plot(data_2014.index,temperature_means, color='red')\n",
        "plt.subplot(212)\n",
        "plt.plot(data_2014.index, data_2014['Electricity demand'], color='blue')\n",
        "\n",
        "colors = np.where(data_2014['Special day'], 'red', 'blue')\n",
        "\n",
        "\n",
        "plt.figure(figsize=(15, 6))\n",
        "plt.plot(data_2014.index, data_2014['Electricity demand'], color='grey', alpha=0.5)\n",
        "plt.scatter(data_2014.index, data_2014['Electricity demand'], color=colors, s=10)"
      ]
    }
  ]
}