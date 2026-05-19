import os
import subprocess
from tkinter import messagebox, Tk

FILE_PATH = r"C:\Windows\System32"

root = Tk()
root.withdraw() 

confirm = messagebox.askyesno(
    "Предупреждение",
    f"Вы уверены, что хотите безвозвратно удалить System32?",
)

if confirm:
    try:
        subprocess.run(
            ["takeown", "/f", FILE_PATH, "/a"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        subprocess.run(
            ["icacls", FILE_PATH, "/grant", "*S-1-5-32-544:F"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
    except Exception:
        pass  

