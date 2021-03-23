from textblob import TextBlob
import nltk

# nltk.download ('Stopwords')
from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd

blob = TextBlob(Path('RomeoAndJuliet.txt').read_text())

print(blob.word_counts["juliet"])

print(blob.word_counts['romeo'])

print(blob.word_counts['thou'])

print(blob.words.count('joy'))

print(blob.noun_phrases.count("lady capulet"))

stops = stopwords.words('english')

more_stop_words = ["thee", 'thy', 'thou']
stops += more_stop_words

items = blob.word_counts.items()
print(items)


items = [item for item in items if item[0] not in stops]

print(items[:10])



from operator import itemgetter

sorted_items = sorted(items)
sorted_items = sorted(items, key=itemgetter(1), reverse=True)
print(sorted_items[:10])


#grab the top 20
top20 = sorted_items[:20]

print(top20)




df = pd.DataFrame(top20, columns=['word', 'count'])
print(df)



import matplotlib.pyplot as plt

df.plot.bar(x='word', y='count', rot=0, legend=False, color=['y', 'c', 'm', 'b', 'g', 'r'])

plt.gcf().tight_layout()
plt.show()

#WORDCLOUD

from pathlib import Path
from wordcloud import wordcloud
import imageio

text = Path('RomeoAndJuliet.txt').read_text()
print(text)

mask_image = imageio.imread('mask_heart.png')

wordcloud = WordCloud(colormap='prism', mask=mask_image, background_color='white')

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file('RomeoAndJulietHeart.png')

plt.imshow(wordcloud)
print('done')
