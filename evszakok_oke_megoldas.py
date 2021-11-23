class Evszak:
    def __init__(self, nev, honapok):
        self.Nev = nev
        self.Honapok = honapok

ev = [
    Evszak('tavasz', ['március',    'április', 'május'    ]),
    Evszak('nyár',   ['júnuis',     'július',  'augusztus']),
    Evszak('ősz',    ['szeptember', 'október', 'november' ]),
    Evszak('tél',    ['december',   'január',  'február'  ])
    ]

keresett_honap = input('írd be egy hónap nevét: ')
i = 0
while keresett_honap not in ev[i].Honapok:
    i += 1

print(f'{keresett_honap} {ev[i].Nev} évszakban van')