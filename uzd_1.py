skoleni= [ {"vards" : "Anna" , "klase" : "9.A" , "atzime" : 8 },
          {"vards" : "Jānis" , "klase" : "9.B" , "atzime" : 6},
          {"vards" : "Līga" , "klase" : "9.A" , "atzime" : 9 },
          {"vards" : "Mārtiņš" , "klase" : "9.B" , "atzime" : 7},
          {"vards" : "Elīna" , "klase" : "9.A" , "atzime" : 10}

          ]

#Visi skolēni,  9.a klases skolēni, saskaita skolēnus, aprēķina vidējo, atrod labāko.

print("-" *20)
for skolens in skoleni:
    print(f" {skolens['vards']}, klase; {skolens['klase']}, atzīme; {skolens['atzime']}")

print("-" *20) 

print(f" \n 9. a klases skolēni;")

for skolens in skoleni:
    if skolens["klase"]=="9.A":
        print(f" {skolens["vards"]}")

print("-" *20) 


print(f" \n Kopā ir {len(skoleni)} skolēni.")

atzimes=0

for skolens in skoleni:
    atzimes+=(skolens['atzime'])


videja_atzime=atzimes/len(skoleni)
print(f"Vidējā atzīme ir {videja_atzime:2f}")

labakais=skoleni[0]

for skolens in skoleni:
    if skolens['atzime']>labakais['atzime']:  
        labakais=skolens

print(f"Labākais skolēns ir {labakais['vards']} - {labakais['atzime']}")