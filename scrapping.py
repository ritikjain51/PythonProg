import bs4
import requests

url = "https://www.mycodingzone.net/tutorials/python/english/getting-started-with-python"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text,'html.parser')
print(soup.prettify())

##for para in soup.find('p'): #for paricular paragraph
##    print(para)

##for para in soup.find_all('p'): # for  all paragraphs
##    print(para)

##for para in soup.find_all('p'): # if we want text only
##    print(para.text)

##for links in soup.find_all('a'): # if we need to get all links
##    link = links.get('href')
##    print(link)

##
##url2 = "https://www.youtube.com/channel/UCa5UDzFzpIjJ1VSxCSlQP_g/videos"
##data = requests.get(url2)
##soup = bs4.BeautifulSoup(data.text,'html.parser')
##for link in soup.find_all('a'):
##    link = link.get("href")
##    if link[0:3] == "/wa": ##array slicing
##        print("https://www.youtube.com/"+link)

##url3 = "https://www.mycodingzone.net/tutorials/python/english/getting-started-with-python"
##data = requests.get(url3)
##soup = bs4.BeautifulSoup(data.text,'html.parser')
####print(soup.prettify())
##
##for para in soup.find_all('p'): #for paricular paragraph
##    print(para.text)
