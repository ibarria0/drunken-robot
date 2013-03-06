import time
import re
import operator
import praw
import sys
import argparse

r = praw.Reddit('Sr. Trends v0.1')
words = []

class Word:
  def __init__(self, marker, raw):
    self.marker = marker
    self.raw = raw

def print_words(words):
  for word in words[:100]:
    print word[0] + " " +  str(word[1])

def rank_words(words):
  h = {}
  for word in words:
    try:
      if h.has_key(word):
        v = h.get(word)
        h.update({word: v + 1})
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
            words.extend(comment.body.split())
          except AttributeError:
            print "comment with no body"
      rank_words(words)
      time.sleep(1800)
main()
