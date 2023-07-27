from tkinter import *
from tkinter import messagebox
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"


screen= Tk()
screen.title("Flash Card")
screen.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

try:
    word_dto_lear_data = pandas.read_csv("data/words_to_learn.csv")
except:
    data = pandas.read_csv("data/french_words.csv")
    new_data = data.to_dict(orient="records")
else:
    new_data = word_dto_lear_data.to_dict( orient="records")
    print(new_data)


def to_english():
    canvas.itemconfig(front_image, image=eng_front_img)
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=chosen["English"], fill="white")


def french():
    global chosen, flip
    screen.after_cancel(flip)
    chosen = random.choice(new_data)
    canvas.itemconfig(front_image, image=fre_front_img)
    canvas.itemconfig(lang, text="French", fill="black")
    canvas.itemconfig(word, text=chosen["French"], fill="black")
    flip = screen.after(2000, to_english)


def know():
    print(new_data.index(chosen))
    try:
        new_data.remove(chosen)
    except IndexError:
        messagebox.showinfo("Congrats! You know all words!")
    else:
        yet_to_learn = pandas.DataFrame(new_data)
        yet_to_learn.to_csv("data/words_to_learn.csv", index=False)
        french()

flip = screen.after(2000, to_english)
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
fre_front_img = PhotoImage(file="images/card_front.png")
eng_front_img = PhotoImage(file="images/card_back.png")
front_image = canvas.create_image(400, 263, image=fre_front_img)
canvas.grid(row=0, column=0, columnspan=2)
lang = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 300, text="trouve", font=("Arial", 60, "bold"))
#buttons
my_img = PhotoImage(file="images/right.png")
right_button = Button(image=my_img, highlightthickness=0, command=know)
right_button.grid(row=1, column=1)

my_second_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=my_second_img, highlightthickness=0, command=french)
wrong_button.grid(row=1, column=0)

messagebox.showinfo(title="Flash Game", message="Can you see the check and cancel logos there?")
messagebox.showinfo(title="Flash Game", message="When you click the check box, it means that you know the word "
                                                "and again it won't show you that word! And uncheck means you "
                                                "don't know the Word!")
french()

screen.mainloop()
