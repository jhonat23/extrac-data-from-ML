import urllib.request, urllib.parse, urllib.error
import BeautifulSoup
import ssl, sys
import pandas as pd
from datetime import datetime

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
    url='https://tendencias.mercadolibre.com.co/1000-electronica__audio_y_video'#check the specific link to your country
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags=soup('a')

    #Extracting all url in main url
    for tag in tags:
        print(tag.get('href', None))
        x=tag.get('href', None)
        lst.append(str(x))

    #Shorting the list
    for link in lst:
        if ('listado.mercadolibre'in link
        or 'electronica.mercadolibre' in link
        or 'vehiculos.mercadolibre' in link
        or 'computacion.mercadolibre' in link
        or 'celulares.mercadolibre' in link
        or 'carros.mercadolibre' in link):
            f=link.rfind('/')
            lstt.append(link[f+1:])

    for linka in lstt:
        linka.replace("-","")

    #check if all item are included (min 40)
    print('length of list:')
    print(len(lstt))

    #preparing data to get in Excel
    data=pd.DataFrame(lstt,columns=[t])
    print('date of list:')
    print(t)

    # reading de seed file and creating final list
    datai=pd.read_excel('Informe_ted_ML.xlsx') #save in same folder of scrip
    dataf=pd.concat([data,datai], axis=1)
    dataf.to_excel('Informe_ted_ML.xlsx')
    #dataf
    break
print('Done')
