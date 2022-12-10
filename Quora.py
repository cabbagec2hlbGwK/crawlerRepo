# Step 1: Install required libraries
#pip install beautifulsoup4

# Step 2: Import required libraries and modules
from bs4 import BeautifulSoup
import requests

# Step 3: Make a request to the Quora website to retrieve the HTML content of the page
url = "https://www.quora.com/topic/Python-programming-language"
page = requests.get(url)

# Step 4: Create a Beautiful Soup object using the HTML content of the page
soup = BeautifulSoup(page.content, "html.parser")

# Step 5: Extract the questions from the page
questions = soup.find_all("div", class_="question_text")
for question in questions:
    print(question.get_text())

# Step 6: Extract the answers to the questions on the page
answers = soup.find_all("span", class_="ui_qtext_rendered_qtext")
for answer in answers:
    print(answer.get_text())
