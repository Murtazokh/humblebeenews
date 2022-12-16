import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.shortcuts import render

HEADERS = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}

#Kun.uz
kun_uz_l = []
kun_uz_img = []
kun_uz_t=[]

#Uzreport
uzre_l=[]
uzre_img=[]
uzre_t=[]

#BBS Uzbeistan
bbc_l=[]
bbc_img=[]
bbc_t=[]

#gazeta.uz
gaz_l=[]
gaz_img=[]
gaz_t=[]

#UZDAILY.UZ
daily_l=[]
daily_img=[]
daily_t=[]

#QALAMPIR.UZ
qal_l=[]
qal_img=[]
qal_t=[]

#DARYO.UZ
dar_l=[]
dar_img=[]
dar_t=[]

#ANIQ.UZ
aniq_l=[]
aniq_img=[]
aniq_t=[]

#ONSIDE.UZ
side_l=[]
side_img=[]
side_t=[]

#SPORT.UZ
sport_l=[]
sport_img=[]
sport_t=[]

#UZ24.UZ
uz24_l=[]
uz24_img=[]
uz24_t=[]

#NUZ.UZ
nuz_l=[]
nuz_img=[]
nuz_t=[]

#KR.UZ
kr_l=[]
kr_img=[]
kr_t=[]

#sputniknews-uz.com
sputnik_l=[]
sputnik_img=[]
sputnik_t=[]

#SAMARKANDNEWS.UZ
samnews_l=[]
samnews_img=[]
samnews_t=[]

#UZA.UZ
uza_l=[]
uza_img=[]
uza_t=[]

#ZAMIN.UZ
zamin_l=[]
zamin_img=[]
zamin_t=[]

#UZMATBUOT.UZ
matbuot_l=[]
matbuot_img=[]
matbuot_t=[]

#BUGUN.UZ
bugun_l=[]
bugun_img=[]
bugun_t=[]

#AMERIKAOVOZI.COM
antimon_l=[]
antimon_img=[]
antimon_t=[]

#Function to scrape Kun.uz
def get_kun():
    page = requests.get("https://kun.uz/news/category/uzbekiston")
    soup = BeautifulSoup(page.content, 'html.parser')
    #Get all links
    a = soup.find_all('div', class_='col-md-4 mb-25 l-item')
    l1=[]
    l2=[]
    l3=[]
    for x in a:
        for link in x.find_all('a', {"class":"news__img"}):
            a=link.get('href')
            b='https://kun.uz'+link.get('href')
            l1.append(b)
        for img in x.find_all('img'):
            l2.append(img['src']) 
        for hd in x.find_all('a', {"class":"news__title"}):
            l3.append(hd.text)   
    
    [kun_uz_l.append(x) for x in l1 if x not in kun_uz_l]  
    [kun_uz_img.append(x) for x in l2 if x not in kun_uz_img]
    [kun_uz_t.append(x) for x in l3 if x not in kun_uz_t]
    
#Function to scrape Uzreport
def get_uzre():
    page2 = requests.get("https://www.uzreport.news/l/uz/football/")
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    #Get all links
    b = soup2.find_all('div', class_='col-xs-12 col-sm-12 col-md-12 col-lg-6')
    l1=[]
    l2=[]
    l3=[]
    l4=["/buzz/","/movies/","/sports/","/cricketnext/","/tech/","/football/"]
    for x in b:
        for link in x.find_all('a'):
            a = link.get('href')
            if a not in l4:
                l1.append(a)
        for img in x.find_all('img'):
            l2.append(img['src']) 
        for hd in x.find_all('div', class_="col-xs-7 col-sm-6 heading_newsbox_txt"):
         for a in hd.find('a'):
          l3.append(a.text.strip())

    [uzre_l.append(x) for x in l1 if x not in uzre_l]  
    [uzre_img.append(x) for x in l2 if x not in uzre_img]
    [uzre_t.append(x) for x in l3 if x not in uzre_t]

#Function to srape BBC
def get_bbc():
    page3 = requests.get("https://www.bbc.com/uzbek/topics/c8y949r98pgt")
    soup3 = BeautifulSoup(page3.content, 'html.parser')
    #Get all links
    b = soup3.find_all('ul', class_='bbc-1kz5jpr')
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all('h2', class_="bbc-hz8bw2 e47bds20"):
            for o in link.find_all("a"):
             l1.append(o.get("href"))
        for img in x.find_all('img'):
            l2.append(img['src']) 
        for hd in x.find_all('h2', class_="bbc-hz8bw2 e47bds20"):
            for a in hd.find_all('a'):
                l3.append(a.text)

    [bbc_l.append(x) for x in l1 if x not in bbc_l]  
    [bbc_img.append(x) for x in l2 if x not in bbc_img]
    [bbc_t.append(x) for x in l3 if x not in bbc_t]
    
#Function to scrape Gazeta.uz
def get_gaz():
    page4 = requests.get("https://www.gazeta.uz/uz/", headers=HEADERS)
    soup4 = BeautifulSoup(page4.content, 'html.parser')
    #Get all links
    b = soup4.find_all('div', class_='nblock')
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all('a'):
            a=link.get('href')
            b='https://gazeta.uz'+link.get('href')
            l1.append(b)
        for img in x.find_all('img'):
            l2.append(img['data-src']) 
        for hd in x.find_all('h3'):
            for a in hd.find_all('a'):
                l3.append(a.text.strip())

    [gaz_l.append(x) for x in l1 if x not in gaz_l]  
    [gaz_img.append(x) for x in l2 if x not in gaz_img]
    [gaz_t.append(x) for x in l3 if x not in gaz_t]

#function to scrape UZDAILY.UZ
def get_daily():
    page5 = requests.get("https://www.uzdaily.uz/uz/section/1", headers=HEADERS)
    soup5 = BeautifulSoup(page5.content, 'html.parser')
    #Get all links
    b = soup5.find_all('div', class_='row justify-content-between second_new_content')
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all('a'):
            a=link.get('href')
            l1.append(a)
        for img in x.find_all('img'):
            l2.append("http://uzdaily.uz"+img['src']) 
        for hd in x.find_all('h3', class_="title mt-1 text_wrap"):
                l3.append(hd.text.strip())
    del l1[0]
    [daily_l.append(x) for x in l1 if x not in daily_l]  
    [daily_img.append(x) for x in l2 if x not in daily_img]
    [daily_t.append(x) for x in l3 if x not in daily_t]    

#function to scrape QALAMPIR.UZ
def get_qal():
    page6 = requests.get("https://qalampir.uz/", headers=HEADERS)
    soup6 = BeautifulSoup(page6.content, 'html.parser')
    #Get all links
    b = soup6.find_all('div', class_='small_boxes')
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all('a', class_="ss_item item flex_row"):
            a=link.get('href')
            b='https://qalampir.uz'+link.get('href')
            l1.append(b)
        for img in x.find_all('img'):
            l2.append(img['src']) 
        for hd in x.find_all('div', class_="title"):
                l3.append(hd.text.strip())
    [qal_l.append(x) for x in l1 if x not in qal_l]  
    [qal_img.append(x) for x in l2 if x not in qal_img]
    [qal_t.append(x) for x in l3 if x not in qal_t]

#function to scrape DARYO.UZ
def get_daryo():
    page7 = requests.get("https://daryo.uz/", headers=HEADERS)
    soup7 = BeautifulSoup(page7.content, 'html.parser')
    #Get all links
    b = soup7.find_all('div', class_='main-tab-featured')
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all('a', class_="article__link"):
            b='https://daryo.uz'+link.get('href')
            l1.append(b)
        for img in x.find_all('img'):
            try:
                l2.append("http://daryo.uz"+img['src'])
            except:
                l2.append(("http://daryo.uz"+img['data-src'])) 
        for hd in x.find_all('b'):
                l3.append(hd.text.strip())
    [dar_l.append(x) for x in l1 if x not in dar_l]  
    [dar_img.append(x) for x in l2 if x not in dar_img]
    [dar_t.append(x) for x in l3 if x not in dar_t]  

#function to scrap ANIQ.UZ
def get_aniq():
    page8 = requests.get("https://aniq.uz/siyosat", headers=HEADERS)
    soup8 = BeautifulSoup(page8.content, 'html.parser')
    #Get all links
    b = soup8.find_all('div', class_='posts news-list')
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all('h2', class_="news-item_name"):
            for u in link.find_all('a'):
                a=u.get('href')
                l1.append(a)
        for img in x.find_all('img'):
            l2.append("http://aniq.uz"+img['src']) 
        for hd in x.find_all('h2'):
                l3.append(hd.text.strip())
    [aniq_l.append(x) for x in l1 if x not in aniq_l]  
    [aniq_img.append(x) for x in l2 if x not in aniq_img]
    [aniq_t.append(x) for x in l3 if x not in aniq_t]     

#function for scrape ONSIDE.UZ
def get_side():
    page9 = requests.get("http://onside.uz/home", headers=HEADERS)
    soup9 = BeautifulSoup(page9.content, 'html.parser')
    #Get all links
    b = soup9.find_all('div', class_='col-sm-9')
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all('a'):
            a=link.get('href')
            b='http://onside.uz'+link.get('href')
            l1.append(b)
        for img in x.find_all('img'):
            l2.append("http://onside.uz"+img['src']) 
        for hd in x.find_all('h2', class_='title'):
                l3.append(hd.text.strip())
    [side_l.append(x) for x in l1 if x not in side_l]  
    [side_img.append(x) for x in l2 if x not in side_img]
    [side_t.append(x) for x in l3 if x not in side_t]

#function to scrap SPORT.UZ 
def get_sport():
    page10 = requests.get("https://sports.uz/", headers=HEADERS)
    soup10 = BeautifulSoup(page10.content, 'html.parser')
    #Get all links
    b = soup10.find_all('div', class_='news-list')
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all('a'):
            a=link.get('href')
            b='https://sport.uz'+link.get('href')
            l1.append(b)
        for img in x.find_all('div', class_="img-block"):
            for z in img.find_all("img"):
                l2.append(z['data-src']) 
        for hd in x.find_all('h3'):
                l3.append(hd.text.strip())
    [sport_l.append(x) for x in l1 if x not in sport_l]  
    [sport_img.append(x) for x in l2 if x not in sport_img]
    [sport_t.append(x) for x in l3 if x not in sport_t]   

#function to scrap UZ24.UZ 
def get_uz24():
    page11 = requests.get("https://uz24.uz/uz", headers=HEADERS)
    soup11 = BeautifulSoup(page11.content, 'html.parser')
    #Get all links
    b = soup11.find_all('div', class_='block desktop-flex')
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all('a'):
            a=link.get('href')
            b='https://uz24.uz'+link.get('href')
            l1.append(b)
        for img in x.find_all('img'):
            l2.append(img.get("src")) 
        for hd in x.find_all('h3'):
                l3.append(hd.text.strip())
    [uz24_l.append(x) for x in l1 if x not in uz24_l]  
    [uz24_img.append(x) for x in l2 if x not in uz24_img]
    [uz24_t.append(x) for x in l3 if x not in uz24_t] 

#function to scrap NUZ.UZ 
def get_nuz():
    page12 = requests.get("https://nuz.uz/uz/", headers=HEADERS)
    soup12 = BeautifulSoup(page12.content, 'html.parser')
    #Get all links
    b = soup12.find_all('div', attrs={'id':'tdi_83'})
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all('h3', class_="entry-title td-module-title"):
            for w in link.find_all("a"):
                a=w.get('href')
                l1.append(a)
        for img in x.find_all('span'):
            l2.append(img.get("data-img-url")) 
        for hd in x.find_all('h3', class_="entry-title td-module-title"):
                l3.append(hd.text.strip())
    [nuz_l.append(x) for x in l1 if x not in nuz_l]  
    [nuz_img.append(x) for x in l2 if x not in nuz_img]
    [nuz_t.append(x) for x in l3 if x not in nuz_t] 

#function to scrap KR.UZ 
def get_kr():
    page13 = requests.get("https://www.kruz.uz/uz/", headers=HEADERS)
    soup13 = BeautifulSoup(page13.content, 'html.parser')
    #Get all links
    b = soup13.find_all('div', attrs={'class':'composs-blog-list lets-do-1'})
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all('div', class_="item-header"):
            for w in link.find_all("a"):
                a=w.get('href')
                l1.append("https://www.kruz.uz"+a)
        for img in x.find_all('img'):
            l2.append("https://www.kruz.uz"+img.get("src")) 
        for hd in x.find_all('h2'):
                l3.append(hd.text.strip())
    [kr_l.append(x) for x in l1 if x not in kr_l]  
    [kr_img.append(x) for x in l2 if x not in kr_img]
    [kr_t.append(x) for x in l3 if x not in kr_t]

#function to scrap SPUTNIKNEWS-UZ.COM 
def get_sputnik():
    page14 = requests.get("https://sputniknews-uz.com/?_ga=2.254437195.294759592.1670995243-1421766000.1670995243", headers=HEADERS)
    soup14 = BeautifulSoup(page14.content, 'html.parser')
    #Get all links
    b = soup14.find_all('div', attrs={'data-floor':'8'})
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all("a"):
                a=link.get('href')
                l1.append("https://sputniknews-uz.com"+a)
        for img in x.find_all('img'):
            l2.append(img.get("src")) 
        for hd in x.find_all('span', class_="cell-list__item-title"):
                l3.append(hd.text.strip())
    [sputnik_l.append(x) for x in l1 if x not in sputnik_l]  
    [sputnik_img.append(x) for x in l2 if x not in sputnik_img]
    [sputnik_t.append(x) for x in l3 if x not in sputnik_t]

#function to scrap SAMARKANDNEWS.UZ 
def get_samnews():
    page15 = requests.get("http://www.samarkandnews.uz/", headers=HEADERS)
    soup15 = BeautifulSoup(page15.content, 'html.parser')
    #Get all links
    b = soup15.find_all('div', attrs={'class':'col-lg-12 col-md-12'})
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all("a"):
                a=link.get('href')
                l1.append("http://www.samarkandnews.uz"+a)
        for img in x.find_all('img'):
            l2.append("http://www.samarkandnews.uz"+img.get("src")) 
        for hd in x.find_all('h2'):
                l3.append(hd.text.strip())
    [samnews_l.append(x) for x in l1 if x not in samnews_l]  
    [samnews_img.append(x) for x in l2 if x not in samnews_img]
    [samnews_t.append(x) for x in l3 if x not in samnews_t]

#function to scrap UZA.UZ
def get_uza():
    page16 = requests.get("https://uza.uz/uz", headers=HEADERS)
    soup16 = BeautifulSoup(page16.content, 'html.parser')
    #Get all links
    b = soup16.find_all('div', attrs={'class':'small-news-list'})
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all("a", class_="small-news__title"):
                a=link.get('href')
                l1.append("https://uza.uz/"+a)
        for img in x.find_all('img'):
            l2.append(img.get("src")) 
        for hd in x.find_all('a', class_="small-news__title"):
                l3.append(hd.text.strip())
    [uza_l.append(x) for x in l1 if x not in uza_l]  
    [uza_img.append(x) for x in l2 if x not in uza_img]
    [uza_t.append(x) for x in l3 if x not in uza_t]

#function to scrap ZAMIN.UZ
def get_zamin():
    page17 = requests.get("https://zamin.uz/uz/ozbekiston/", headers=HEADERS)
    soup17 = BeautifulSoup(page17.content, 'html.parser')
    #Get all links
    b = soup17.find_all('div', attrs={'class':'sect-content fx-row'})
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all("a"):
                l1.append("https:"+link.get("href"))
        for img in x.find_all('img'):
            l2.append("https://zamin.uz"+img.get("src")) 
        for hd in x.find_all('div', class_="short-text"):
                l3.append(hd.text.strip())
    [zamin_l.append(x) for x in l1 if x not in zamin_l]  
    [zamin_img.append(x) for x in l2 if x not in zamin_img]
    [zamin_t.append(x) for x in l3 if x not in zamin_t]

#function to scrap ZAMIN.UZ
def get_matbuot():
    page18 = requests.get("https://uzmatbuot.uz/category/jarayen/", headers=HEADERS)
    soup18 = BeautifulSoup(page18.content, 'html.parser')
    #Get all links
    b = soup18.find_all('div', attrs={'class':'page-content'})
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all('h4', class_="archive-post__title feature"):
            for o in link.find_all("a"):
                l1.append(o.get("href"))
        for img in x.find_all('div', class_="archive-post__img"):
                for r in img.find_all("img"):
                    l2.append(r.get("nitro-lazy-src")) 
        for hd in x.find_all('h4', class_="archive-post__title feature"):
                l3.append(hd.text.strip())
    [matbuot_l.append(x) for x in l1 if x not in matbuot_l]  
    [matbuot_img.append(x) for x in l2 if x not in matbuot_img]
    [matbuot_t.append(x) for x in l3 if x not in matbuot_t]

#function to scrap ZAMIN.UZ
def get_bugun():
    page19 = requests.get("https://bugun.uz/", headers=HEADERS)
    soup19 = BeautifulSoup(page19.content, 'html.parser')
    #Get all links
    b = soup19.find_all('div', attrs={'class':'post__inner'})
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all("a", class_="post__photo"):
                l1.append(link.get("href"))
        for img in x.find_all('img'):
            l2.append(img.get("data-src"))        
        for hd in x.find_all('img'):
                l3.append(hd.get('alt'))
    [bugun_l.append(x) for x in l1 if x not in bugun_l]  
    [bugun_img.append(x) for x in l2 if x not in bugun_img]
    [bugun_t.append(x) for x in l3 if x not in bugun_t]

#function to scrap ANTIMON.GOV.UZ
def get_antimon():
    page20 = requests.get("https://antimon.gov.uz/prezident-matbuot-xizmati-yangiliklari/", headers=HEADERS)
    soup20 = BeautifulSoup(page20.content, 'html.parser')
    #Get all links
    b = soup20.find_all('div', attrs={'class':'wpb_wrapper'})
    l1=[]
    l2=[]
    l3=[]
    for x in b:
        for link in x.find_all("div", class_='post-thumbnail'):
                for o in link.find_all('a'):
                    l1.append(o.get("href"))
        for img in x.find_all('img'):
            l2.append(img.get("data-src"))        
        for hd in x.find_all('h3', class_="entry-title"):
                l3.append(hd.text.strip())
    [antimon_l.append(x) for x in l1 if x not in antimon_l]  
    [antimon_img.append(x) for x in l2 if x not in antimon_img]
    [antimon_t.append(x) for x in l3 if x not in antimon_t]

get_kun()     #1
get_uzre()    #2 
get_bbc()     #3
get_gaz()     #4
get_daily()   #5
get_qal()     #6
get_daryo()   #7
get_aniq()    #8
get_side()    #9
get_sport()   #10 
get_uz24()    #11 
get_nuz()     #12
get_kr()      #13
get_sputnik() #14
get_samnews() #15
get_uza()     #16
get_zamin()   #17
get_matbuot() #18
get_bugun()   #19
get_antimon() #20

def index(req):
    context = {
    'kun_uz_l':kun_uz_l, 
    'kun_uz_img': kun_uz_img, 
    'kun_uz_t':kun_uz_t, 

    'uzre_l':uzre_l, 
    'uzre_img':uzre_img,
    'uzre_t':uzre_t , 

    'bbc_l':bbc_l, 
    'bbc_img':bbc_img,
    'bbc_t':bbc_t,

    'gaz_l':gaz_l,
    'gaz_img':gaz_img,
    'gaz_t':gaz_t,

    'daily_l':daily_l,
    'daily_img':daily_img,
    'daily_t':daily_t,

    'qal_l': qal_l,
    'qal_img':qal_img,
    'qal_t':qal_t,

    'dar_l':dar_l,
    'dar_img':dar_img,
    'dar_t':dar_t,

    'aniq_l':aniq_l,
    'aniq_img':aniq_img,
    'aniq_t':aniq_t,
    
    'side_l':side_l,
    'side_img':side_img,
    'side_t':side_t,

    'sport_l':sport_l,
    'sport_img':sport_img,
    'sport_t':sport_t,

    'uz24_l':uz24_l,
    'uz24_img':uz24_img,
    'uz24_t':uz24_t,

    'nuz_l':nuz_l,
    'nuz_img':nuz_img,
    'nuz_t':nuz_t,

    'kr_l':kr_l,
    'kr_img':kr_img,
    'kr_t':kr_t,

    'sputnik_l':sputnik_l,
    'sputnik_img':sputnik_img,
    'sputnik_t':sputnik_t,

    'samnews_l':samnews_l,
    'samnews_img':samnews_img,
    'samnews_t':samnews_t,

    'uza_l':uza_l,
    'uza_img':uza_img,
    'uza_t':uza_t,

    'zamin_l':zamin_l,
    'zamin_img':zamin_img,
    'zamin_t':zamin_t,

    'matbuot_l':matbuot_l,
    'matbuot_img':matbuot_img,
    'matbuot_t':matbuot_t,

    'bugun_l':bugun_l,
    'bugun_img':bugun_img,
    'bugun_t':bugun_t,

    'antimon_l':antimon_l,
    'antimon_img':antimon_img,
    'antimon_t':antimon_t,
    }
    return render(req, 'news/index.html', context )