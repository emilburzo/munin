#!/usr/bin/env python2

import sys
from lxml import html
import requests

if len(sys.argv) != 2:
    print "missing url argument"
    sys.exit(1)

page = requests.get(sys.argv[1])
tree = html.fromstring(page.text)

rating = tree.xpath('string(//meta[@itemprop="ratingValue"]/@content)')

print round(float(rating), 2)

