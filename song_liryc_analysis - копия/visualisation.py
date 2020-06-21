import pandas as pd
import matplotlib.pyplot as plt

songs_df = pd.read_csv('example.csv')


def visualisate(songs_df):
    positive = songs_df['polarity'] > 0
    negative = songs_df['polarity'] < 0
    neutral = songs_df['polarity'] == 0

    pdf = songs_df[positive]
    nedf = songs_df[negative]
    nudf = songs_df[neutral]

    positive_songs_precent = round(len(pdf['polarity']) * 100 / len(songs_df), 2)
    negative_songs_precent = round(len(nedf['polarity']) * 100 / len(songs_df), 2)
    neutral_songs_precent = round(len(nudf['polarity']) * 100 / len(songs_df), 2)

    cols = ['Positive {} %'.format(positive_songs_precent),
            'Negative {} %'.format(negative_songs_precent),
            'Neutral {} %'.format(neutral_songs_precent)]

    precentdf = pd.DataFrame([[positive_songs_precent,
                               negative_songs_precent,
                               neutral_songs_precent]],
                             index=['Songs'],
                             columns=cols)

    precentdf.plot.bar()
    plt.yticks(list(range(0, 110, 10)), [str(i * 10) + ' %' for i in range(0, 11)])
    plt.xticks(rotation=0)
    plt.title('Percent of songs by sentiment')

    pdf = tuple(songs_df[positive]['Popularity'])
    nedf = tuple(songs_df[negative]['Popularity'])
    nudf = tuple(songs_df[neutral]['Popularity'])

    apdf = sum(pdf) / len(pdf)
    anedf = sum(nedf) / len(nedf)
    anudf = sum(nudf) / len(nudf)
    df = pd.DataFrame([[apdf, anedf, anudf]],
                      index=["Songs"],
                      columns=['Positive', 'Negative', 'Neutral'])
    df.plot.bar()
    plt.yticks(tuple(range(0, 110, 10)))
    plt.ylabel('Popularity')
    plt.xticks(rotation=0)
    plt.title('Average popularity of songs by mood')

    genres = list(songs_df['genre'].dropna())
    genres = list(set(genres))
    popularity = []
    for genre in genres:
        pop_of_gen = songs_df['genre'] == genre

        data = songs_df[pop_of_gen]['Popularity']
        average = sum(tuple(data)) / len(data)
        popularity.append(average)
    df = pd.DataFrame([popularity], columns=genres, index=['Songs'])
    df.plot.bar()
    plt.yticks(tuple(range(0, 110, 10)))
    plt.ylabel('Popularity')
    plt.xticks(rotation=0)
    plt.title('Average popularity of songs by genre')

    years = list(songs_df['Year'].dropna())
    years = list(set(years))
    popularity = []
    for year in years:
        pop_of_gen = songs_df['Year'] == year

        data = songs_df[pop_of_gen]['Popularity']
        average = sum(tuple(data)) / len(data)
        popularity.append([average])
    df = pd.DataFrame(popularity, columns=["Popularity"], index=years)
    df.plot.bar(figsize=(16, 4))
    plt.yticks(tuple(range(0, 110, 10)))
    plt.ylabel('Popularity')
    plt.xticks(rotation=45)
    plt.title('Average popularity of songs by year')


visualisate(songs_df)
plt.show()
