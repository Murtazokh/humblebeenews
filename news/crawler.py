import requests
import re
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
from django.shortcuts import render, redirect
from news.models import *

HEADERS = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
SESSION = requests.Session()


def get_latest(request):
    Post.objects.all().delete()  

    #kun.uz
    page = SESSION.get("https://kun.uz/news/category/uzbekiston")
    strainer = SoupStrainer('div', attrs={'class': 'col-md-4 mb-25 l-item'})
    soup = BeautifulSoup(page.content, 'html.parser', parse_only=strainer)
    a = soup.find_all('div', class_='col-md-4 mb-25 l-item')[:4]

    page1 = SESSION.get("https://www.uzdaily.uz/uz/section/1", headers=HEADERS)
    strainer1 = SoupStrainer('div', attrs={'class': 'dis_flex box_shadow margin_block'})
    soup1 = BeautifulSoup(page1.content, 'html.parser', parse_only=strainer1)
    e = soup1.find_all('div', class_='dis_flex box_shadow margin_block')[:4]

    page2 = SESSION.get("https://www.gazeta.uz/uz/", headers=HEADERS)
    strainer4 = SoupStrainer('div', attrs={'class': 'nblock'})
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    d = soup2.find_all('div', class_='nblock')[:4]
    
    page3 = SESSION.get("https://daryo.uz/")
    strainer4 = SoupStrainer('article', attrs={'class': 'article__small border'})
    soup3 = BeautifulSoup(page3.content, 'html.parser', parse_only=strainer4)
    b = soup3.find_all('article', class_='article__small border')[:4]

    page4 = SESSION.get("https://uza.uz/uz")
    strainer7 = SoupStrainer('div', attrs={'class': 'small-news'})
    soup4 = BeautifulSoup(page4.content, 'html.parser', parse_only=strainer7)
    f = soup4.find_all('div', class_='small-news')[:4]
        
    for x in a:
        t = x.find('a', {"class":"news__title"})
        title = t.text       
        l = x.find('a', {"class":"news__img"})
        link = 'https://kun.uz'+l.get('href')
        i = x.find('img')
        image = i['src']
        p = SESSION.get(f"{link}")
        strainer2 = SoupStrainer('div', attrs={'class': 'single-content'})
        s = BeautifulSoup(p.content, 'html.parser', parse_only=strainer2)
        strainer_2 = SoupStrainer('div', attrs={'class': 'main-img'})
        s_ = BeautifulSoup(p.content, 'html.parser', parse_only=strainer_2)
        body = s.find("div",class_="single-content").text
        try:
                body_image_kun = s_.find("img").get('src')
        except:
                body_image_kun = "no photo"        
               
        p = Post()
        p.title = title
        p.image = image
        p.body = body
        p.body_image = body_image_kun
        p.save() 
    
    for r in e:
        t4 = r.find("h3", class_="title mt-1 text_wrap")
        daily_t = t4.text        
        l4 = r.find('a', class_="read_more")
        daily_l = l4.get('href')
        i4 = r.find('img')
        daily_img = "http://uzdaily.uz"+i4['src']
        p1 = SESSION.get(f"{daily_l}",headers=HEADERS)
        strainer3 = SoupStrainer('div', attrs={'class': 'main links'})
        s1 = BeautifulSoup(p1.content, 'html.parser', parse_only=strainer3)
        body1 = s1.find("div", class_="main links").text
        body_image_daily ="http://uzdaily.uz"+ s1.find("img", class_="img-fluid").get('src')

        p = Post()
        p.title = daily_t
        p.image = daily_img
        p.body = body1
        p.body_image = body_image_daily
        p.save()

    for e in d:
        t3 = e.find("h3")
        gaz_t = t3.a.text        
        l3 = e.find('a')
        gaz_l = 'https://gazeta.uz'+l3.get('href')
        i3 = e.find('img')
        gaz_img = i3['data-src']
        p1 = SESSION.get(f"{gaz_l}",headers=HEADERS)
        strainer5 = SoupStrainer('div', attrs={'class': 'js-mediator-article article-text'})
        s1 = BeautifulSoup(p1.content, 'html.parser',parse_only= strainer5)
        body2 = s1.find("div", class_="js-mediator-article article-text").text  
        strainer_5 = SoupStrainer('div', attrs={'class': 'articleTopBG'})
        s_1 = BeautifulSoup(p1.content, 'html.parser',parse_only= strainer_5)
        body_image_gazeta = s_1.find("img", class_="lazy articleBigPic").get('data-src')

        p = Post()
        p.title = gaz_t
        p.image = gaz_img
        p.body = body2
        p.body_image = body_image_gazeta
        p.save() 

    for q in b:
        t1 = q.find('a', class_="article__link")
        daryo_t = t1.text.strip()        
        daryo_l = 'https://daryo.uz'+t1.get('href')
        i1 = q.find('img')
        try:
            daryo_img = 'https://daryo.uz'+i1['src']
        except:
            daryo_img = 'https://daryo.uz'+i1['data-src']
        p1 = SESSION.get(f"{daryo_l}",headers=HEADERS)
        strainer6 = SoupStrainer('div', attrs={'class': 'default__section border'})
        s1 = BeautifulSoup(p1.content, 'html.parser', parse_only=strainer6)
        body3 = s1.find("div", class_="default__section border").text 
        try:   
                body_image_daryo = 'https://daryo.uz'+s1.find('img').get('src') 
        except:
                body_image_daryo = "No photo provided"       

        p = Post()
        p.title = daryo_t
        p.image = daryo_img
        p.body = body3
        p.body_image = body_image_daryo
        p.save() 

    for z in f:
        t1 = z.find('a', class_="small-news__title")
        uza_t = t1.text.strip()        
        uza_l ="https://uza.uz/uz/"+ t1.get('href')
        i1 = z.find('img')
        uza_img = i1['src']
        p1 = SESSION.get(f"{uza_l}",headers=HEADERS)
        strainer6 = SoupStrainer('div', attrs={'class': 'content-block'})
        strainer8 = SoupStrainer('div', attrs={'class': 'news-top-head__content'})
        s1 = BeautifulSoup(p1.content, 'html.parser',parse_only= strainer6)
        s2 = BeautifulSoup(p1.content, 'html.parser',parse_only= strainer8)
        body4 = s1.find("div", attrs={'class': 'content-block'}).text  
        body_image_uza = s2.find("img").get('src')  


        p = Post()
        p.title = uza_t
        p.image = uza_img
        p.body = body4
        p.body_image = body_image_uza
        p.save()

    return redirect( '../')


def get_sport(request):
    """This function scrapes 5 websites and give the information to class"""
    #DELETING OLD NEWS FROM DATABASE:
    Sport.objects.all().delete()

    #URL AND MAIN TAG OF daryo.uz:
    page6 = SESSION.get("https://daryo.uz/category/sport", headers=HEADERS)
    strainer6 = SoupStrainer('div', attrs={'class': 'mini__article'})
    soup6 = BeautifulSoup(page6.content, 'html.parser', parse_only=strainer6)
    a = soup6.find_all('div', class_='mini__article')[:4]
   
    #URL AND MAIN TAG OF ONSIDE.UZ:
    page7 = SESSION.get("http://onside.uz/home", headers=HEADERS)
    strainer7 = SoupStrainer('div', attrs={'class': 'col-sm-6'})
    soup7 = BeautifulSoup(page7.content, 'html.parser', parse_only=strainer7)
    b = soup7.find_all('div', class_='col-sm-6')[:4]
   
    #URL AND MAIN TAGS OF SPORTS.UZ:
    page8 = SESSION.get("https://sports.uz/", headers=HEADERS)
    strainer8 = SoupStrainer('div', attrs={'class': 'news-body'})
    soup8 = BeautifulSoup(page8.content, 'html.parser')
    strainer_8 = SoupStrainer('div', attrs={'class': 'item'})
    soup_8 = BeautifulSoup(page8.content, 'html.parser',parse_only=strainer_8)
    d = soup8.find_all('div', class_='news-body')[:4]
    dd = soup_8.find_all('div', class_='img-block')[:4]
   
    #URL AND MAIN TAGS OF NUZ.UZ:
    page9 = SESSION.get("https://sportuz.net/", headers=HEADERS)
    strainer9 = SoupStrainer('div', attrs={'class': 'col-sm-4'})
    soup9 = BeautifulSoup(page9.content, 'html.parser', parse_only=strainer9)
    c = soup9.find_all('div', class_='col-sm-4')[:4]
   
    #URL AND MAIN TAGS OF sputniknews-uz.com:
    page10 = SESSION.get("https://sputniknews-uz.com/sport/", headers=HEADERS)
    strainer10 = SoupStrainer('div', attrs={'class': 'list__item'})
    soup10 = BeautifulSoup(page10.content, 'html.parser')
    e_1 = soup10.find_all('div', class_='list__item')[:4]
    
    
    for q in a:
        # daryo.uz
        t1 = q.find("b")
        dar_t = t1.text.strip()        
        l1 = q.find('a', class_="mini__article-link")
        dar_l = 'https://daryo.uz'+l1.get('href')
        i1 = q.find('img')
        try:
                dar_img=("http://daryo.uz"+i1['src'])
        except:
                dar_img=(("http://daryo.uz"+i1['data-src']))
        p6 = SESSION.get(dar_l)
        strainer6 = SoupStrainer('div', attrs={'class': 'default__section border'})
        s6 = BeautifulSoup(p6.content, 'html.parser', parse_only=strainer6)        
        body6 = s6.find("div", class_="default__section border").text 
        try:
                body_image_daryo = 'https://daryo.uz'+s6.find('img').get('src')
        except:
                body_image_daryo = 'https://daryo.uz'+s6.find('img').get('data-src')
        S = Sport()
        S.title = dar_t
        S.image = dar_img
        S.body = body6
        S.body_image = body_image_daryo
        S.save()

    for w in b:
        t2 = w.find('h2', class_='title')
        side_t = t2.text.strip()        
        l2 = w.find('a')
        side_l = 'http://onside.uz'+l2.get('href')
        i2 = w.find('img')
        side_img=("http://onside.uz"+i2['src']) 
        p8 = SESSION.get(side_l)
        strainer8 = SoupStrainer('div', attrs={'class': 'col-sm-8 pl-15'})
        s7 = BeautifulSoup(p8.content, 'html.parser', parse_only=strainer8)        
        body7 = s7.find("p").text 
        strainer_8 = SoupStrainer('div', attrs={'class': 'col-sm-4 minh'})
        s_7 = BeautifulSoup(p8.content, 'html.parser', parse_only=strainer_8)
        body_image_side = "http://onside.uz"+s_7.find('img').get('src')
        S = Sport()
        S.title = side_t
        S.image = side_img
        S.body = body7
        S.body_image = body_image_side
        S.save() 

    for r,e in zip(d,dd):
        t3 = r.find('h3')
        sport_t = t3.text.strip()        
        l3 = e.find('a')
        sport_l = 'https://sports.uz'+l3.get('href')
        i3 = e.find('img')
        sport_img=i3['data-src']
        p11 = SESSION.get(sport_l)
        strainer11 = SoupStrainer('div', attrs={'class': 'news-body'})
        s11 = BeautifulSoup(p11.content, 'html.parser', parse_only=strainer11) 
        strainer_11 = SoupStrainer('div', attrs={'class': 'news-container'})
        s_11 = BeautifulSoup(p11.content, 'html.parser', parse_only=strainer_11)       
        body11 = s11.text
        try:
            body_image_sport = s_11.find('img').get('src')
        except:
            body_image_sport = s_11.find('img').get('data-src')     
        S = Sport()
        S.title = sport_t
        S.image = sport_img 
        S.body = body11
        S.body_image = body_image_sport  
        S.save()

    for t in c:
        t4 = t.find('p', class_="titlenews")
        nuz_t = t4.text.strip()        
        nuz_l = "https://sportuz.net/"+t4.find('a').get('href')
        i4 = t.find('img')
        nuz_img="https://sportuz.net/"+i4['src']

        p11 = SESSION.get(nuz_l, headers=HEADERS)
        strainer11 = SoupStrainer('div', attrs={'class': 'newspage'})
        s11 = BeautifulSoup(p11.content, 'html.parser', parse_only=strainer11) 
        body11 = s11.find('div', attrs={'class': 'newspage'})
        body_image11 = "https://sportuz.net/ufc/"+s11.find('img', class_='img').get('src')
        # for i in body11.find_all('p'):
        #         a=i.text
                
        regex = re.compile(r"/imageboksufc/../")
        body_image_11 = regex.sub('/',body_image11)    
        S = Sport()
        S.title = nuz_t
        S.image = nuz_img
        
        S.body_image = body_image_11
        S.save()

    for f in e_1:
        t5= f.find('a', attrs={'class':"list__title"})
        sputnik_t = t5.text.strip()       
        l5 = f.find('a', class_="list__title")
        sputnik_l = "https://sputniknews-uz.com"+l5.get('href')
        i5 = f.find('img')
        sputnik_img= i5['src']    
        p10 = SESSION.get(sputnik_l)
        strainer10 = SoupStrainer('div', attrs={'class': 'photoview__open'})
        s10 = BeautifulSoup(p10.content, 'html.parser', parse_only=strainer10) 
        strainer_10 = SoupStrainer('div', attrs={'class': 'article__body'})
        s_10 = BeautifulSoup(p10.content, 'html.parser', parse_only=strainer_10)       
        body10 = s_10.find('div', attrs={'class': 'article__body'}).text
        body_image_sputnik = s10.find('img').get('src')     
        
        S = Sport()
        S.title = sputnik_t
        S.image = sputnik_img
        S.body = body10
        S.body_image = body_image_sputnik
        S.save()
    return redirect("../sport/")              


def get_siyosat(request):
    """This function scrapes 5 websites and give the information to class"""
    #DELETING OLD NEWS FROM DATABASE:
    Politics.objects.all().delete()

    #URL AND MAIN TAG OF daryo.UZ:
    page1 = SESSION.get("https://aniq.uz/siyosat", headers=HEADERS)
    strainer1 = SoupStrainer('div', class_='news-list_item article')
    soup1 = BeautifulSoup(page1.content, 'html.parser', parse_only=strainer1)
    a = soup1.find_all('div', class_='news-list_item article')[:4]

    page2 = SESSION.get("https://water.gov.uz/uz/posts/1545735855", headers=HEADERS)
    strainer2 = SoupStrainer('div', attrs={'id':'section-to-print'})
    soup2 = BeautifulSoup(page2.content, 'html.parser', parse_only=strainer2)
    b = soup2.find_all('div', class_='item')[:4]

    page3 = SESSION.get("https://uz24.uz/uz/categories/politics", headers=HEADERS)
    strainer3 = SoupStrainer('article', class_='article-row tablet-flex block')
    soup3 = BeautifulSoup(page3.content, 'html.parser', parse_only=strainer3)
    c = soup3.find_all('article', class_='article-row tablet-flex block')[:4]

    page4 = SESSION.get("https://www.bbc.com/uzbek/topics/cwr9j9dz4gpt", headers=HEADERS)
    strainer4 = SoupStrainer('li', class_='bbc-v8cf3q')
    soup4 = BeautifulSoup(page4.content, 'html.parser', parse_only=strainer4)
    d = soup4.find_all('li', class_='bbc-v8cf3q')[:4]

    page5 = SESSION.get("https://president.uz/uz", headers=HEADERS)
    strainer4 = SoupStrainer('div', class_='col-md-4 col-sm-4 events_box')
    soup5 = BeautifulSoup(page5.content, 'html.parser',parse_only=strainer4)
    e = soup5.find_all('div', class_='col-md-4 col-sm-4 events_box')[:4]

    for a in a:
        t1 = a.find('h2')
        aniq_t = t1.text.strip()        
        l1 = a.find('a')
        aniq_l = l1.get('href')
        i1 = a.find('img')
        aniq_img="http://aniq.uz"+i1['src']

        p1 = SESSION.get(aniq_l)
        strainer_1 = SoupStrainer('div', attrs={'class': 'news-item_text'})
        strainer__1 = SoupStrainer('div', attrs={'class': 'news-item_img'})
        body1 = BeautifulSoup(p1.content, 'html.parser', parse_only=strainer_1).text        
        body_image_1 = BeautifulSoup(p1.content, 'html.parser', parse_only=strainer__1)
        body_image__1 = "http://aniq.uz"+body_image_1.find('img').get('src')

        P = Politics()
        P.title = aniq_t
        P.image = aniq_img
        P.body = body1
        P.body_image = body_image__1
        P.save()

    for b in b:
        t2 = b.find('h4')
        antimon_t = t2.text.strip()        
        l2 = b.find('a')
        antimon_l = l2.get('href')
        i2 = b.find('img')
        antimon_img=i2['src']

        p2 = SESSION.get(antimon_l)
        strainer_2 = SoupStrainer('div', attrs={'class': 'col-md-10 col-sm-10'})
        strainer__2 = SoupStrainer('div', attrs={'class': 'col-md-12 col-sm-12'})
        body2 = BeautifulSoup(p2.content, 'html.parser', parse_only=strainer_2).text        
        body_image_2 = BeautifulSoup(p2.content, 'html.parser', parse_only=strainer__2)
        body_image__2 = body_image_2.find('img').get('src')

        P = Politics()
        P.title = antimon_t
        P.image = antimon_img
        P.body = body2
        P.body_image = body_image__2
        P.save()
    
    for c in c:
        t3 = c.find('h3')
        uz24_t = t3.text.strip()        
        l3 = c.find('a')
        uz24_l = "https://uz24.uz"+l3.get('href')
        i3 = c.find('img')
        uz24_img=i3['src']

        p3 = SESSION.get(uz24_l)
        strainer_3 = SoupStrainer('div', attrs={'class': 'block'})
        strainer__3 = SoupStrainer('picture', attrs={'class': 'full'})
        body3 = BeautifulSoup(p3.content, 'html.parser', parse_only=strainer_3).text        
        body_image_3 = BeautifulSoup(p3.content, 'html.parser', parse_only=strainer__3)
        body_image__3 = body_image_3.find('img').get('src')

        P = Politics()
        P.title = uz24_t
        P.image = uz24_img
        P.body = body3
        P.body_image = body_image__3
        P.save()

    for d in d:
        t4 = d.find('h2', class_="bbc-hz8bw2 e47bds20")
        bbc_t = t4.text.strip()        
        l4 = d.find('a', class_="bbc-uk8dsi e1d658bg0")
        bbc_l = l4.get('href')
        i4 = d.find('img')
        bbc_img=i4['src']

        p4 = SESSION.get(bbc_l)
        strainer_4 = SoupStrainer('div', attrs={'class': 'bbc-19j92fr ebmt73l0'})
        strainer__4 = SoupStrainer('div', attrs={'class': 'bbc-997y1y eihqrxw0'})
        body4 = BeautifulSoup(p4.content, 'html.parser', parse_only=strainer_4).text        
        body_image_4 = BeautifulSoup(p4.content, 'html.parser', parse_only=strainer__4)
        body_image__4 = body_image_4.find('img').get('src')

        P = Politics()
        P.title = bbc_t
        P.image = bbc_img
        P.body = body4
        P.body_image = body_image__4
        P.save()

    for e in e:
        t5 = e.find('a', class_="events_title")
        pr_t = t5.text.strip()        
        l5 = e.find('a', class_="events_title")
        pr_l = "https://president.uz"+l5.get('href')
        i5 = e.find('img')
        pr_img= "https://president.uz"+i5['src'] 

        p5 = SESSION.get(pr_l)
        strainer_5 = SoupStrainer('div', attrs={'class': 'status_box_second'})
        body5 = BeautifulSoup(p5.content, 'html.parser', parse_only=strainer_5).text        
        body_image_5 = BeautifulSoup(p5.content, 'html.parser', parse_only=strainer_5)
        body_image__5 = "https://president.uz"+body_image_5.find('img').get('src')

        P = Politics()
        P.title = pr_t
        P.image = pr_img
        P.body = body5
        P.body_image = body_image__5
        P.save()

    return redirect("../politics/")


def get_economy(request):
    """This function scrapes 5 websites and give the information to class"""
    #DELETING OLD NEWS FROM DATABASE:
    Economy.objects.all().delete()

    page1 = SESSION.get("http://samarkandnews.uz/post/category/Iqtisodiyot", headers=HEADERS)
    strainer1 = SoupStrainer('div', class_='col-12 col-md-6')
    soup1 = BeautifulSoup(page1.content, 'html.parser', parse_only=strainer1)
    a = soup1.find_all('div', class_='col-12 col-md-6')[:4]

    page2 = SESSION.get("https://www.gazeta.uz/uz/economy/", headers=HEADERS)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    b = soup2.find_all('div', class_='nblock')[:4]

    page3 = SESSION.get("https://kommers.uz/", headers=HEADERS)
    strainer3 = SoupStrainer('div', class_='post')
    soup3 = BeautifulSoup(page3.content, 'html.parser', parse_only=strainer3)
    d = soup3.find_all('div', class_='post')[:4]

    page4 = SESSION.get("https://kun.uz/news/category/iktisodiet", headers=HEADERS)
    strainer4 = SoupStrainer('div', class_='col-md-4 mb-25 l-item')
    soup4 = BeautifulSoup(page4.content, 'html.parser', parse_only=strainer4)
    c = soup4.find_all('div', class_='col-md-4 mb-25 l-item')[:4]

    page5 = SESSION.get("https://aniq.uz/uz/iktisod", headers=HEADERS)
    strainer5 = SoupStrainer('div', class_='news-item_img')
    soup5 = BeautifulSoup(page5.content, 'html.parser', parse_only=strainer5)
    e = soup5.find_all('div', class_='news-item_img')[:4]

    for a in a:
        t1= a.find('h2', class_="post-title title-large")
        samnews_t = t1.text.strip()        
        l1 = a.find('a')
        samnews_l = "http://samarkandnews.uz"+l1.get('href')
        i1 = a.find('img', class_="img-fluid")
        samnews_img= "http://samarkandnews.uz"+i1['src'] 

        p6 = SESSION.get(samnews_l)
        strainer6 = SoupStrainer('div', attrs={'class': 'entry-content'})
        strainer_6 = SoupStrainer('div', attrs={'class': 'post-media post-featured-image'})
        body6 = BeautifulSoup(p6.content, 'html.parser', parse_only=strainer6).text        
        body_image_6 = BeautifulSoup(p6.content, 'html.parser', parse_only=strainer_6)
        body_image__6 = "http://samarkandnews.uz"+body_image_6.find('img').get('src')

        E = Economy()
        E.title = samnews_t
        E.image = samnews_img
        E.body = body6
        E.body_image = body_image__6
        E.save()

    for d in d:
        t3= d.find('img')
        bugun_t = t3.get('alt')        
        l3 = d.find('a', class_="post__photo")
        bugun_l = l3.get('href')
        i3 = d.find('img')
        bugun_img= i3['src']

        p7 = SESSION.get(bugun_l)
        strainer7 = SoupStrainer('div', attrs={'class': 'blog__body'})
        body7 = BeautifulSoup(p7.content, 'html.parser', parse_only=strainer7).text        
        body_image_7 = BeautifulSoup(p7.content, 'html.parser', parse_only=strainer7)
        body_image__7 = body_image_7.find('img').get('src')

        E = Economy()
        E.title = bugun_t
        E.image = bugun_img
        E.body = body7
        E.body_image = body_image__7
        E.save()

    for c in c:
        t4= c.find('a', class_='news__title')
        uza_t = t4.text.strip()        
        l4 = c.find('a', class_="news__title")
        uza_l = "https://kun.uz"+l4.get('href')
        i4 = c.find('img')
        uza_img= i4['src']

        p8 = SESSION.get(uza_l)
        strainer8 = SoupStrainer('div', attrs={'class': 'single-content'})
        s8 = BeautifulSoup(p8.content, 'html.parser', parse_only=strainer8)
        strainer_8 = SoupStrainer('div', attrs={'class': 'main-img'})
        s_8 = BeautifulSoup(p8.content, 'html.parser',parse_only=strainer_8)
        body8 = s8.find("div",class_="single-content").text
        try:
                body_image__8 = s_8.find('img').get('src')
        except:
                body_image__8 = "no photo" 

        E = Economy()
        E.title = uza_t
        E.image = uza_img
        E.body = body8
        E.body_image = body_image__8
        E.save() 

    for e in e:
        t5= e.find('img')
        aniq_t = t5.get('alt')      
        l5 = e.find('a')
        aniq_l = l5.get('href')
        i5 = e.find('img')
        aniq_img= "https://aniq.uz"+i5['src']

        p9 = SESSION.get(aniq_l)
        strainer9 = SoupStrainer('div', attrs={'class': 'news-item_text'})
        s9 = BeautifulSoup(p9.content, 'html.parser', parse_only=strainer9)
        strainer_9 = SoupStrainer('div', attrs={'class': 'news-item_img'})
        s_9 = BeautifulSoup(p9.content, 'html.parser',parse_only=strainer_9)
        body9 = s9.find("div",class_="news-item_text").text
        try:
                body_image_9 = "https://aniq.uz"+s_9.find('img').get('src')
        except:
                body_image_9 = "no photo"

        E = Economy()
        E.title = aniq_t
        E.image = aniq_img
        E.body = body9
        E.body_image = body_image_9
        E.save()    

    for e in b:
        t3 = e.find("h3")
        gaz_t = t3.a.text        
        l3 = e.find('a')
        gaz_l = 'https://gazeta.uz'+l3.get('href')
        i3 = e.find('img')
        gaz_img = i3['data-src']
        p1 = SESSION.get(f"{gaz_l}",headers=HEADERS)
        strainer5 = SoupStrainer('div', attrs={'class': 'js-mediator-article article-text'})
        s1 = BeautifulSoup(p1.content, 'html.parser',parse_only= strainer5)
        body2 = s1.find("div", class_="js-mediator-article article-text").text  
        strainer_5 = SoupStrainer('div', attrs={'class': 'articleTopBG'})
        s_1 = BeautifulSoup(p1.content, 'html.parser',parse_only= strainer_5)
        try:
            body_image_gazeta = s_1.find("img", class_="lazy articleBigPic").get('data-src')
        except:
            body_image_gazeta = "no photo provided"  

        E = Economy()
        E.title = gaz_t
        E.image = gaz_img
        E.body = body2
        E.body_image = body_image_gazeta
        E.save()       
    return redirect("../economy/") 