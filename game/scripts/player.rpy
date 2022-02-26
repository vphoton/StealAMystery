default k_dir = "front"
default e_dir = "front"
default f_dir = "front"

image player = "player [k_dir]"
image ella = "ella [e_dir]"
image fred = "fred [f_dir]"

define k_offset = 0

init python:
    def getFacingTile():
        if k_dir == "front":
            return (player_sprite.x, player_sprite.y + 1)
        elif k_dir == "back":
            return (player_sprite.x, player_sprite.y - 1)
        elif k_dir == "left":
            return (player_sprite.x - 1, player_sprite.y)
        else:
            return (player_sprite.x + 1, player_sprite.y)

    def playerInteracts():
        x, y = getFacingTile()
        main_map.triggerInteraction(x, y)

# PLAYER
image player back:
    anim.Filmstrip("raccoon_idle.png",(128,128),(2,1),0.5,loop=True)

image player front:
    xzoom -1.0
    anim.Filmstrip("raccoon_idle.png",(128,128),(2,1),0.5,loop=True)

image player left:
    xzoom -1.0
    anim.Filmstrip("raccoon_idle.png",(128,128),(2,1),0.5,loop=True)

image player right:
    anim.Filmstrip("raccoon_idle.png",(128,128),(2,1),0.5,loop=True)

# NPCS
image ella back:
    anim.Filmstrip("EllaIdle.png",(128,128),(2,1),0.5,loop=True)

image ella front:
    xzoom -1.0
    anim.Filmstrip("EllaIdle.png",(128,128),(2,1),0.5,loop=True)

image fred back:
    anim.Filmstrip("Fred.png",(128,128),(2,1),0.5,loop=True)

image fred front:
    xzoom -1.0
    anim.Filmstrip("Fred.png",(128,128),(2,1),0.5,loop=True)

# "kright1.png"
# 0.15
# "kright2.png"
# 0.2
# "kright3.png"
# 0.15
# "kright2.png"
# 0.2
