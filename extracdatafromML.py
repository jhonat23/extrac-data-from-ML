# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl, sys
import pandas as pd
from datetime import datetime
#from openpyxl import load_workbook

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#creating list and variables
lst=list()
lstt=list()
t=datetime.today().strftime('%Y-%m-%d')

while True:
    print('working...')

    #reading thr url
    #url = input('Enter - ')
    #if len(url)<1:
    url='https://tendencias.mercadolibre.com.co/1000-electronica__audio_y_video'
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    #print(soup)
    tags=soup('a')

    #Extracting all url in main url
    for tag in tags:
        print(tag.get('href', None))
        x=tag.get('href', None)
        lst.append(str(x))
    #print(lst)

    #shorting the list
    for link in lst:
        if ('listado.mercadolibre'in link
        or 'electronica.mercadolibre' in link
        or 'vehiculos.mercadolibre' in link
        or 'computacion.mercadolibre' in link
        or 'celulares.mercadolibre' in link
        or 'carros.mercadolibre' in link):
            #print(link)
            f=link.rfind('/')
            lstt.append(link[f+1:])
            #lstt.append(link)

    for linka in lstt:
        #print(type(link1))
        linka.replace("-","")
        #print(linka)
    #VALIDAR POR QUE ESTE PEDAZO DE CÓDIGO NO FUNCIONA!!!

    #print(lstt)
    #check if all item are included (40)
    print('length of list:')
    print(len(lstt))

    #preparing data to get in Excel
    #print(type(lstt))
    data=pd.DataFrame(lstt,columns=[t])
    #data
    print('date of list:')
    print(t)
    #data.to_excel('resultados8nov2021.xlsx')

    # reading de seed file and creating final list
    datai=pd.read_excel('Informe_ted_ML.xlsx')
    #datai
    dataf=pd.concat([data,datai], axis=1)
    dataf.to_excel('Informe_ted_ML.xlsx')
    #dataf
    break
print('Done')
