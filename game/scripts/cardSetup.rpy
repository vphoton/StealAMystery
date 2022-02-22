

init python:
    import pygame

    class Card:
        def __init__(self,name,info,sus,posx,posy,rot,sprite,active):
            self.name = name
            self.info = info
            self.sus = sus
            self.xpos = posx
            self.ypos = posy
            self.rotate = rot
            self.sprite = sprite
            self.active = active
            self.dragging = False


    class Inventory:
        def __init__(self):
            pass
