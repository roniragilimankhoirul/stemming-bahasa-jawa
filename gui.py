from pathlib import Path
from tkinter import *
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, BOTH, END, LEFT, font
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from deep_translator import GoogleTranslator

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0/")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Kelompok 3 || Stemmer Bahasa Jawa")
window.geometry("810x540")
window.configure(bg = "#FFFFFF")




factory = StemmerFactory()
stemmer = factory.create_stemmer()


def stem_now():
    text_input=entry_1.get(1.0,END)
    translated = GoogleTranslator(source='jw', target='id').translate(text_input)
    sastrawi_stem = stemmer.stem(translated)
    output = GoogleTranslator(source='id', target='jw').translate(sastrawi_stem)

    entry_2.delete(1.0,END)
    entry_2.insert(END,output)




canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 540,
    width = 810,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    405.0,
    270.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    191.0,
    269.0,
    image=image_image_2
)

canvas.create_text(
    456.0,
    126.0,
    anchor="nw",
    text="Input",
    fill="#000000",
    font=("RobotoRoman Light", 14 * -1)
)

canvas.create_text(
    456.0,
    245.0,
    anchor="nw",
    text="Output",
    fill="#000000",
    font=("RobotoRoman Light", 14 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    611.0,
    197.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    606.0,
    313.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=stem_now,
    relief="flat"
)
button_1.place(
    x=456.0,
    y=393.0,
    width=95.0,
    height=30.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    611.0,
    176.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=469.0,
    y=164.0,
    width=284.0,
    height=23.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    606.0,
    291.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=464.0,
    y=279.0,
    width=284.0,
    height=23.0
)
window.resizable(False, False)
window.mainloop()