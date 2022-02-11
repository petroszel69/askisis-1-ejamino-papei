import random

def kapcheck(k):
  global kapleftmikra
  global kapleftmesea
  global kapleftmegala
  if k==1 and kapleftmikra > 0:
    kapleftmikra-=1
    return True
  elif k==2 and kapleftmesea > 0:
    kapleftmesea-=1
    return True
  elif k==3 and kapleftmegala > 0:
    kapleftmegala-=1
    return True
  else:
    return False

thesis=["th1","th2","th3","th4","th5","th6","th7","th8","th9"]
# 1=mikra 2=mesea 3=megala
kapakia=[1,2,3]
smoves=0

for i in range(100):
  # kathe fora oles i thesis tha midenizonte (adiazoun)
  th1=0
  th2=0
  th3=0
  th4=0
  th5=0
  th6=0
  th7=0
  th8=0
  th9=0
  # oi kinisis tis partidas
  moves=0
  telospart = False
  kapleftmikra=9
  kapleftmesea=9
  kapleftmegala=9
  while telospart != True:
    thes= random.choice(thesis)
    kap= random.choice(kapakia)
    if thes=="th1":
      if th1==0:
        if kapcheck(kap):
          th1=kap
          moves+=1
      elif th1==1 and kapcheck(kap) and kap>1:
        th1=kap
        moves+=1
      elif th1==2 and kapcheck(kap) and kap>2:
        th1=kap
        moves+=1

    elif thes=="th2":
      if th2==0:
        if kapcheck(kap):
          th2=kap
          moves+=1
      elif th2==1 and kapcheck(kap) and kap>1:
        th2=kap
        moves+=1
      elif th2==2 and kapcheck(kap) and kap>2:
        th2=kap
        moves+=1

    elif thes=="th3":
      if th3==0:
        if kapcheck(kap):
          th3=kap
          moves+=1
      elif th3==1 and kapcheck(kap) and kap>1:
        th3=kap
        moves+=1
      elif th3==2 and kapcheck(kap) and kap>2:
        th3=kap
        moves+=1

    elif thes=="th4":
      if th4==0:
        if kapcheck(kap):
          th4=kap
          moves+=1
      elif th4==1 and kapcheck(kap) and kap>1:
        th4=kap
        moves+=1
      elif th4==2 and kapcheck(kap) and kap>2:
        th4=kap
        moves+=1

    elif thes=="th5":
      if th5==0:
        if kapcheck(kap):
          th5=kap
          moves+=1
      elif th5==1 and kapcheck(kap) and kap>1:
        th5=kap
        moves+=1
      elif th5==2 and kapcheck(kap) and kap>2:
        th5=kap
        moves+=1

    elif thes=="th6":
      if th6==0:
        if kapcheck(kap):
          th6=kap
          moves+=1
      elif th6==1 and kapcheck(kap) and kap>1:
        th6=kap
        moves+=1
      elif th6==2 and kapcheck(kap) and kap>2:
        th6=kap
        moves+=1

    elif thes=="th7":
      if th7==0:
        if kapcheck(kap):
          th7=kap
          moves+=1
      elif th7==1 and kapcheck(kap) and kap>1:
        th7=kap
        moves+=1
      elif th7==2 and kapcheck(kap) and kap>2:
        th7=kap
        moves+=1

    if thes=="th8":
      if th8==0:
        if kapcheck(kap):
          th8=kap
          moves+=1
      elif th8==1 and kapcheck(kap) and kap>1:
        th8=kap
        moves+=1
      elif th8==2 and kapcheck(kap) and kap>2:
        th8=kap
        moves+=1

    if thes=="th9":
      if th9==0:
        if kapcheck(kap):
          th9=kap
          moves+=1
      elif th9==1 and kapcheck(kap) and kap>1:
        th9=kap
        moves+=1
      elif th9==2 and kapcheck(kap) and kap>2:
        th9=kap
        moves+=1
#edo telionoume me tin topothetisi ton kapakion
#kai arxizoume ton elenxo gia na teliosi i partida
#proti sira orizontia
    if th1!=0 and th2!=0 and th3!=0:
      if th1==1 and th2==1 and th3==1:
        telospart = True
      elif th1==2 and th2==2 and th3==2:
        telospart = True
      elif th1==3 and th2==3 and th3==3:
        telospart = True
      elif th1==1 and th2==2 and th3==3:
        telospart = True
      elif th1==3 and th2==2 and th3==1:
        telospart = True
#deuteri sira orizontia
    if th4!=0 and th5!=0 and th6!=0:
      if th4==1 and th5==1 and th6==1:
        telospart = True
      elif th4==2 and th5==2 and th6==2:
        telospart = True
      elif th4==3 and th5==3 and th6==3:
        telospart = True
      elif th4==1 and th5==2 and th6==3:
        telospart = True
      elif th4==3 and th5==2 and th6==1:
        telospart = True
#triti sira orizontia
    if th7!=0 and th8!=0 and th9!=0:
      if th7==1 and th8==1 and th9==1:
        telospart = True
      elif th7==2 and th8==2 and th9==2:
        telospart = True
      elif th7==3 and th8==3 and th9==3:
        telospart = True
      elif th7==1 and th8==2 and th9==3:
        telospart = True
      elif th7==3 and th8==2 and th9==1:
        telospart = True
#proti sira katheta
    if th1!=0 and th4!=0 and th7!=0:
      if th1==1 and th4==1 and th7==1:
        telospart = True
      elif th1==2 and th4==2 and th7==2:
        telospart = True
      elif th1==3 and th4==3 and th7==3:
        telospart = True
      elif th1==1 and th4==2 and th7==3:
        telospart = True
      elif th1==3 and th4==2 and th7==1:
        telospart = True
#deuteri sira katheta
    if th2!=0 and th5!=0 and th8!=0:
      if th2==1 and th5==1 and th8==1:
        telospart = True
      elif th2==2 and th5==2 and th8==2:
        telospart = True
      elif th2==3 and th5==3 and th8==3:
        telospart = True
      elif th2==1 and th5==2 and th8==3:
        telospart = True
      elif th2==3 and th5==2 and th8==1:
        telospart = True
#triti sira katheta
    if th3!=0 and th6!=0 and th9!=0:
      if th3==1 and th6==1 and th9==1:
        telospart = True
      elif th3==2 and th6==2 and th9==2:
        telospart = True
      elif th3==3 and th6==3 and th9==3:
        telospart = True
      elif th3==1 and th6==2 and th9==3:
        telospart = True
      elif th3==3 and th6==2 and th9==1:
        telospart = True
#proti sira diagonia
    if th1!=0 and th5!=0 and th9!=0:
      if th1==1 and th5==1 and th9==1:
        telospart = True
      elif th1==2 and th5==2 and th9==2:
        telospart = True
      elif th1==3 and th5==3 and th9==3:
        telospart = True
      elif th1==1 and th5==2 and th9==3:
        telospart = True
      elif th1==3 and th5==2 and th9==1:
        telospart = True
#deuteri sira diagonia
    if th3!=0 and th5!=0 and th7!=0:
      if th3==1 and th5==1 and th7==1:
        telospart = True
      elif th3==2 and th5==2 and th7==2:
        telospart = True
      elif th3==3 and th5==3 and th7==3:
        telospart = True
      elif th3==1 and th5==2 and th7==3:
        telospart = True
      elif th3==3 and th5==2 and th7==1:
        telospart = True
#elenxos gia na teliosi i partida se periptosi pou mas teliosoun ta kapakia
    if kapleftmikra==0 and kapleftmesea==0 and kapleftmegala==00:
      telospart = True
  smoves+=moves
print("o mesos oros ton kiniseon gia na teliosi i partida einai:",smoves/100,"kinisis")
