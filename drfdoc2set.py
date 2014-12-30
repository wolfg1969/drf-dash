#!/usr/bin/env python

import os, re, sqlite3, sys
from bs4 import BeautifulSoup, NavigableString, Tag 

version_3 = not '--v2' in sys.argv

if version_3:
     docset_path = 'django-rest-framework-3.0.docset'
else:
    docset_path = 'django-rest-framework-2.4.docset'

db = sqlite3.connect('%s/Contents/Resources/docSet.dsidx' % docset_path)
cur = db.cursor()

try: cur.execute('DROP TABLE searchIndex;')
except: pass
cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

docpath = '%s/Contents/Resources/Documents' % docset_path

page = open(os.path.join(docpath,'index.html')).read()
soup = BeautifulSoup(page)

cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', ('Home', 'Guide', 'index.html'))

any = re.compile('.*')
for tag in soup.find_all('a', {'href':any}):
    name = tag.text.strip()
    if len(name) > 0:
        path = tag.attrs['href'].strip()
        if path.split('/')[0] in ['tutorial', 'api-guide', 'topics']:
            if version_3:
                path = path + 'index.html'
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Guide', path))
            print 'name: %s, path: %s' % (name, path)

db.commit()
db.close()
