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
