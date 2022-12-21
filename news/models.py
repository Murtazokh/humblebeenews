from django.db import models

class News(models.Model):
  #KUN.UZ 
  kun_uz_t = models.CharField(max_length=200)
  kun_uz_img = models.URLField(null=True, blank=True)
  kun_uz_l = models.TextField() 
  #Uzreport 
  uzre_t = models.CharField(max_length=200)
  uzre_img = models.URLField(null=True, blank=True)
  uzre_l = models.TextField()
  #Gazeta.uz 
  gaz_t = models.CharField(max_length=200)
  gaz_img = models.URLField(null=True, blank=True)
  gaz_l = models.TextField()  
  #UZDAILY.UZ 
  daily_t = models.CharField(max_length=200)
  daily_img = models.URLField(null=True, blank=True)
  daily_l = models.TextField()
  #QALAMPIR.UZ
  qal_t = models.CharField(max_length=200)
  qal_img = models.URLField(null=True, blank=True)
  qal_l = models.TextField() 
  def __str__(self):
    return self.title

class Sport(models.Model):
  #DARYO.UZ 
  dar_t = models.CharField(max_length=200)
  dar_img = models.URLField(null=True, blank=True)
  dar_l = models.TextField()
  #SPORT.UZ 
  sport_t = models.CharField(max_length=200)
  sport_img = models.URLField(null=True, blank=True)
  sport_l = models.TextField()
  #NUZ.UZ
  nuz_t = models.CharField(max_length=200)
  nuz_img = models.URLField(null=True, blank=True)
  nuz_l = models.TextField()  
  #ONSIDE.UZ 
  side_t1 = models.CharField(max_length=200)
  side_img1 = models.URLField(null=True, blank=True)
  side_l1 = models.TextField()
  #SPUTNIKNEWS-UZ.COM 
  sputnik_t = models.CharField(max_length=200)
  sputnik_img = models.URLField(null=True, blank=True)
  sputnik_l = models.TextField() 

  def __str__(self):
    return self.title

class Politics(models.Model): 
  #ANIQ.UZ 
  aniq_t = models.CharField(max_length=200)
  aniq_img = models.URLField(null=True, blank=True)
  aniq_l = models.TextField() 
  #ANTIMON.GOV.UZ 
  antimon_t = models.CharField(max_length=200)
  antimon_img = models.URLField(null=True, blank=True)
  antimon_l = models.TextField() 
  #UZ24.UZ 
  uz24_t = models.CharField(max_length=200)
  uz24_img = models.URLField(null=True, blank=True)
  uz24_l = models.TextField()
  #BBC UZBEK
  bbc_t = models.CharField(max_length=200)
  bbc_img = models.URLField(null=True, blank=True)
  bbc_l = models.TextField() 
  #PREZIDENT.UZ
  pr_t = models.CharField(max_length=200)
  pr_img = models.URLField(null=True, blank=True)
  pr_l = models.TextField()    
   
  def __str__(self):
    return self.title  

class Economy(models.Model):
  #SAMARKANDNEWS.UZ 
  samnews_t = models.CharField(max_length=200)
  samnews_img = models.URLField(null=True, blank=True)
  samnews_l = models.TextField()
  #ZAMIN.UZ 
  zamin_t = models.CharField(max_length=200)
  zamin_img = models.URLField(null=True, blank=True)
  zamin_l = models.TextField()
  #Bugun.UZ 
  bugun_t = models.CharField(max_length=200)
  bugun_img = models.URLField(null=True, blank=True)
  bugun_l = models.TextField()
  #UZA.UZ 
  uza_t = models.CharField(max_length=200)
  uza_img = models.URLField(null=True, blank=True)
  uza_l = models.TextField()
  #ANIQ.UZ 
  aniq_t = models.CharField(max_length=200)
  aniq_img = models.URLField(null=True, blank=True)
  aniq_l = models.TextField() 