import csv
'''
with open("Skoleni.csv", "r", encoding="utf-8-sig") as datne:
    lasitajs=csv.reader(datne, delimiter=",")

    for rinda in lasitajs:

        print(rinda)
          '''

#Izmantojot galvenes funkciju next() sakārtot datus pēc parauga

with open("Skoleni.csv", "r", encoding="utf-8-sig") as datne:
    lasitajs=csv.reader(datne, delimiter=",")

    galvene=next(lasitajs)
    print("="*40)
    print("          Skolēnu vērtējumi")
    print("="*40)

   

    for rinda in lasitajs:
        vards=rinda[0]
        klase=rinda[2]
        atzime=rinda[3]


        print(f"Vārds: {vards:<10} | Klase: {klase} | Atzīme: {atzime:>2}")
        
    print("="*40)

#Aprēķināt visu atzīmju vidējo vērtību

    summa=0
    atzimes=[]
    for rinda in lasitajs:
        atzime=rinda[3]
        atzimes.append(atzime)
        print(atzimes)

        sum(atzimes)