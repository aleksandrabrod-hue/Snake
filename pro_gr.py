import pygame
import argparse
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
KOLOR_TLA_PLANSZY = (150, 150, 250)
KOLOR_TLA_PASKA = (50, 150, 50)
KOLOR_TLA_GAME_OVER = (100, 0, 0)
KOLOR_WEZA_JASNY = (150, 255, 0)
KOLOR_WEZA_CIEMNY = (0, 180, 0)
okno.fill(KOLOR_TLA_PLANSZY)
pygame.display.update()

TLA_GRY = {
    "domyslne": {  
        "plansza": (150, 150, 250),
        "pasek": (50, 150, 50),
        "game_over": (100, 0, 0)
    },
    "pomaranczowe": {
        "plansza": (255, 210, 150),  
        "pasek": (255, 165, 80),
        "game_over": (180, 80, 0)
    },
    "szare": {
        "plansza": (200, 200, 200),
        "pasek": (120, 120, 120),
        "game_over": (80, 80, 80)
    }
}



# --- Funkcje rysujące ---
def rysuj_snake_kostka(poz, kolor_weza=(150, 255, 0)):

    x, y = poz
    pozycja = (x * kratka, y * kratka + WYS_PASKA, kratka, kratka)
    pygame.draw.rect(okno, kolor_weza, pozycja)
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
    for i, kostka in enumerate(snake):
        if i % 2 == 0:
            kolor_weza = KOLOR_WEZA_JASNY
        else:
            kolor_weza = KOLOR_WEZA_CIEMNY

        rysuj_snake_kostka(kostka, kolor_weza)


    
def czyszczenie():
    okno.fill(KOLOR_TLA_PLANSZY)

    
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
        pygame.draw.rect(
            okno,
            KOLOR_TLA_GAME_OVER,
            (0, WYS_PASKA, szerokosc, szerokosc)
        )

       
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

def instrukcja_pomoc():
    global KOLOR_TLA_PLANSZY, KOLOR_TLA_PASKA, KOLOR_TLA_GAME_OVER

    parser = argparse.ArgumentParser(
        prog="pro_gr.py",
        description=(
            "=== Gra Snake ===\n\n"
            "Sterowanie:\n"
            "  Strzałki: poruszanie wężem\n"
            "  P: pauza / wznowienie gry\n"
            "  Spacja: tymczasowe przyspieszenie\n"
            "  A: przyspieszenie do stalej predkosci 6 fps (blokuje funkcje chwilowego przyspieszania spacją)\n"
            "  N: nowa gra (po zakończeniu gry)\n"
            "  K: zakończenie gry\n\n"
            
            "Cel gry:\n"
            "  Zdobycie jak największej liczby punktów poprzez zbieranie jedzenia\n"
            "  i unikanie kolizji ze ścianami oraz własnym ogonem.\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "--tlo",
        choices=TLA_GRY.keys(),
        default="domyslne",
        help=(
            "Motyw tła gry:\n"
            "  domyslne      - Twój obecny kolor (niebieskie tło)\n"
            "  pomaranczowe  - jasny pomarańczowy\n"
            "  szare         - szary"
        )
    )

    argumenty = parser.parse_args()

    wybrane_tlo = TLA_GRY[argumenty.tlo]
    KOLOR_TLA_PLANSZY = wybrane_tlo["plansza"]
    KOLOR_TLA_PASKA = wybrane_tlo["pasek"]
    KOLOR_TLA_GAME_OVER = wybrane_tlo["game_over"]


# --- Funkcja resetu gry ---
def reset_gry():
    global snake, kierunek, kolo, pauza, temp_FPS, temp2_FPS

    pauza = False
    
    temp_FPS = False
    temp2_FPS = False
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
    KOLOR_TLA_PASKA,
    (0, 0, szerokosc, WYS_PASKA)

    )

    wynik = f"Twój wynik: {len(snake)-1}"
    tekst = font.render(wynik, True, (255, 255, 255))

    # wyśrodkowanie w poziomie i pionie
    x = (szerokosc - tekst.get_width()) // 2
    y = (WYS_PASKA - tekst.get_height()) // 2

    okno.blit(tekst, (x, y))



#losujemy początkowe położenie weza i jedzenia wywołłując gunkcje reset_gry
reset_gry()
kierunek = "PRAWO"  # domyślny kierunek
clock = pygame.time.Clock()
pauza = False
temp_FPS =False
temp2_FPS = False
temp_snake=1
ruch_wykonany = False




if __name__ == "__main__":
    instrukcja_pomoc()
# --- Główna pętla ---
    while True:
        if len(snake)-1 >=10 :
            FPS=3  
        else:
            FPS=6
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pauza = not pauza
                    #continue

                elif not pauza and not ruch_wykonany:
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
                    elif event.key == pygame.K_a:
                        temp2_FPS = not temp2_FPS
        # przyspieszanie
        if temp_FPS == True:
            FPS=FPS+6

        if temp2_FPS == True:
            FPS= 6
        
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