import tkinter as tk
from tkinter import messagebox
import random
import string
import os


chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

def encrypt_message():
    plain_text = plain_text_entry.get("1.0", tk.END).strip()
    cypher_text = ""
    for letter in plain_text:
        if letter in chars:
            index = chars.index(letter)
            cypher_text += key[index]
        else:
            messagebox.showerror("Error", f"Unsupported character: {letter}")
            return
    encrypted_text_entry.delete("1.0", tk.END)
    encrypted_text_entry.insert(tk.END, cypher_text)

def decrypt_message():
    cypher_text = encrypted_text_entry.get("1.0", tk.END).strip()
    plain_text = ""
    for letter in cypher_text:
        if letter in key:
            index = key.index(letter)
            plain_text += chars[index]
        else:
            messagebox.showerror("Error", f"Unsupported character: {letter}")
            return
    decrypted_text_entry.delete("1.0", tk.END)
    decrypted_text_entry.insert(tk.END, plain_text)

def generate_new_key():
    global key
    key = chars.copy()
    random.shuffle(key)
    messagebox.showinfo("Key Generated", "A new key has been generated!")

def save_key():
    with open("key.txt", "w") as file:
        file.write("".join(key))
    messagebox.showinfo("Key Saved", "The key has been saved to key.txt")

def load_key():
    global key
    if not os.path.exists("key.txt"):
        messagebox.showerror("Error", "No saved key found! Please save a key first.")
        return
    with open("key.txt", "r") as file:
        saved_key = file.read()
    if len(saved_key) != len(chars) or set(saved_key) != set(chars):
        messagebox.showerror("Error", "Invalid key file!")
        return
    key = list(saved_key)
    messagebox.showinfo("Key Loaded", "The key has been successfully loaded!")

root = tk.Tk()
root.title("Substitution Cipher")


tk.Label(root, text="Plain Text:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
plain_text_entry = tk.Text(root, height=5, width=50)
plain_text_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Encrypted Text:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
encrypted_text_entry = tk.Text(root, height=5, width=50)
encrypted_text_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Decrypted Text:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
decrypted_text_entry = tk.Text(root, height=5, width=50)
decrypted_text_entry.grid(row=2, column=1, padx=10, pady=5)


encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=3, column=0, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message)
decrypt_button.grid(row=3, column=1, padx=10, pady=10)

generate_key_button = tk.Button(root, text="Generate New Key", command=generate_new_key)
generate_key_button.grid(row=4, column=0, padx=10, pady=10)

save_key_button = tk.Button(root, text="Save Key", command=save_key)
save_key_button.grid(row=4, column=1, padx=10, pady=10)

load_key_button = tk.Button(root, text="Load Key", command=load_key)
load_key_button.grid(row=5, column=0, padx=10, pady=10)


root.mainloop()
