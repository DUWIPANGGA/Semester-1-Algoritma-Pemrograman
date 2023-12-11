import tkinter as tk

def ambil_dan_tampilkan_teks():
    teks_input = entry.get()
    print(f"Teks yang diambil: {teks_input}")

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Ambil Teks dari Entry")

# Membuat elemen Entry
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Membuat tombol untuk mengambil dan menampilkan teks
tombol_ambil_teks = tk.Button(root, text="Ambil Teks", command=ambil_dan_tampilkan_teks)
tombol_ambil_teks.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()