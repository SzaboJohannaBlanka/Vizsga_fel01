import random

def feladat01() -> None:
    nev:str = str(input('Írd be kérlek a neved: '))
    kor:int = int(input('Írd be mikor születtél: '))
    karakterek:list[str] = ['@','&','#']

    nev_pasw:str = nev[0].upper() + nev[1:3].capitalize() #javítsd ki, hogy a jelszó az első karakternek adjon .upper-t és a következő 3-nak peddig picit!
    #kor_pasw:int = int(kor[-2:])
    kor_pasw:int = kor % 100  #sajnos buta vagyok hozzá, és még a pysuli-val sem értetem, hogy ez miért jó....... :D
    karakterek_pasw01:str = ''.join(random.choice(karakterek))
    karakterek_pasw02:str = ''.join(random.choice(karakterek))

    jelszo:str = nev_pasw + str(kor_pasw)  + karakterek_pasw01 + karakterek_pasw02 #itt a kor_pasw-nél írt egy hibát, mely ,,can only concatenate str (not "int") to str"

    print(f'És a jelszavad nem más mint: {jelszo}')