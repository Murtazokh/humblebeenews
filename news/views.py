import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.shortcuts import render, redirect
from news.models import News, Sport, Politics, Economy

HEADERS = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}

def get_kun(request):
    """This function scrapes 5 websites and give the information to class"""
    #DELETING OLD NEWS FROM DATABASE:
    News.objects.all().delete()

    #URL AND MAIN TAGS OF KUN.UZ:
    page = requests.get("https://kun.uz/news/category/uzbekiston")
    soup = BeautifulSoup(page.content, 'html.parser')
    a = soup.find_all('div', class_='col-md-4 mb-25 l-item')[:4]
    
    #URL AND MAIN TAGS OF UZREPORT.NEWS :   
    page2 = requests.get("https://www.uzreport.news")
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    b = soup2.find_all('div', class_='col-xs-12 col-sm-12 col-md-3 item')
    
    #URL AND MAIN TAGS OF QALAMPIR.UZ :    
    page3 = requests.get("https://qalampir.uz/", headers=HEADERS)
    soup3 = BeautifulSoup(page3.content, 'html.parser')
    dd = soup3.find_all('a', class_='ss_item item flex_row')
    
    #URL AND MAIN TAGS OF GAZETA.UZ :
    page4 = requests.get("https://www.gazeta.uz/uz/", headers=HEADERS)
    soup4 = BeautifulSoup(page4.content, 'html.parser')
    d = soup4.find_all('div', class_='nblock')
    
    #URL AND MAIN TAGS OF UZDAILY.UZ :
    page5 = requests.get("https://www.uzdaily.uz/uz/section/1", headers=HEADERS)
    soup5 = BeautifulSoup(page5.content, 'html.parser')
    e = soup5.find_all('div', class_='dis_flex box_shadow margin_block')

    for x,q,e,r,y in zip(a,b,d,e,dd):
        #kun.uz
        t = x.find('a', {"class":"news__title"})
        kun_uz_t = t.text        
        l = x.find('a', {"class":"news__img"})
        kun_uz_l = 'https://kun.uz'+l.get('href')
        i = x.find('img')
        kun_uz_img = i['src']
        
        #uzreport.news
        t1 = q.find('p')
        uzre_t = t1.text.strip()        
        l1 = q.select_one('a')
        uzre_l = l1.get('href')
        i1 = q.find('img')
        uzre_img = i1['src']
        
        #qalampir.uz
        t2 = y.find('div', class_="title")
        qal_t = t2.text        
        # l2 = y.find('a')
        qal_l = "https://qalampir.uz"+y.get('href')
        i2 = y.find('img')
        qal_img = i2['src']

        #gazeta.uz
        t3 = e.find("h3")
        gaz_t = t3.a.text        
        l3 = e.find('a')
        gaz_l = 'https://gazeta.uz'+l3.get('href')
        i3 = e.find('img')
        gaz_img = i3['data-src']

        #uzdaily.uz
        t4 = r.find("h3", class_="title mt-1 text_wrap")
        daily_t = t4.text        
        l4 = r.find('a', class_="read_more")
        daily_l = l4.get('href')
        i4 = r.find('img')
        daily_img = "http://uzdaily.uz"+i4['src']
        
        #SAVING THE SCRAPED INFO TO CLASS
        n = News()        
        
        n.kun_uz_l = kun_uz_l
        n.kun_uz_img = kun_uz_img 
        n.kun_uz_t = kun_uz_t 

        n.uzre_l = uzre_l
        n.uzre_t = uzre_t 
        n.uzre_img = uzre_img  

        n.qal_l = qal_l
        n.qal_t = qal_t 
        n.qal_img = qal_img 
        
        n.gaz_l = gaz_l  
        n.gaz_t = gaz_t 
        n.gaz_img = gaz_img     

        n.daily_t = daily_t  
        n.daily_l = daily_l 
        n.daily_img = daily_img 
        n.save()
  
    return redirect("../")

def get_sport(request):
    """This function scrapes 5 websites and give the information to class"""
    #DELETING OLD NEWS FROM DATABASE:
    Sport.objects.all().delete()

    #URL AND MAIN TAG OF daryo.uz:
    page6 = requests.get("https://daryo.uz/category/sport", headers=HEADERS)
    soup6 = BeautifulSoup(page6.content, 'html.parser')
    a = soup6.find_all('div', class_='mini__article')[:4]
    #URL AND MAIN TAG OF ONSIDE.UZ:
    page7 = requests.get("http://onside.uz/home", headers=HEADERS)
    soup7 = BeautifulSoup(page7.content, 'html.parser')
    b = soup7.find_all('div', class_='col-sm-6')[:4]
    #URL AND MAIN TAGS OF SPORTS.UZ:
    page8 = requests.get("https://sports.uz/", headers=HEADERS)
    soup8 = BeautifulSoup(page8.content, 'html.parser')
    d = soup8.find_all('div', class_='news-body')[:4]
    dd = soup8.find_all('div', class_='img-block')[:4]
    #URL AND MAIN TAGS OF NUZ.UZ:
    page9 = requests.get("https://nuz.uz/uz/category/sport", headers=HEADERS)
    soup9 = BeautifulSoup(page9.content, 'html.parser')
    c = soup9.find_all('div', class_='tdb_module_loop td_module_wrap td-animation-stack')
    #URL AND MAIN TAGS OF sputniknews-uz.com:
    page10 = requests.get("https://sputniknews-uz.com/sport/", headers=HEADERS)
    soup10 = BeautifulSoup(page10.content, 'html.parser')
    e = soup10.find_all('div', class_='list__item')


    for q,w,r,e,t,f in zip(a,b,d,dd,c,e):
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
        # ONSIDE.UZ
        t2 = w.find('h2', class_='title')
        side_t = t2.text.strip()        
        l2 = w.find('a')
        side_l = 'http://onside.uz'+l2.get('href')
        i2 = w.find('img')
        side_img=("http://onside.uz"+i2['src'])
        # SPORTS.UZ     
        t3 = r.find('h3')
        sport_t = t3.text.strip()        
        l3 = r.find('a')
        sport_l = 'https://sport.uz'+l3.get('href')
        i3 = e.find('img')
        sport_img=i3['data-src'] 
        # NUZ.UZ
        t4 = t.find('h3', class_="entry-title td-module-title")
        nuz_t = t4.text.strip()        
        l4 = t.find('a')
        nuz_l = l4.get('href')
        i4 = t.find('span')
        nuz_img=i4['data-img-url']  
        # sputniknews-uz.com
        t5= f.find('a', class_="list__title")
        sputnik_t = t5.text.strip()        
        l5 = f.find('a', class_="list__title")
        sputnik_l = "https://sputniknews-uz.com"+l5.get('href')
        i5 = f.find('img')
        sputnik_img= i5['src']     
        
        #SAVING THE SCRAPED INFO TO CLASS
        S = Sport()        
        
        S.dar_t = dar_t
        S.dar_l = dar_l 
        S.dar_img = dar_img  

        S.side_t1 = side_t
        S.side_l1 = side_l 
        S.side_img1 = side_img

        S.sport_t = sport_t
        S.sport_l = sport_l 
        S.sport_img = sport_img

        S.nuz_l = nuz_l
        S.nuz_t = nuz_t
        S.nuz_img = nuz_img

        S.sputnik_t = sputnik_t
        S.sputnik_img = sputnik_img
        S.sputnik_l = sputnik_l
        S.save()
  
    return redirect("../sport/")              

def get_siyosat(request):
    """This function scrapes 5 websites and give the information to class"""
    #DELETING OLD NEWS FROM DATABASE:
    Politics.objects.all().delete()

    #URL AND MAIN TAG OF daryo.UZ:
    page1 = requests.get("https://aniq.uz/siyosat", headers=HEADERS)
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    a = soup1.find_all('div', class_='news-list_item article')[:4]

    page2 = requests.get("https://antimon.gov.uz/prezident-matbuot-xizmati-yangiliklari/", headers=HEADERS)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    b = soup2.find_all('article')

    page3 = requests.get("https://uz24.uz/uz/categories/politics", headers=HEADERS)
    soup3 = BeautifulSoup(page3.content, 'html.parser')
    c = soup3.find_all('article', class_='article-row tablet-flex block')

    page4 = requests.get("https://www.bbc.com/uzbek/topics/cwr9j9dz4gpt", headers=HEADERS)
    soup4 = BeautifulSoup(page4.content, 'html.parser')
    d = soup4.find_all('li', class_='bbc-v8cf3q')

    page5 = requests.get("https://president.uz/uz", headers=HEADERS)
    soup5 = BeautifulSoup(page5.content, 'html.parser')
    e = soup5.find_all('div', class_='col-md-4 col-sm-4 events_box')
    for a,b,c,d,e in zip(a,b,c,d,e):
        t1 = a.find('h2')
        aniq_t = t1.text.strip()        
        l1 = a.find('a')
        aniq_l = l1.get('href')
        i1 = a.find('img')
        aniq_img="http://aniq.uz"+i1['src'] 
        
        t2 = b.find('h3', class_="entry-title")
        antimon_t = t2.text.strip()        
        l2 = b.find('a')
        antimon_l = l2.get('href')
        i2 = b.find('img')
        antimon_img=i2['data-src']
        
        t3 = c.find('h3')
        uz24_t = t3.text.strip()        
        l3 = c.find('a')
        uz24_l = "https://uz24.uz"+l3.get('href')
        i3 = c.find('img')
        uz24_img=i3['src']

        t4 = d.find('h2', class_="bbc-hz8bw2 e47bds20")
        bbc_t = t4.text.strip()        
        l4 = d.find('a', class_="bbc-uk8dsi e1d658bg0")
        bbc_l = l4.get('href')
        i4 = d.find('img')
        bbc_img=i4['src'] 

        t5 = e.find('a', class_="events_title")
        pr_t = t5.text.strip()        
        l5 = e.find('a', class_="events_title")
        pr_l = "https://president.uz"+l5.get('href')
        i5 = e.find('img')
        pr_img= "https://president.uz"+i5['src']       
        #SAVING THE SCRAPED INFO TO CLASS
        P = Politics()        
        
        P.aniq_t = aniq_t
        P.aniq_l = aniq_l 
        P.aniq_img = aniq_img  

        P.antimon_l = antimon_l
        P.antimon_t = antimon_t 
        P.antimon_img = antimon_img

        P.uz24_img = uz24_img
        P.uz24_l = uz24_l 
        P.uz24_t = uz24_t

        P.bbc_img = bbc_img
        P.bbc_t = bbc_t 
        P.bbc_l = bbc_l

        P.pr_img = pr_img
        P.pr_t = pr_t 
        P.pr_l = pr_l
        P.save()
  
    return redirect("../politics/")

def get_economy(request):
    """This function scrapes 5 websites and give the information to class"""
    #DELETING OLD NEWS FROM DATABASE:
    Economy.objects.all().delete()

    page1 = requests.get(r"http://samarkandnews.uz/post/category/%D0%98%D2%9B%D1%82%D0%B8%D1%81%D0%BE%D0%B4%D0%B8%D1%91%D1%82", headers=HEADERS)
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    a = soup1.find_all('div', class_='col-12 col-md-6')[:4]

    page2 = requests.get("https://zamin.uz/uz/iqtisodiyot/", headers=HEADERS)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    b = soup2.find_all('div', class_='short-item')

    page3 = requests.get("https://kommers.uz/", headers=HEADERS)
    soup3 = BeautifulSoup(page3.content, 'html.parser')
    d = soup3.find_all('div', class_='post')

    page4 = requests.get("https://kun.uz/news/category/iktisodiet", headers=HEADERS)
    soup4 = BeautifulSoup(page4.content, 'html.parser')
    c = soup4.find_all('div', class_='col-md-4 mb-25 l-item')

    page5 = requests.get("https://aniq.uz/uz/iktisod", headers=HEADERS)
    soup5 = BeautifulSoup(page5.content, 'html.parser')
    e = soup5.find_all('div', class_='news-item_img')
    
    for a,b,d,c,e in zip(a,b,d,c,e):
        t1= a.find('h2', class_="post-title title-large")
        samnews_t = t1.text.strip()        
        l1 = a.find('a')
        samnews_l = "http://samarkandnews.uz"+l1.get('href')
        i1 = a.find('img', class_="img-fluid")
        samnews_img= "http://samarkandnews.uz"+i1['src']

        t2= b.find('div', class_="short-text")
        zamin_t = t2.text.strip()        
        l2 = b.find('a', class_="short-title title")
        zamin_l = "http:"+l2.get('href')
        i2 = b.find('img')
        zamin_img= "http://zamin.uz"+i2['src']

        t3= d.find('img')
        bugun_t = t3.get('alt')        
        l3 = d.find('a', class_="post__photo")
        bugun_l = l3.get('href')
        i3 = d.find('img')
        bugun_img= i3['src']

        t4= c.find('a', class_='news__title')
        uza_t = t4.text.strip()        
        l4 = c.find('a', class_="news__title")
        uza_l = "https://kun.uz"+l4.get('href')
        i4 = c.find('img')
        uza_img= i4['src']

        t5= e.find('img')
        aniq_t = t5.get('alt')      
        l5 = e.find('a')
        aniq_l = l5.get('href')
        i5 = e.find('img')
        aniq_img= "https://aniq.uz"+i5['src']



        #SAVING THE SCRAPED INFO TO CLASS
        E = Economy()

        E.samnews_img = samnews_img
        E.samnews_l = samnews_l
        E.samnews_t = samnews_t

        E.zamin_img = zamin_img
        E.zamin_l = zamin_l
        E.zamin_t = zamin_t

        E.bugun_l = bugun_l
        E.bugun_t = bugun_t
        E.bugun_img = bugun_img

        E.uza_l = uza_l
        E.uza_t = uza_t
        E.uza_img = uza_img

        E.aniq_t = aniq_t
        E.aniq_l = aniq_l
        E.aniq_img = aniq_img
        E.save()
    return redirect("../jahon/")

def index(req):
    """This function renders scraped information to html file"""
    n = News.objects.all()[::-1]
    context = {
       "object_list":n
    }
    return render(req, 'news/index.html', context )

def sport(req):
    """This function renders scraped information to html file that about sport"""
    sport = Sport.objects.all()[::-1]
    context = {
       "object_list":sport
    }
    return render(req, 'news/sport.html', context )

def siyosat(req):
    """This function renders scraped information to html file that about politics"""
    n = Politics.objects.all()[::-1]
    context = {
       "object_list":n
    }
    return render(req, 'news/siyosat.html', context )

def jahon(req):
    """This function renders scraped information to html file that about economics"""
    objects = Economy.objects.all()[::-1]
    context = {
       "object_list":objects
    }
    return render(req, 'news/jahon.html', context )    
