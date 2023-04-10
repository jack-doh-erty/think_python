"""
zipf law describes the relationship between the rank and freqneucy on words in languages:
log(f) = log(c) - s*log(r),
where r is the rank, f is the frequency and s and c are constants based on the language
"""

from word_frequency import read_words, skip_header, count_words
import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

words = read_words('crime_and_punishment.txt')
hist = count_words(words)

rank = 1
res = []

def frequency_rank(hist):
	frequencies = list(hist.values())
	frequencies.sort(reverse=True)

	rf = [(r+1, f) for r, f in enumerate(frequencies)]
	return rf


df = pd.DataFrame(frequency_rank(hist), columns =['rank', 'frequency'])
  
print(df) 

sns.lineplot(data=df, x="rank", y="frequency")
plt.xscale('log')
plt.yscale('log')
plt.show()