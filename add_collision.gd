#v1

@tool
extends EditorScript

#func _run() :
	#print("Hello World")
	#pass
	
	
func _run() :
	var children : Array = get_editor_interface().get_selection().get_selected_nodes()[0].get_children()
	print(children)
	for child in children:
		var body : RigidBody3D = RigidBody3D.new()
		var childObject : MeshInstance3D = child
		var parent : Node = childObject.get_parent()
		
		body.transform = childObject.transform
		
		parent.remove_child((childObject))
		parent.add_child(body)
		body.set_owner(parent.get_tree().get_edited_scene_root())
		body.add_child(childObject)
		
		childObject.position = Vector3.ZERO
		childObject.rotation = Vector3.ZERO
		
		childObject.set_owner(body.get_tree().get_edited_scene_root())
		
		childObject.create_convex_collision()
		var collider = childObject.get_child(0).get_child(0)
		childObject.get_child(0).remove_child(collider)
		body.add_child(collider)
		collider.set_owner(body.get_tree().get_edited_scene_root())
		childObject.get_child(0).queue_free()
		
		body.add_to_group("Test",true)
		
	pass

#v2

@tool
extends EditorScript

#func _run() :
	#print("Hello World")
	#pass
	
	
func _run() :
	var children : Array = get_editor_interface().get_selection().get_selected_nodes()[0].get_children()
	print(children)
	for child in children:
		var childObject : MeshInstance3D = child
		#var childObject_dup : MeshInstance3D = child.duplicate(true)
		var childObject_dup : MeshInstance3D = childObject.duplicate(true)
		var parent : Node = childObject.get_parent()
		var body : RigidBody3D = RigidBody3D.new()
		
		body.transform = childObject.transform
		
		parent.remove_child((childObject))
		parent.add_child(body)
		body.set_owner(parent.get_tree().get_edited_scene_root())
		body.add_child(childObject_dup)
		
		childObject_dup.position = Vector3.ZERO
		childObject_dup.rotation = Vector3.ZERO
		
		childObject_dup.set_owner(body.get_tree().get_edited_scene_root())
		
		childObject_dup.create_convex_collision()
		var collider = childObject_dup.get_child(0).get_child(0)
		childObject_dup.get_child(0).remove_child(collider)
		body.add_child(collider)
		collider.set_owner(body.get_tree().get_edited_scene_root())
		childObject_dup.get_child(0).queue_free()
		
		body.add_to_group("Test",true)
		
	pass

