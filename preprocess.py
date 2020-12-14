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
