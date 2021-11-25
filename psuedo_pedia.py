import tkinter as tk
from bs4 import BeautifulSoup
import requests

class ArticlePriorityFinder:

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Pseudo-Wikipedia")
        self.root.config(bg="black")

        self.word_input = tk.Entry(self.root, font=("Cascadia Code", 15), width=30, bg="black", fg="white")
        self.word_input.grid(row=0, column=0, columnspan=1, padx=65, pady=10)
        self.sr = tk.Button(self.root, font=("Cascadia Code", 10), text="Find Article", command=self.scrape, bg="black", fg="white")
        self.sr.grid(row=1, column=0, columnspan=1, padx=65, pady=10)

        self.root.mainloop()
    
    def scrape(self) -> None:
        self.typed = self.word_input.get().lower()

        dict_url = f"https://www.wikipedia.com/wiki/{self.typed}"
        page = requests.get(dict_url).text
        page = BeautifulSoup(page, "html.parser")
        first_paragraph = page.find_all("p")[2].text
        result = tk.Label(self.root, font=("Cascadia Code", 10), text=first_paragraph, 
                          fg="white", bg="black", wrap=True, wraplength=300)
        result.grid(row=2, column=0, columnspan=1, padx=65, pady=10)
        
        print(first_paragraph)

ArticlePriorityFinder()
