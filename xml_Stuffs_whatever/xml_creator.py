from xml.dom import minidom
import xml.etree.ElementTree as ET
#from xml.etree.ElementTree import Element, SubElement, Comment, tostring

#%% functions
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def create_variable(name, value):
    globals()[name] = value
    
def create_folder(var,main_folder,name):
    #globals()[var] =  ET.SubElement(main_folder, 'viewfolder')
    var =  ET.SubElement(main_folder, 'viewfolder')
    var.set('name', name)
    var.set('guid', '')

def create_set(fold,item,el_para,para_loc):
    selset = ET.SubElement(fold, 'selectionset')
    selset.set('name', item[0])
    selset.set('guid', '')
    
    findspec = ET.SubElement(selset, 'findspec')
    findspec.set('mode', 'all')
    findspec.set('disjoint', '0')
    
    conds = ET.SubElement(findspec, 'conditions')
    
    cond_a = ET.SubElement(conds, 'condition')
    cond_a.set('test', 'equals')
    cond_a.set('flags', '10')
    
    cat = ET.SubElement(cond_a, 'category')
    
    name_int = ET.SubElement(cat, 'name')
    name_int.set('internal', para_loc)
    name_int.text = el_para
    
    porp = ET.SubElement(cond_a, 'property')
    
    name_int = ET.SubElement(porp, 'name')
    name_int.set('internal', 'lcldrevit_parameter_sequence_Location_PG_TEXT')
    name_int.text = 'sequence_Location'
    
    val = ET.SubElement(cond_a, 'value')
    
    name_int = ET.SubElement(val, 'data')
    name_int.set('type', 'wstring')
    name_int.text = item[1]
    #name_int.text = 'VH-FS'
    
    cond_b = ET.SubElement(conds, 'condition')
    cond_b.set('test', 'equals')
    cond_b.set('flags', '10')
    
    cat = ET.SubElement(cond_b, 'category')
    
    name_int = ET.SubElement(cat, 'name')
    name_int.set('internal', para_loc)
    name_int.text = el_para
    
    porp = ET.SubElement(cond_b, 'property')
    
    name_int = ET.SubElement(porp, 'name')
    name_int.set('internal', 'lcldrevit_parameter_sequence_Work_PG_TEXT')
    name_int.text = 'sequence_Work'
    
    val = ET.SubElement(cond_b, 'value')
    
    name_int = ET.SubElement(val, 'data')
    name_int.set('type', 'wstring')
    name_int.text = item[2]
    #name_int.text = 'UW'
    
    cond_c = ET.SubElement(conds, 'condition')
    cond_c.set('test', 'equals')
    cond_c.set('flags', '10')
    
    cat = ET.SubElement(cond_c, 'category')
    
    name_int = ET.SubElement(cat, 'name')
    name_int.set('internal', para_loc)
    name_int.text = el_para
    
    porp = ET.SubElement(cond_c, 'property')
    
    name_int = ET.SubElement(porp, 'name')
    name_int.set('internal', 'lcldrevit_parameter_sequence_WorkPart_PG_TEXT')
    name_int.text = 'sequence_WorkPart'
    
    val = ET.SubElement(cond_c, 'value')
    
    name_int = ET.SubElement(val, 'data')
    name_int.set('type', 'wstring')
    name_int.text = item[3]

#%% parameter

address_a = 'http://www.w3.org/2001/XMLSchema-instance'
address_b = 'http://download.autodesk.com/us/navisworks/schemas/nw-exchange-12.0.xsd'

el_para = 'Custom'
para_loc = 'LcRevitData_Custom'

#
search_list = [['VH-FS-UW-1','FS','UW','1'],
     ['VH-FS-UW-2','FS','UW','2'],
     ['VH-FS-UW-3','FS','UW','3']]
#

#%% main

head = ET.Element('exchange')
head.set('xmlns:xsi', address_a)
head.set('xsi:noNamespaceSchemaLocation', address_b)
head.set('units', 'ft')
head.set('filename', '')
head.set('filepath', '')

#comment = ET.Comment('Generated for PyMOTW')
#top.append(comment)

selsets = ET.SubElement(head, 'selectionsets')

fld_a = create_variable('fld_a', [])
fld_b = create_variable('fld_b', [])

fld_a = create_folder(fld_a,selsets,'Front side of building GL.1A')
fld_b = create_folder(fld_b,fld_a,'Underground Water feature + inlet')

# =============================================================================
# fld_a = ET.SubElement(selsets, 'viewfolder')
# fld_a .set('name', 'Front side of building GL.1A')
# fld_a .set('guid', '')
# 
# fld_b = ET.SubElement(fld_a, 'viewfolder')
# fld_b.set('name', 'Underground Water feature + inlet')
# fld_b.set('guid', '')
# =============================================================================
# =============================================================================
# 
# for item in search_list:
#     create_set(fld_b,item,el_para,para_loc)
# =============================================================================

print (prettify(head))
