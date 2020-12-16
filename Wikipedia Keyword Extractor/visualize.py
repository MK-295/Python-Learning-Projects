
"""
Visualisation below using Matplotlib. The pie chart and bar chart take in a dictionary of word:frequency,
the word cloud takes in a list of words
"""
def visualise_piechart(input: dict):
    # store k,v in a list
    import matplotlib.pyplot as plt
    words = list(input.keys())
    freq = list(input.values())
    plt.figure(figsize=(3, 3))
    plt.pie(freq, labels=words)
    plt.title('Wikipedia Article Keyword Frequency')
    
    fig= plt.gcf()
    return fig
    #return plt.show()

def bar_chart(input: dict):
    import matplotlib.pyplot as plt
    keys = input.keys()
    values = input.values()
    plt.figure(figsize=(3, 3))
    plt.xticks(rotation=90)
    plt.title('Wikipedia Article Keyword Frequency')
    plt.bar(keys, values, width=0.3, color='orange') 
    fig=plt.gcf()
    return fig
    #return plt.show()
    
def word_cloud_2(input: list):
    import seaborn as sns
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud

    #read in list of phrases:
    string = '\n'.join(input)
    # create a word cloud from string
    wordcloud = WordCloud().generate(string) 
                                             
    wordcloud = WordCloud(background_color="white",max_words=len(string),max_font_size=30, relative_scaling=.5).generate(string)
    plt.figure(figsize=(5,3))
    plt.title('Wikipedia Data Word Cloud')
    plt.imshow(wordcloud)
    plt.axis("off")
    fig=plt.gcf()
    return fig
