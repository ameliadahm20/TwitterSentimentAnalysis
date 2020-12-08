import nltk
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import string, re
string.punctuation

## setting stopwords and punctuations
stop_words=stopwords.words("english")
stop_words += list(string.punctuation)
stop_words += ['...','u','w','2',"i'm",'via',"we're",'6','3','hey']
# print(stop_words)
sw_set = set(stop_words)

def process_tweet(tweet):
    tokenizer = RegexpTokenizer(r"(iPad\s2|[a-zA-Z0-9-]+'?\w+)")

    tokens = tokenizer.tokenize(tweet)
    sw_removed = [token.lower().replace(" ","") for token in tokens if token.lower() not in sw_set]
    return sw_removed

def word_count_func(data):
#     #using the process_tweet function to tokenize, lower and remove stopwords
    process_data = list(map(process_tweet, data))
    
#     #lemmatizing words
    from nltk.stem import WordNetLemmatizer 
      
#     #instantiating
    lemmatizer = WordNetLemmatizer() 

#     #process_data is a list of lists - here looping over the lists and then the words in the list
    lemmatizer_tweets=[]
    for l in process_data:
        new_row = []
        for w in l:
            new_row.append(lemmatizer.lemmatize(w))
        lemmatizer_tweets.append(new_row)   
    
    #This is more descriptive info - calculating the unique vocab of the subset
    overall_lem_vocab = set()
    for tweet in lemmatizer_tweets:
        overall_lem_vocab.update(tweet)
    print(f'Overall vocab of subset: {len(overall_lem_vocab)}')

    #Flattening (going from a list of lists to one single list) the lemmatized tweets for freq
    flat_lemmatizer_tweets = [item for sublist in lemmatizer_tweets for item in sublist]
    
    #applying nltk freqdist function to the flat list
    lem_freq = FreqDist(flat_lemmatizer_tweets)
    print('30 most common words in subset:')
    print(lem_freq.most_common(30))
    
    #returning normalized word freq because there are different N's
    total_words = sum(lem_freq.values())
    top_30 = lem_freq.most_common(30)
    print("Word \t\t Normalized Frequency")
    print()
    for word in top_30:
        normalized_frequency = word[1]/total_words
        print("{} \t\t {:.4}".format(word[0], normalized_frequency))
        
    #Creating word clouds - input is a dict with key word value num of occurences 
    word_dict = dict(top_30)
    from wordcloud import WordCloud
    wordcloud = WordCloud(colormap='Spectral').generate_from_frequencies(word_dict)
    
    # Display the generated image w/ matplotlib:

    plt.figure(figsize=(10,10), facecolor='k')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()