#  Ogrenci No: 22100011074
#  Ad-Soyad: Sude Özsoy

while 0==0:
    print('\n-------------------------------------------')
    print('   1-Ikilik tabandan onluk tabana çevirme \n   2-Onluk tabandan ikilik tabana çevirme \n   3-Cıkış')
    secim=int(input('Secim yapin:'))
    if secim == 1:
        while 0 == 0:                               #ikilik sistemden sayi girilmediginde yeniden sayi istenmesi icin sonsuz dongu.
            sayi = int(input('Sayiyi girin:'))
            kontrol = sayi
            while kontrol != 0:
                bas = kontrol % 10                  #son basamagın kontrolu icin mod 10unu aldim.
                if bas != 0 and bas != 1:           #eger son basamak 1 ve 0'dan herhangi biri degilse ikilik sisteme uymadıgını gosterir.
                    break                           #ikilik sisteme uymadigi icin tekrar sayi istemesi icin donguden cikar.
                else:
                    kontrol = kontrol // 10         #sayinin son basamagi ikilige uyuyorsa bi sonraki basamaga gecmesi icin 10'a bolunur.
                    continue
            if kontrol == 0:                        #tum basamaklar kontrol edilmis ve dogru girilmis oldugu belirlenir.
                break
        i = 0                                       #kacıncı basamakta olundugu hesap edilmesi icin sifirdan baslatilir.
        onluk = 0
        while sayi != 0:
            kalan = sayi % 10                       #sayinin son basamagi alinir.
            onluk += kalan * (2 ** i)               #onluga cevirmek icin son basamak uzerinde gerekli islem yapilir.
            sayi = sayi // 10                       #bir sonraki basamak icin 10'a bolumunden tam kismi alinir.
            i += 1
        print('İstenen sayi onluk tabana çevrilmiştir: {}'.format(onluk))
        print('***Ana menuye yonlendiriliyorsunuz***')
    elif secim == 2:
        sayi = int(input('Sayiyi girin:'))
        ikilik = 0
        bas = 1                                    #istenen basamaga ulasmasi icin 1'den baslattim.
        while sayi != 0:
            ters = sayi % 2
            ters = ters * bas                      #sayinin mod2'sinin tersine cevrilmis hali bulunmasi icin basamak sayisina gore carpilir.
            sayi = sayi // 2
            ikilik += ters                         #her seferinde bulunan sayilar toplanir ve ters haline ulasilir.
            bas *= 10                              #bir sonraki basamagin islemleri icin basamak 10'la carpilir.
        print('İstenen sayi ikilik tabana çevrilmiştir: {}'.format(ikilik))
        print('***Ana menuye yonlendiriliyorsunuz***')
    elif secim == 3:
        break
    else:
        print('Yanlis secim yaptiniz! Tekrar deneyin.')
