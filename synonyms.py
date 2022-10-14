import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('ocean_traits.csv')

import nltk
from nltk.corpus import wordnet

def synonym_extractor(phrase):
     synonyms = []

     for syn in wordnet.synsets(phrase):
          for l in syn.lemmas():
               synonyms.append(l.name())
     print('These are synonyms = ',set(synonyms),'\n\n')
     
     return(set(synonyms))

column_names = {}

Column = set()
for j in range(len(dataset.columns)):
    column_wise_synonyms = []
    for i in range(len(dataset.iloc[:, 0].values)):
        print('\n')
        print(dataset.iloc[:, 0].values[i],":- ")
        for element in synonym_extractor(dataset.iloc[:, j].values[i]):
            column_wise_synonyms.append(element)
    column_wise_synonyms_set = list(set(column_wise_synonyms))
    print('/////////////////////////////////////////////////////////////////////////')
    print(f"this is {dataset.columns[j]}  synonyms set:",column_wise_synonyms_set)
    print('/////////////////////////////////////////////////////////////////////////')
    while len(column_wise_synonyms_set) != 73:
        column_wise_synonyms_set.append(np.nan)
#     column_names.append(column_wise_synonyms_set)
    column_names.update({dataset.columns[j]:column_wise_synonyms_set})

# dataset2 = pd.DataFrame(column_names, columns=["Openness", "Conscintiousness","Extraversion", "Agreeableness", "Neuroticism"])
  
# dataset2

dataset2 = pd.DataFrame.from_dict(column_names, orient='index')
dataset2 = dataset2.transpose()

dataset2.to_csv('Enhanced_ocean_traits')
dataset2

    
               
    