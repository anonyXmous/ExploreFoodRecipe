import pandas as pd
import nltk

df = pd.read_csv('grill-and-bbq.csv', encoding='utf-8', header=1, sep='|')
all_ingredients = [row[5].lower() for row in df.itertuples()]

all_words = []
for w in all_ingredients:
    for l in w.split(" ",w.count(" ")):    
        all_words.append(l)

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(30))
