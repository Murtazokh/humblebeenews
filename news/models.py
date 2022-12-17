from django.db import models

# Create your models here.

class News(models.Model):
  #KUN.UZ 1
  kun_uz_t = models.CharField(max_length=200)
  kun_uz_img = models.URLField(null=True, blank=True)
  kun_uz_l = models.TextField()
  
  #football Uzreport 2
  uzre_t = models.CharField(max_length=200)
  uzre_img = models.URLField(null=True, blank=True)
  uzre_l = models.TextField()
  
  #bbc technology 3
  bbc_t = models.CharField(max_length=200)
  bbc_img = models.URLField(null=True, blank=True)
  bbc_l = models.TextField()
  
  #Gazeta.uz 4
  gaz_t = models.CharField(max_length=200)
  gaz_img = models.URLField(null=True, blank=True)
  gaz_l = models.TextField()
  
  #UZDAILY.UZ 5
  daily_t = models.CharField(max_length=200)
  daily_img = models.URLField(null=True, blank=True)
  daily_l = models.TextField()
  
  #QALAMPIR.UZ 6
  qal_t = models.CharField(max_length=200)
  qal_img = models.URLField(null=True, blank=True)
  qal_l = models.TextField()
  #DARYO.UZ 7
  dar_t = models.CharField(max_length=200)
  dar_img = models.URLField(null=True, blank=True)
  dar_l = models.TextField()
  #ANIQ.UZ 8
  aniq_t = models.CharField(max_length=200)
  aniq_img = models.URLField(null=True, blank=True)
  aniq_l = models.TextField()
  
  #ONSIDE.UZ 9
  side_t = models.CharField(max_length=200)
  side_img = models.URLField(null=True, blank=True)
  side_l = models.TextField()
  
  #SPORT.UZ 10
  sport_t = models.CharField(max_length=200)
  sport_img = models.URLField(null=True, blank=True)
  sport_l = models.TextField()
  
  #UZ24.UZ 11
  uz24_t = models.CharField(max_length=200)
  uz24_img = models.URLField(null=True, blank=True)
  uz24_l = models.TextField()
  
  #NUZ.UZ 12
  nuz_t = models.CharField(max_length=200)
  nuz_img = models.URLField(null=True, blank=True)
  nuz_l = models.TextField()
  
  #KR.UZ 13
  kr_t = models.CharField(max_length=200)
  kr_img = models.URLField(null=True, blank=True)
  kr_l = models.TextField()
  
  #SPUTNIKNEWS-UZ.COM 14
  sputnik_t = models.CharField(max_length=200)
  sputnik_img = models.URLField(null=True, blank=True)
  sputnik_l = models.TextField()
  
  #SAMARKANDNEWS.UZ 15
  samnews_t = models.CharField(max_length=200)
  samnews_img = models.URLField(null=True, blank=True)
  samnews_l = models.TextField()
  
  #UZA.UZ 16
  uza_t = models.CharField(max_length=200)
  uza_img = models.URLField(null=True, blank=True)
  uza_l = models.TextField()  
  
  #ZAMIN.UZ 17
  zamin_t = models.CharField(max_length=200)
  zamin_img = models.URLField(null=True, blank=True)
  zamin_l = models.TextField()
  
  #MATBUOT.UZ 18
  matbuot_t = models.CharField(max_length=200)
  matbuot_img = models.URLField(null=True, blank=True)
  matbuot_l = models.TextField()
  
  #Bugun.UZ 19
  bugun_t = models.CharField(max_length=200)
  bugun_img = models.URLField(null=True, blank=True)
  bugun_l = models.TextField()
  
  #ANTIMON.GOV.UZ 20
  antimon_t = models.CharField(max_length=200)
  antimon_img = models.URLField(null=True, blank=True)
  antimon_l = models.TextField()   
  
  def __str__(self):
    return self.title