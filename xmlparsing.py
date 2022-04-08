import xml.dom.minidom

document = xml.dom.minidom.parse("libreria.xml")

mapping = {}

for nodeBook in document.getElementsByTagName("book"):
    isbn = nodeBook.getAttribute("isbn")
    titles = nodeBook.getElementsByTagName("title")
    for nodeTitle in titles:
        nodeText = nodeTitle.firstChild
        title = nodeText.data
        mapping[isbn] = title

    print(mapping)