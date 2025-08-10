import tkinter as tk
from tkinter import messagebox

def kaydet():
    veri = entry.get()
    if veri.strip():
        messagebox.showinfo("Veri", f"Veriniz: {veri}")
    else:
        messagebox.showwarning("Uyarı", "Boş bırakmayın!")

pencere = tk.Tk()
pencere.title("Basit Tkinter Uygulaması")
pencere.geometry("300x150")

etiket = tk.Label(pencere, text="Metin girin:")
etiket.pack(pady=5)

entry = tk.Entry(pencere, width=30)
entry.pack(pady=5)

buton = tk.Button(pencere, text="Kaydet", command=kaydet)
buton.pack(pady=10)


pencere.mainloop()