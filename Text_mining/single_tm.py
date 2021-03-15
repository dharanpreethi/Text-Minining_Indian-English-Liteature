
# Single Text Analysis
# Import the installed modules into IDLE and also import the tokenization and stopwords modules from nltk package. The former is applied to convert the text into tokens and the latter is deployed to remove the stopwords (such as a, an, the, they etc.) in the text.
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import requests
from bs4 import BeautifulSoup

# We import a html link of the text Rabindranath Tagore's Mashi And Other Stories and parse the text from the html
url = "http://www.gutenberg.org/files/34757/34757-h/34757-h.htm" #get the link of a text
get = requests.get(url) #get the url
html = get.text # get the text from the url
text = BeautifulSoup(html, "html.parser").get_text() # parsing the html


# The text contains metadata about the author, publisher and Project Gutenberg. We just simply use find function to find the primary text as those details will affect our output. The advangae of Project Gutenberg files is that they have tags of "start of this project..." and "end of this project..."for each file which we can as tags to extract the text between these tags.
extract1 = text.find("*** START OF THIS PROJECT GUTENBERG EBOOK MASHI AND OTHER STORIES ***") #find the index of starting of the text to elminate the metadata
extract2 = text.rfind("*** END OF THIS PROJECT GUTENBERG EBOOK MASHI AND OTHER STORIES ***")

analysis_part = text[extract1:extract2]# combining them


# Next we extract only words in the sentence by using reguar experssion tokenizer
tokenizer = RegexpTokenizer('\w+') 
tokens = tokenizer.tokenize(analysis_part) # tokenize the text


# We convert all the tokens into lower case. Then, we remove the stopwords which will create an impact in our analysis as they appear frequently in the text. The below code also demonstrates how to add new stopwords in the existing stopwords list of nltk. Though there are multiple ways to remove stopwords, I used list data type and append function as they are easy to follow and understand code. 
words = []
for word in tokens:
    words.append(word.lower()) # convert the entire text into lowercase

new_stopwords = ("could", "would", "also", "us") # add few more words to the list of stopwords


stopwords = stopwords.words("english") # calling the stopwords from nltk

for i in new_stopwords:
    stopwords.append(i) # adding new stopwords to the list of existing stopwords

words_list = []

for without_stopwords in words:
    if without_stopwords not in stopwords:
        words_list.append(without_stopwords) # applying stopwords


# We use nltk.FreqDist function to find the frequent words in the text
fre_word_list = nltk.FreqDist(words_list) #extracting the frequently appeared words
n= 15 # the top 15 frequent words 
fre_word_list.plot(n, color='green')

