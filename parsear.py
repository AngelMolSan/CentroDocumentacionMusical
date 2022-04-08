import os, sys
from xml.dom import minidom
#import xml.etree.ElementTree as ET
#tree = ET.parse('Alpujarra.xml')
#root = tree.getroot()
#ruta= "/home/cdma/Escritorio/script/"
ruta= "D:/Angelms/Escritorio/Informatica/ASIR/script/"
xml = minidom.parse(ruta+"Alpujarra.xml")
records = xml.getElementsByTagName("record")
for record in records:
    controlfield = record.getElementsByTagName("controlfield")[0]
    controlfield=controlfield.firstChild.data

    ini = 1 #posiciÃ³n inicial
    subcadena = controlfield[ini: -3] 
    print(f"{subcadena}")
        
    for datafield in record.getElementsByTagName("datafield"):
        tag = datafield._attrs['tag'].value
        if tag == '245':
            subfield = datafield.getElementsByTagName("subfield")   
                #letra en la posicion a
            subfield_a = datafield.getElementsByTagName("subfield")[0]
                #letra en la posicion b
            if len(datafield.getElementsByTagName("subfield")) == 1:
                subfield_b = datafield.getElementsByTagName("subfield")[0]
            else:
                subfield_b = datafield.getElementsByTagName("subfield")[-2]
            #Comprueba que concatena a y b del 245, y si no tiene b que muestre la a
            for subfield in datafield.getElementsByTagName("subfield"):
                letra_subfield_a = subfield_a._attrs['code'].nodeValue
                letra_subfield_b = subfield_b._attrs['code'].value
                if len(datafield.getElementsByTagName("subfield")) >= 3:
                    if letra_subfield_a == 'a' and letra_subfield_b == 'b':
                        subfield=print(f"{subfield_a.firstChild.data}"+f"{subfield_b.firstChild.data}")
                        break
                    elif letra_subfield_b != 'b':
                        subfield=print(f"{subfield_a.firstChild.data}")
                        break
                elif len(datafield.getElementsByTagName("subfield")) == 2:
                    if letra_subfield_a == 'a' and letra_subfield_b == 'b':
                        subfield=print(f"{subfield_a.firstChild.data}"+f"{subfield_b.firstChild.data}")
                        break
                    elif letra_subfield_a != 'a' and letra_subfield_b != 'b':
                        break
                    else:
                        subfield=print(f"{subfield_a.firstChild.data}")
                        break
                else:
                    subfield=print(f"{subfield_a.firstChild.data}")

                    #subfield=print(f"{subfield.firstChild.data}")
                    # if letra_subfield == 'a' or letra_subfield == 'b':
                    #     subfield=print(f"{subfield.firstChild.data}"+f"{subfield_b.firstChild.data}")

            #controlfield=print(f"{controlfield.firstChild.data}")
                #datafield=datafield._attrs['tag'].value
                #print(datafield)
#def valorA(subfield_a):
#    subfield=print(f"{subfield_a.firstChild.data}")
#def valorB(subfield_b):
#    subfield=print(f"{subfield_b.firstChild.data}")