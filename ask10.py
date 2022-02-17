import string
import math


#ta print se sxolio iparxoun gia logous debugging
#sinisto gia pio clean output na mpei se sxolio to print stin grami 41 (den einai se sxolio epidi to zitai i askisi)


#sinartisi i opio metaferi tous ascii xaraktires se diadikous arithmous
def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return(decimal)   

#file= open("test.txt", "r")
file= open("two_cities_ascii.txt", "r")
f= file.readlines()

lista= []
for line in f:
  lista.append(line.strip())
#print(lista)

#fiaxnoume mia lista me ta diadika cifia
blist= []
for i in range(0, len(lista)):
  blist.append(toBinary(lista[i]))
#print(blist)


#edo thelo na min iparxoun listes mesa se listes opote tis enono se mia megali lista
for i in range(0, len(blist)):
  while type(blist[i]) is list:
    for item in blist[i]:
      blist.append(item)
    blist.remove(blist[i])
#print(blist)


#pernoume ta 2 prota kai 2 teleutea cifia tou kathe arithmou
simbolosira= ""
for i in range(0, len(blist)):
  z= str(blist[i])
  #print(z)
  y= z[0:2] + z[-2:]
  #print(y)
  simbolosira+= y
#print(simbolosira)

#xorizoume tin akolouthia se arithmous ton 16 bit
lbit16= []
#kratame to sinolo ton arithmon gia na broume stin sinexia to pososto
s16bit= 0
while len(simbolosira) >16:
  f= simbolosira[0:16]
  lbit16.append(f)
  s16bit+= 1
  simbolosira= simbolosira[16:]
if len(simbolosira)!= 0:
  lbit16.append(simbolosira)
  s16bit+= 1
#print(lbit16)

for i in range(0, len(lbit16)):
  lbit16[i]= binaryToDecimal(int(lbit16[i]))
#print(lbit16)

#blepoume posi arithmi dierounte akribos me to 2,3,5,7
sd2=0
sd3=0
sd5=0
sd7=0
for i in range(0, len(lbit16)):
  if lbit16[i]% 2 == 0:
    sd2+= 1
  elif lbit16[i]% 3 == 0:
    sd3+= 1
  elif lbit16[i]% 5 == 0:
    sd5+= 1
  elif lbit16[i]% 7 == 0:
    sd7+= 1

print("Το", (sd2/float(s16bit))*100, "% είναι ζυγοί")
print("Το", (sd3/float(s16bit))*100, "% διαιρείται ακριβώς με το 3")
print("Το", (sd5/float(s16bit))*100, "% διαιρείται ακριβώς με το 5")
print("Το", (sd7/float(s16bit))*100, "% διαιρείται ακριβώς με το 7")