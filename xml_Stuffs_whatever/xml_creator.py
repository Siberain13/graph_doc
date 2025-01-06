import os  
from xml.dom import minidom 

  
root = minidom.Document() 
  
# =============================================================================
# xml = root.createElement('exchange')  
# root.appendChild(xml) 
#   
# productChild = root.createElement('product') 
# productChild.setAttribute('name', 'Geeks for Geeks');
# xml.appendChild(productChild)    
# =============================================================================

#productChild2 = root.createElement('product2')
#xml.appendChild(productChild2) 
  


#- minidom_Build_XML.py
#- Copyright (c) 2018 HerongYang.com. All Rights Reserved.

#- Create new XML document with its root element
doc = minidom.parseString("<dictionary/>")
root = doc.documentElement

#- Create new element
word = doc.createElement("word")

#- Add new element to root
root.appendChild(word)

#- Create new element with an attribute
first = doc.createElement("update")
first.setAttribute("date", "2100-01-01")

#- Add new element to "word"
word.appendChild(first)

#- Add second element to "word"
second = doc.createElement("name")
second.setAttribute("is_acronym","true");
text = doc.createTextNode("DTD")
second.appendChild(text)
word.appendChild(second)

#- Add third element to "word"
third = doc.createElement("definition")
third.appendChild(doc.createTextNode("Document Type Definition"))
word.appendChild(third)

#- Print out the document as pretty XML
print(doc.toprettyxml())
  
# =============================================================================
# xml_str = root.toprettyxml(indent ="\t")
# print(xml_str)  
# =============================================================================
  
save_path_file = "C:\\Users\\d.suniwat\\Documents\\gfg.xml"
  
#with open(save_path_file, "w") as f: 
#    f.write(xml_str)  
