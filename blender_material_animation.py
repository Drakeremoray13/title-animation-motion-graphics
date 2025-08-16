import bpy
import math

def create_glowing_material(obj_name="AnimatedTitle"):
    """
    Creates a glowing, animated material for film titles
    """
    
    # Get the text object
    text_obj = bpy.data.objects.get(obj_name)
    if not text_obj:
        print(f"Object '{obj_name}' not found!")
        return
    
    # Create material with nodes
    mat = bpy.data.materials.new(name="GlowingTitleMaterial")
    mat.use_nodes = True
    text_obj.data.materials.clear()
    text_obj.data.materials.append(mat)
    
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    # Clear default nodes
    nodes.clear()
    
    # Add nodes
    output = nodes.new(type='ShaderNodeOutputMaterial')
    principled = nodes.new(type='ShaderNodeBsdfPrincipled')
    emission = nodes.new(type='ShaderNodeEmission')
    mix_shader = nodes.new(type='ShaderNodeMixShader')
    color_ramp = nodes.new(type='ShaderNodeValToRGB')
    noise_texture = nodes.new(type='ShaderNodeTexNoise')
    
    # Position nodes
    output.location = (400, 0)
    mix_shader.location = (200, 0)
    principled.location = (0, 100)
    emission.location = (0, -100)
    color_ramp.location = (-200, -100)
    noise_texture.location = (-400, -100)
    
    # Connect nodes
    links.new(principled.outputs[0], mix_shader.inputs[3])
    links.new(emission.outputs, mix_shader.inputs[4])
    links.new(mix_shader.outputs, output.inputs)
    links.new(color_ramp.outputs, emission.inputs)
    links.new(noise_texture.outputs, color_ramp.inputs)
    
    # Set material properties
    principled.inputs.default_value = (0.05, 0.05, 0.05, 1.0)  # Dark base
    principled.inputs[1].default_value = 0.9  # Metallic
    principled.inputs[2].default_value = 0.1  # Roughness
    
    # Set emission strength
    emission.inputs[3].default_value = 5.0  # Emission strength
    
    # Configure color ramp
    color_ramp.color_ramp.elements.color = (0.1, 0.1, 1.0, 1.0)  # Blue
    color_ramp.color_ramp.elements[3].color = (1.0, 0.5, 0.1, 1.0)  # Orange
    
    # Animate mix factor for pulsing glow effect
    scene = bpy.context.scene
    
    for frame in range(1, 151):
        scene.frame_set(frame)
        mix_factor = 0.3 + 0.4 * math.sin(frame * 0.1)  # Pulsing between 0.3 and 0.7
        mix_shader.inputs[0].default_value = mix_factor
        mix_shader.inputs.keyframe_insert("default_value")
    
    print("Created glowing animated material")

if __name__ == "__main__":
    create_glowing_material()
