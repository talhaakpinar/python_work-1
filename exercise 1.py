
def bolunensayibulma(min_sayi , max_sayi , bolunecek_sayi):
    sayilar = []
    toplam = 0
    for x in range(min_sayi, max_sayi):
        if x % bolunecek_sayi == 0:
            sayilar.append(x)
            print(x)

    lenght = len(sayilar)

    print("dizinin uzunluğu :" + str(lenght))


bolunensayibulma(2, 6, 4)

