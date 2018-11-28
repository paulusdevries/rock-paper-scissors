def print_dict(dictionary):
    for key,val in dictionary.items():
        print(f'Ik ben {key}, en ik woon in {val}')

def wpl_count(dictionary):
    wpls = list(dictionary.values())
    for wpl in set(wpls):
        num = wpls.count(wpl)
        print(f'Er wonen {num} namen in {wpl}')

naw = {}

while True:
    naam = input('Je naam: ')
    wpl = input('Je woonplaats: ')

    meer = input('wil je nog meer invullen? (j/n)')
    naw[naam] = wpl
    if meer == 'j':
        continue
    else:
        break

#print_dict(naw)
wpl_count(naw)
