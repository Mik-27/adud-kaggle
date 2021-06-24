import requests
import subprocess
from bs4 import BeautifulSoup

url = "https://www.mohfw.gov.in"

try:
    site = requests.get(url)
except:
    print("Cannot connect to www.mohfw.gov.in")

html_content = site.content

soup = BeautifulSoup(html_content, "html.parser")

pdf_url = None

element = soup.find_all(class_="col-sm-2 btns")[0]
child = element.findChildren("ul", recursive=False)[0].findChildren("li", recursive=False)[0].findChildren("a", recursive=False)[0]
link = child.get("href")
# link = element[0].select("div > ul > a")

print(link)
# print(child)
item = subprocess.Popen([r".\fetch2.bat", link], shell=True)