birler = ["", "bir", "iki", "uc", "dort", "bes", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kırk"," elli", "altmıs", "yetmis", "seksen", "doksan"]

def okunus(sayi):
    if (sayi >= 1 and sayi <= 99):
        birinci = sayi % 10
        ikinci = sayi // 10
        print("Sayi: " + onlar[ikinci] + " " + birler[birinci])
    else:
        print("Lütfen ondalıklı bir sayı giriniz")

okunus(int(input("Sayı:")))
