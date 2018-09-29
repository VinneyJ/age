
import tkinter as tk

window = tk.Tk()
window.title("Greetings____")
window.geometry("400x400")

#_____LEBEL_____

label1 = tk.Label(text="Welcome to my App :)")
label1.grid(column = 0, row = 0)


label2 = tk.Label(text="What is your name?")
label2.grid(column = 0, row = 1)

#___ENTRIES____
entry1 = tk.Entry()
entry1.grid(column = 1, row = 2)


#____BUTTONS___
button1 = tk.Button(text = "CLICK ME")
button1.grid(column =0, row =2)
window.mainloop()