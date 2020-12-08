import scipy.stats as sp
import matplotlib.pyplot as plt
import seaborn as sns

def bivar_analyzer(dataframe, sent_met):
    apple = dataframe.loc[dataframe['product_agg'] == 'Apple', sent_met]
    google = dataframe.loc[dataframe['product_agg'] == 'Google', sent_met]
    android = dataframe.loc[dataframe['product_agg'] == 'Android', sent_met]
    unknown = dataframe.loc[dataframe['product_agg'] == 'Unknown', sent_met]
    
    a = dataframe.groupby(['product_agg'])[sent_met].mean()
    print(f'Mean {sent_met} by product')
    print(a)
    print(sp.f_oneway(apple, google, android, unknown))
    print(f'Median {sent_met} by product')
    print(dataframe.groupby(['product_agg'])[sent_met].median())
    print(sp.kruskal(apple, google, android, unknown))
    
    plt.figure(figsize=(10,5))
    chart = sns.barplot(x=a.index,y=a, data=dataframe, )
    chart.set_xticklabels(labels=a.index, rotation=45);
    chart.set_xlabel('Product');
    chart.set_ylabel(f'Mean {sent_met}');
    chart.set_title(f'Mean {sent_met} by product');