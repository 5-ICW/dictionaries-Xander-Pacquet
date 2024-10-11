fruit_prijzen = {
    "appel":1,
    "banaan":2,
    "kiwi":2.5,
    "watermeloen":4.0
}

def totaal_prijs(prijzen):
    return sum(prijzen.values())
    

print(f"Totale prijs = {totaal_prijs(fruit_prijzen)}")       