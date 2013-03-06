import time
import re
import operator
import praw

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

while True:
    subreddit = r.get_subreddit('trees')
    comments = subreddit.get_comments(limit=500)
    for comment in  comments:
        try: 
          words.extend(comment.body.split())
        except AttributeError:
          print "comment with no body"
    rank_words(words)
    time.sleep(1800)
