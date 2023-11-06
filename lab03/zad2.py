import requests
import random
from bs4 import BeautifulSoup

# Funkcja do pobierania losowego artykułu z Wikipedii
def get_random_wikipedia_article():
    # Pobierz tytuł losowego artykułu
    url = "https://pl.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=1&format=json"
    response = requests.get(url)
    data = response.json()
    title = data["query"]["random"][0]["title"]

    # Pobierz treść artykułu
    url = f"https://pl.wikipedia.org/w/api.php?action=parse&page={title}&format=json"
    response = requests.get(url)
    data = response.json()
    article_text = data["parse"]["text"]["*"]

    # Parsowanie treści artykułu
    soup = BeautifulSoup(article_text, "html.parser")
    article_text = soup.get_text()

    return title, article_text

# Funkcja do zapisania artykułu do pliku tekstowego
def save_article_to_file(title, article_text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(title + '\n\n')
        file.write(article_text)

if __name__ == "__main__":
    # Pobieramy losowy artykuł
    title, article_text = get_random_wikipedia_article()

    # Zapisujemy artykuł do pliku tekstowego
    filename = "losowy_artykul_wikipedia.txt"
    save_article_to_file(title, article_text, filename)

    print(f"Losowy artykuł został zapisany w pliku '{filename}'.")
