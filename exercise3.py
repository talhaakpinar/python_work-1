vize1 = int(input("vize 1. sınav notu giriniz: "))
vize2 = int(input("vize 2. sınav notu giriniz: "))
final = int(input("final sınav notu giriniz: "))
if 0 < vize1 < 100 and 0 < vize2 < 100 and 0 < final < 100:
    toplam_not = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)
    if toplam_not >= 90:
        print("harf notunuz: AA")
    elif toplam_not >= 85 and toplam_not < 90:
        print("harf notunuz: BA")
    elif toplam_not >= 80 and toplam_not < 85:
        print("harf notunuz: BB")
    elif toplam_not >= 75 and toplam_not < 80:
        print("harf notunuz: CB")
    elif toplam_not >= 70 and toplam_not < 75:
        print("harf notunuz: CC")
    elif toplam_not >= 65 and toplam_not < 70:
        print("harf notunuz: DC")
    elif toplam_not >= 60 and toplam_not < 65:
        print("harf notunuz: DD")
    elif toplam_not >= 55 and toplam_not < 60:
        print("harf notunuz: FD")
    elif toplam_not < 55:
        print("harf notunuz: FF")
elif (0 > vize1 or 100 < vize1) or (0 > vize2 or 100 < vize2) or (0 > final or 100 < final):
    print("Lütfen 0 ile 100 arasında sayılar giriniz.")
else:
    print("Harf notunuz FF Malesef kaldınız ")
