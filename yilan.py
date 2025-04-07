import pygame
import time
import random

# Pygame başlatma
pygame.init()

# Renkler
beyaz = (255, 255, 255)
siyah = (0, 0, 0)
kirmizi = (213, 50, 80)
yesil = (0, 255, 0)
mavi = (50, 153, 213)

# Ekran boyutları
genislik = 600
yukseklik = 400

# Ekran oluşturma
dislay = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption('Yılan Oyunu')

# Saat
saat = pygame.time.Clock()

# Yılan özellikleri
yilan_block = 10
yilan_hiz = 15

# Yazı fontları
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Skor gösterme
def skor_goster(score):
    deger = score_font.render("Skor: " + str(score), True, siyah)
    dislay.blit(deger, [0, 0])

# Yılanı çizme
def yilan_ciz(yilan_block, yilan_listesi):
    for x in yilan_listesi:
        pygame.draw.rect(dislay, yesil, [x[0], x[1], yilan_block, yilan_block])

# Mesaj yazma
def mesaj(yazı, renk):
    mesaj_ekrani = font_style.render(yazı, True, renk)
    dislay.blit(mesaj_ekrani, [genislik / 6, yukseklik / 3])

# Ana oyun fonksiyonu
def oyun():
    oyun_bitti = False
    oyun_kapanma = False

    # Yılan başlangıç koordinatları
    x1 = genislik / 2
    y1 = yukseklik / 2

    # Yılan hareketi için değişkenler
    x1_hareket = 0
    y1_hareket = 0

    yilan_listesi = []
    uzunluk_yilan = 1

    # Yiyecek koordinatları
    yemek_x = round(random.randrange(0, genislik - yilan_block) / 10.0) * 10.0
    yemek_y = round(random.randrange(0, yukseklik - yilan_block) / 10.0) * 10.0

    while not oyun_bitti:

        while oyun_kapanma:
            dislay.fill(mavi)
            mesaj("Kaybettiniz! Q-Quit veya C-Yeni Oyun", kirmizi)
            skor_goster(uzunluk_yilan - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        oyun_bitti = True
                        oyun_kapanma = False
                    if event.key == pygame.K_c:
                        oyun()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                oyun_bitti = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_hareket = -yilan_block
                    y1_hareket = 0
                elif event.key == pygame.K_RIGHT:
                    x1_hareket = yilan_block
                    y1_hareket = 0
                elif event.key == pygame.K_UP:
                    y1_hareket = -yilan_block
                    x1_hareket = 0
                elif event.key == pygame.K_DOWN:
                    y1_hareket = yilan_block
                    x1_hareket = 0

        if x1 >= genislik or x1 < 0 or y1 >= yukseklik or y1 < 0:
            oyun_kapanma = True
        x1 += x1_hareket
        y1 += y1_hareket
        dislay.fill(mavi)
        pygame.draw.rect(dislay, siyah, [yemek_x, yemek_y, yilan_block, yilan_block])
        yilan_baslangic = []
        yilan_baslangic.append(x1)
        yilan_baslangic.append(y1)
        yilan_listesi.append(yilan_baslangic)
        if len(yilan_listesi) > uzunluk_yilan:
            del yilan_listesi[0]

        for x in yilan_listesi[:-1]:
            if x == yilan_baslangic:
                oyun_kapanma = True

        yilan_ciz(yilan_block, yilan_listesi)
        skor_goster(uzunluk_yilan - 1)

        pygame.display.update()

        # Yılan yemek yediğinde
        if x1 == yemek_x and y1 == yemek_y:
            yemek_x = round(random.randrange(0, genislik - yilan_block) / 10.0) * 10.0
            yemek_y = round(random.randrange(0, yukseklik - yilan_block) / 10.0) * 10.0
            uzunluk_yilan += 1

        saat.tick(yilan_hiz)

    pygame.quit()
    quit()

# Oyunu başlat
oyun()
