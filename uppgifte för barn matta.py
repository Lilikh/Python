import random
print("5 matte-uppgifter till småbarn")
print("================================\n")
print("programmet avsluta om man skriver 0")
for x in range(3):
 tal1=random.randint(1,10)
 tal2=random.randint(1,10)
 while True:
  uppgift=str(tal1)+"+"+str(tal2)+"="
  svar=int(input(uppgift))
  if svar== tal1+tal2:
   print("Rätt savr!")
   break;
  else:
   print("Nästan rätt,försök igen!")
print("Hejdå!")

