# Dokumentacja techniczna projektu Snake

## Informacje ogólne
Projekt Snake został zrealizowany w języku Python z wykorzystaniem biblioteki pygame.  
Celem projektu było stworzenie gry komputerowej typu Snake z zachowaniem zasad
programowania strukturalnego, czytelności kodu oraz możliwości testowania.

Projekt realizowany był zespołowo z użyciem systemu kontroli wersji Git oraz repozytorium GitHub.

---

## Technologie
- **Język:** Python 3
- **Biblioteka:** pygame
- **Środowisko wirtualne:** venv
- **System kontroli wersji:** Git / GitHub

---

## Struktura projektu
Projekt składa się z następujących plików:

- `pro_gr.py` – główny plik gry, zawiera całą logikę programu
- `test_pro_gr.py` – testy jednostkowe funkcji gry
- `README.md` – instrukcja użytkownika i informacje ogólne
- `DOCUMENTATION.md` – dokumentacja techniczna projektu
- `requirements.txt` – lista wymaganych bibliotek
- `.gitignore` – pliki i katalogi ignorowane przez Git

---

## Opis działania programu
Program uruchamia okno gry, w którym gracz steruje wężem poruszającym się po planszy
podzielonej na kratki. Wąż porusza się automatycznie w zadanym kierunku, a gracz może
zmieniać kierunek ruchu za pomocą klawiatury.

Celem gry jest zbieranie elementów jedzenia, co powoduje:
- wydłużenie węża,
- zwiększenie punktacji,
- zmianę prędkości gry.

Gra kończy się w momencie kolizji węża ze ścianą planszy lub z własnym ciałem.

---

## Zmienne globalne
- `kratka` – rozmiar jednej kratki planszy
- `ilkrat` – liczba kratek w jednym wymiarze planszy
- `snake` – lista przechowująca segmenty węża jako pary współrzędnych `(x, y)`
- `kolo` – aktualna pozycja jedzenia
- `kierunek` – aktualny kierunek ruchu węża
- `FPS` – liczba klatek na sekundę (prędkość gry)
- `pauza` – flaga wstrzymania gry
- `temp_FPS` – flaga tymczasowego przyspieszenia gry

---

## Opis funkcji

### `rysuj_snake_kostka(poz)`
Funkcja rysuje pojedynczy segment węża w zadanej pozycji.
Jeżeli rysowany segment jest głową węża, rysowane są dodatkowo oczy.

---

### `rysuj_kolo(poz)`
Rysuje element jedzenia w postaci czerwonego koła w podanej pozycji.

---

### `rysuj_snake(snake)`
Iteruje po wszystkich segmentach węża i wywołuje funkcję rysującą
pojedyncze elementy węża.

---

### `czyszczenie()`
Czyści ekran gry, wypełniając go kolorem tła.

---

### `rysuj(snake, kolo)`
Funkcja odpowiedzialna za:
- czyszczenie ekranu,
- rysowanie wyniku,
- rysowanie węża,
- rysowanie jedzenia,
- odświeżenie ekranu gry.

---

### `rysuj_wynik()`
Wyświetla aktualny wynik gracza na pasku informacyjnym u góry ekranu.

---

### `reset_gry()`
Resetuje stan gry poprzez:
- ustawienie początkowej pozycji węża,
- wylosowanie nowego położenia jedzenia,
- ustawienie domyślnego kierunku ruchu,
- wyzerowanie pauzy i prędkości tymczasowej.

---

### `ekran_game_over()`
Wyświetla ekran zakończenia gry oraz umożliwia:
- rozpoczęcie nowej gry,
- zakończenie programu.

---

## Główna pętla gry
Główna pętla gry odpowiada za:
- obsługę zdarzeń klawiatury,
- zmianę kierunku ruchu węża,
- obsługę pauzy i przyspieszenia,
- wykrywanie kolizji,
- aktualizację stanu gry i rysowanie kolejnych klatek.

## Testy jednostkowe
- Projekt zawiera testy jednostkowe sprawdzające:
- poprawność resetu gry,
- losowanie jedzenia poza ciałem węża,
- poprawność punktacji,
- poprawne działanie funkcji rysujących (brak błędów wykonania),
- istnienie wszystkich kluczowych funkcji.


## Odporność na błędne dane
- Program został zaprojektowany w sposób odporny na nieprawidłowe działania użytkownika:
- niemożliwe jest cofnięcie węża w przeciwnym kierunku,
- gra poprawnie obsługuje wyjście poza planszę,
- obsłużone są kolizje z własnym ciałem,
- obsługiwana jest pauza i ponowne uruchomienie gry.


