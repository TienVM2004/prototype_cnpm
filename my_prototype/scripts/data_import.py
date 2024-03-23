import csv
from dictionary.models import Word
import pandas as pd 

def run():

    data = pd.read_csv('wordlist_10000.txt', sep = " ", header= None)
    data.columns = ['Word']
    model_instance = [Word(e_word=row['Word']) for index, row in data.iterrows()]
    Word.objects.bulk_create(model_instance)

