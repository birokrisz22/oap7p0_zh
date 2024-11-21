Név: Biró Zoltán Krisztián

Neptun kód: OAP7P0

Tantárgy: Szkript nyelvek

--

A program három alapvető paraméter alapján generál egy jelszót a felhasználónak. Meg kell adnia, hogy hány karakter hosszúságú legyen, legyen e benne speciális karakter (igen-nem) illetve szám (igen - nem).
Az így kapot jelszavunk így biztosan megfelelő erősségű lesz és nehezen feltörhető, de mivel a tárolása és a megjegyzése is rendkívül nehéz így, ezért van lehetőségünk arra, hogy titkosítsuk Caesar kódoló segítségével.
Az így kapott jelszót elmenthetjük, mivel csak mi tudjuk, hogy pontosan hogy volt kódolva.

A Caesar kódoló ebben az esetben a betűket kicséréli az abc tíz poziciójával későbbi karakterére.

A program egy fő main részből áll.

A main részei:
caesar_cipher -> A Ceasar kódolónál itt tudjuk megadni, az eltolás értékét és ez végzi el a későbbiekben magát a titkosítást.
BzKgenerate_password -> A bekért adatok alapján legenerálja a jelszót
BzK_generate_and_display() ->  Megjeleníti a legenerált jelszót
BzK_encrypt_and_display() -> Megjeleníti a titkosított jelszót

A program további része, az ablak megjelenítésére szolgál illetve az adatok bekérésére.

Felhasznált importált modulok:
import tkinter as tk
from tkinter import messagebox
import random
import string
