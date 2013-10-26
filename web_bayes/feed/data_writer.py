from web_bayes.util.file_util import get_parent
import os.path

import logging
log = logging.getLogger(__name__)

__HERE__ = os.path.dirname(__file__)
DATA_ROOT = os.path.join(get_parent(__HERE__, 2), 'train')
ENTRY_DELIMITER = "\n----\n"

def write_entry(file_path, data):
    """
    Writes data to specified file path,
    appending a delimiter if necessary
    """
    new_file = not os.path.exists(file_path)
    print(str(new_file))
    handler = open(file_path, 'w' if new_file else 'a')
    if not new_file:
        handler.write(ENTRY_DELIMITER)
    handler.write(data.encode('UTF-8'))
    print open(file_path, 'r').read()
    print "-"*40
    print "\n"

def get_path(label, name):
    """
    Returns path to file for label and name of feed
    """
    return reduce(lambda directory, path: os.path.join(directory, path),
                  [DATA_ROOT, label, name])
    
