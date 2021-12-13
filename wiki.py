import wikipediaapi
from tkinter import *
from bs4 import BeautifulSoup


class WikiBot:
    @staticmethod
    def initiate(result, kw):

        kw_layout = Tk()
        kw_layout.configure(background='#1C1C1C', pady=15)
        kw_layout.resizable(False, False)
        kw_layout.title(kw)

        mainframe = Frame(kw_layout, bg="#DADADA")
        mainframe.grid(row=1, column=0, padx=50)

        label_title = Label(kw_layout, text=kw, bg="#1C1C1C", fg="white", font="Arial 16 bold")
        label_title.grid(row=0, column=0, pady=10)

        text_result = Text(mainframe, fg="#616161", font="Arial 12", bd=0, wrap=WORD,
                           background='#DADADA')
        text_result.insert(INSERT, result)
        text_result.grid(sticky=W, pady=5, padx=35)

        scrollb = Scrollbar(mainframe, command=text_result.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        text_result['yscrollcommand'] = scrollb.set

    @staticmethod
    def start_searching(kw):
        wiki_wiki = wikipediaapi.Wikipedia(
                    language='en',
                    extract_format=wikipediaapi.ExtractFormat.HTML
        )
        page_py = wiki_wiki.page(kw)
        print(page_py.fullurl)

        soup = BeautifulSoup(page_py.text, features="html.parser")
        result = soup.get_text()
        return result


class WikiGUI:
    def __init__(self):
        wiki_layout = Tk()
        wiki_layout.configure(background='#1C1C1C', pady=50, padx=100)
        wiki_layout.resizable(False, False)
        wiki_layout.title("Wikipedia Bot")

        label_wiki = Label(wiki_layout, text="What to learn?", background='#1C1C1C', font="Arial 15 bold", fg="white")
        label_wiki.grid(row=0, column=0, padx=15)

        input_wiki = Entry(wiki_layout, background='#949494', width=20, font="Arial 15", fg="white", borderwidth=0)
        input_wiki.grid(row=1, column=0, ipady=5, pady=10, padx=20)

        btn_wiki = Button(wiki_layout, text="Search", font="Arial 10 bold", bg="#949494", fg="white", borderwidth=0,
                          command=lambda: keyword_get())
        btn_wiki.grid(row=2, column=0, pady=10, ipady=5, ipadx=5)

        def keyword_get():
            kw = input_wiki.get()
            kw = kw.capitalize()
            input_wiki.delete(0, END)

            wiki = WikiBot()
            result = wiki.start_searching(kw)
            wiki.initiate(result, kw)

        wiki_layout.mainloop()


layout = WikiGUI()
