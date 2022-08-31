vd=["mån","tis","ond","tor","fre","lör","sön"]
maxD=[31,28,31,30,31,30,31,30,31,31,30,31,30,31]
mon=["jan","feb","mar","apr","maj","jun","jul","aug","sep","okt","nov","dec"]
m=int(input("Vilken månad vill du se\nAnge med en siffra [1-12]:"))
start=6
if (m>1):
    for i in range(m-1):
        start=start+maxD[i]
print()
print(mon[m-1].upper(),"2023")
for i in range(maxD[m-1]):
    print(vd[(start+i)%7],(i+1),mon[m-1])
    if (start+i)%7 ==6:
        print("-----------")

