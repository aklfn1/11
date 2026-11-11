
import csv


def vertejums_ievads():

    while True:
        try: 
            vertejums=int(input("Ievadiet vērtējumu; "))
            if 1<=vertejums<=10:
                return vertejums
            else:
                print("Vērtējumam jābūt intervālā no 1-10.")

        except ValueError:
            print("Kļūda! Ievadi veselu skaitli!")

def vecum_ievads():

    while True:
        try: 
            vecums=int(input("Ievadiet vecumu; "))
            if 1<=vecums<=100:
                return vecums
            else:
                print("vecumam jābūt intervālā no 1-100.")

        except ValueError:
            print("Kļūda! Ievadi veselu skaitli!")

def varda_ievade():

    while True:

            vards=(input("Ievadiet vārdu: ")).strip()
            if vards=="":
                print("Vārds netika ievadīts!")
            else:
                return vards

def klases_ievade():
    klases=['10.A' , '10.B', '10.C', '10.D']

    while True:
        klase=input("Ievadiet klasi: ").strip().upper()
        if klase in klases:
            return klase
        else:
            print("Šāda klase nepastāv!")


vards=varda_ievade()
vecums=vecum_ievads()
klase=klases_ievade()
vertejums=vertejums_ievads()


with open("skoleni.csv", "a", newline="", encoding="utf-8-sig") as datne:
    rakstitajs=csv.writer(datne)

    #rakstitajs.writerow(['Pēteris', 18, '10C', 6])
    rakstitajs.writerow([vards, vecums, klase, vertejums])