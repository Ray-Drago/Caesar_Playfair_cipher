import tkinter as tk
from tkinter import ttk

def encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def on_encrypt():
    plain_text = entry_plain.get()
    shift = int(entry_shift.get())
    encrypted_text = encrypt(plain_text, shift)
    entry_encrypted.delete(0, tk.END)
    entry_encrypted.insert(0, encrypted_text)

def on_decrypt():
    encrypted_text = entry_encrypted.get()
    shift = int(entry_shift.get())
    decrypted_text = decrypt(encrypted_text, shift)
    entry_decrypted.delete(0, tk.END)
    entry_decrypted.insert(0, decrypted_text)

# Create the GUI
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("400x250")
root.configure(background="white")

# Create styles
style = ttk.Style()
style.configure("TLabel", background="white")
style.configure("TEntry", background="white")
style.configure("TButton", background="#e6e6e6", relief="flat")

# Create frame
frame = ttk.Frame(root)
frame.pack(pady=20)

label_plain = ttk.Label(frame, text="Enter the plain text:")
label_plain.grid(row=0, column=0, sticky="e", padx=10, pady=5)
entry_plain = ttk.Entry(frame)
entry_plain.grid(row=0, column=1, padx=10, pady=5)

label_shift = ttk.Label(frame, text="Enter the shift value:")
label_shift.grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_shift = ttk.Entry(frame)
entry_shift.grid(row=1, column=1, padx=10, pady=5)

button_encrypt = ttk.Button(frame, text="Encrypt", command=on_encrypt)
button_encrypt.grid(row=2, column=1, padx=10, pady=5)

label_encrypted = ttk.Label(frame, text="Encrypted data:")
label_encrypted.grid(row=3, column=0, sticky="e", padx=10, pady=5)
entry_encrypted = ttk.Entry(frame)
entry_encrypted.grid(row=3, column=1, padx=10, pady=5)

button_decrypt = ttk.Button(frame, text="Decrypt", command=on_decrypt)
button_decrypt.grid(row=4, column=1, padx=10, pady=5)

label_decrypted = ttk.Label(frame, text="Decrypted data:")
label_decrypted.grid(row=5, column=0, sticky="e", padx=10, pady=5)
entry_decrypted = ttk.Entry(frame)
entry_decrypted.grid(row=5, column=1, padx=10, pady=5)

root.mainloop()
