import webbrowser
import pandas as pd
from random import randint
import tkinter


def search(query):
    query.replace(' ', '+')
    url = 'https://www.youtube.com/results?search_query={}'.format(query)
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)


def check_song(sentiment):
    df = pd.read_csv('example.csv')
    positive = df['sentiment'] == sentiment
    data = df[positive]
    artists = list(data['Artist'])
    songs = list(data['Name'])
    result = list(zip(artists, songs))
    end = len(result) - 1
    ind = randint(0, end)
    search_text = ' '.join(result[ind])
    search_text = search_text.replace('Lyrics', '')
    search(search_text)


root = tkinter.Tk()
root.configure(background='black')
label = tkinter.Label(root, text="How is your mood?", bg='black', fg='white', font=('', 60))
photo1 = tkinter.PhotoImage(file=r"images/sp.png")

Button1 = tkinter.Button(root, text="Happy", image=photo1,
                         compound=tkinter.LEFT, width=200, bg='black', fg='green', font=('', 13),
                         command=lambda: check_song("Strongly positive"))
photo2 = tkinter.PhotoImage(file=r"images/wp.png")
Button2 = tkinter.Button(root, text="Fine", image=photo2,
                         compound=tkinter.LEFT, width=200, bg='black', fg='green', font=('', 13),
                         command=lambda: check_song("Weakly positive"))
photo3 = tkinter.PhotoImage(file=r"images/n.png")
Button3 = tkinter.Button(root, text="Neutral", image=photo3,
                         compound=tkinter.LEFT, width=200, bg='black', fg='green', font=('', 13),
                         command=lambda: check_song("Neutral"))
photo4 = tkinter.PhotoImage(file=r"images/wn.png")
Button4 = tkinter.Button(root, text="Little sad", image=photo4,
                         compound=tkinter.LEFT, width=200, bg='black', fg='green', font=('', 13),
                         command=lambda: check_song("Weakly negative"))
photo5 = tkinter.PhotoImage(file=r"images/sn.png")
Button5 = tkinter.Button(root, text="Sad", image=photo5,
                         compound=tkinter.LEFT, width=200, bg='black', fg='green', font=('', 13),
                         command=lambda: check_song("Strongly negative"))
label.grid(row=0, column=0, columnspan=5)
Button1.grid(row=1, column=0)
Button2.grid(row=1, column=1)
Button3.grid(row=1, column=2)
Button4.grid(row=1, column=3)
Button5.grid(row=1, column=4)
root.mainloop()
