# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import scraperwiki
import re
import lxml

# <codecell>

f=open("data/raw/Parteienverzeichnis_gem__1_Abs_4_PartG_Stand_2013_10_01.pdf")
pdf=f.read()
f.close()
x=scraperwiki.pdftoxml(pdf)
x

# <codecell>

r=lxml.etree.fromstring(x)

# <codecell>

e=[i.text for i in r.xpath("//text[@font=0]")]
e

# <codecell>

import itertools

# <codecell>

e=[i for i in itertools.ifilter(lambda x: re.match('[0-9][0-9 ][0-9 ".].*?',x),e)
   ]
e

# <codecell>

def take2(x):
    it=(i for i in x)
    r=[i for i in itertools.islice(it,2)]
    while r:
        yield r
        r=[i for i in itertools.islice(it,2)]
        

# <codecell>

parties=[i for i in take2(e)]

# <codecell>

parties=[p[0].split(" ",1)+[p[1]] for p in parties]

# <codecell>

import csv
f=open("data/parties.csv","wb")
w=csv.writer(f)
w.writerow(["Nr.","Bezeichnung","Hinterlegung"])
for p in parties:
    w.writerow([i.encode("utf-8") for i in p])
f.close()

# <codecell>


