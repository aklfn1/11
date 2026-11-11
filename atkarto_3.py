vertejumi={
    "Matematika" : 8,
    "Latviesu_valoda" : 7,
    "Anglu_valoda" : 8,
    "Programmesana" : 9,
    "Vesture" : 6


}

print("=" *50 )
print(f" SKOLĒNA SEKMES")
print("=" *50, "\n")

for prieksmets, atzime in vertejumi.items():
    print(f"{prieksmets:<15} : {atzime:>2}")


#vid augstaka labakais prieksmets

print("\n" ,"=" *50,)

videja_atzime=(sum(vertejumi.values()))/len(vertejumi.items())
print(f"Vidējā atzīme ir {videja_atzime}")
vertejumi.values()

augstaka_atzime=(max(vertejumi.values()))
print(f"Augstākā atzīme ir {augstaka_atzime}")

labakais_prieksmets=max(vertejumi, key=vertejumi.get)
print(f"Labākais priekšmets ir {labakais_prieksmets}")

'''
for key, value in vertejumi.items():
    if value==augstaka_atzime:
        labakais_prieksmets=(key)
        print(f"Labākais priekšmets ir {labakais_prieksmets}")

'''

print("=" *50, "\n" )