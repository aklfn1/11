import csv

vards=input("Ievadiet vārdu:")
vecums=input("Ievadiet vecumu:")
klase=input("Ievadiet klasi:")
vertejums=int(input("Ievadiet vērtējumu:"))

with open("skoleni.csv", "a", newline="", encoding="utf-8-sig") as datne:
    rakstitajs=csv.writer(datne)

    #rakstitajs.writerow(['Pēteris', 18, '10C', 6])
    rakstitajs.writerow([vards, vecums, klase, vertejums])

#vards-> nav tukšs,
#vecums-> 1...100
#klase-> [10A, 10B, 10C, 10D]
#vertejums-> NO 1-10 +int

