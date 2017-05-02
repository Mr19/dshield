#!/usr/bin/env python

"""Site Copy 0.5

Usage:
  sitecopy.py -s SOURCE -u USERAGENT [-d DEST]
  sitecopy.py (-h | --help)
  sitecopy.py (-v | --version)

Options:
  -h --help                           Show this screen
  -v --version                        Show version
  -s SOURCE --source=SOURCE           Select a source website to scrape, e.g: https://www.example.com
  -u USERAGENT --useragent=USERAGENT  Select a useragent
  -d DEST --dest=DEST                 Location to store scraped website

"""

import os
from docopt import docopt

def scrape(values):
    # TODO: Setup destination logic
    cline = 'wget -E -H -k -p --header="Accept: text/html" --user-agent=' + values['--useragent'] + ' ' + values['--source']
    os.system(cline)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Site Copy 0.5')
    scrape(arguments)
