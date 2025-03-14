g='Türkiye nin en büyük teknoloji etkinliği TEKNOFEST, bu yil İstanbul da düzenleniyor.'
kelimeler=g.split('')

def donustur(a):
    sayac=[]
    for kelime in a:
        print(kelime)
        sayici=0
        for harf in range(len(kelime)):
            sayici+=1
            print(sayici)
        sayac.append(sayici)
    return sayac

b=donustur(kelimeler)