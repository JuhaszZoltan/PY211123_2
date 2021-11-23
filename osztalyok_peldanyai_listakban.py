class Tanulo:
    def __init__ (self, nev, kor):
        self.Nev = nev
        self.Kor = kor

egy_db_tanulo = Tanulo('Alap Imre', 18)

print(egy_db_tanulo.Kor)
print(egy_db_tanulo.Nev)

tanulok = []

tanulok.append(Tanulo('Rikárdó', 16))
tanulok.append(Tanulo('Zoli', 14))
tanulok.append(Tanulo('Lukrécia', 15))
tanulok.append(Tanulo('Hektor', 16))

# összes tanuló neve egymás alatt:
for t in tanulok:
    print(t.Nev)

# tanulók átlagéletkora
sum = 0
for t in tanulok:
    sum += t.Kor
print(f"tanulók átlagéletkora: {sum/len(tanulok)}")