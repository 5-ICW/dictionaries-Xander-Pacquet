personen = [
    {"titel": "HarryPotter", "aurteur": "Jk rowling","release date": 2020},
    {"titel": "Trhown Of glass", "auteur": "Dekesel","release date": 2018},
    {"titel": "leven van een loser", "auteur": "XenXheka","release date": 2024}
]

def titel(persoon):
    for i in persoon:
        print(i["titel"])


(titel(personen))

