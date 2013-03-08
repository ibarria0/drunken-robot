import time
import re
import operator
import praw
import sys
import argparse
from nltk.corpus import stopwords

r = praw.Reddit('Sr. Trends v0.1')
words = []
contractions = [ "dont", "cant","im", "didnt", "aint", "id", "ive"]


class Word:
  def __init__(self, marker, raw):
    self.marker = marker
    self.raw = raw

def print_words(words):
  for word in words[:100]:
    print word[0] + " " +  str(word[1])

def filter_comment(comment):
  text = comment.body.lower()
  words = re.sub("\. |,|;|: |'","" , text ).split()
  important_words = filter(lambda x: x not in stopwords.words('english') and x not in contractions, words)
  return important_words

def rank_words(words):
  h = {}
  for word in words:
    try:
      if h.has_key(word):
        v = h.get(word)          #get current counter
        h.update({word: v + 1})  #increment counter
      else:
        h.update({word: 1}) 
    except KeyError:
      print word
  print_words(sorted(h.iteritems(), key=operator.itemgetter(1), reverse=True))


def parse_args():
  parser = argparse.ArgumentParser(description='Gets trending words in a subreddit.')
  parser.add_argument('subreddit', metavar='subreddit', type=str,help='subreddit to scrape')
  parser.add_argument('limit', type=int, default=100, help="limit amount of comments scraped (max 1000, default 100)")
  args = parser.parse_args()
  if (args.limit < 1) or (args.limit > 1000):
    raise Exception("limit must be between 1 and 1000")
  return args

def main():
  args = parse_args()
  while True:
      subreddit = r.get_subreddit(args.subreddit)
      comments = subreddit.get_comments(limit=args.limit)
      for comment in  comments:
          try: 
            words.extend(filter_comment(comment))
          except AttributeError:
            print "comment with no body"
      rank_words(words)
      time.sleep(1800)
main()
