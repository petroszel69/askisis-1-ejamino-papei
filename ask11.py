import json
import math
from urllib.request import Request, urlopen

total_rounds = 20

def find_last_round():

    req = Request('https://drand.cloudflare.com/public/latest',
                  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = json.loads(urlopen(req).read())
    return data['round']


def find_randoms(last):
    req = Request('https://drand.cloudflare.com/public/'+str(last),
                  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = json.loads(urlopen(req).read())
    return data['randomness']


def populate_values(values,new_random):
    for i in range(0, len(new_random)):
        pointer = int(new_random[i],16)
        values[pointer] +=1
    return values


def calculate_entropy(value, total):
    probability = value/total
    return probability*math.log10(probability)




entropy = 0 #edo tha apothikeusoume tin entropia
values = [0] * 16 # o pinakas pou kratai tis times emfanisis kathe dekaejadikou cifiou
total_digits = 0 #o sinolikos arithmos ton cifion

# euresi tou teleuteou girou
last_round = find_last_round()
print("ο τελευταίος γύρος είναι ο: " + str(last_round))

# pernoume tis 20 teleutees times
for round in range (last_round - total_rounds + 1, last_round+1):
  new_random = find_randoms(round)
  print("Η τυχαία τιμή στον γύρο " + str(round) + " είναι η: " + str(new_random))
  total_digits = total_digits + len(new_random)

  # gia kathe timi, upologismos text kai enimerosi tou values[]
  values = populate_values(values, new_random)

# ektiposi tis entropias kathe xaraktira
print("Εντροπία ανά χαρακτήρα:")
for character in range(0,16):
  entropy -= calculate_entropy(values[character], total_digits)
print("Η εντροπία, λαμβάνοντας υπόψιν " + str(total_rounds) + " τυχαία αλφαριθμητικά, είναι: " + str(entropy))