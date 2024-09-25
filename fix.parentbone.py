import bpy
import csv
#import pathlib

file_Path = 'C:\\Users\\d.suniwat\\Desktop\\link.csv'

bpy.ops.object.mode_set(mode='EDIT', toggle=False)

name_list =[]

with open(file_Path,mode='r',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        name_list.append(str(row[0]))

#print(name_list)

for name in name_list:
    
    bpy.ops.object.mode_set(mode='OBJECT')  
      
    obj = bpy.data.objects[name]
    armature = bpy.data.objects['Armature']
    parent_bone = name  # choose the bone name which you want to be the parent

    bpy.ops.object.select_all(action='DESELECT')

    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature
    
    print(name)

    bpy.ops.object.mode_set(mode='EDIT')
    armature.data.edit_bones.active = armature.data.edit_bones[parent_bone]

    bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.select_all(action='DESELECT')  # deselect all objects
    obj.select_set(True)
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature
    # the active object will be the parent of all selected object

    bpy.ops.object.parent_set(type='BONE_RELATIVE', keep_transform=True)


SOURCE::https://blender.stackexchange.com/questions/77465/python-how-to-parent-an-object-to-a-bone-without-transformation?newreg=58384217f5ed47e18e6987bbe79e7cb6
