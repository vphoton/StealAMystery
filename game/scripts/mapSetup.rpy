

define tile_size = 128

init python:

    class MainMap:
        def __init__(self, map, img, start_x, start_y):
            self.map = map
            self.img = img
            self.center_x = start_x
            self.center_y = start_y

        def isEmpty(self, x, y):
            return self.map[y][x].occupant is None

        def occupy(self, x, y, denizen):
            if not self.isEmpty(x, y):
                return
            self.map[y][x].occupant = denizen

        def unoccupy(self, x, y):
            self.map[y][x].occupant = None

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

        def triggerInteraction(self, x, y):
            if x < 0 or x >= len(self.map[0]):
                return
            if y < 0 or y >= len(self.map):
                return
            if self.isEmpty(x, y):
                return
            self.map[y][x].occupant.interact()

    class MapTile:
        def __init__(self, occupant = None):
            self.occupant = occupant

    class MapOccupant:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def interact(self):
            pass

    class MapDenizen(MapOccupant):
        def __init__(self, x, y, img, width, height, interaction):
            super(MapDenizen, self).__init__(x,y)
            self.img = img
            self.width = width
            self.height = height
            self.interaction = interaction

        def getOffset(self):
            return (tile_size - self.width, tile_size - self.height)

        def interact(self):
            self.interaction(self)

    main_map_array = []

    for i in range(16):
        new_row = []
        for j in range(16):
            new_row.append(MapTile())
        main_map_array.append(new_row)

        # https://youtu.be/ZYdBq4veSEs?t=5649
    main_map = MainMap(main_map_array, "MainMap.png", 8, 7)
    player_sprite = MapDenizen(8, 7, "player", 128, 128, no_op)
    main_map.occupy(8, 7, player_sprite)
    # water
    wall1 = MapOccupant(8, 9)
    main_map.occupy(8, 9, wall1)
    wall2 = MapOccupant(8, 8)
    main_map.occupy(8, 8, wall2)
    wall3 = MapOccupant(8, 7)
    main_map.occupy(8, 7, wall3)
    #cupcake_sprite = MapDenizen(5, 5, "cupcake.png", 35,26, disappear)
    #main_map.occupy(5, 5, cupcake_sprite)



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
