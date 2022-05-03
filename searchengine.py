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




def Jobat_Spark():


    # combine prefix and keywords to useable url
    url = "https://careers.sparknz.co.nz/search?search=kw-"+Keywords

    # parse the page from url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # filter parse result using class
    job_elements = soup.find_all("div", class_="col-xs-12 col-sm-11 col-md-11 col-lg-11")

    # find job information
    for job_details in job_elements:
        try:
            job_info = job_details.find("a", class_="clicker-link")

            # find job title
            job_names = job_info.find("span")
            job_name = job_names.text
            print("Title: " + job_name)

            # find job link
            job_link1 = job_info.get("href")
            url = "https://careers.sparknz.co.nz" + job_link1
            type_tiny = pyshorteners.Shortener()
            job_url = type_tiny.tinyurl.short(url)
            print("Link:  " + job_url)
        except:
            break

# user input
Keywords = input("Please input keywords to search: ")

website = input("Please input which website you want to search: Spark, Seek or just press enter for all: ")

if website in ['Spark', 'spark']:
    Jobat_Spark()
elif website in ['Seek', 'seek']:
    Jobat_Seek()
else:
    Jobat_Spark()
    Jobat_Seek()
