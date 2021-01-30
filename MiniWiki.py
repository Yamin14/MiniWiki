from tkinter import *
import wikipedia

root = Tk()
bg = "sky blue"
fg = "#007777"
root.config(background=bg)

def search():
	text.delete(1.0, END)
	to_search = search_bar.get()
	my_ans = wikipedia.summary(to_search)
	text.insert(1.0, my_ans)

heading = Label(root, text="MiniWiki", bg=bg, font=("Comic Sans MS", 25, 'underline'), fg=fg)
heading.place(relx=0.5, rely=0.1, anchor=CENTER)

search_bar = Entry()
search_bar.place(relx=0.4, rely=0.2, anchor=CENTER)

search_button = Button(root, text="Search", bg="green", fg="#00dd00", activebackground="green", command=search)
search_button.place(relx=0.8, rely=0.2, anchor=CENTER)

text = Text(root, bg=bg, fg=fg, font=("Comic Sans MS", 7), width=40, pady=70)
text.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
