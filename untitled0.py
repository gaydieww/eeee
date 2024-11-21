# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:57:21 2024

@author: user
"""
import tkinter as tk
from PIL import Image,ImageTk

def undate_count():
    global click_count
    click_count +=1
    count_label.config(text=f"點擊次數:{click_count}")
    
def on_click(event):
    cat_label.config(image=rk1_image)
    window.after(200,lambda: cat_label.config(image=rk2_image))
    undate_count()
    
def reset():
    global click_count
    click_count =0
    count_label.config(text="點擊次數:0")

window = tk.Tk()
window.title("Popcat 點擊遊戲")
window.geometry("400x500")
window.resizable(False,False)


rk1_image = ImageTk.PhotoImage(Image.open("rk1.png").resize((300,300)))
rk2_image = ImageTk.PhotoImage(Image.open("rk2.jpg").resize((300,300)))

cat_label = tk.Label(window, image=rk2_image)
cat_label.pack(pady=20)


count_label = tk.Label(window, text="點擊次數:0",font=("Arial",18))
count_label.pack(pady=10)



click_count=0
cat_label.bind("<Button-1>",on_click)


reset_button = tk.Button(window, text="重製",command=reset,font=("Arial",14),bg="blue")
reset_button.pack(pady=10)

window.mainloop()
