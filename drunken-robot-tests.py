import unittest
import praw
from Bot import Bot

class DrunkenRobotTests(unittest.TestCase):

  def setUp(self):
    self.bot = Bot("trees",10)

  def test_scrape_comments(self):
    comments = self.bot.scrape_comments()
    self.assertIsNotNone(comments, "scrape comments must return something")
    for comment in comments:
      self.assertIsInstance(comment, praw.objects.Comment, 'scrape_comment must return comment objects')

  def test_filter_comment(self):
    comments = self.bot.scrape_comments()
    original_words = self.bot.words
    self.bot.filter_comment(comments.next())
    self.assertEqual(original_words,self.bot.words)

if __name__ == '__main__':
      unittest.main()
