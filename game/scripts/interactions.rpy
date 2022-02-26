

# $ showAscreen(theScreen):
#     show screen theScreen


init python:

    def no_op(denizen):
        pass

    def disappear(denizen):
        #need to know the actual map that will be using
        main_map.unoccupy(denizen.x, denizen.y)

    def roomTP(theScreen):
        "ahhh"
