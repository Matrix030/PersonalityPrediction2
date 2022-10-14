import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

def synonym_antonym_extractor(phrase):
     synonyms = []
     antonyms = []

     for syn in wordnet.synsets(phrase):
          for l in syn.lemmas():
               synonyms.append(l.name())
               if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())

     print('These are synonyms = ',set(synonyms),'\n\n')
     print('Thes are antonyms = ',set(antonyms))

synonym_antonym_extractor(phrase="bad")