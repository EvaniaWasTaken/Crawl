# import HTMLSession from requests_html
from requests_html import HTMLSession
import pprint
 
pp = pprint.PrettyPrinter(indent=4)
# create an HTML Session object
session = HTMLSession()
 
# Use the object above to connect to needed webpage
r = session.get('http://python-requests.org/')

dic1 = r.html.absolute_links

r.html.render()

#for html in r.html:
#    print(html)
dic2 = r.html.absolute_links

#pp.pprint(dic1)
for i in dic1:
  if i not in dic2:
    print(i)
print()
print()
print()
print()
