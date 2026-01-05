import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

import unittest
import pygame
import pro_gr


class TestSnakeGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pygame.init()

    # --- reset_gry ---
    def test_reset_gry(self):
        pro_gr.reset_gry()
        self.assertEqual(len(pro_gr.snake), 1)
        self.assertEqual(pro_gr.kierunek, "PRAWO")
        self.assertNotIn(pro_gr.kolo, pro_gr.snake)

    # --- rysuj_snake_kostka ---
    def test_rysuj_snake_kostka(self):
        pro_gr.reset_gry()
        try:
            pro_gr.rysuj_snake_kostka((5, 5))
        except Exception as e:
            self.fail(f"rysuj_snake_kostka wywołało błąd: {e}")

    # --- rysuj_kolo ---
    def test_rysuj_kolo(self):
        try:
            pro_gr.rysuj_kolo((3, 4))
        except Exception as e:
            self.fail(f"rysuj_kolo wywołało błąd: {e}")

    # --- rysuj_snake ---
    def test_rysuj_snake(self):
        snake = [(1, 1), (2, 1), (3, 1)]
        try:
            pro_gr.rysuj_snake(snake)
        except Exception as e:
            self.fail(f"rysuj_snake wywołało błąd: {e}")

    # --- czyszczenie ---
    def test_czyszczenie(self):
        try:
            pro_gr.czyszczenie()
        except Exception as e:
            self.fail(f"czyszczenie wywołało błąd: {e}")

    # --- rysuj ---
    def test_rysuj(self):
        snake = [(2, 2), (3, 2)]
        kolo = (5, 5)
        try:
            pro_gr.rysuj(snake, kolo)
        except Exception as e:
            self.fail(f"rysuj wywołało błąd: {e}")

    # --- rysuj_wynik ---
    def test_rysuj_wynik(self):
        try:
            pro_gr.rysuj_wynik()
        except Exception as e:
            self.fail(f"rysuj_wynik wywołało błąd: {e}")

    # --- ekran_game_over ---
    def test_ekran_game_over_istnieje(self):
        self.assertTrue(callable(pro_gr.ekran_game_over))

    # --- logika punktacji ---
    def test_punktacja(self):
        pro_gr.snake = [(1, 1), (2, 1), (3, 1)]
        wynik = len(pro_gr.snake) - 1
        self.assertEqual(wynik, 2)


if __name__ == "__main__":
    unittest.main()

