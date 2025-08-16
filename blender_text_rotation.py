import bpy
import bmesh
from mathutils import Vector
import math

def create_animated_title(text_content="FILM TITLE", font_size=2.0):
    """
    Creates an animated 3D text title with rotation and scaling effects
    """
    
    # Clear existing mesh objects (optional)
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)
    
    # Create text object
    bpy.ops.object.text_add(location=(0, 0, 0))
    text_obj = bpy.context.active_object
    text_obj.name = "AnimatedTitle"
    
    # Set text content and properties
    text_obj.data.body = text_content
    text_obj.data.size = font_size
    text_obj.data.extrude = 0.1  # Give it some depth
    text_obj.data.bevel_depth = 0.02  # Add beveling for better lighting
    
    # Position text at origin
    text_obj.location = (0, 0, 0)
    
    # Animation keyframes
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = 150
    
    # Initial rotation keyframe
    scene.frame_set(1)
    text_obj.rotation_euler = (0, 0, 0)
    text_obj.scale = (0.1, 0.1, 0.1)  # Start small
    text_obj.keyframe_insert(data_path="rotation_euler")
    text_obj.keyframe_insert(data_path="scale")
    
    # Mid-animation keyframe
    scene.frame_set(75)
    text_obj.rotation_euler = (0, 0, math.radians(180))  # Half rotation
    text_obj.scale = (1.2, 1.2, 1.2)  # Slightly oversized
    text_obj.keyframe_insert(data_path="rotation_euler")
    text_obj.keyframe_insert(data_path="scale")
    
    # Final keyframe
    scene.frame_set(150)
    text_obj.rotation_euler = (0, 0, math.radians(360))  # Full rotation
    text_obj.scale = (1.0, 1.0, 1.0)  # Normal size
    text_obj.keyframe_insert(data_path="rotation_euler")
    text_obj.keyframe_insert(data_path="scale")
    
    # Set interpolation to smooth
    for fcurve in text_obj.animation_data.action.fcurves:
        for keyframe in fcurve.keyframe_points:
            keyframe.interpolation = 'BEZIER'
            keyframe.handle_left_type = 'AUTO'
            keyframe.handle_right_type = 'AUTO'
    
    print(f"Created animated title: '{text_content}'")
    return text_obj

def add_lighting_setup():
    """
    Adds professional lighting setup for the title
    """
    
    # Add key light
    bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
    key_light = bpy.context.active_object
    key_light.name = "KeyLight"
    key_light.data.energy = 3
    key_light.rotation_euler = (math.radians(30), 0, math.radians(45))
    
    # Add fill light
    bpy.ops.object.light_add(type='AREA', location=(-3, 2, 5))
    fill_light = bpy.context.active_object
    fill_light.name = "FillLight"
    fill_light.data.energy = 1.5
    fill_light.data.size = 5
    
    print("Added professional lighting setup")

def create_material_animation(text_obj):
    """
    Creates animated material for the text with color changes
    """
    
    # Create new material
    mat = bpy.data.materials.new(name="TitleMaterial")
    mat.use_nodes = True
    text_obj.data.materials.append(mat)
    
    # Get material nodes
    nodes = mat.node_tree.nodes
    principled = nodes.get("Principled BSDF")
    
    if principled:
        # Set initial material properties
        principled.inputs[0].default_value = (0.1, 0.1, 0.8, 1.0)  # Blue
        principled.inputs[1].default_value = 0.8  # Metallic
        principled.inputs[2].default_value = 0.1  # Roughness
        
        # Animate base color
        scene = bpy.context.scene
        
        scene.frame_set(1)
        principled.inputs.default_value = (0.1, 0.1, 0.8, 1.0)  # Blue
        principled.inputs.keyframe_insert("default_value")
        
        scene.frame_set(75)
        principled.inputs.default_value = (0.8, 0.1, 0.1, 1.0)  # Red
        principled.inputs.keyframe_insert("default_value")
        
        scene.frame_set(150)
        principled.inputs.default_value = (0.8, 0.8, 0.1, 1.0)  # Gold
        principled.inputs.keyframe_insert("default_value")
    
    print("Added animated material to title")

# Main execution
if __name__ == "__main__":
    # Create the animated title
    title_obj = create_animated_title("YOUR FILM TITLE", 2.5)
    
    # Add lighting
    add_lighting_setup()
    
    # Add animated material
    create_material_animation(title_obj)
    
    # Set camera position for good framing
    bpy.ops.object.camera_add(location=(0, -8, 2))
    camera = bpy.context.active_object
    camera.rotation_euler = (math.radians(80), 0, 0)
    
    print("Title animation setup complete!")
    print("Press SPACE to play animation in viewport")
