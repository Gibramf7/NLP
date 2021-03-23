from textblob import TextBlob

text = "Today is a beautiful day. Tommorow looks like bad weather."

blob = TextBlob(text)

#print(blob)


#print(blob.sentences)

#print(blob.words)

#print(blob.tags)

#print(blob.noun_phrases)

#print(blob.sentiment)
'''
print(round(blob.sentiment.polarity,3))
print(round(blob.sentiment.subjectivity,3))

sentences = blob.sentences

for sentence in sentences:
    print(sentence)
    print(sentence.sentiment)
    print(round(sentence.sentiment.polarity,3))

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

print(blob)

print(blob.detect_language())

spanish = blob.translate(to='es')

print(spanish)
'''
from textblob import Word

index = Word('index')

print(index.pluralize())

cacti = Word('cacti')

print(cacti.singularize())

animals = TextBlob('dog cat fish bird').words

print(animals.pluralize())

word = Word('theyr')

print(word.spellcheck())

word.correct()

print(word)

sentence = TextBlob('Ths sentance has missplled wrds.')

corrected_sentence = sentence.correct()

print(corrected_sentence)


from textblob import Word

word1 = Word('studies')
word2 = Word('variety')

print(word1.lemmatize())
print(word2.lemmatize())

happy = Word('happy')

print(happy.definitions)

'''
for synset in happy.synsets:
    print(synset)
    for lemma in synset.lemmas():
        print(lemma)
        print(lemma.name())


lemmas = happy.synsets[0].lemmas()
print(lemmas)


for lemma in lemmas[0].synsets.antonyms():
    print(lemma.name())
'''

import nltk

#nltk.download('stopwords')

from nltk.corpus import stopwords

stops = stopwords.words("english")

#print(stops)

blob = TextBlob('Today is a beautiful day.')

print(blob.words)

cleanlist = [word for word in blob.words if word not in stops]

print(cleanlist)