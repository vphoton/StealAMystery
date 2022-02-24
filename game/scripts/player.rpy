default k_dir = "front"

image player = "player [k_dir]"

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


# "kright1.png"
# 0.15
# "kright2.png"
# 0.2
# "kright3.png"
# 0.15
# "kright2.png"
# 0.2
