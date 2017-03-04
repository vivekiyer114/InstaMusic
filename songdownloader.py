from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

x=1
while (x==1):
 songname=input ("Enter song name:\n")
 song_name=songname.replace(" ","+")


 youlink="https://www.youtube.com/results?search_query="+song_name

 html=urllib.request.urlopen(youlink).read()

 yousoup=BeautifulSoup(html,'html.parser')

 x=yousoup.find_all("h3",{"class":"yt-lockup-title"})

 c=0
 for z in x:
  if(c<5):
   print (str(c+1)+")"+z.a['title'])
   c=c+1

 linklist=[1,2,3,4,5]
 c=0
 for z in x:
    if(c<5):
      linklist[c]=z.a['href']
      c=c+1 ;

 print("\nWhich one do you wish to download ? Please select a NUMBER from above list")

 choice=eval(input())

 convlink=linklist[choice-1]
 actualconvlink="https://www.youtube.com"+convlink



 driver=webdriver.PhantomJS("pjs/bin/phantomjs")
 driver.get("https://www.youtube2mp3.cc/")
 songinput=driver.find_element_by_id("input")
 songinput.clear()
 songinput.send_keys(actualconvlink)
 elem=driver.find_element_by_id("button")
 elem.click()
 time.sleep(10)
 html=driver.page_source
 soup=BeautifulSoup(html,'html.parser')

 x=soup.find('a',{"id":"download"})
 downloads=x['href']
 fullname=songname+".mp3"

 if(os.path.isdir('music/')):
  name1=os.path.join("music/",fullname)
  urllib.request.urlretrieve(downloads,name1)
  print("\n-------------------------------------------------------------\n")
  print("Your music will be downloaded on songdownloader/music\n")
  print("-------------------------------------------------------------\n")
  x=input("Want to continue? Y or N\n")
  if(x=='Y' or x=='y'):
   x=1
  else :
   x=0
 else:
  os.mkdir('music')
  name1=os.path.join("music/",fullname)
  urllib.request.urlretrieve(downloads,name1)
  print("\n-------------------------------------------------------------\n")
  print("Your music will be downloaded on songdownloader/music\n")
  print("-------------------------------------------------------------\n")
  x=input("\nWant to continue ? Y or N\n ")
  if(x=='Y' or x=='y'):
   x=1
  else :
   x=0
