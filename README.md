# Flashy

Flashy is a Python program designed to help users learn French words and their English translations. The program utilizes the tkinter and pandas libraries and features a simple and intuitive user interface.

![Screenshot (14)](https://user-images.githubusercontent.com/87391223/234362819-18abfe24-9486-4d78-a7e8-e9ead236692d.png)


## Features
   


## Getting Started
To get started with this program, simply clone the repository and run the `main.py` file. 

### Prerequisites
- Python 3.x
- tkinter
- random

### Installation
```
   1. Clone the repository from GitHub using `git clone https://github.com/gokulbakkiyarasu/Flashy.git`.
   2. Install the required libraries using `pip install tkinter pandas`.
   3. Navigate to the cloned repository using the command line.
   4. Run the program using `main.py`.
 ```

## Usage
```
   Here are some of the important parts of the code in the program:

1. **Reading the CSV file:** The program reads the CSV file using `pandas.read_csv()`, and if the file is not found, it reads a different CSV file:

```python
try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = read_csv("data/french_words.csv")
french_word_list = data["French"].to_list()
english_word_list = data["English"].to_list()
word_dictionary = {keys: values for (keys, values) in zip(french_word_list, english_word_list)}
```

2. **Generating a French word:** The program generates a random French word from the list of French words using `random.choice()`:

```python
def random_french_word():
    return choice(french_word_list)
```

3. **Displaying the French word:** The program uses `tkinter` to create a user interface with a canvas that displays the randomly generated French word. The canvas has an image on it, as well as text objects for the topic and the current French word:

```python
window = Tk()
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file=r"images\card_front.png")
back_img = PhotoImage(file=r"images\card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
topic = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
text = canvas.create_text(400, 263, text=new_word, font=("Ariel", 60, "bold"))
```

4. **Revealing the English translation:** When the user clicks the button to reveal the English translation, the program changes the canvas image and text objects to display the English translation of the current French word:

```python
def meaning():
    global new_word
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(topic, text="English", fill="white")
    canvas.itemconfig(text, text=word_dictionary[new_word], fill="white")
    new_word = random_french_word()
```

5. **Saving words for further practice:** If the user clicks the button to indicate that they got the answer correct, the program removes the current French word and its corresponding English translation from the lists of words read from the CSV file. When the program exits, it saves the remaining words to a new CSV file called "words_to_learn.csv":

```python
new_word_dictionary = {"French": [keys for keys in french_word_list],
                       "English": [values for values in english_word_list]}
df = DataFrame.from_dict(new_word_dictionary)
df.to_csv("data/words_to_learn.csv", index=False)
```

These are just some of the important parts of the code in the program, and there are many other details and nuances to the implementation.

When the program starts, a randomly generated French word will be displayed on the screen. The user can then click the "✓" button to reveal the English translation, or the "✗" button if they do not know the answer.

If the user clicks the "✓" button and gets the answer correct, the program will generate a new random word. If the user clicks the "✗" button or gets the answer wrong, the program will save the word for further practice.

## File structure
```
├── main.py                    # Main program file
├── data folder                # consist csv data files 
└── images folder              # image file
```

## Contributing
Contributions to this project are welcome. To contribute, follow these steps:
1. Fork this repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Make and commit your changes (`git commit -am "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a new Pull Request
## Find me on
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/gokul-bakkiyarasu-531535251)
