# Corpus of text analysis

# Now, we can mine the corpus of texts using little more advanced methods of Python.
#1.Install glob using pip and import the module 
#2. Import other necessary modules which we already installed in our previous analysis
#3. Asterisk mark will import all plain text files in the corpus
#4. Create a corpus of text files and call them using glob
#5. Store the stopwords of nltk in a variable


import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import glob

corpus = glob.glob("E:\Medium Blog\Text_mining\*.txt")
stop_words = set(stopwords.words('english'))


# Pre-processing and analysis
# We will call the corpus using for loop and then read the texts and convert them into lowercase. We extract the content for analysis, apply stopwords list and tokenization as we did for the single text, but everything should be in the for loop as in the below code.

for i in range(len(corpus)):

    text_file = open(corpus[i], "r", encoding = "UTF-8")

    lines = []
    lines = text_file.read().lower()
    
    extract1 =lines.find("start of this project")
    extract2 = lines.rfind("end of this project")
    lines = lines[extract1:extract2]
    
    
    tokenizer = RegexpTokenizer('\w+') # extracting words

    tokens = tokenizer.tokenize(lines) # tokenize the text
    new_stopwords = ("could", "would", "also", "us") # add few more words to the list of stopwords


    stop_words = stopwords.words('english')

    for i in  new_stopwords:
        stop_words.append(i) # adding new stopwords to the list of existing stopwords"""
    

    words_list = [w for w in tokens if not w in stop_words]
    
    filtered_words = []
    for w in tokens:  
        if w not in stop_words:  
            filtered_words.append(w) 



    fre_word_list = nltk.FreqDist(filtered_words) #extracting frequently appeared words
    
    print(fre_word_list.most_common(5)) # check the most common frequent words
    
    fre_word_list.plot(25) #create a plot for the output
    
    
    pos = nltk.pos_tag(filtered_words, tagset = 'universal') # applying parts of speech (pos) tag for further analysis
        
    
    p = []
    y = ['NOUN'] # change the pos here to store them separately 
    for j in pos:
        for l in y:
            if l in j:
                p.append(j)
    
      
    noun = nltk.FreqDist(p)# check the frequency of each pos 
    noun.plot(20)# creating a plot for pos
        


