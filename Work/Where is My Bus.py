# Where is My Bus.py
#
# Exercise 1.4
#%%
import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
print(u)
from xml.etree.ElementTree import parse
doc = parse(u)
type(doc)
for pt in doc.findall('.//pt'):
        print(pt.text)
# %%
