import customtkinter as ctk
import os

ICON_PATH = os.path.join(os.path.dirname(__file__), "icon.ico")

def run(start_cb, stop_cb):
    ctk.set_appearance_mode("dark")

    app = ctk.CTk()        
    app.geometry("500x500")
    app.title("BoczkowyMajner")
    app.iconbitmap(ICON_PATH)

    label = ctk.CTkLabel(app, text="BoczkowyMajner 2000")
    label.pack(pady=20)
    entry = ctk.CTkEntry(app, placeholder_text="Ile blokow")
    entry.pack(pady=10)

    def on_start():
        try:
            b = int(entry.get())
            start_cb(b)
        except ValueError:
            print("podaj liczbe")

    btn_start = ctk.CTkButton(app, text="Start", command=on_start)
    btn_start.pack(pady=5)

    btn_stop = ctk.CTkButton(app, text="Stop", command=stop_cb)
    btn_stop.pack(pady=5)

    
    app.mainloop()    


