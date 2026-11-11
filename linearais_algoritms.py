skaitli=[12,7,25,4,18]

mekletais=4
atrasts= False



'''
for skaitlis in skaitli:
    if skaitlis==mekletais:
        print("Skaitlis ir atrasts.")
        break

    elif skaitlis!=mekletais:
        continue
   
    else:
        print("Skaitlis nav atrasts.")


for skaitlis in skaitli:

    if skaitlis==mekletais:
        atrasts=True
        break

if atrasts:
    print(f"Skaitlis ir atrasts.")
else:
    print("Skaitlis nav atrasts.")

''' 
#Ja ir atrasts, paziņot, kurā pozīcījā tas atrodas.

for i, skaitlis in enumerate(skaitli):
    if skaitlis==mekletais:
            atrasts=True
            
        
   
    
if atrasts:
    print(f"Skaitlis ir atrasts.")
    print(f"Tas atrodas {i+1}. vietā.")
else:
    print("Skaitlis nav atrasts.")
