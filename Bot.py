from nltk.corpus import stopwords
import nltk
import time
import re
import operator
import sys
import praw

extra_stopwords = ["wont","would","youve","youre","dont", "cant","im", "didnt", "aint", "id", "ive"]

class Bot:

  def __init__(self,subreddit,limit):
    self.useragent = "drunken-robot v0.2"
    self.words = []
    self.urls = []
    self.comments = []
    self.already_done =[]
    self.subreddit = subreddit
    self.limit = limit
    ## setup praw
    try:
      self.r = praw.Reddit(self.useragent)
    except:
      raise Exception("Something went wrong with PRAW")

  def scrape_comments(self):
    subreddit = self.r.get_subreddit(self.subreddit)
    return subreddit.get_comments(limit=self.limit)

  def filter_comment(self,comment):
    text = comment.body.lower().encode('ascii', 'ignore')
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    words = re.sub("\.|,|;|:|'|\*|-|!|\?|\"|[)]|[(]","" , text ).split()
    important_words = filter(lambda x: x not in stopwords.words('english') and x not in extra_stopwords, words)
    self.words.extend(important_words)
    self.urls.extend(urls)
  
  def crunch_comments(self,comments):
    for comment in comments:
      if (comment.id not in self.already_done):
        self.filter_comment(comment)
        self.already_done.append(comment.id)
        self.comments.append(comment)

  def status(self):
    print "############################################"
    print "Bot status"
    print "Total Words: " + str(len(self.words))
    print "Total Comments: " + str(len(self.comments))
    print "Total Urls: " + str(len(self.urls))
    print "############################################"
    for word,times in nltk.FreqDist(self.words).items():
      if (times > 1):
        print word + " " +  str(times)
    for url,times in nltk.FreqDist(self.urls).items():
      print url + " " + str(times)

  def status_short(self):
    print "short status report:"
    for word,times in nltk.FreqDist(self.words).items()[:10]:
      if (times > 1):
        print word + " " +  str(times)
    for url,times in nltk.FreqDist(self.urls).items()[:5]:
      print url + " " + str(times)

  def start(self):
    while True:
      self.crunch_comments(self.scrape_comments())
      self.status_short()
      time.sleep(100)
