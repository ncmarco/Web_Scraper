from bs4 import BeautifulSoup
import requests
import csv
user_input_1=input("Va rugam sa introduceti rulajul maxim: ")  
user_input_2=input("Va rugam sa introduceti anul minim de fabricatie: ")
user_input_3=input("Va rugam sa introduceti pretul maxim: ")
with open("data.txt", 'w') as f:
    text_html=requests.get('https://www.autovit.ro/autoturisme/audi').text
    soup=BeautifulSoup(text_html,'lxml')
    anunturi=soup.find_all('section', class_="ooa-10gfd0w e1oqyyyi1")
    for anunt in anunturi:
        titlu=anunt.find('h1',class_="e1oqyyyi9 ooa-1ed90th er34gjf0").text
        pret=anunt.find('h3', class_="e1oqyyyi16 ooa-1n2paoq er34gjf0").text
        valuta=anunt.find('p',class_="e1oqyyyi17 ooa-8vn6i7 er34gjf0").text
        an_fabricatie=anunt.find("dd", attrs={"data-parameter":"year"}).text
        kilometraj=anunt.find("dd", attrs={"data-parameter":"mileage"}).text
        if kilometraj<=user_input_1 and an_fabricatie>=user_input_2 and pret<=user_input_3:
            f.write(f'Masina: {titlu} \n')
            f.write(f'Pret: {pret} \n')
            f.write(f'An Fabricatie: {an_fabricatie} \n')
            f.write(f'Kilometraj: {kilometraj} \n')
            f.write('\n')