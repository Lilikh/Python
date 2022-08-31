#for x in range(599,299,-2):
   # print(x)

#user_pass = ""

#while user_pass.lower() != "komvux":
   # user_pass = input("Skriv in korrekt losenord: ").lower()
   # if user_pass == "komvux":
        #print("Korrekt!")
    #else:
       # print("Forsok igen!")
#print("Tack for losenordet!")

losen = ["komvux", "Komvux"]
fel = 0
svar = (input("Välkommen till hemliga klubben! Vad är lösenordet? "))
while svar not in losen:
    fel += 1
    print("Fel lösenord nr " + str(fel) + "! Vänligen försök igen.")
    svar = (input("Vad är lösenordet? "))
if svar in losen:
    print("Välkommen in!")