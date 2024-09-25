import bpy

def parent_to_bone(obj_name, armature_name, bone_name):
    # Get the object to be parented
    obj = bpy.data.objects.get(obj_name)
    if obj is None:
        print(f"Object '{obj_name}' not found.")
        return

    # Get the armature
    armature = bpy.data.objects.get(armature_name)
    if armature is None:
        print(f"Armature '{armature_name}' not found.")
        return

    # Check if the armature has the bone
    if bone_name not in armature.data.bones:
        print(f"Bone '{bone_name}' not found in armature '{armature_name}'.")
        return

    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Select the object to parent
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    a = obj.matrix_world

    # Enter object mode
    bpy.ops.object.mode_set(mode='OBJECT')


    # Set the parent to the armature with bone
    bpy.ops.object.parent_set(type='BONE', keep_transform=True)
    
    # Assign the bone to the parent bone attribute
    obj.parent = armature
    obj.parent_bone = bone_name
    obj.parent_type = 'BONE'
    obj.matrix_world = a
    
    print(f"'{obj_name}' successfully parented to bone '{bone_name}' in armature '{armature_name}'.")


# Example usage
object_name = "Cube"  # Replace with your instance object name


armature_name = "Armature"      # Replace with your armature object name
bone_name = "Bone.001"              # Replace with your bone name

parent_to_bone(object_name, armature_name, bone_name)
#bpy.ops.object.parent_set(type='BONE_RELATIVE')