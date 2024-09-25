import bpy

obj = bpy.data.objects['Cube']
armature = bpy.data.objects['Armature']
parent_bone = 'Bone.001'  # choose the bone name which you want to be the parent

bpy.ops.object.select_all(action='DESELECT')

armature.select_set(True)
bpy.context.view_layer.objects.active = armature

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