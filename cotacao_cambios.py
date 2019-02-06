#-*- coding: UTF-8 -*-

#Criado por Eduardo Melgaço
#https://github.com/pythonbyte/
import requests
import urllib.request
from tkinter import Tk, Label, Button, Entry
from functools import lru_cache

green_media_dolar = 0
green_media_dolar_au = 0
green_media_dolar_ca = 0
green_media_dolar_nz = 0
green_media_euro = 0
green_media_libra = 0

# confidence
# https://23hu4n4gq0.execute-api.sa-east-1.amazonaws.com/production/api/v1/cotacoes?idProduto=57&idCidade=4854
# auth ecommerce.confidence|ECommerce|null|2760|MCwCFHR9v54Zh3NSStFTH6qZQNcjRZbwAhRBcNjWyU7ufGJw62q/uN8acQL+vg==
picchioni_ids = {
    "dolar": '"id":2,"simbolo":"USD","descricao":"Dólar (USD)"',
    "euro": '"id":4,"simbolo":"EUR","descricao":"Euro (EUR)"',
    "libra": '"id":6,"simbolo":"GBP","descricao":"Libra Esterlina (GBP)"',
    "dolar_cad": '"id":9,"simbolo":"CAD","descricao":"Dólar Canadense (CAD)"',
    "dolar_au": '"id":10,"simbolo":"AUD","descricao":"Dólar Australiano (AUD)"'
}

confidence_ids = {
    "dolar": 29,
    "euro": 35,
    "libra": 57,
    "dolar_cad": 43,
    "dolar_au": 45
}




@lru_cache(maxsize=None)
def get_picchioni_cotation():
    picchioni_response = requests.get('https://www.picchioni.com.br')
    picchioni_text = picchioni_response.text
    cotation_data = []

    for k,v in picchioni_ids.items():

        if k == 'dolar':
            end_line = int(picchioni_text.find(v)) + 152
            begin_line = end_line - 9
            cotation_data.append(float(picchioni_text[begin_line:end_line]))

        elif k == 'euro':
            end_line = int(picchioni_text.find(v)) + 151
            begin_line = end_line - 9
            cotation_data.append(float(picchioni_text[begin_line:end_line]))

        elif k == 'libra':
            end_line = int(picchioni_text.find(v)) + 162
            begin_line = end_line - 9
            cotation_data.append(float(picchioni_text[begin_line:end_line]))

        elif k == 'dolar_cad':
            end_line = int(picchioni_text.find(v)) + 162
            begin_line = end_line - 9
            cotation_data.append(float(picchioni_text[begin_line:end_line]))

        elif k == 'dolar_au':
            end_line = int(picchioni_text.find(v)) + 165
            begin_line = end_line - 9
            cotation_data.append(float(picchioni_text[begin_line:end_line]))

    return cotation_data

@lru_cache(maxsize=None)
def get_confidence():
    url = 'https://23hu4n4gq0.execute-api.sa-east-1.amazonaws.com/production/api/v1/cotacoes?idProduto={}&idCidade=4854'
    cotation_data =  []

    for k,v in confidence_ids.items():
        response = requests.get(url.format(v), headers={'auth': 'ecommerce.confidence|ECommerce|null|2760|MCwCFHR9v54Zh3NSStFTH6qZQNcjRZbwAhRBcNjWyU7ufGJw62q/uN8acQL+vg=='})
        cotation_data.append(response.json()['cotacao'])
    return cotation_data

@lru_cache(maxsize=None)
def stb():
    url = 'https://www.stb.com.br/servicos/conversor-de-moedas'
    pagina = urllib.request.urlopen(url)
    texto = pagina.read().decode('utf-8')

    stb_local_am = texto.find('Americano</s')
    final = stb_local_am + 155
    inicio = final - 5
    stb_cot_dolar = float(texto[inicio:final].replace(',', '.'))


    stb_local_au = texto.find('Australiano</s')
    final_au = stb_local_au + 157
    inicio_au = final_au - 5
    stb_cot_dolar_au = float(texto[inicio_au:final_au].replace(',', '.'))


    stb_local_ca = texto.find('Canadense</s')
    final_ca = stb_local_ca + 155
    inicio_ca = final_ca - 5
    stb_cot_dolar_ca = float(texto[inicio_ca:final_ca].replace(',', '.'))


    stb_local_euro = texto.find('Euro</s')
    final_euro = stb_local_euro + 150
    inicio_euro = final_euro - 5
    stb_cot_euro = float(texto[inicio_euro:final_euro].replace(',', '.'))


    stb_local_libra = texto.find('Esterlina</s')
    final_libra = stb_local_libra + 155
    inicio_libra = final_libra - 5
    stb_cot_libra = float(texto[inicio_libra:final_libra].replace(',', '.'))

    stb_lista = [stb_cot_dolar, stb_cot_euro, stb_cot_libra, stb_cot_dolar_ca, stb_cot_dolar_au]
    return stb_lista

print('Programa abrindo... Aguarde...')
picchioni_data = get_picchioni_cotation()
confidence_data = get_confidence()
stb_data = stb()

green_data = []
green_stb = []

for x in range(5):
    green_value = (picchioni_data[x]+confidence_data[x])/2
    comparison_value = green_value - stb_data[x]
    green_stb.append(comparison_value)
    green_data.append(green_value)


labels = ['Picchioni', 'Confidence', 'Green', 'STB', 'Green - STB']
money_labels = ['Dolar AM', 'Euro', 'Libra', 'Dolar Cad', 'Dolar AU', ]

root = Tk()

root.title(' C O T A T O R  -  1.0')

for i in range(5):
    Label(text=labels[i], width=15).grid(row=0,column=i+1)
    Label(text='R$ {:.3f}'.format(picchioni_data[i]), width=15).grid(row=i+1,column=1)
    Label(text='R$ {:.3f}'.format(confidence_data[i]), width=15).grid(row=i+1,column=2)
    Label(text='R$ {:.3f}'.format(green_data[i]), width=15).grid(row=i+1,column=3)
    Label(text='R$ {:.3f}'.format(stb_data[i]), width=15).grid(row=i+1,column=4)
    Label(text='R$ {:.3f}'.format(green_stb[i]), width=15).grid(row=i+1,column=5)
    for j in range(5):
        Label(text=money_labels[j], width=15).grid(row=j+1,column=0)


print('Programa Aberto')

root.mainloop()
print('Programa Fechado !')

