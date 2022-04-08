#!/usr/bin/env python
def sumar(n,*args):
    resultado =n
    for i in args:
        resultado+=i
    return resultado

def tag111(n,*args):
    records = xml.getElementsByTagName("record")
    for record in records:
        print("\t<item>")
        for datafield in record.getElementsByTagName("datafield"):
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