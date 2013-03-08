import time
import re
import operator
import praw
import sys
import argparse
from nltk.corpus import stopwords
import nltk

r = praw.Reddit('Sr. Trends v0.1')
contractions = [ "dont", "cant","im", "didnt", "aint", "id", "ive"]

def parse_args():
  global args
  parser = argparse.ArgumentParser(description='Gets trending words in a subreddit.')
  parser.add_argument('subreddit', metavar='subreddit', type=str,help='subreddit to scrape')
  parser.add_argument('limit', type=int, default=100, help="limit amount of comments scraped (max 1000, default 100)")
  args = parser.parse_args()
  validate_args

def validate_args():
  if (args.limit < 1) or (args.limit > 1000):
    raise Exception("limit must be between 1 and 1000")

def print_words(words):
  for word,times in words.items():
    if (times > 1):
      print word + " " +  str(times)

def filter_comment(comment):
  text = comment.body.lower().encode('ascii', 'ignore')
  words = re.sub("\. |,|;|: |'","" , text ).split()
  important_words = filter(lambda x: x not in stopwords.words('english') and x not in contractions, words)
  return important_words

def main():
  parse_args()
  words = []
  subreddit = r.get_subreddit(args.subreddit)
  comments = subreddit.get_comments(limit=args.limit)
  for comment in  comments:
      try: 
        words.extend(filter_comment(comment))
      except AttributeError:
        print "whooooooops"
  print_words(nltk.FreqDist(words))

main()
