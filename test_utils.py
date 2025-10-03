from utils import process_tweet, build_freqs
import numpy as np
from nltk.corpus import twitter_samples

tweet = "This is a ridiculously bright movie. The plot was terrible and I was sad until the ending!"
print("Processed tweet:", process_tweet(tweet))

positive_tweets = twitter_samples.strings('positive_tweets.json')[:100]
labels = np.ones((100,))
freqs = build_freqs(positive_tweets, labels)
print("Sample frequencies:", {k: freqs[k] for k in list(freqs)[:5]})