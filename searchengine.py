import requests
from bs4 import BeautifulSoup
import pyshorteners



def Jobat_Seek():
    Page = 1
    while True:

        Page_number = str(Page)
        url = "https://www.seek.co.nz/" + Keywords + "-jobs?page=" + Page_number
        response = requests.get(url)
        if response.status_code != 200:
            break
        if Page > 99:
            break

        soup = BeautifulSoup(response.text, 'html.parser')

        job_elements = soup.find_all("a", class_="_1tmgvw5 _1tmgvw8 _1tmgvwb _1tmgvwc _1tmgvwf yvsb870 yvsb87f _14uh994h")

        for a in job_elements:

                if a != None:
                    title_elements = a.text
                    print("Title: " + title_elements)
                    link_elements = a.get("href")
                    url = "https://www.seek.co.nz" + link_elements
                    type_tiny = pyshorteners.Shortener()
                    job_url = type_tiny.tinyurl.short(url)
                    print("Link:  " + job_url)

        Page = Page + 1

Keywords = input("Please input keywords to search: ")
Jobat_Seek()