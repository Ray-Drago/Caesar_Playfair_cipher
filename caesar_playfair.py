import tkinter as tk
from tkinter import ttk

def encrypt_caesar(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def generate_matrix(key):
    key = key.replace("j", "i")
    key = key + "abcdefghiklmnopqrstuvwxyz"
    key = "".join(dict.fromkeys(key))
    matrix = []
    k = 0
    for i in range(5):
        row = []
        for j in range(5):
            row.append(key[k])
            k += 1
        matrix.append(row)
    return matrix

def find_position(matrix, c):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == c:
                return (i, j)
    return None

def encrypt_playfair(plain_text, key):
    matrix = generate_matrix(key.lower())
    plain_text = plain_text.lower().replace("j", "i").replace(" ", "")
    if len(plain_text) % 2 != 0:
        plain_text += "x"
    encrypted_text = ""
    i = 0
    while i < len(plain_text):
        a = plain_text[i]
        b = plain_text[i + 1]
        a_pos = find_position(matrix, a)
        b_pos = find_position(matrix, b)
        encrypted_a, encrypted_b = '', ''
        if a_pos[0] == b_pos[0]:
            encrypted_a = matrix[a_pos[0]][(a_pos[1] + 1) % 5]
            encrypted_b = matrix[b_pos[0]][(b_pos[1] + 1) % 5]
        elif a_pos[1] == b_pos[1]:
            encrypted_a = matrix[(a_pos[0] + 1) % 5][a_pos[1]]
            encrypted_b = matrix[(b_pos[0] + 1) % 5][b_pos[1]]
        else:
            encrypted_a = matrix[a_pos[0]][b_pos[1]]
            encrypted_b = matrix[b_pos[0]][a_pos[1]]
        encrypted_text += encrypted_a + encrypted_b
        i += 2
    return encrypted_text

def decrypt_playfair(encrypted_text, key):
    matrix = generate_matrix(key.lower())
    encrypted_text = encrypted_text.lower().replace("j", "i").replace(" ", "")
    decrypted_text = ""
    i = 0
    while i < len(encrypted_text):
        a = encrypted_text[i]
        b = encrypted_text[i + 1]
        a_pos = find_position(matrix, a)
        b_pos = find_position(matrix, b)
        decrypted_a, decrypted_b = '', ''
        if a_pos[0] == b_pos[0]:
            decrypted_a = matrix[a_pos[0]][(a_pos[1] - 1) % 5]
            decrypted_b = matrix[b_pos[0]][(b_pos[1] - 1) % 5]
        elif a_pos[1] == b_pos[1]:
            decrypted_a = matrix[(a_pos[0] - 1) % 5][a_pos[1]]
            decrypted_b = matrix[(b_pos[0] - 1) % 5][b_pos[1]]
        else:
            decrypted_a = matrix[a_pos[0]][b_pos[1]]
            decrypted_b = matrix[b_pos[0]][a_pos[1]]
        decrypted_text += decrypted_a + decrypted_b
        i += 2
    return decrypted_text

def on_encrypt():
    plain_text = entry_plain.get()
    shift = int(entry_shift.get())
    caesar_encrypted_text = encrypt_caesar(plain_text, shift)
    playfair_encrypted_text = encrypt_playfair(caesar_encrypted_text, entry_key.get())
    entry_encrypted.delete(0, tk.END)
    entry_encrypted.insert(0, playfair_encrypted_text)

def on_decrypt():
    encrypted_text = entry_encrypted.get()
    shift = int(entry_shift.get())
    caesar_decrypted_text = decrypt_playfair(encrypted_text, entry_key.get())
    playfair_decrypted_text = decrypt_caesar(caesar_decrypted_text, shift)
    entry_decrypted.delete(0, tk.END)
    entry_decrypted.insert(0, playfair_decrypted_text)

# Create the GUI
root = tk.Tk()
root.title("Combined Cipher")
root.geometry("400x300")
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

label_key = ttk.Label(frame, text="Enter the Playfair key:")
label_key.grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_key = ttk.Entry(frame)
entry_key.grid(row=2, column=1, padx=10, pady=5)

button_encrypt = ttk.Button(frame, text="Encrypt", command=on_encrypt)
button_encrypt.grid(row=3, column=1, padx=10, pady=5)

label_encrypted = ttk.Label(frame, text="Encrypted data:")
label_encrypted.grid(row=4, column=0, sticky="e", padx=10, pady=5)
entry_encrypted = ttk.Entry(frame)
entry_encrypted.grid(row=4, column=1, padx=10, pady=5)

button_decrypt = ttk.Button(frame, text="Decrypt", command=on_decrypt)
button_decrypt.grid(row=5, column=1, padx=10, pady=5)

label_decrypted = ttk.Label(frame, text="Decrypted data:")
label_decrypted.grid(row=6, column=0, sticky="e", padx=10, pady=5)
entry_decrypted = ttk.Entry(frame)
entry_decrypted.grid(row=6, column=1, padx=10, pady=5)

root.mainloop()
