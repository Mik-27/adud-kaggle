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

element = soup.find_all(class_="icon-dashboard")[1]
child = element.findChildren("a", recursive=False)[0]
link = child.get("href")

print(link)
item = subprocess.Popen([r".\fetch2.bat", link], shell=True)