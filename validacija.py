#vards-> nav tukšs,
#vecums-> 1...100
#klase-> [10A, 10B, 10C, 10D]
#vertejums-> NO 1-10 +int
try:
    vertejums=int(input("Ievadiet vērtējumu; "))

    if vertejums>=1 and vertejums<=10:
        print("Validācija izieta")

    if vertejums<1 or vertejums>10:
        print("Validācija nav izieta")

    while vertejums<1 or vertejums>10:
        print("Nepareizs vērtējums ")
        vertejums=int(input("Ievadiet vērtējumu; "))
        print("Validācija izieta")





    vecums=int(input("Ievadiet vecumu:"))

    if vecums>=1 and vecums<=100:
        print("Validācija izieta")

    if vecums<1 or vecums>100:
        print("Validācija nav izieta")
        
    while vecums<1 or vecums>100:
        print("Neiespējams vecums! ")
        vecums=int(input("Ievadiet vecumu; "))
        print("Validācija izieta")


except ValueError:
    print("Kļūda! Nav ievadīts skaitlis.")

