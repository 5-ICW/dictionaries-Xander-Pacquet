persoon = {"naam": "Peters", "voornaam" : "Jos", "leeftijd" : 45, "woonplaats": "stokstraat 13"}
print(persoon["naam"])
print(persoon["voornaam"])
print(persoon["leeftijd"])
print(persoon["woonplaats"])
persoon["beroep"] = "dokter "
print(persoon.get("beroep", "niet gekend"))