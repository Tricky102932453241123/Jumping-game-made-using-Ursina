from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
Sky()
player.x = 6,
player.y = 6
boxes = []
for p in range(2):
    for d in range(8):
        box = Button(
            position=(d, 1, -2),
      highlight_color=color.lime,
      model='cube',
      color = color.gray,
      texture= 'white_cube',
      origin_y= 0.5,
      parent=scene
        )
        box = Button(
            position=(d, 1, -6),
      highlight_color=color.lime,
      model='cube',
      color = color.gray,
      texture= 'white_cube',
      origin_y= 0.5,
      parent=scene
        )
        box = Button(
            position=(d, 1.5, -10),
      color=color.gray,
      highlight_color=color.lime,
      model='cube',
      texture='white_cube',
      origin_y= 0.5,
      parent=scene
        )
        box = Button(
            position=(d, 2, -12),
      color=color.gray,
      highlight_color=color.lime,
      model='cube',
      texture='white_cube',
      origin_y= 0.5,
      parent=scene
        )
        box = Button(
            position=(d, 2, -13),
      color=color.gray,
      highlight_color=color.lime,
      model='cube',
      texture='white_cube',
      origin_y= 0.5,
      parent=scene
        )
        box = Button(
            position=(d, 2.5, -15),
      color=color.gray,
      highlight_color=color.lime,
      model='cube',
      texture='white_cube',
      origin_y= 0.5,
      parent=scene
        )
        box = Button(
            position=(d, 2.5, -16),
      color=color.gray,
      highlight_color=color.lime,
      model='cube',
      texture='white_cube',
      origin_y= 0.5,
      parent=scene
        )
        box = Button(
            position=(d, 2.5, -17),
      color=color.gray,
      highlight_color=color.lime,
      model='cube',
      texture='white_cube',
      origin_y= 0.5,
      parent=scene
        )
        box = Button(
            position=(d, 2.5, -18),
      color=color.gray,
      highlight_color=color.lime,
      model='cube',
      texture='white_cube',
      origin_y= 0.5,
      parent=scene
        )
for z in range(0, -5):
    for n in range(15):
        for k in range(15):
          box = Button(
      position=(k, z, n),
      color=color.gray,
      highlight_color=color.lime,
      model='cube',
      texture='white_cube',
      origin_y=0.5,
      parent=scene
    )
cube = Entity(model='cube', color=color.red, position=(-2, 1, 0), texture='white_cube')
def update():
    if held_keys['p']:
        print('player is in the position',player.x,player.y,player.z)
    cube.color=color.random_color()
    
app.run()
