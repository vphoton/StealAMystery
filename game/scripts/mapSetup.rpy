

init python:

    class MainMap:
        def __init__(self, map_grid, img, start_x, start_y):
            self.map_grid = map_grid
            self.img = img
            self.center_x = start_x
            self.center_y = start_y

        def isEmpty(self, x, y):
            return self.map[y][x].occupant is None

        def occupy(self, x, y, denizen):
            if not self.isEmpty(x, y):
                return
            self.map[y][x].occupant = denizen

        def moveDenizen(self, x, y, offx, offy):
            if self.isEmpty(x, y):
                return
            if x + offx >= len(self.map[0]) or x + offx < 0:
                return
            if y + offy >= len(self.map) or y + offy < 0:
                return
            if not self.isEmpty(x + offx, y + offy):
                return
            denizen = self.map[y][x].occupant
            self.map[y][x].occupant = None
            self.map[y + offy][x + offx].occupant = denizen
            denizen.x += offx
            denizen.y += offy
            if self.center_x == x and self.center_y == y:
                self.center_x += offx
                self.center_y += offy

        class MapTile:
            def __init__(self, occupant = None):
                self.occupant = occupant

        class MapOccupant:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        class MapDenizen(MapOccupant):
            def __init__(self, x, y, img, width, height):
                super(MapDenizen, self).__init__(x,y)
                self.img = img
                self.width = width
                self.height = height

            def getOffset(self):
                return (tile_size - self.width, tile_size - self.height)

        house_map = []

        for i in range(12):
            new_row = []
            for j in range(19):
                new_row.append(MapTile())
            house_map.append(new_row)

            # https://youtu.be/ZYdBq4veSEs?t=5649

        kotachis_house = AstersmMap(house_map, "kotachis house inside.png", )
        kotachi_sprite = MapDenizen(10, 10, "kotachi", 79, `36`)
        kotachis_house.occupy(10, 10, kotachi_sprite)
        wall = MapOccupant(8, 10)
        kotachis_house.occupy(8, 10, wall)




    # import pygame


    # def __rect_overlap_area(r1, r2):
    #     if r1 is None or r2 is None:
    #         return 0
    #
    #     x1, y1, w1, h1 = r1
    #     x2, y2, w2, h2 = r2
    #
    #     maxleft = max(x1, x2)
    #     minright = min(x1 + w1, x2 + w2)
    #     maxtop = max(y1, y2)
    #     minbottom = min(y1 + h1, y2 + h2)
    #
    #     if minright < maxleft:
    #         return 0
    #
    #     if minbottom < maxtop:
    #         return 0
    #
    #     return (minright - maxleft) * (minbottom - maxtop)
    #
    # class Building:
    #     def __init__(self,name,posx,posy,isLocked,sprite):
    #         self.name = name
    #         self.xpos = posx
    #         self.ypos = posy
    #         self.isLocked = isLocked
    #         self.sprite = sprite
    #
    #     def mouseOver(self,mx,my):
    #         # this will scale the image up with transform
    #
    # class Person:
    #     def __init__(self,name,posx,posy,sprite):
    #         self.name = name
    #         self.xpos = posx
    #         self.ypos = posy
    #         self.sprite = sprite
