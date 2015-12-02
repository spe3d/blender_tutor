import bpy
from math import pi

FRAME_START = 0
FRAME_END = 30

# Clear current animation.
bpy.ops.pose.select_all(action = "SELECT")
bpy.context.active_object.animation_data_clear()

# Setup scene.
scene = bpy.context.scene
scene.frame_current = FRAME_START
scene.frame_start = FRAME_START
scene.frame_end = FRAME_END

# Make sure the current mode is in pose mode.
bpy.data.objects["Armature"].select = True
while not bpy.context.mode == "POSE":
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.posemode_toggle()

bpy.ops.pose.loc_clear()
bpy.ops.pose.rot_clear()

bpy.ops.pose.select_all(action = "DESELECT")
armature = bpy.data.armatures["Armature"]
bones = armature.bones

def move1():
    bpy.ops.pose.select_all(action = "DESELECT")
    bone_leg_c_L = bones["Leg_C.L"]
    bone_leg_c_L.select = True
    bpy.ops.transform.translate(value = (0, 0, 1.8))
    
    bone_stomatch = bones["Stomatch"]
    bone_stomatch.select = True
    bpy.ops.transform.rotate(value = pi/6, axis = (0, 1, 0))
    

def move1_inv():
    bpy.ops.pose.select_all(action = "DESELECT")
    bone_leg_c_L = bones["Leg_C.L"]
    bone_leg_c_L.select = True
    bpy.ops.transform.translate(value = (0, 0, -1.8))
    
    bone_stomatch = bones["Stomatch"]
    bone_stomatch.select = True
    bpy.ops.transform.rotate(value = -pi/6, axis = (0, 1, 0))
    

def move2():
    bpy.ops.pose.select_all(action = "DESELECT")
    bone_leg_c_L = bones["Leg_C.R"]
    bone_leg_c_L.select = True
    bpy.ops.transform.translate(value = (0, 0, 1.8))
    
    bone_stomatch = bones["Stomatch"]
    bone_stomatch.select = True
    bpy.ops.transform.rotate(value = pi/6, axis = (0, 1, 0))
    
 
def move2_inv():
    bpy.ops.pose.select_all(action = "DESELECT")
    bone_leg_c_L = bones["Leg_C.R"]
    bone_leg_c_L.select = True
    bpy.ops.transform.translate(value = (0, 0, -1.8))
    
    bone_stomatch = bones["Stomatch"]
    bone_stomatch.select = True
    bpy.ops.transform.rotate(value = -pi/6, axis = (0, 1, 0))

## Start animation
after_move1 = False
after_move2 = False

def animate():
    for ind in range(4):
        frame_ind = ind * 10
        scene.frame_set(frame = frame_ind)
        if ind % 2 == 1:
            move1()
        else:
            move1_inv()
        bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
