#!/usr/bin/env python
import os, sys
from xml.dom import minidom

def analiza_datafield(datafield, lista_codes):
        '''
        En esta función analizamos todas los datafield que hay dentro de cada record.
        '''
        datafields = datafield.getElementsByTagName("subfield")
        i = -1
        texto = ''
        for subfield in datafields:
            letra_subfield = subfield._attrs['code'].nodeValue
            if letra_subfield in lista_codes:
                i += 1
                subfield = datafield.getElementsByTagName("subfield")[i]
                texto += subfield.firstChild.data
        return texto

def carga(fichero):
    xml = minidom.parse(fichero)
    versionA= 'version="1.0"'
    versionA= 'version="1.0"'
    versionB= '<rss version="2.0">'
    encoding= 'encoding="UTF-8"'
    print(f'{"<?xml "}',versionA,encoding,' ?>')
    print(versionB)
    print("<channel>")
    print("\t<title>Festival de Música Tradicional de La Alpujarra</title>")
    print("\t<link>https://www.centrodedocumentacionmusicaldeandalucia.es/-/fondo-festival-de-musica-tradicional-de-la-alpujarra</link>")
    print("\t<description>El Festival de Música Tradicional de la Alpujarra, representa la principal manifestación cultural y musical del folclore alpujarreño. Es portador y conservador de la memoria cultura, folclórica e histórica de la comarca. Se celebra con carácter anual desde 1982, el segundo domingo  de agosto, en alguna localidad de las Alpujarra granadina o almeriense, que varía para cada ocasión. Tiene carácter de concurso, otorgándose varios premios según especialidades.</description>")
    
    records = xml.getElementsByTagName("record")
    for record in records:
        #Lo primero generamos por defecto la cabecera para el rss
        print("\t<item>")
        '''
        Si es datafield tag='245' que nos muestre el code a y b
        Si es datafield tag='505' que nos muestre el a y/o si hay tag='111' que muestre el code a,n,d y c
        '''
        descripcion = ''
        for datafield in record.getElementsByTagName("datafield"):
            tag = datafield._attrs['tag'].value
            if tag == '245':
                titulo = analiza_datafield(datafield, ['a','b'])
            if tag == '505':
                descripcion += analiza_datafield(datafield, ['a'])
            if tag == '111':
                descripcion += analiza_datafield(datafield, ['a','n','d','c'])

        controlfield = record.getElementsByTagName("controlfield")[0]
        tagA = controlfield.attributes._attrs['tag'].nodeValue
        if tagA == '001':
            controlfield=controlfield.firstChild.data
            ini = 1 #posición inicial
            subcadena = controlfield[ini: -3]
            print(f"\t\t<title>{titulo}</title>")
            print(f"\t\t<link>https://www.juntadeandalucia.es/cultura/idea/opacidea/abnetcl.cgi?TITN={subcadena}</link>")
            print(f"\t\t<description>{descripcion}</description>")
        
        print("\t</item>")


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            carga(arg)