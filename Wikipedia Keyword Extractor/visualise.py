
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
from wordcloud import WordCloud
 

"""
Visualisation below using Matplotlib. The pie chart and bar chart take in a dictionary of word:frequency,
the word cloud takes in a list of words
"""
def bar_chart(input: dict, ax):
    keys = input.keys()
    values = input.values()
    ax.set_xticklabels(list(keys), Rotation=90,fontsize=7)
    ax.bar(keys, values, width=0.3, color='lightseagreen') 
    ax.set_title('Bar Chart - Keyword Frequency',fontsize=8)
    return ax
   
def visualise_piechart(input: dict,ax):
    words = list(input.keys())
    values = list(input.values())
    color=['lightseagreen','mediumslateblue','indigo','yellowgreen','gold','lightcoral','olivedrab','lightpink','plum']
    ax.pie(values, labels=words,colors=color,textprops={'fontsize': 7})
    ax.axis('equal') 
    ax.set_title('Pie Chart - Keyword Frequency',fontsize=8)
    return ax


def word_cloud_2(input2: list,ax):
    #read in list of phrases:
    string = '\n'.join(input2)
    # create a word cloud from string
    wordcloud = WordCloud().generate(string)                                              
    wordcloud = WordCloud(background_color="white",max_words=len(string),max_font_size=30, relative_scaling=.5).generate(string)
    ax.imshow(wordcloud)
    ax.set_title('Wikipedia Data Word Cloud',fontsize=8)
    ax.axis("off")
    return ax
