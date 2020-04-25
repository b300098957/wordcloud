# https://machinelearningmastery.com/clean-text-machine-learning-python/


import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
import re
import string

# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

#_upload()

def _file_upload():

   f=open("pg6695.txt", "r")

   global file_contents
   file_contents = f.read()
   print('Uploaded `{}` ({:.2f} kB)'.format( file_contents, len(file_contents) / 2 **10))

_file_upload()

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    words = file_contents.split(" ")
    
    # Strip punctuation
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in words]
    print(stripped[:100])

    tmpDict = {}

    # making dict for counting frequencies
    for text in stripped:
        if re.match("|".join(uninteresting_words), text):
            continue
        val = tmpDict.get(text, 0)
        tmpDict[text.lower()] = val + 1

    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(tmpDict)
    return cloud.to_array()

myimage = calculate_frequencies(file_contents)
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
