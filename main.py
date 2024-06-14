# encoding:utf-8
# -*- coding:utf-8 -*-
from sqlite3 import Cursor
from bs4 import BeautifulSoup
import requests
import mysql.connector
import pymysql.cursors
num=1
moba = pymysql.connect(user='root', password ='1234', host='127.0.0.1', db='prolan',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
bag=moba.cursor()
site = requests.get("https://www.trendyol.com/sr?q=laptop&qt=laptop&st=laptop&mid=108699&os=1&pi=2")
soup = BeautifulSoup(site.content, "lxml")
laptp = soup.find_all("div",attrs={"class":"prdct-cntnr-wrppr"})
print("-------------------------------------")              
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.95"}
for don in laptp:
    don_link = don.find_all("div",attrs={"class":"p-card-wrppr with-campaign-view"})
    for i in don_link:
        ozell = i.find("div",attrs={"class":"card-border"})
        lptp_link=ozell.a.get("href")
       
        site_link = "https://www.trendyol.com"
        lptp_tam = site_link+lptp_link
        print(lptp_tam)

        ozel2 = requests.get(lptp_tam, headers = header)
        ayrim = BeautifulSoup(ozel2.content, "lxml")
        
        ayrinti = ayrim.find_all("div",attrs={"class":"starred-attributes"})
        ayrintim=ayrim.find_all("div",attrs={"class":"product-price-container"})
        for cozum in ayrinti:
            
            for ayrinti3 in ayrintim:
                print("BURDA")
                ozell3= ayrinti3.find_all("div",attrs={"with-org-prc"})
                ayrintilar = cozum.find_all("li")
                for i in ayrintilar:
                    
                    for j in ozell3:
                        
                        try:            
                            
                            ism = i.find("span",attrs={"class":"attribute-label"}).text
                            ozel = i.find("span",attrs={"class":"attribute-value"}).text
                            fiyat= j.find("span",attrs={"class":"prc-dsc"}).text
                            tabl=bag.execute('INSERT INTO tablo VALUES(%s,%s,%s,%s,%s)',(num,ozel,ism,fiyat,lptp_tam))
                            moba.commit()  
                            
                            print(ism," = ",ozel,fiyat)
                            num=num+1
                     
                        except:
                            print("---------")

k=0
for i in range(24):
    print("\n")
    i=k
    for j in range(6):
        
        bag.execute('SELECT * FROM tablo WHERE num=%s',i+1)
        tablo=bag.fetchall()
        print(tablo)
        i=i+1
        k=i

moba = pymysql.connect(user='root', password ='1234', host='127.0.0.1', db='prolan',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
bag=moba.cursor()
site = requests.get("https://www.amazon.com.tr/gp/bestsellers/computers/12601898031/ref=zg_bs_nav_computers_1")
soup = BeautifulSoup(site.content, "lxml")
laptp = soup.find_all("div",attrs={"class":"_cDEzb_grid-column_2hIsc"})
print("-------------------------------------")
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.95"}
for don in laptp:
    don_link = don.find_all("div",attrs={"class":"zg-grid-general-faceout"})
    for i in don_link:
        ozell = i.find("div",attrs={"class":"p13n-sc-uncoverable-faceout"})
        lptp_link=ozell.a.get("href")
        
        site_link = "https://www.amazon.com.tr"
        lptp_tam = site_link+lptp_link
        print(lptp_tam)

        ozel2 = requests.get(lptp_tam, headers = header)
        ayrim = BeautifulSoup(ozel2.content, "lxml")
        
        ayrinti = ayrim.find_all("div",attrs={"class":"a-spacing-top-small"})
        ayrintim=ayrim.find_all("div",attrs={"class":"celwidget"})
        for cozum in ayrinti:
            for ayrinti3 in ayrintim:
                ayrintilar = cozum.find_all("tr")
                ozell3=ayrinti3.find_all("div",attrs={"class":"aok-align-center"})
                for i in ayrintilar:
                    for j2 in ozell3:
                        try:               
                            ism = i.find("td",attrs={"class":"a-span3"}).text
                            ozel = i.find("td",attrs={"class":"a-span9"}).text
                            fiyat=j2.find("span",attrs={"class":"a-offscreen"}).text
                            tabl=bag.execute('INSERT INTO tablo VALUES(%s,%s,%s,%s,%s)',(num,ozel,ism,fiyat,lptp_tam))
                            moba.commit()
                            num=num+1
                            print(ism," = ",ozel)

                        except:
                            print("---------")

moba.close()