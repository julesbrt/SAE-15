import pandas as pd

df = pd.read_csv('../../data/processed/resultat.csv')
SF = df['SF']

#Calcul du temps moyen de transmission :

def ComputeMean():
    a = 0
    i = 0
    c = 0
    mean = 0

    for a in SF:
        c += a
        i += 1

    pmean = c/i
    mean = round(pmean,2)
    print(f'Le temps moyen de transmission est de : {mean}')
    return (mean)

ComputeMean()

#Calcul du temps médian de transmission :

def ComputeMedian():

    tab_SF = []
    median_SF = 0

    for i in SF:
        tab_SF.append(i)

    tab_SF.sort()
    a = len(tab_SF) / 2
    median_SF = tab_SF[int(a)]

    return median_SF
valeur = ComputeMedian()
print(f'Le temps médian de transmission est de : {valeur}')