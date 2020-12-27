from tkinter import *
import tkinter
import os
import time
import tkinter.messagebox as mb


synccolor = "#2867B2"
wordcolor = '#FFFFFF'

## Create Window
app = Tk()
app.title('Free Sync Storage')
app.geometry('400x300')
app.config(bg=synccolor)
photo = PhotoImage(file = "download.png")
app.iconphoto(False, photo)




def click():
    a = sync_entry.get()
    b = pass_entry.get()
    app.destroy()

    global params
    params = [a, b]

    with open('output.txt', 'w') as f:
        f.write(a + '\n')
        f.write(b)

    import sync
    sync


def cancel():
    app.destroy()


# Email Address
sync_text = StringVar
sync_label = Label(app, text="Input Six Letters:", font=('bold', 14), pady=20, bg=synccolor, fg=wordcolor)
sync_label.grid(row=1, column=0, sticky=W)
sync_entry = Entry(app, textvariable=sync_text)
sync_entry.grid(row=1, column=1)

# Referral Code
pass_text = StringVar
pass_label = Label(app, text="Your Referral Code:", font=('bold', 14), pady=20, bg=synccolor, fg=wordcolor)
pass_label.grid(row=2, column=0, sticky=W)
pass_entry = Entry(app, textvariable=sync_text)
pass_entry.grid(row=2, column=1)

# Copywrite
copywrite_text = StringVar
copywrite_label = Label(app, text="© Zac Nicholson 2020", font=('bold', 14), pady=20, bg=synccolor, fg=wordcolor)
copywrite_label.grid(row=7, column=0, sticky=W)

# #Buttons
submit_btn = Button(app, text="Run", width=12, bg=synccolor, fg=synccolor, command=click)
submit_btn.grid(row=6, column=0, pady=20)

cancel_btn = Button(app, text="Cancel", width=12, bg=synccolor, fg=synccolor, command=lambda: cancel())
cancel_btn.grid(row=6, column=1, pady=20)

# Start Program
app.mainloop()
