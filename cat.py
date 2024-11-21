# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:57:21 2024

@author: user
"""
import tkinter as tk
from PIL import Image,ImageTk
window = tk.Tk()
window.title("Popcat 點擊遊戲")
window.geometry("400x500")
window.resizable(False,False)


rk1_image = ImageTk.PhotoImage(Image.open("rk1.jpg").resize((300,300)))
rk2_image = ImageTk.PhotoImage(Image.open("rk2.jpeg").resize((300,300)))

cat_label = tk.Label(window,image=rk2_image)
cat_label.pack(pady=20)

count_labe1 = tk.Label(window, text="點擊次數:0",font=("Arial",18))
count_label.pack(pady=10)

click_count=0
cat_label.bind("<Button-1>",on_click)

def undate_count():
    global click_count
    click_count +=1
    count_label.config(text=f"點擊次數:{click_count}")
def undate_count():
    global click_count
    click_count +=1
    count_label.config(text=f"點擊次數:{click_count}")


window.mainloop()
