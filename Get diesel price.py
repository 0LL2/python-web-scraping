from lxml import etree                                                                  #Käyttää lxml kirjastoa
from urllib.request import urlopen                                                      #Ja url avaamiseen urllib kirjastoa

url = 'https://www.tankille.fi/suomi/'                                                  #Aseta url
response = urlopen(url)                                                                 #Avaa url
htmlparser = etree.HTMLParser()                                                         #Aseta html parseri
tree = etree.parse(response, htmlparser)                                                #Parsee
hinta = tree.xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div/div[3]/h6')     #Diesel elementti
#hinta = tree.xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div/div[2]/h6')    #98 elementti
#hinta = tree.xpath('/html/body/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/h6')    #95 elementti
valmis = hinta[0].text                                                                  #Talleta elementin ensimmäinen "arvo" valmis muuttujaan
final = valmis.replace('Keskiarvo','').strip()                                          #Siisti lopputulosta
print(final)