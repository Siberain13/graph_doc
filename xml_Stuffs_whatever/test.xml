import os  
from xml.dom import minidom 

def create_element(root_a,root_b):
    root_a.appendChild(root_b)
    return 1

def append_child(root_a,root_b):
    root_a.appendChild(root_b)
    return 1

def set_attr(root_b,name,value):
    root_b.setAttribute(f'{name}', f'{value}')
    return 1

def create_variable(name, value):
    globals()[name] = value
 
#import minidom
root = minidom.Document() 

#static var
text_a = 'http://www.w3.org/2001/XMLSchema-instance'
text_b = 'http://download.autodesk.com/us/navisworks/schemas/nw-exchange-12.0.xsd'

#xml header
xml = root.createElement('exchange')
set_attr(xml,'xmlns:xsi',text_a)
set_attr(xml,'xsi:noNamespaceSchemaLocation',text_b)
set_attr(xml,'units','ft')
set_attr(xml,'filenam','')
set_attr(xml,'filepath','')
append_child(root,xml)
  
#create folder
root1 = root.createElement('viewfolder')
set_attr(root1,'name','1 FL. Finishing work')
set_attr(root1,'guid','')
append_child(xml,root1)

#create folder
root2 = root.createElement('viewfolder')
set_attr(root2,'name','Underground Water feature + inlet')
set_attr(root2,'guid','')
append_child(root1,root2)


#create search set
a = [['root4','selectionset','name','VH-FS-UW-1','guid',''],
     ['root5','category','Custom','test',"equals"],
     ['root6','findspec','mode','all','disjoint','0'],
     ['root7','name','internal','LcRevitData_Custom','Custom'],
     ['root7','name']]

b = [[] for i in a]

for j, item in enumerate(b):
    item.append(create_variable(a[j][0],[]))

#print(b)

for k, var in enumerate(b):
    var[0] = root.createElement(a[k][1])
    b = len(a[k])
        
    if 'text' in a[k][0]:    
        if b > 3 and b < 5 :
            set_attr(var[0],a[k][2],a[k][3])
        elif b > 5 and b < 7:
            set_attr(var[0],a[k][2],a[k][3])
            set_attr(var[0],a[k][4],a[k][5])
        else:
            1            
        text = root.createTextNode(a[k][b - 1])
        append_child(var[0],text)
    else:
        if b > 3 and b < 5 :
            set_attr(var[0],a[k][2],a[k][3])
        elif b > 5 and b < 7:
            set_attr(var[0],a[k][2],a[k][3])
            set_attr(var[0],a[k][4],a[k][5])
        else:
            1
    append_child(root2,var[0])
    append_child(root1,root2)
    append_child(xml,root1)
        

xml_str = root.toprettyxml(indent ="\t")
print(xml_str)  
  
#save_path_file = "C:\\Users\\d.suniwat\\Documents\\gfg.xml"

  
#with open(save_path_file, "w") as f: 
#    f.write(xml_str)  
