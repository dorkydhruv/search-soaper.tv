import requests
from bs4 import BeautifulSoup
import webbrowser
import tkinter as tk

def search_soaper(keyword):
  """Searches soaper.tv for the given keyword and opens links in a web browser.
  Args:
      keyword: The keyword to search for.
  """
  url = f"https://soaper.tv/search.html?keyword={keyword.replace(' ', '%20')}"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")

  for link in soup.findAll('div', class_='panel panel-info panel-default'):
    image_container = link.findAll('div', class_='img-group')
    if "href" in str(image_container):
      link_url =  str(image_container).split('href="')[1].split('"')[0]
      webbrowser.open(f"https://soaper.tv{link_url}")

def get_keyword():
    """Gets the keyword from the entry field and searches soaper.tv for it."""
    keyword = entry_var.get()
    search_soaper(keyword)

root = tk.Tk()
root.title("Soaper.tv Search")
label = tk.Label(root, text="Enter your Series/Movie Name: ")
label.pack()
entry_var = tk.StringVar()
entry = tk.Entry(root,textvariable=entry_var)
entry.pack()
search = tk.Button(root,text="Search",command=get_keyword, bg="blue", fg="white")
search.pack()
root.mainloop()
