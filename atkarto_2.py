preces={

"piens" : 1.25,
"maize" : 0.99,
"siers" : 3.49,
"āboli" : 1.80,
"sula" : 2.15



}

kopeja_summa=0

print("=" *20)
print(f"PREČU SARAKSTS")
print("=" *20)

for prece, cena in preces.items():
    print(f"{prece:<6} : {cena:>5.2f} eur")
kopeja_summa+=cena

print("=" *20)
print(f" Kopējā summa ir : {kopeja_summa} ")
print("=" *20)