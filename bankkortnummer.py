nr=input("Ange bankkortnummer :")
while True:
    if nr.isdigit()==False:
        print("Du ska enbart ange siffror")
        input("skrive again ange kortnummer :")
        break
    antal=len(nr)
    kortnr=[None]*antal
    for n in range(antal):
        kortnr[n]=ord(nr[n])-48
    sum=0
    for x in range(antal-1):
        if x%2==0:
            tmp=2*kortnr[x]
            if tmp>9:
                tmp=tmp-9
            sum +=tmp
        else:
            sum +=kortnr[x]
    kontroll=sum%10
    if kontroll >10:
        kortnr=10-kontroll
    if kortnr[antal-1]==kontroll:
        if kortnr[0]==5:
            print("Korrekt Mastercard-kortnummer")
        elif kortnr[0]==4:
            print("Korrekt Visa kortnummer")
        else:
            print("korrekt bankortnummer")
        break
    else:
        print("olitigt bankortnummer")
        break

