def get_sentiment(df):
    ###### Valence Shifters ######
    v_shift = pd.read_csv('data/valenceshifter.csv')
    
    ###### NRC ######
    nrc = pd.read_csv('data/NRC.csv')
    nrc = pd.concat([nrc,v_shift])
    sentiment = []
    for tweet in df['lemmatizer_tweets']:
        tweet = tweet.split(' ')
        total = 0
        count = 0
        for word in tweet:
            if word in list(nrc['word']):
                total = total + (nrc[nrc['word'] == word].polar).iloc[0]
                count = count + 1
        try:
            sent = (float(total) / float(count))
        except:
            sent = 0
        sentiment.append(sent)
    df['nrc_sentiment'] = sentiment
    
    ###### GI ######
    gi = pd.read_csv('data/GI_en.csv')
    gi = pd.concat([gi,v_shift])
    sentiment = []
    for tweet in df['lemmatizer_tweets']:
        tweet = tweet.split(' ')
        total = 0
        count = 0
        for word in tweet:
            if word in list(gi['word']):
                total = total + (gi[gi['word'] == word].polar).iloc[0]
                count = count + 1
        try:
            sent = (float(total) / float(count))
        except:
            sent = 0
        sentiment.append(sent)
    df['gi_sentiment'] = sentiment


    ###### HENRY ######
    henry = pd.read_csv('data/HENRY_en.csv')
    henry = pd.concat([henry,v_shift])
    sentiment = []
    for tweet in df['lemmatizer_tweets']:
        tweet = tweet.split(' ')
        total = 0
        count = 0
        for word in tweet:
            if word in list(henry['word']):
                total = total + (henry[henry['word'] == word].polar).iloc[0]
                count = count + 1
        try:
            sent = (float(total) / float(count))
        except:
            sent = 0
        sentiment.append(sent)
    df['henry_sentiment'] = sentiment
    
    
    ###### HULIU ######
    huliu = pd.read_csv('data/HULIU.csv')
    huliu = pd.concat([huliu,v_shift])
    sentiment = []
    for tweet in df['lemmatizer_tweets']:
        tweet = tweet.split(' ')
        total = 0
        count = 0
        for word in tweet:
            if word in list(huliu['word']):
                total = total + (huliu[huliu['word'] == word].polar).iloc[0]
                count = count + 1
        try:
            sent = (float(total) / float(count))
        except:
            sent = 0
        sentiment.append(sent)
    df['huliu_sentiment'] = sentiment
    
    
    ###### JOCKERS ######
    jockers = pd.read_csv('data/JOCKERS.csv')
    jockers = pd.concat([jockers,v_shift])
    sentiment = []
    for tweet in df['lemmatizer_tweets']:
        tweet = tweet.split(' ')
        total = 0
        count = 0
        for word in tweet:
            if word in list(jockers['word']):
                total = total + (jockers[jockers['word'] == word].polar).iloc[0]
                count = count + 1
        try:
            sent = (float(total) / float(count))
        except:
            sent = 0
        sentiment.append(sent)
    df['jockers_sentiment'] = sentiment


    ###### LM ######
    lm = pd.read_csv('data/LM_en.csv')
    lm = pd.concat([lm,v_shift])
    sentiment = []
    for tweet in df['lemmatizer_tweets']:
        tweet = tweet.split(' ')
        total = 0
        count = 0
        for word in tweet:
            if word in list(lm['word']):
                total = total + (lm[lm['word'] == word].polar).iloc[0]
                count = count + 1
        try:
            sent = (float(total) / float(count))
        except:
            sent = 0
        sentiment.append(sent)
    df['lm_sentiment'] = sentiment
    
    
    ###### SENTICNET ######
    senticnet = pd.read_csv('data/SENTICNET.csv')
    senticnet = pd.concat([senticnet,v_shift])
    sentiment = []
    for tweet in df['lemmatizer_tweets']:
        tweet = tweet.split(' ')
        total = 0
        count = 0
        for word in tweet:
            if word in list(senticnet['word']):
                total = total + (senticnet[senticnet['word'] == word].polar).iloc[0]
                count = count + 1
        try:
            sent = (float(total) / float(count))
        except:
            sent = 0
        sentiment.append(sent)
    df['senticnet_sentiment'] = sentiment
    
    
    ###### SENTIWORD ######
    sentiword = pd.read_csv('data/SENTIWORD.csv')
    sentiword = pd.concat([sentiword,v_shift])
    sentiment = []
    for tweet in df['lemmatizer_tweets']:
        tweet = tweet.split(' ')
        total = 0
        count = 0
        for word in tweet:
            if word in list(sentiword['word']):
                total = total + (sentiword[sentiword['word'] == word].polar).iloc[0]
                count = count + 1
        try:
            sent = (float(total) / float(count))
        except:
            sent = 0
        sentiment.append(sent)
    df['sentiword_sentiment'] = sentiment
    
    
    ###### SOCAL ######
    socal = pd.read_csv('data/SOCAL.csv')
    socal = pd.concat([socal,v_shift])
    sentiment = []
    for tweet in df['lemmatizer_tweets']:
        tweet = tweet.split(' ')
        total = 0
        count = 0
        for word in tweet:
            if word in list(socal['word']):
                total = total + (socal[socal['word'] == word].polar).iloc[0]
                count = count + 1
        try:
            sent = (float(total) / float(count))
        except:
            sent = 0
        sentiment.append(sent)
    df['socal_sentiment'] = sentiment
    
    

    return df