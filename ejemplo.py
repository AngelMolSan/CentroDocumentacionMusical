import os, sys
from xml.dom import minidom

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
        for datafield in record.getElementsByTagName("datafield"):
            tagB = datafield._attrs['tag'].value
            if tagB == '245':
                subfield_a = datafield.getElementsByTagName("subfield")   
                #letra en la posicion a
                subfield_a = datafield.getElementsByTagName("subfield")[0]
                #letra en la posicion b
                if len(datafield.getElementsByTagName("subfield")) == 1:
                    subfield_b = datafield.getElementsByTagName("subfield")[0]
                elif len(datafield.getElementsByTagName("subfield")) == 2:
                    subfield_b = datafield.getElementsByTagName("subfield")[-1]
                else:
                    subfield_b = datafield.getElementsByTagName("subfield")[-2]
                #letra en la posicion c
                subfield_c = datafield.getElementsByTagName("subfield")
                subfield_c = datafield.getElementsByTagName("subfield")[-1]
                #Comprueba que concatena a y b del 245, y si no tiene b que muestre la a
                for subfield_a in datafield.getElementsByTagName("subfield"):
                    letra_subfield_a = subfield_a._attrs['code'].nodeValue
                    letra_subfield_b = subfield_b._attrs['code'].value
                    letra_subfield_c = subfield_c._attrs['code'].value
                    if len(datafield.getElementsByTagName("subfield")) >= 3:
                        if letra_subfield_a == 'a' and letra_subfield_b == 'b':
                            subfield_a=print(f"\t\t<title>{subfield_a.firstChild.data}"+f"{subfield_b.firstChild.data}</title>")
                            break
                        elif letra_subfield_a == 'a' and letra_subfield_c == 'b':
                            subfield_a=print(f"\t\t<title>{subfield_a.firstChild.data}"+f"{subfield_c.firstChild.data}</title>")
                            break
                        elif letra_subfield_b == 'b':
                            subfield_b=print(f"\t\t<title>{subfield_b.firstChild.data}</title>")
                            break
                        elif letra_subfield_c == 'a':
                            subfield_c=print(f"\t\t<title>{subfield_c.firstChild.data}</title>")
                            break
                        elif letra_subfield_a == 'a':
                            subfield_a=print(f"\t\t<title>{subfield_a.firstChild.data}</title>")
                        else:
                            break
                    elif len(datafield.getElementsByTagName("subfield")) == 2:
                        if letra_subfield_a == 'a' and letra_subfield_b == 'b':
                            subfield_a=print(f"\t\t<title>{subfield_a.firstChild.data}"+f"{subfield_b.firstChild.data}</title>")
                            break
                        elif letra_subfield_a == 'a':
                            subfield_a=print(f"\t\t<title>{subfield_a.firstChild.data}</title>")
                            break
                        elif letra_subfield_b == 'b':
                            subfield_b=print(f"\t\t<title>{subfield_b.firstChild.data}</title>")
                            break
                        else:
                            break
                    else:
                        subfield_a=print(f"{subfield_a.firstChild.data}")
                        break
                    
        controlfield = record.getElementsByTagName("controlfield")[0]
        tagA = controlfield.attributes._attrs['tag'].nodeValue
        if tagA == '001':
            controlfield=controlfield.firstChild.data
            ini = 1 #posición inicial
            subcadena = controlfield[ini: -3] 
            print(f"\t\t<link>https://www.juntadeandalucia.es/cultura/idea/opacidea/abnetcl.cgi?TITN={subcadena}</link>")

            for datafield in record.getElementsByTagName("datafield"):
                tagB = datafield._attrs['tag'].value    
                if tagB == '505':
                    subfield_505 = datafield.getElementsByTagName("subfield")
                    #letra en la posicion a
                    subfield_505 = datafield.getElementsByTagName("subfield")[0]
                    #Comprueba que muestre el subfield code="a" del 505
                    for subfield_505 in datafield.getElementsByTagName("subfield"):
                        letra_subfield_505 = subfield_505._attrs['code'].nodeValue
                        #letra_subfield_x = subfield_a._attrs['code'].nodeValue
                        if len(datafield.getElementsByTagName("subfield")) >= 2:
                            if letra_subfield_505 == 'a':
                                subfield_505=subfield_505.firstChild.data
                                for datafield in record.getElementsByTagName("datafield"):
                                    tagC = datafield._attrs['tag'].value
                                    if tagC == '111':
                                        #letra en la posicion a
                                        subfield_a = datafield.getElementsByTagName("subfield")[0]
                                        #letra en la posicion b
                                        subfield_b = datafield.getElementsByTagName("subfield")[-3]
                                        #Comprueba que una vez entra en tag=111 son las letras indicadas 
                                        for subfield_a in datafield.getElementsByTagName("subfield"):
                                            letra_subfield_a = subfield_a._attrs['code'].nodeValue
                                            letra_subfield_b = subfield_b._attrs['code'].value
                                            letra_subfield_c = subfield_c._attrs['code'].value
                                            letra_subfield_d = subfield_d._attrs['code'].value
                                            #letra_subfield_x = subfield_a._attrs['code'].nodeValue
                                            if len(datafield.getElementsByTagName("subfield")) == 4:
                                                if letra_subfield_a == 'a' and letra_subfield_b == 'n' and letra_subfield_c == 'd' and letra_subfield_d == 'c':
                                                    subfield_111=subfield_a.firstChild.data+subfield_b.firstChild.data+subfield_c.firstChild.data+subfield_d.firstChild.data 
                                                    print(f"\t\t<description>{subfield_505}"+f"{subfield_111}</description>")
                                                    break
                                                else:
                                                    subfield_505=print(f"\t\t<description>{subfield_505.firstChild.data}</description>")
                                                    break
                                            else:
                                                break
                                        break
                                if tagC == '111':
                                    break
                                else:
                                    print(f"\t\t<description>{subfield_505}</description>")
                                    break        
                        elif len(datafield.getElementsByTagName("subfield")) == 1:
                            if letra_subfield_505 == 'a':
                                subfield_505=subfield_505.firstChild.data
                                for datafield in record.getElementsByTagName("datafield"):
                                    tagC = datafield._attrs['tag'].value
                                    if tagC == '111':
                                        #letra en la posicion a
                                        subfield_a = datafield.getElementsByTagName("subfield")[0]
                                        #letra en la posicion b
                                        subfield_b = datafield.getElementsByTagName("subfield")[-3]
                                        #letra en la posicion c
                                        subfield_c = datafield.getElementsByTagName("subfield")
                                        subfield_c = datafield.getElementsByTagName("subfield")[-2]
                                        #letra en la posicion d
                                        subfield_d = datafield.getElementsByTagName("subfield")[-1]
                                        #Comprueba que una vez entra en tag=111 son las letras indicadas 
                                        for subfield_a in datafield.getElementsByTagName("subfield"):
                                            letra_subfield_a = subfield_a._attrs['code'].nodeValue
                                            letra_subfield_b = subfield_b._attrs['code'].value
                                            letra_subfield_c = subfield_c._attrs['code'].value
                                            letra_subfield_d = subfield_d._attrs['code'].value
                                            #letra_subfield_x = subfield_a._attrs['code'].nodeValue
                                            if len(datafield.getElementsByTagName("subfield")) == 4:
                                                if letra_subfield_a == 'a' and letra_subfield_b == 'n' and letra_subfield_c == 'd' and letra_subfield_d == 'c':
                                                    subfield_111=subfield_a.firstChild.data+subfield_b.firstChild.data+subfield_c.firstChild.data+subfield_d.firstChild.data 
                                                    print(f"\t\t<description>{subfield_505}"+''f"{subfield_111}</description>")
                                                    break
                                                else:
                                                    subfield_505=print(f"\t\t<description>{subfield_505.firstChild.data}</description>")
                                                    break
                                            else:
                                                break
                                        break
                                if tagC == '111':           
                                    break
                                else:
                                    print(f"\t\t<description>{subfield_505}</description>")
                                    break
                    break
                if tagB == '111':
                    #letra en la posicion a
                    subfield_a = datafield.getElementsByTagName("subfield")[0]
                    #letra en la posicion b
                    subfield_b = datafield.getElementsByTagName("subfield")[-3]
                    #letra en la posicion c
                    subfield_c = datafield.getElementsByTagName("subfield")
                    subfield_c = datafield.getElementsByTagName("subfield")[-2]
                    #letra en la posicion d
                    subfield_d = datafield.getElementsByTagName("subfield")[-1]

                    #Comprueba que una vez entra en tag=111 son las letras indicadas 
                    for subfield_a in datafield.getElementsByTagName("subfield"):
                        letra_subfield_a = subfield_a._attrs['code'].nodeValue
                        letra_subfield_b = subfield_b._attrs['code'].value
                        letra_subfield_c = subfield_c._attrs['code'].value
                        letra_subfield_d = subfield_d._attrs['code'].value
                        #letra_subfield_x = subfield_a._attrs['code'].nodeValue
                        if len(datafield.getElementsByTagName("subfield")) == 4:
                            if letra_subfield_a == 'a' and letra_subfield_b == 'n' and letra_subfield_c == 'd' and letra_subfield_d == 'c':
                                subfield_a=subfield_a.firstChild.data+subfield_b.firstChild.data+subfield_c.firstChild.data+subfield_d.firstChild.data
                                for datafield in record.getElementsByTagName("datafield"):
                                    tagC = datafield._attrs['tag'].value
                                    if tagC == '505':
                                        subfield_505 = datafield.getElementsByTagName("subfield")
                                        #letra en la posicion a
                                        subfield_505 = datafield.getElementsByTagName("subfield")[0]
                                        #Comprueba que muestre el subfield code="a" del 505
                                        for subfield_505 in datafield.getElementsByTagName("subfield"):
                                            letra_subfield_505 = subfield_505._attrs['code'].nodeValue
                                            #letra_subfield_x = subfield_a._attrs['code'].nodeValue
                                            if len(datafield.getElementsByTagName("subfield")) >= 2:
                                                if letra_subfield_505 == 'a':
                                                    subfield_505=subfield_505.firstChild.data
                                                    print(f"\t\t<description>{subfield_505}"+f"{subfield_a}</description>")
                                                    break
                                                break
                                            elif len(datafield.getElementsByTagName("subfield")) == 1:
                                                if letra_subfield_505 == 'a':
                                                    subfield_505=subfield_505.firstChild.data
                                                    print(f"\t\t<description>{subfield_505}"+f"{subfield_a}</description>")
                                                    break
                                                break
                                        break
                                if tagC == '505':           
                                    break
                                else:
                                    print(f"\t\t<description>{subfield_a}</description>")
                                    break
                        else:
                            break
                    break
        print("\t</item>")
    print("</channel>")
    print("</rss>")

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            carga(arg)