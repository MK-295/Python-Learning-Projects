#imports
from preprocess import *
from visualise import *
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
        
        # Create a main figure and all subplots (bar chart, pie chart and a word cloud)
        fig = plt.figure(figsize=(15, 10))
        outer = gridspec.GridSpec(2, 2, wspace=0.5, hspace=0.5)
        inner = gridspec.GridSpecFromSubplotSpec(1, 2,
                    subplot_spec=outer[0], wspace=0.5, hspace=0.3)
        ax = plt.Subplot(fig, inner[0])
        ax = bar_chart(freq_top20, ax) # visualize the chart on the subplot
        fig.add_subplot(ax)
        ax = plt.Subplot(fig, inner[1])
        ax = visualise_piechart(freq_top20, ax) # visualize the chart on the subplot
        fig.add_subplot(ax)
        inner = gridspec.GridSpecFromSubplotSpec(1, 1,
                    subplot_spec=outer[2], wspace=0.2, hspace=0.2)
        ax = plt.Subplot(fig, inner[0])
        ax = word_cloud_2(keywords_noun, ax) # visualize the chart on the subplot
        fig.add_subplot(ax)
        fig= plt.gcf()
        fig_canvas_agg = draw_figure(window['canvas'].TKCanvas,fig )
                
                
window.close()
