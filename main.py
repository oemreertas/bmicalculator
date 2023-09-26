from tkinter import *
from tkinter import messagebox



'-------------------window-----------'

window = Tk()
window.geometry("300x300")
window.resizable(False, False)
window.title("BMI CALCULATOR")
window.config(background="#1c1c1c")
'-------------------------------------------'
'-------------WindowCenter-------------------'
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window.winfo_reqwidth()) / 2
y = (screen_height - window.winfo_reqheight()) / 2
window.geometry("+%d+%d" % (x, y))
'-------------------------------------'
'---------------------------BMI FUNCTION-------------------'


def BMIFunction():
    try:
        value1 = float(entry1.get())
        value2 = float(entry2.get()) / 100
        sonuc = value1 / (value2 * value2)
        print(sonuc)

        if sonuc < 18.5:
            label4.config(text=f"Underweight :(")
            label5.config(text=f"{sonuc}")
        elif 18.5 < sonuc < 24.9:
            label4.config(text=f"Normal weight :)")
            label5.config(text=f"{sonuc}")
        elif 25 < sonuc < 29.9:
            label4.config(text=f"Overweight :/")
            label5.config(text=f"{sonuc}")
        elif 30 < sonuc < 34.9:
            label4.config(text=f"Obesity!")
            label5.config(text=f"{sonuc}")
        elif sonuc > 35:
            label4.config(text=f"Extrame Obesity!!!")
            label5.config(text=f"{sonuc}")
    except ValueError:
        messagebox.showerror("Error", "An invalid number entry was completed.")


'----------------------------------------------------------'

'----------------------LABELS----------------------'
new_font = ("Bebas Neue", 10, "bold")
label1 = Label(window, text="Enter Your Weight(kg)")
label1.config(background="#1c1c1c", font=new_font, fg="White")
label1.place(x=150, y=55, anchor="center")
label2 = Label(window, text="Enter Your Height(cm)")
label2.config(background="#1c1c1c", font=new_font, fg="White")
label2.place(x=150, y=105, anchor="center")
label3 = Label(window, text=f"According to your BMI index:")
label3.config(background="#1c1c1c", font=new_font, fg="White")
label3.place(x=150, y=225, anchor="center")
label4 = Label(window)
label4.config(background="#1c1c1c", font=new_font, fg="White")
label4.place(x=150, y=255, anchor="center")
label5 = Label(window)
label5.config(background="#1c1c1c", font=new_font, fg="White")
label5.place(x=150, y=200, anchor="center")
'---------------------------------------------------'
'-------------------Entry---------------------------'


def entryClick(_event):
    if entry1.get() == "For exp:75":
        entry1.delete(0, "end")
        entry1.config(background="black",
                      fg="White",
                      font=("Arial", 10, "bold"))
        print(entry1.get())


def entryClick2(_event):
    if entry2.get() == "For exp:170":
        entry2.delete(0, "end")
        entry2.config(background="black",
                      fg="White",
                      font=("Arial", 10, "bold"))


entry1 = Entry(window, highlightthickness=1)
entry1.insert(0, "For exp:75")
entry1.bind("<FocusIn>", entryClick)
entry1.place(x=150, y=80, anchor="center")
entry1.config(background="#1c1c1c",
              borderwidth=2,
              fg="dark gray",
              highlightbackground="White",
              highlightcolor="White",
              relief="solid",
              insertbackground="White",
              insertborderwidth=5
              )

entry2 = Entry(window, highlightthickness=1)
entry2.insert(0, "For exp:170")
entry2.bind("<FocusIn>", entryClick2)
entry2.place(x=150, y=130, anchor="center")
entry2.config(background="#1c1c1c",
              borderwidth=2,
              fg="dark gray",
              highlightbackground="White",
              highlightcolor="White",
              relief="solid",
              insertbackground="White",
              insertborderwidth=5)

'---------------------------------------------------'
'---------------------BUTTON------------------------'
button1 = Button(window, text="Calculator", command=BMIFunction)
button1.config(borderwidth=2,
               background="#8b1a1a",
               font=new_font,
               fg="White",
               highlightcolor="White",
               highlightbackground="White",
               relief="solid")
button1.place(x=150, y=170, anchor="center")
button1.bind()
window.mainloop()
