#noskaidrot, vai ievadītais vārds ir sarakstā.

skoleni=["Anna", "Jānis", "Laura", "Mārtiņš", "Elīna"]
mekletais=input("Ievadiet skolēna vārdu; ").strip()
atrasts=False

for skolens in skoleni:
    if skolens.lower()==mekletais.lower():
        atrasts=True
    break
if atrasts:
    print("Skolēna vārds ir sarakstā.")
else:
    print("Sarakstā vārda nav.")