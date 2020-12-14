

#example input URL: https://en.wikipedia.org/wiki/Ancient_Egypt

#Functions

def wikipedia_web_scraper(input_url):
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    source= urlopen(input_url).read()
    soup = BeautifulSoup(source,'lxml')
    text = []
    #extracts the header 2
    for header2 in soup.find_all('h2'):
        text.append(str(header2.text))
    #extracts the paragraph text only
        for paragraph in soup.find_all('p'):
            text.append(str(paragraph.text))
        break 
    text =''.join(text)
   #text=list(text)
    return text

def data_preprocessing(text):
    ''' 
   This function takes input text and cleans the citations from Wikipedia e.g[1],[2].
   The input is a text in string format and returns a cleaned output string
   '''
    import re
    text=str(text)
    data = re.sub('\[.*?[\w]\]+', '', text)
    data = data.replace('\n', '')
    return data


def noun_capture(text):
    import nltk
    from nltk.tokenize import word_tokenize 
    nltk.download('brown')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    from nltk.corpus import treebank_chunk
    from nltk import Tree
    
    text =[text]
   #tokenize sentences and pos
    for i in text:
        tokenize = nltk.word_tokenize(i)
        pos = nltk.pos_tag(tokenize)
    grammar = "NP: {(<JJ>?<NN>*<NNS>)|(<JJ>?<NN>*<NN>)|(<NNP>*<NNP>)|}"  # I update the grammar to capture all type of nouns: NN, NNS and NNP and noun phrase with JJ
    cp = nltk.RegexpParser(grammar)
    tree= cp.parse(pos)
    result = []
    for child in tree:
        if isinstance(child, Tree):   # If it's not a leaf       
            if child.label() == 'NP': # And it's a NP node
                temp = []
                for num in range(len(child)):
                    temp.append(child[num][0]) # Get all leaves of that node (leave is the word)
                result.append(' '.join(temp))
    return result

def frequency(input_list: list):
    '''
    Input a list of words and phrases, the output will be a dictionary with the frequency of each word
    '''
    from collections import Counter 
    frequency = Counter(input_list)
    return frequency

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
   

import matplotlib
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
sg.theme('Reddit')
matplotlib.use('TkAgg')

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

layout = [  [sg.Text('      '),sg.Text('                        Wikipedia Article Keyword Extractor')],
            [sg.Text('Enter URL Here:'), sg.Input(key='input_link', enable_events=True),sg.Button('Process',enable_events=True)], 
            [sg.Text('')], 
            [sg.Canvas(size=(500, 300), key='canvas', background_color= '#e3e3e3')],
            [sg.OK(), sg.Cancel()]] 
#window.Maximize= True
window = sg.Window('Wikipedia Article Keyword Extractor', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif event=='Process':
        
        #take input URL and convert it to string
        try:
            link= str(values['input_link'])
        except Exception as e:
            sg.Popup('Please enter a URL')
        #apply all the functions here, web scarping, data cleaning, keywords and finding words that are more than 10
            
        wikipedia_page = wikipedia_web_scraper(link)
        cleaning_wiki_page = data_preprocessing(wikipedia_page)
        keywords_noun = noun_capture(cleaning_wiki_page)
        freq = frequency(keywords_noun)
        freq_top20 = dict((k, v) for k, v in freq.items() if v >= 10)
    
        #visualisations
        
        pie_chart = visualise_piechart(freq_top20)
        fig_canvas_agg = draw_figure(window['canvas'].TKCanvas, pie_chart)
        bc= bar_chart(freq_top20)
        fig_canvas_agg = draw_figure(window['canvas'].TKCanvas, bc)
        word_cloud= word_cloud_2(keywords_noun) 
        fig_canvas_agg = draw_figure(window['canvas'].TKCanvas, word_cloud)
                
        

       
     
        
        
window.close()
