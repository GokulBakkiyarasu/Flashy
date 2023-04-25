from tkinter import *
from pandas import *
from random import *
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = read_csv("data/french_words.csv")
french_word_list = data["French"].to_list()
english_word_list = data["English"].to_list()
word_dictionary = {keys: values for (keys, values) in zip(french_word_list, english_word_list)}


# ------------------------Generating french word----------------------
def random_french_word():
    return choice(french_word_list)


new_word = random_french_word()


def card1config1():
    global new_word, french_word_list, english_word_list
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(topic, text="French", fill="black")
    canvas.itemconfig(text, text=new_word, fill="black")
    window.after(ms=3000, func=meaning)
    french_word_list.remove(new_word)
    english_word_list.remove(word_dictionary[new_word])


def card1config2():
    global new_word, french_word_list
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(topic, text="French", fill="black")
    canvas.itemconfig(text, text=new_word, fill="black")
    window.after(ms=3000, func=meaning)


# ---------------------Generating relevant english word------------
def meaning():
    global new_word
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(topic, text="English", fill="white")
    canvas.itemconfig(text, text=word_dictionary[new_word], fill="white")
    new_word = random_french_word()


# ---------------------UI-------------------------
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file=r"images\card_front.png")
back_img = PhotoImage(file=r"images\card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
topic = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
text = canvas.create_text(400, 263, text=new_word, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


tick_img = PhotoImage(file=r"images\right.png")
yes_button = Button(image=tick_img, highlightthickness=0, command=card1config1)
yes_button.grid(row=1, column=1)

wrong_img = PhotoImage(file=r"images\wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=card1config2)
wrong_button.grid(row=1, column=0)
window.eval('tk::PlaceWindow . center')
window.after(ms=3000, func=meaning)

window.mainloop()
new_word_dictionary = {"French": [keys for keys in french_word_list],
                       "English": [values for values in english_word_list]}
df = DataFrame.from_dict(new_word_dictionary)
df.to_csv("data/words_to_learn.csv", index=False)
