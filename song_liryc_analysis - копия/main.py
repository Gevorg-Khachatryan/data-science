import pandas as pd
from textblob import TextBlob
import os


def add_sentiment(df):
    sdf = pd.DataFrame(columns=['polarity', 'sentiment'])
    df = df.join(sdf)

    for i in list(df.index):

        text = df['lyrics'][i]

        df.loc[i, 'genre'] = df['genre'][i][:df['genre'][i].index(')')].split('"')[-2]
        if type(text) == str:

            an = TextBlob(text)
            df.loc[i, 'polarity'] = an.sentiment.polarity

            if an.sentiment.polarity == 0:
                df.loc[i, 'sentiment'] = 'Neutral'
            elif 0.9 > an.sentiment.polarity > 0:
                df.loc[i, 'sentiment'] = 'Weakly positive'
            elif an.sentiment.polarity >= 0.9:
                df.loc[i, 'sentiment'] = 'Strongly positive'
            elif 0 > an.sentiment.polarity > -0.9:
                df.loc[i, 'sentiment'] = 'Weakly negative'
            elif an.sentiment.polarity <= -0.9:
                df.loc[i, 'sentiment'] = 'Strongly negative'

        else:
            df = df.drop([i])
    return df


def read_and_join_files():
    print("please wait, it'll take about 30 seconds. ")
    dir = os.path.dirname(os.path.abspath(__file__))
    files_list = os.listdir(dir + "/data")
    df = pd.DataFrame()
    for file in files_list:
        odf = pd.read_csv('data/' + file)
        odf = add_sentiment(odf)
        df = df.append(odf)
    df.drop_duplicates()
    df.to_csv('data.csv')


read_and_join_files()
