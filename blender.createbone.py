import bpy
import csv
#import pathlib

file_Path = 'C:\\Users\\Loki\\Desktop\\test.csv'

bpy.ops.object.mode_set(mode='EDIT', toggle=False)

with open(file_Path,mode='r',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        # !!!add enum to remove head row!!!
        print(row)

        obArm = bpy.context.active_object #get the armature object
        ebs = obArm.data.edit_bones
        eb = ebs.new(row[0])
        eb.head = (int(row[1]), int(row[2]), int(row[3])) # if the head and tail are the same, the bone is deleted
        eb.tail = (int(row[4]), int(row[5]), int(row[6]))    # upon returning to object mode
