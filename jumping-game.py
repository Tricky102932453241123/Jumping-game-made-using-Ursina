from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
Sky()
boxes = []
for p in range(2):
    for d in range(8):
        box = Button(
            position=(d, 1, -2),
      color=color.orange,
      highlight_color=color.lime,
      model='cube',
      texture='white_cube',
      origin_y= 0.5,
      parent=scene
        )
        box = Button(
            position=(d, 1, -6),
      color=color.orange,
      highlight_color=color.lime,
      model='cube',
      texture='white_cube',
      origin_y= 0.5,
      parent=scene
        )
        box = Button(
            position=(d, 1.5, -10),
      color=color.orange,
      highlight_color=color.lime,
      model='cube',
      texture='white_cube',
      origin_y= 0.5,
      parent=scene
        )
for n in range(15):
      for k in range(15):
        box = Button(
      position=(k, 0, n),
      color=color.orange,
      highlight_color=color.lime,
      model='cube',
      texture='white_cube',
      origin_y=0.5,
      parent=scene
    )
def update():
    if held_keys['p']:
        print('player is in the position',player.x,player.y,player.z)
app.run()
