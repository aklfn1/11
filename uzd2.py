skoleni= [{"vards" :  "Anna" , "klase" : "10.A" , "vecums" : 16 , "atzime" : 8 },
{"vards" :  "Jānis" , "klase" : "10.B" , "vecums" : 17 , "atzime" : 6 },
{"vards" :  "Marta" , "klase" : "10.A" , "vecums" : 16 , "atzime" : 9 },
{"vards" :  "Roberts" , "klase" : "10.C" , "vecums" : 17 , "atzime" : 7 },
{"vards" :  "Laura" , "klase" : "10.B" , "vecums" : 16 , "atzime" : 10},
{"vards" :  "Kārlis" , "klase" : "10.A" , "vecums" : 17 , "atzime" : 5 },
{"vards" :  "Elīna" , "klase" : "10.A" , "vecums" : 16 , "atzime" : 7 },
{"vards" :  "Rihards" , "klase" : "10.B" , "vecums" : 17 , "atzime" : 9 }]

for skolens in skoleni:
    if skolens["vards"]=="Laura":
        print(skolens)

for skolens in skoleni:
    if skolens["atzime"]>=9:
        print(skolens["vards"])

for skolens in skoleni:
    if skolens["klase"]=="10.A":
        print(skolens["vards"])

print(f"\n")

#Kārtošana pēc atzīmes

sakartoti=sorted(skoleni, key=lambda x: x ["atzime"], reverse=True) #Atslēga ar vērtību, pēc kuras kārto sarakstu , reverse-- no lielākā uz mazāko

for skolens in sakartoti:
   # print(f"{skolens["vards"]}, {skolens['atzime']}")
    print(skolens)


print(f"\n")

#Sakārtot sarakstu pēc vecuma

pec_vecuma=sorted(skoleni, key=lambda x: x ["vecums"])
for skolens in pec_vecuma:
    print(skolens)

    