import sys
import argparse
import signal

from Bot import Bot


def validate_args(args):
  if (args.limit < 1) or (args.limit > 1000):
    raise Exception("limit must be between 1 and 1000")
  return args

def parse_args():
  parser = argparse.ArgumentParser(description='Gets trending words in a subreddit.')
  parser.add_argument('subreddit', metavar='subreddit', type=str,help='subreddit to scrape')
  parser.add_argument('limit', type=int, default=100, help="limit amount of comments scraped (max 1000, default 100)")
  return validate_args(parser.parse_args())

def signal_handler(signal, frame):
  print bot.status()
  sys.exit(0)

args = parse_args()
bot = Bot(args.subreddit,args.limit)
signal.signal(signal.SIGINT, signal_handler)
bot.start()
signal.pause()
