import string

#ta print pou einai se sxolio iparxoun gia logous debugging
'''to arxio test.txt einai apla pio mikro gia na tsekaroume pio grigora
an douleui to programa'''

file= open("test.txt", "r")
#file= open("two_cities_ascii.txt", "r")
f= file.readlines()

lista= []
for line in f:
  lista.append(line.strip())
#print(lista)
#edo tha ftiajoume mia simbolosira me osous xaraxtires mas zitai i askisi
alliwant= string.ascii_uppercase
alliwant+= " "
alliwant+= string.ascii_lowercase
#print(alliwant)

for i in range(0, len(lista)):
  for letter in lista[i]:
    if letter not in alliwant:
      lista[i]= lista[i].replace(letter,"")
      #print(list[i])
#print(lista)

#xorizoume tis lejis me basi to keno
newlist= []
for i in range (0, len(lista)):
  #print(list[i])
  if " " not in lista[i]:
    newlist.append(lista[i])
  else:
    temp= lista[i].split()
    for word in temp:
      newlist.append(word)
#print(newlist)

#edo aferoume zeugaria lejeon pou exoun athrisma 20
for i in range(0,len(newlist)):
  for j in range(0,len(newlist)):
    x= len(newlist[i]) + len(newlist[j])
    #print(x)
    if x == 20:
      newlist[i]= ''
      newlist[j]= ''
#print(newlist)

slej=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0,len(newlist)):
  for j in range(0, len(slej)):
    y= len(newlist[i])
    if y == j+1:
      slej[j]+= 1

for i in range(0, len(slej)):
  print(slej[i], "λέξεις του", i+1, "γράμματος/γραμμάτων")