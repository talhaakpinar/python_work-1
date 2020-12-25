birler = ["", "bir", "iki", "uc", "dort", "bes", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kırk"," elli", "altmıs", "yetmis", "seksen", "doksan"]

def okunus(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10
    return onlar[ikinci] + " " + birler[birinci]

sayı =  int(input("Sayı:"))

print(okunus(sayı))