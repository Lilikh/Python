zyrkoOrdlista ={"vi":"vg","kommer":"thang","som":"zonv","vänner":"agh","hej":"kodig","får":"zznak"}
svenskIndata =input("skrive ett svenskt ord som ska översätta till zyrko :")
svenskOrd =svenskIndata.lower().split()
zyrkOrd=[]
for ord in svenskOrd:
    if ord in zyrkoOrdlista:
        zyrkOrd.append(zyrkoOrdlista[ord])
    else:
        zyrkOrd.append(ord)
print("Blir på zyrko :"," ".join(zyrkOrd))