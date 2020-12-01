import pandas as pd


def get_sentiment(df):
    ###### Valence Shifters ######
#     v_shift = pd.read_csv('data/valenceshifter.csv')
    
    ###### NRC ######
#     nrc = pd.read_csv('data/NRC.csv')
#     nrc = pd.concat([nrc,v_shift])
#     sentiment = []
#     for tweet in df['lemmatizer_tweets']:
#         tweet = tweet.split(' ')
#         total = 0
#         count = 0
#         for word in tweet:
#             if word in list(nrc['word']):
#                 total = total + (nrc[nrc['word'] == word].polar).iloc[0]
#                 count = count + 1
#         try:
#             sent = (float(total) / float(count))
#         except:
#             sent = 0
#         sentiment.append(sent)
#     df['nrc_sentiment'] = sentiment
    
    ###### GI ######
#     gi = pd.read_csv('data/GI_en.csv')
#     gi = pd.concat([gi,v_shift])
#     sentiment = []
#     for tweet in df['lemmatizer_tweets']:
#         tweet = tweet.split(' ')
#         total = 0
#         count = 0
#         for word in tweet:
#             if word in list(gi['word']):
#                 total = total + (gi[gi['word'] == word].polar).iloc[0]
#                 count = count + 1
#         try:
#             sent = (float(total) / float(count))
#         except:
#             sent = 0
#         sentiment.append(sent)
#     df['gi_sentiment'] = sentiment
    
    

    return df