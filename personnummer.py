pnr = input("Ange personnummer på formen ÅÅMMDDNNNN :")
nr =[None]*10
maxD = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
for i in range(len(pnr)):
    nr[i] = ord(pnr[i])-48
year = nr[0] * 10 + nr[1];
mon = nr[2] * 10 + nr[3];
dag = nr[4] * 10 + nr[5];
if year % 4 == 0:
     maxD[1] = 29; #Skottår, feb har 29 dagar
if mon < 1 or mon > 12 or dag < 1 or dag > maxD[mon - 1]:
     print("Ogiltigt födelsedatum")
else:
     summa = 0
     for n in range(len(pnr)-1):
         if n % 2 == 0:
             tmp = 2*nr[n]
             if tmp >9:
                 tmp = tmp -9
             summa += tmp
         else:
              summa += nr[n]
     kontroll = 0
     if summa % 10 != 0:
         kontroll = 10 -(summa % 10)
     if kontroll == nr[9]:
         if nr[8] % 2 == 0:
             print("Damen har ett korrekt personnummer")
         else:
             print("Herrn har ett korrekt personnummer")
     else:
         print("Ogiltigt personnummer")