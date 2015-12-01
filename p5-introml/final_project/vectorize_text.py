import pickle
import sys
import re
sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification

    the actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project

    the data is stored in lists and packed away in pickle files at the end

"""


def get_word_data_from_email(email_addr,n_counter=10):
    "Get word data given email address"
#     print email
    DIR = '../dataset/emails_by_address'
    try:
        f_emails = open('{dir}/from_{addr}.txt'.format(addr=email_addr,dir=DIR),'r')
    except IOError:
        return 'NaN'
    
    counter=0
    word_data = []
    for path in f_emails:
        counter += 1
        if counter > n_counter:
            break
        path = "{dir}/".format(dir=DIR)+path[:-1]
#         print path
        email = open(path, "r")

        ### use parseOutText to extract the text from the opened email
        words = parseOutText(email).replace('\n','').replace('\r','')
        
        word_data.append(words)
    
    document = ' '.join(word_data)
    
    
    return document
 