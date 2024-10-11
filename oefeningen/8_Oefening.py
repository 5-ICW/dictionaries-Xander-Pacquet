resultaten = [
    {"naam": "Xander", "score": "99",},
    {"naam": "Jarne", "score": "30"},
    {"naam": "Xen", "score": "69"}
]

def hoogste_score(score):
    for i in score:
        if score > 60:
            return i[score]
        else:
            return "niet verwacht"
       


print(hoogste_score(resultaten))