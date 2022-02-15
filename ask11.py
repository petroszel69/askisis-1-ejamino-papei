from urllib.request import Request, urlopen
from scipy.stats import entropy

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
print(data)

text= str(data)
x= text.split('"randomness":',1)
y= str(x[1])
z= y.split(",",1)
number= int((z[0][-21:-1]),16)
print(z[0][-21:-1])
print(number)
print(hex(number))
entropy(number)