from ursina import *
from ursina.prefabs.ursfx import ursfx
from ursina.prefabs.first_person_controller import FirstPersonController
import time, soundfile, sounddevice, ast
count = 0
n = input('world name?')
i = input('load save file? y/n ')
class SaveTextError(Exception):
    pass
if i == 'n':
    app = Ursina()
    window.fullscreen = True
    mo_entity = []
    for y in range(-4, 0):
        for x in range(-5, 7):
            for z in range(-5, 7):
                mo_entity.append(Entity(model = "cube", scale = 1, texture = "grass" if y == -1 else 'stone', position = (x, y+0.5, z), collider = 'box', name = f"cube{count}"))
                count+=1
    label = Text(x = -0.77, y = 0.47, text = 'text')
    label1 = Text(x = -0.77, y = 0.44, text = 'text')
elif i == 'y':
    f = input('save file ')
    app = Ursina()
    window.fullscreen = True
    label = Text(x = -0.77, y = 0.47, text = 'text')
    label1 = Text(x = -0.77, y = 0.44, text = 'text')
    try:
        with open(f, 'r') as file:
            safe_globals = {"Entity": Entity,"Vec3": Vec3}
            o = file.read()
            mo_entity = eval(o, safe_globals)
    except:
        raise SaveTextError('Invalid save file, plz try again.')
# Cam = EditorCamera(move_speed=2, rotation_speed=100)
Sky()
type1 = ['stone','glass','arrow_down', 'arrow_right', 'brick', 'circle', 'circle_hollow', 'circle_outlined', 'cog', 'cursor', 'checkerboard_transparent', 'file_icon', 'folder', 'grass', 'grass_tintable', 'heightmap_1', 'horizontal_gradient', 'nine_sliced', 'nineslice_double', 'nineslice_rainbow', 'noise', 'perlin_noise', 'radial_gradient', 'rainbow', 'reflection_map_3', 'shore', 'sky_default', 'sky_sunset', 'test_tileset', 'tilemap_test_level', 'ursina_logo', 'ursina_wink_0000', 'ursina_wink_0001', 'vertical_gradient', 'vignette', 'white_cube', 'bag', 'gem', 'orb', 'bow_arrow', 'sword']
b = 0
player = FirstPersonController()
player.speed = 7.5
player.mouse_sensitivity = Vec2(300,300)
player.jump_height = 1
fly_true = False
audiowait2 = False
op = ''
of = [] 
def entities_to_str(entities):
    safe_entities = []
    for e in entities:
        # skip destroyed ones
        if e.parent is None:
            continue
        try:
            safe_entities.append(
                f"Entity(model='cube', position={e.position}, name='{e.name}', "
                f"scale={e.scale}, collider='{e.collider}', texture='{e.texture}')"
            )
        except Exception:
            # if accessing attributes fails, treat as destroyed
            continue
    return "[" + ", ".join(safe_entities) + "]"
mouse.locked = True
def input(key):
    global fly_true, count, mo_entity, type1, b,audiowait2, n
    if key == 'right mouse down':
        count+=1
        try:
            sound, sample = soundfile.read('block place.wav')
            sounddevice.play(sound, sample)
            l = tuple(mouse.world_point)
            ro_l = list(round(n) for n in l)
            ro_l[1] +=0.5
            mo_entity.append(Entity(model = 'cube', position = tuple(ro_l), name = f'cube_{count}', scale = 1, collider = 'box', texture = type1[b]))
        except TypeError:
            pass
    if key == 'c':
        b += 1
        if b > len(type1)-1:
            b = 0
    if key == 'z':
        b -= 1
        if b < 0:
            b = len(type1)-1
    if key == 'left mouse down':
        if mo_entity and str(mouse.hovered_entity).startswith('cube'):
            sound, sample = soundfile.read('block destroy.wav')
            sounddevice.play(sound, sample)
            audiowait2 = True
    try:
        if not key == 'left mouse down' and sounddevice.get_stream().active and not key == 'right mouse down':
            audiowait2 = False
            sounddevice.stop()
    except ValueError:
        pass
    except RuntimeError:
        pass
    if key == "o":
        mouse.locked = False if mouse.locked == True else True
    if key == 'k':
        fly_true = True if fly_true == False else False
    if key == 'l':
        window.fullscreen = False if window.fullscreen == True else True
    if key == 'p':
        with open(n, 'w') as q:
            q.write(entities_to_str(mo_entity))
    global op
    op = key    
    
        
       
elapsed = 0              
        
def update():
    global fly_true, b, type1, audiowait2, op, of, elapsed
    try:   
        if op == 'left mouse down' and sounddevice.get_stream().active:
            if not of:
                of.append(Entity(model = 'cube', scale = mouse.hovered_entity.scale, texture = 'circle', position = mouse.hovered_entity.position, alpha = 1))
            elapsed += time.dt
            if elapsed>=0.2:
                mouse.hovered_entity.alpha-=0.2
                for f in of:
                    f.alpha-=0.2
                elapsed = 0
                
            
        else:
            mouse.hovered_entity.alpha = 1
            for f in of:
                of.remove(f)
                destroy(f)
            elapsed = 0
    except RuntimeError:
        pass
    except AttributeError:
        pass
    except UnboundLocalError:
        pass
    if audiowait2 and not sounddevice.get_stream().active:
        if str(mouse.hovered_entity).startswith('cube'):
            try:
                for f in of:
                    destroy(f)
            except UnboundLocalError:
                pass
            destroy(mouse.hovered_entity)
            
            audiowait2 = False
            
    player.y = player.y
    if held_keys['f']:
        ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.6, 0.75), (1.0, 0.0)], volume=0.5, wave='square', speed=4)
    if fly_true:
        player.gravity = 0
        if held_keys['space']:
            player.y+=0.2
        elif held_keys['shift']:
            player.y-=0.2
    else:
        player.gravity = 1
        if held_keys['shift']:
            player.speed = 12.5
        else:
            player.speed = 7.5
    label.text = f"position x, y, z:{player.position} hit: {mouse.hovered_entity}, position_hit: {mouse.world_point}"
    label1.text = f"block type: {type1[b]}"
    

    
        

app.run()

