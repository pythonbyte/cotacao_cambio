#-*- coding: UTF-8 -*-

#Criado por Eduardo Melgaço
#https://github.com/pythonbyte/

import urllib.request
from tkinter import Tk, Label, Button
from functools import lru_cache

green_media_dolar = 0
green_media_dolar_au = 0
green_media_dolar_ca = 0
green_media_dolar_nz = 0
green_media_euro = 0
green_media_libra = 0








@lru_cache(maxsize=None)
def pega_cotacao():
	pagina = urllib.request.urlopen('https://www.cotacao.com.br/cotacao-das-moedas.html')
	texto = pagina.read().decode('utf-8')
	
	dolar_am_cot = float(texto[19822:19827].replace(',', '.'))

	dolar_au_cot = float(texto[20194:20199].replace(',', '.'))

	dolar_ca_cot = float(texto[20321:20326].replace(',', '.'))
	
	dolar_nz_cot = float(texto[20925:20930].replace(',', '.'))

	euro_cot = float(texto[19938:19943].replace(',', '.'))
	
	libra_cot = float(texto[20065:20070].replace(',', '.'))
	

	moedas_cot = [dolar_am_cot, dolar_au_cot, dolar_ca_cot, euro_cot, libra_cot, dolar_nz_cot]
	return moedas_cot

@lru_cache(maxsize=None)
def melhorcambio_dolar_am(x):
	global green_media_dolar
	url = 'https://www.melhorcambio.com/cotacao/compra/dolar-turismo/belo-horizonte'
	pagina = urllib.request.urlopen(url)
	texto = pagina.read().decode('utf-8')

	confidence_local = texto.find('e"><b>Confidence Câmbio')
	final = confidence_local + 601
	inicio = final - 4
	confidence_cot = float(texto[inicio:final].replace(',', '.'))

	picchioni_local = texto.find('e"><b>Picchioni')
	final2 = picchioni_local + 593
	inicio2 = final2 - 4
	picchioni_cot = float(texto[inicio2:final2].replace(',', '.'))
	green_media_dolar  = (picchioni_cot + confidence_cot + x)/3
	return ('R${:.2f}     -     R${:.2f}     -     R${:.2f}     -     R${:.2f}'.format(confidence_cot, picchioni_cot, x, green_media_dolar))

	
@lru_cache(maxsize=None)
def melhorcambio_dolar_au(x):
	global green_media_dolar_au
	url = 'https://www.melhorcambio.com/cotacao/compra/dolar-australiano/belo-horizonte'
	pagina = urllib.request.urlopen(url)
	texto = pagina.read().decode('utf-8')

	confidence_local = texto.find('e"><b>Confidence Câmbio')
	final = confidence_local + 601
	inicio = final - 4
	confidence_cot_au = float(texto[inicio:final].replace(',', '.'))

	picchioni_local = texto.find('e"><b>Picchioni')
	final2 = picchioni_local + 593
	inicio2 = final2 - 4
	picchioni_cot_au = float(texto[inicio2:final2].replace(',', '.'))
	green_media_dolar_au = (picchioni_cot_au + confidence_cot_au + x)/3
	return 'R${:.2f}     -     R${:.2f}     -     R${:.2f}     -     R${:.2f}'.format(confidence_cot_au, picchioni_cot_au, x, green_media_dolar_au)
	
@lru_cache(maxsize=None)
def melhorcambio_dolar_ca(x):
	global green_media_dolar_ca
	url = 'https://www.melhorcambio.com/cotacao/compra/dolar-canadense/belo-horizonte'
	pagina = urllib.request.urlopen(url)
	texto = pagina.read().decode('utf-8')

	confidence_local = texto.find('e"><b>Confidence Câmbio')
	final = confidence_local + 601
	inicio = final - 4
	confidence_cot_ca = float(texto[inicio:final].replace(',', '.'))

	picchioni_local = texto.find('e"><b>Picchioni')
	final2 = picchioni_local + 593
	inicio2 = final2 - 4
	picchioni_cot_ca = float(texto[inicio2:final2].replace(',', '.'))
	green_media_dolar_ca = (picchioni_cot_ca + confidence_cot_ca + x)/3
	return 'R${:.2f}     -     R${:.2f}     -     R${:.2f}     -     R${:.2f}'.format(confidence_cot_ca, picchioni_cot_ca, x, green_media_dolar_ca)
	

@lru_cache(maxsize=None)
def melhorcambio_euro(x):
	global green_media_euro
	url = 'https://www.melhorcambio.com/cotacao/compra/euro/belo-horizonte'
	pagina = urllib.request.urlopen(url)
	texto = pagina.read().decode('utf-8')

	confidence_local = texto.find('e"><b>Confidence Câmbio')
	final = confidence_local + 601
	inicio = final - 4
	confidence_cot_euro = float(texto[inicio:final].replace(',', '.'))

	picchioni_local = texto.find('e"><b>Picchioni')
	final2 = picchioni_local + 593
	inicio2 = final2 - 4
	picchioni_cot_euro = float(texto[inicio2:final2].replace(',', '.'))
	green_media_euro = (picchioni_cot_euro + confidence_cot_euro + x)/3
	return 'R${:.2f}     -     R${:.2f}     -     R${:.2f}     -     R${:.2f}'.format(confidence_cot_euro, picchioni_cot_euro, x, green_media_euro)
	
@lru_cache(maxsize=None)
def melhorcambio_libra(x):
	global green_media_libra
	url = 'https://www.melhorcambio.com/cotacao/compra/libra/belo-horizonte'
	pagina = urllib.request.urlopen(url)
	texto = pagina.read().decode('utf-8')

	confidence_local = texto.find('e"><b>Confidence Câmbio')
	final = confidence_local + 601
	inicio = final - 4
	confidence_cot_libra = float(texto[inicio:final].replace(',', '.'))

	picchioni_local = texto.find('e"><b>Picchioni')
	final2 = picchioni_local + 593
	inicio2 = final2 - 4
	picchioni_cot_libra = float(texto[inicio2:final2].replace(',', '.'))
	green_media_libra = (picchioni_cot_libra + confidence_cot_libra + x)/3
	return 'R${:.2f}     -     R${:.2f}     -     R${:.2f}     -     R${:.2f}'.format(confidence_cot_libra, picchioni_cot_libra, x, green_media_libra)
	


@lru_cache(maxsize=None)
def stb():
	url = 'https://www.stb.com.br/servicos/conversor-de-moedas'
	pagina = urllib.request.urlopen(url)
	texto = pagina.read().decode('utf-8')

	stb_local_am = texto.find('Americano</s')
	final = stb_local_am + 155
	inicio = final - 5
	stb_cot_dolar = float(texto[inicio:final].replace(',', '.'))
	#print(stb_cot_dolar)

	stb_local_au = texto.find('Australiano</s')
	final_au = stb_local_au + 157
	inicio_au = final_au - 5
	stb_cot_dolar_au = float(texto[inicio_au:final_au].replace(',', '.'))
	#print(stb_cot_dolar_au)

	stb_local_ca = texto.find('Canadense</s')
	final_ca = stb_local_ca + 155
	inicio_ca = final_ca - 5
	stb_cot_dolar_ca = float(texto[inicio_ca:final_ca].replace(',', '.'))
	#print(stb_cot_dolar_ca)

	stb_local_nz = texto.find('Zelandia</s')
	final_nz = stb_local_nz + 150
	inicio_nz = final_nz - 5
	stb_cot_dolar_nz = texto[inicio_nz:final_nz]
	#print(stb_cot_dolar_nz)

	stb_local_euro = texto.find('Euro</s')
	final_euro = stb_local_euro + 150
	inicio_euro = final_euro - 5
	stb_cot_euro = float(texto[inicio_euro:final_euro].replace(',', '.'))
	#print(stb_cot_euro)

	stb_local_libra = texto.find('Esterlina</s')
	final_libra = stb_local_libra + 155
	inicio_libra = final_libra - 5
	stb_cot_libra = float(texto[inicio_libra:final_libra].replace(',', '.'))
	#print(stb_cot_libra)
	stb_lista = [stb_cot_dolar, stb_cot_dolar_au, stb_cot_dolar_ca, stb_cot_euro, stb_cot_libra, stb_cot_dolar_nz]
	return stb_lista

print('Programa abrindo... Aguarde...')

g = '''
{}   -   R${:.2f}\n
{}   -   R${:.2f}\n
{}   -   R${:.2f}\n
{}   -   R${:.2f}\n
{}   -   R${:.2f}\n'''.format(melhorcambio_dolar_am(pega_cotacao()[0]), stb()[0], melhorcambio_dolar_au(pega_cotacao()[1]), stb()[1], melhorcambio_dolar_ca(pega_cotacao()[2]), stb()[2], melhorcambio_euro(pega_cotacao()[3]), stb()[3], melhorcambio_libra(pega_cotacao()[4]), stb()[4])

f = '''
   -   R${:.2f}\n
   -   R${:.2f}\n
   -   R${:.2f}\n
   -   R${:.2f}\n
   -   R${:.2f}\n'''.format((green_media_dolar-stb()[0]),(green_media_dolar_au-stb()[1]),(green_media_dolar_ca-stb()[2]),(green_media_euro -stb()[3]),(green_media_libra-stb()[4]))


@lru_cache(maxsize=None)
class MyFirstGUI:
    def __init__(self, master):
    	self.master = master
    	master.title(' C O T A T O R - 0.3')
    	master.geometry('490x200')
    	
    	self.label = Label(master, text = 'Confidence    Picchioni     Cotação.com    Green       STB      Green-STB')
    	self.label.pack()
    	self.label = Label(master, text = 'Dólar AM \n\nDólar AU \n\nDólar CA \n\nEuro \n\nLibra')
    	self.label.pack(side = 'left')
    	self.label = Label(master, text=g)
    	self.label.pack(side = 'left')

    	self.label = Label(master, text=f)
    	self.label.pack(side = 'left')


    	self.close_button = Button(master, text="Close", command= self.master.quit)
    	self.close_button.pack(side = 'right')



root = Tk()
my_gui = MyFirstGUI(root)
print('Programa Aberto')

root.mainloop()
print('Programa Fechado !')
