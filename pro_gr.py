import pygame
import sys
import random

pygame.init()

kratka=25
ilkrat=20
WYS_PASKA = 25 #wysokość paska z wynikiem gry na górze ekranu
font = pygame.font.SysFont(None, 22) #font do wyswietlania wyniku
szerokosc = kratka * ilkrat
okno = pygame.display.set_mode((szerokosc, szerokosc+WYS_PASKA))
pygame.display.set_caption("Wąż")
kolor =(150, 150, 250)
okno.fill(kolor)
pygame.display.update()


# --- Funkcje rysujące ---
def rysuj_snake_kostka(poz):
    x, y = poz
    pozycja = (x * kratka, y * kratka+WYS_PASKA, kratka, kratka)
    pygame.draw.rect(okno, (150, 255, 0), pozycja)
    if poz==snake[-1]:
        r = kratka//6
        oko1 = (x*kratka+kratka//3,y*kratka+WYS_PASKA+kratka//3)
        oko2 = (x*kratka+2*kratka//3,y*kratka+WYS_PASKA+kratka//3)
        pygame.draw.circle(okno,(0,0,0),oko1,r)
        pygame.draw.circle(okno,(0,0,0),oko2,r)
    
def rysuj_kolo(poz):
    x, y = poz
    r = kratka // 2
    pozycja = (x * kratka + r, y * kratka+WYS_PASKA + r)
    pygame.draw.circle(okno, (225, 0, 0), pozycja, r)
        
def rysuj_snake(snake):
    for kostka in snake:
        rysuj_snake_kostka(kostka)

    
def czyszczenie():
    okno.fill(kolor)
    
def rysuj(snake, kolo):
    czyszczenie()
    rysuj_wynik()
    rysuj_snake(snake)
    rysuj_kolo(kolo)
    pygame.display.update()


def ekran_game_over():
    font = pygame.font.SysFont(None, 50)
    small_font = pygame.font.SysFont(None, 30)
    rysuj_wynik() 
    while True:
       # okno.fill((100, 0, 0))
       #powyższe zostało zastąpine, aby nie zakrywać linijki z wynikiem 
        pygame.draw.rect(okno, (100, 0, 0), (0, WYS_PASKA, szerokosc, szerokosc))
        tekst = font.render("GAME OVER", True, (255, 255, 255))
        guzik_koniec = small_font.render("K - Koniec gry", True, (255, 255, 255))
        guzik_nowa = small_font.render("N - Nowa gra", True, (255, 255, 255))
        okno.blit(tekst, (szerokosc//2 - tekst.get_width()//2, 100))
        okno.blit(guzik_nowa, (szerokosc//2 - guzik_nowa.get_width()//2, 200))
        okno.blit(guzik_koniec, (szerokosc//2 - guzik_koniec.get_width()//2, 250))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_n:
                    
                    reset_gry()
                    return

# --- Funkcja resetu gry ---
def reset_gry():
    global snake, kierunek, kolo, pauza, temp_FPS

    pauza = False
    
    temp_FPS = False
    start_x = random.randint(0, ilkrat - 10)
    start_y = random.randint(0, ilkrat - 10)

    snake = [(start_x , start_y) ]
    

    kierunek = "PRAWO"

    while True:
        kolo = (random.randint(0, ilkrat - 1),
                random.randint(0, ilkrat - 1))
        if kolo not in snake: #to pilnuje zeby jedzenie nie pojawiło sie na wezu
            break

#funkcja wyswietlajaca wynik gry na górze ekranu
def rysuj_wynik():
    # tło paska
    pygame.draw.rect(
        okno,
        (50, 150, 50),
        (0, 0, szerokosc, WYS_PASKA)
    )

    wynik = f"Twój wynik: {len(snake)-1}"
    tekst = font.render(wynik, True, (255, 255, 255))

    # wyśrodkowanie w poziomie i pionie
    x = (szerokosc - tekst.get_width()) // 2
    y = (WYS_PASKA - tekst.get_height()) // 2

    okno.blit(tekst, (x, y))

# --- Dane początkowe ---
#snake = [(2,2), (3,2), (4,2), (5,2), (5,1)]
#kolo = (11, 14)

#losujemy początkowe położenie weza i jedzenia wywołłując gunkcje reset_gry
reset_gry()
kierunek = "PRAWO"  # domyślny kierunek
#FPS = 3 # szybkość ruchu
clock = pygame.time.Clock()
pauza = False
temp_FPS =False
temp_snake=1
ruch_wykonany = False



# --- Główna pętla ---
if __name__ == "__main__":
    while True:
        if len(snake)-1 >=10 :
            FPS=3  
        else:
            FPS=6
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if not ruch_wykonany:
                    if event.key == pygame.K_UP and kierunek != "DOL":
                        kierunek = "GORA"
                        ruch_wykonany = True
                    elif event.key == pygame.K_DOWN and kierunek != "GORA":
                        kierunek = "DOL"
                        ruch_wykonany = True
                    elif event.key == pygame.K_LEFT and kierunek != "PRAWO":
                        kierunek = "LEWO"
                        ruch_wykonany = True
                    elif event.key == pygame.K_RIGHT and kierunek != "LEWO":
                        kierunek = "PRAWO"
                        ruch_wykonany = True
                    elif event.key == pygame.K_p:
                        pauza = not pauza
                    elif event.key == pygame.K_SPACE:
                        temp_FPS = not temp_FPS
        # przyspieszanie
        if temp_FPS == True:
            FPS=FPS+6
        
        if len(snake) == temp_snake+1:
            temp_FPS = False
        temp_snake=len(snake)

        # --- Ruch węża ---
        if not pauza:
            glowa_x, glowa_y = snake[-1]

            if kierunek == "GORA":
                glowa_y -= 1
            elif kierunek == "DOL":
                glowa_y += 1
            elif kierunek == "LEWO":
                glowa_x -= 1
            elif kierunek == "PRAWO":
                glowa_x += 1

            if glowa_x < 0 or glowa_x >= ilkrat or glowa_y < 0 or glowa_y >= ilkrat:
                ekran_game_over()
                continue

            if (glowa_x, glowa_y) in snake:
                ekran_game_over()
                continue

            snake.append((glowa_x, glowa_y))
            if (glowa_x, glowa_y) == kolo:
                while True:
                    kolo = (
                        random.randint(0, ilkrat - 1),
                        random.randint(0, ilkrat - 1)
                    )
                    if kolo not in snake:
                        break
            else:
                snake.pop(0)

            rysuj(snake, kolo)
            clock.tick(FPS)
            ruch_wykonany = False