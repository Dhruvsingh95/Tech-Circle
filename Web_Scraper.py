import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import webbrowser

def scrape_autocar():
    url = "https://www.autocarindia.com/car-news"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    news_list = []


    articles = soup.select("a")

    for article in articles:
        title = article.get_text(strip=True)
        link = article.get("href")

        if title and link and "/car-news/" in link:
            if not link.startswith("http"):
                link = "https://www.autocarindia.com" + link

            news_list.append((title, link))

    seen = set()
    filtered_news = []
    for title, link in news_list:
        if title not in seen:
            filtered_news.append((title, link))
            seen.add(title)

    return filtered_news[:10]


def open_link(url):
    webbrowser.open(url)

def load_news():
    news = scrape_autocar()
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    for i, (title, link) in enumerate(news):
        btn = tk.Button(
            frame,
            text=title,
            font=("Segoe UI", 11),
            fg="white",
            bg="#1e1e2f",
            activebackground="#00adb5",
            wraplength=600,
            justify="left",
            anchor="w",
            command=lambda url=link: open_link(url)
        )
        btn.pack(fill="x", padx=10, pady=5)

# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("🚗 Indian Automotive News Dashboard")
root.geometry("750x600")
root.configure(bg="#0f172a") 


title_label = tk.Label(
    root,
    text="🚗 Automotive News India",
    font=("Segoe UI", 20, "bold"),
    bg="#0f172a",
    fg="#00adb5"
)
title_label.pack(pady=10)

refresh_btn = tk.Button(
    root,
    text="🔄 Refresh News",
    font=("Segoe UI", 12, "bold"),
    bg="#00adb5",
    fg="black",
    command=load_news
)
refresh_btn.pack(pady=10)


canvas = tk.Canvas(root, bg="#0f172a", highlightthickness=0)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)

frame = tk.Frame(canvas, bg="#0f172a")

frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

load_news()

root.mainloop()