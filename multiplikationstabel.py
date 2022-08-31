while True:
    tal=int(input("Ange med en siffra vilken multiplikationstabell du vi se? \n eller tryck 0 för avsluta : "))
    if tal==0:
        break
    for x in range(1,11):
        print(x,"x",tal,"=",(x *tal))
