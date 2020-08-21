import urllib.request, urllib.parse, urllib.error
import json
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum=0
address = input('Enter location: ')
url = address
uh = urllib.request.urlopen(url)
data = uh.read().decode()
info = json.loads(data)
print('Retrieving', url)
print('Retrieved', len(data), 'characters')
print('Count: ', len(info["comments"]))
i=0
while i<len(info["comments"]):
    sum=sum+info["comments"][i]["count"]
    i=i+1
print(sum)