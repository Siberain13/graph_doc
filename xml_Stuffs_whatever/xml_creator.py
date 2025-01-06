import os  
from xml.dom import minidom 

def append_child(root_a,root_b):
    root_a.appendChild(root_b)
    return 1

def set_attr(root_b,name,value):
    root_b.setAttribute(f'{name}', f'{value}')
    return 1

root = minidom.Document() 
  
xml = root.createElement('exchange')  
root.appendChild(xml) 
  
root1 = root.createElement('viewfolder')
set_attr(root1,'name','Front side of building GL.1A')
set_attr(root1,'guid','')
#root1.setAttribute('name', 'Front side of building GL.1A');
#root1.setAttribute('guid', '');
append_child(xml,root1)

root2 = root.createElement('viewfolder')
set_attr(root2,'name','Underground Water feature + inlet')
set_attr(root2,'guid','')
append_child(root1,root2)
append_child(xml,root1)

root3 = root.createElement('product2')
text = root.createTextNode("DDT")
append_child(root3,text)
append_child(root2,root3)
append_child(root1,root2)
append_child(xml,root1)

#productChild2 = root.createElement('product2')
#xml.appendChild(productChild2) 
  
# =============================================================================
# 
# #- minidom_Build_XML.py
# #- Copyright (c) 2018 HerongYang.com. All Rights Reserved.
# 
# #- Create new XML document with its root element
# doc = minidom.parseString("<dictionary/>")
# root = doc.documentElement
# 
# #- Create new element
# word = doc.createElement("word")
# 
# #- Add new element to root
# root.appendChild(word)
# 
# #- Create new element with an attribute
# first = doc.createElement("update")
# first.setAttribute("date", "2100-01-01")
# 
# #- Add new element to "word"
# word.appendChild(first)
# 
# #- Add second element to "word"
# second = doc.createElement("name")
# second.setAttribute("is_acronym","true");
# text = doc.createTextNode("DTD")
# second.appendChild(text)
# word.appendChild(second)
# 
# #- Add third element to "word"
# third = doc.createElement("definition")
# third.appendChild(doc.createTextNode("Document Type Definition"))
# word.appendChild(third)
# 
# #- Print out the document as pretty XML
# print(doc.toprettyxml())
# =============================================================================
  
xml_str = root.toprettyxml(indent ="\t")
print(xml_str)  
  
save_path_file = "C:\\Users\\d.suniwat\\Documents\\gfg.xml"
  
#with open(save_path_file, "w") as f: 
#    f.write(xml_str)  
