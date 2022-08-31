print("Du befinner dig i ett mörkt rum i drakborgen ")
print("framför dig har du tre dörrar , välje ne av dem ")
spelVal = input("välje 1, 2, eller 3 !")
if spelVal == "1":
    print("du har hittat en skattiska, Du är rik ")
    print("GAME OVER! Du vann!")
elif spelVal == "2":
    print("dörren öppmna och etteklat troll slår dig med sin klubba!")
    print("GAME OVER! DU förlorade!")
elif spelVal == "3":
    print("Du går i rummet och ser en sovande drak!")
    print("draken vaknar och äter upp dig.Du smakar jättgott!")
    print("GAME OVER ! Du förlorade!")
else:
    print("du måste svara 1 ,2 eller 3")
print("kör speal en gång till!")

