#!/usr/bin/env python

import os, re, sqlite3, sys
from bs4 import BeautifulSoup, NavigableString, Tag

version = sys.argv[1]

docset_path = 'django-rest-framework-%s.docset' % version

print(docset_path)

db = sqlite3.connect('%s/Contents/Resources/docSet.dsidx' % docset_path)
cur = db.cursor()

try:
    cur.execute('DROP TABLE searchIndex;')
except:
    pass

cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

docpath = '%s/Contents/Resources/Documents' % docset_path

page = open(os.path.join(docpath,'index.html')).read()
soup = BeautifulSoup(page, features="html.parser")

any = re.compile('.*')
for tag in soup.find_all('a', {'href':any}):
    name = tag.text.strip()
    if len(name) > 0:
        path = tag.attrs['href'].strip()
        if path.split('/')[0] in ['tutorial', 'api-guide', 'topics']:
            if '#' in path:
                parts = path.split('#')
                path = '%s.html#%s' % (
                    parts[0] if parts[0][-1] != '/' else parts[0][:-1], parts[1])
                path = path.replace('/#', '.html#')
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Guide', path))
            print 'name: %s, path: %s' % (name, path)

db.commit()
db.close()
