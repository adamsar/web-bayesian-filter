from web_bayes.exception.feed import FeedReadError
from web_bayes.feed import data_writer
import os.path
import feedparser
import nltk

import logging
log = logging.getLogger(__name__)

UNINTERESTING_LABEL = 'uninteresting'
INTERESTING_LABEL = 'interesting'

UNINTERESTING_RSS = 'uninteresting_rss.txt'
INTERESTING_RSS = 'interesting_rss.txt'

def get_entries(feed_url):
    """
    Returns a list of entries for a url linking to an
    RSS or ATOM feed
    """
    try:
        return feedparser.parse(feed_url)['entries']
    except Exception:
        raise FeedReadError("Unable to read and parse {}".format(feed_url))

def get_data(entry):
    """
    Returns sanitized, tokenizable text for an entry from an
    RSS feed
    """
    return "%s %s" % (entry['title'], nltk.clean_html(entry['summary']))

def collect_feed(label, name, url):
    """
    Collects and organizes feed data based on label, name,
    and url
    """
    entries = get_entries(url)
    all_data = map(get_data, entries)
    path = data_writer.get_path(label, name)
    map(lambda d: data_writer.write_entry(path, d), all_data)

    
def process_all_feeds():
    def process_one(label, file_name):
        handler = open(os.path.join(data_writer.DATA_ROOT, file_name), 'r')
        feeds = filter(lambda line: ',' in line, handler.read().split("\n"))
        for feed in feeds:
            rss, fname = feed.split(",")
            collect_feed(label, fname, rss)
    map(lambda l: process_one(l[0], l[1]), [(UNINTERESTING_LABEL,
                                             UNINTERESTING_RSS),
                                            (INTERESTING_LABEL,
                                             INTERESTING_RSS)])
    
