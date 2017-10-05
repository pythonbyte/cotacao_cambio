#-*- coding: UTF-8 -*-

#Criado por Eduardo Melgaço


import urllib.request
import json
from time import strftime

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


def melhorcambio_dolar_am(x):

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
	media = (picchioni_cot + confidence_cot + x)/3

	print('Confidence Dolar    R${}  - Picchioni Dolar    R${} - Cotacao.com Dolar    R${} - Green Dolar    R${:.2f}'.format(confidence_cot, picchioni_cot, x, media))
	return media

def melhorcambio_dolar_au(x):

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
	media = (picchioni_cot_au + confidence_cot_au + x)/3
	print('Confidence Dolar AU R${}  - Picchioni Dolar AU R${} - Cotacao.com Dolar AU R${} - Green Dolar AU R${:.2f}'.format(confidence_cot_au, picchioni_cot_au, x, media))
	return media

def melhorcambio_dolar_ca(x):

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
	media = (picchioni_cot_ca + confidence_cot_ca + x)/3
	print('Confidence Dolar CA R${}  - Picchioni Dolar CA R${} - Cotacao.com Dolar CA R${} - Green Dolar CA R${:.2f}'.format(confidence_cot_ca, picchioni_cot_ca, x, media))
	return media


def melhorcambio_euro(x):

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
	media = (picchioni_cot_euro + confidence_cot_euro + x)/3
	print('Confidence Euro     R${}  - Picchioni Euro     R${} - Cotacao.com Euro     R${} - Green Euro     R${:.2f}'.format(confidence_cot_euro, picchioni_cot_euro, x, media))
	return media

def melhorcambio_libra(x):

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
	media = (picchioni_cot_libra + confidence_cot_libra + x)/3
	print('Confidence Libra    R${}  - Picchioni Libra    R${} - Cotacao.com Libra    R${} - Green Libra    R${:.2f}'.format(confidence_cot_libra, picchioni_cot_libra, x, media))
	return media



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

	stb_local_nz = texto.find('ndia</s')
	final_nz = stb_local_nz + 150
	inicio_nz = final_nz - 5
	stb_cot_dolar_nz = float(texto[inicio_nz:final_nz].replace(',', '.'))
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




print('Cotação feita no dia ',strftime("%d %b %Y "))
melhorcambio_dolar_am(pega_cotacao()[0])
melhorcambio_dolar_au(pega_cotacao()[1])
melhorcambio_dolar_ca(pega_cotacao()[2])
melhorcambio_euro(pega_cotacao()[3])
melhorcambio_libra(pega_cotacao()[4])
print('')
print('Cotação do STB')
print('')
print('''
Cotação do Dolar    R$ {}
Cotação do Dolar AU R$ {}
Cotação do Dolar CA R$ {}
Cotação da Dolar NZ R$ {}
Cotação do Euro     R$ {}
Cotação da Libra    R$ {}'''.format(stb()[0], stb()[1], stb()[2],stb()[5], stb()[3], stb()[4]))
print('')
print('Dolar NeoZelandes segundo Cotacao.com.br R$ {}'.format(pega_cotacao()[5]))
fechar = input('Aperte enter para fechar')


