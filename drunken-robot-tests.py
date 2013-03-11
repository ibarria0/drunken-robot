import unittest
import praw
from Bot import Bot

class DummyComment():
  def __init__(self,id,body):
    self.body = body
    self.id = id

class DrunkenRobotTests(unittest.TestCase):

  def setUp(self):
    self.bot = Bot("trees",10)
    self.dummy_comment_1 = DummyComment(1,"bacon")
    self.dummy_comment_2 = DummyComment(2,"pancakes")

  def test_scrape_comments(self):
    comments = self.bot.scrape_comments()
    for comment in comments:
      self.assertIsInstance(comment, praw.objects.Comment, 'scrape_comment must return comment objects')

  def test_filter_comment(self):
    self.bot.filter_comment(self.dummy_comment_1)
    original_words = set(self.bot.words)
    self.bot.filter_comment(self.dummy_comment_2)
    self.assertFalse(original_words == set(self.bot.words),"new words must be added")

  def test_crunch_comments_no_dupes(self):
    comments = self.bot.scrape_comments()
    self.bot.crunch_comments(comments)
    old_total = len(self.bot.comments)
    self.bot.crunch_comments(comments)
    self.assertEquals(old_total,len(self.bot.comments))

if __name__ == '__main__':
      unittest.main()
