class Evszak:
    def __init__(self, nev, honapok):
        self.Nev = nev
        self.Honapok = honapok

ev = [
    Evszak('tavasz', ['marcius', 'aprilis', 'majus']),
    Evszak('nyár', ['júnuis', 'július', 'augusztus']),
    Evszak('ősz', ['szeptember', 'október', 'november']),
    Evszak('tél', ['december', 'január', 'fenruár'])]

keresett_honap = input('írd be egy hónap nevét: ')
i = 0
while keresett_honap not in ev[i].Honapok:
    i += 1

print(f'{keresett_honap} {ev[i].Nev} évszakban van')