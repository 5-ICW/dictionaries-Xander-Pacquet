def frequentie_tekens(zin):
    frequentie = {}
    for teken in zin:
        if teken in frequentie:
            frequentie[teken] += 1
        else:
            frequentie[teken] = 1
    return frequentie



zin = input('geef een woord in: ')
print(frequentie_tekens(zin))