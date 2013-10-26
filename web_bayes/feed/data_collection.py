from web_bayes.exception.feed import FeedReadError
from web_bayes.feed import data_writer
import feedparser
import nltk

import logging
log = logging.getLogger(__name__)

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
    return nltk.clean_html(entry['summary'])

def collect_feed(label, name, url):
    """
    Collects and organizes feed data based on label, name,
    and url
    """
    entries = get_entries(url)
    all_data = map(get_data, entries)
    path = data_writer.get_path(label, name)
    map(lambda d: data_writer.write_entry(path, d), all_data)
