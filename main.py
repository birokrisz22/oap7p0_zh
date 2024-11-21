import tkinter as tk
from tkinter import messagebox
import random
import string

#OAP7P0
#Biró Zoltán Krisztián

class BzKCipher:
    @staticmethod
    def caesar_cipher(text, shift=10):
        encrypted_text = []
        for char in text:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                encrypted_text.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
            else:
                encrypted_text.append(char)
        return ''.join(encrypted_text)

def BzKgenerate_password(length, use_numbers, use_specials):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if length < 3:
        return "A jelszó hossza nem lehet kevesebb mint 3 karakter!"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def BzK_generate_and_display():
    try:
        length = int(entry_length.get())
        use_numbers = var_numbers.get()
        use_specials = var_specials.get()
        password = BzKgenerate_password(length, use_numbers, use_specials)
        result_label.config(text=f"Generált jelszó: {password}")
        global last_password
        last_password = password
    except ValueError:
        messagebox.showerror("Hiba", "Kérjük, adjon meg egy érvényes számot a jelszó hosszához!")

def BzK_encrypt_and_display():
    if last_password:
        encrypted_password = BzKCipher.caesar_cipher(last_password)
        encrypted_label.config(text=f"Titkosított jelszó: {encrypted_password}")
    else:
        messagebox.showinfo("Figyelem", "Előbb generáljon egy jelszót!")

root = tk.Tk()
root.title("BzK_OAP7P0_Jelszógenerátor program")
root.geometry("400x400+500+500")
root.configure(bg="lightblue")

tk.Label(root, text="Jelszó hossza:").pack()
entry_length = tk.Entry(root)
entry_length.pack()

var_numbers = tk.BooleanVar()
check_numbers = tk.Checkbutton(root, text="Legyen benne szám", variable=var_numbers)
check_numbers.pack()

var_specials = tk.BooleanVar()
check_specials = tk.Checkbutton(root, text="Legyen benne speciális karakter", variable=var_specials)
check_specials.pack()

generate_button = tk.Button(root, text="Generálás", command=BzK_generate_and_display)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()


encrypt_button = tk.Button(root, text="Titkosítás", command=BzK_encrypt_and_display)
encrypt_button.pack()

encrypted_label = tk.Label(root, text="")
encrypted_label.pack()

last_password = ""

root.mainloop()
