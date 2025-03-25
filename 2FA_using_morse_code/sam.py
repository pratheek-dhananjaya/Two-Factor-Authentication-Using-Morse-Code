import tkinter as tk

window=tk.Tk()
window.title("Morse")
window.geometry("500x500")
window.configure(background="blue")

lbl=tk.Label(window, text="ID", width=10, height=1, bg="black", fg="white", font=("times", 12,"italic"))
lbl.place(x=150, y=50)

txt=tk.Entry(window, text="", bg="black",width=10, fg="white", font=("times", 12,"italic"))
txt.place(x=250, y=50)

def submit():
    ID=txt.get()
    print(ID)

lbl=tk.Button(window, text="submit", command=submit, width=10, height=1, activebackground="green",bg="black", fg="white", font=("times", 12,"italic"))
lbl.place(x=250, y=150)

window.mainloop()
