
init python:
    # keyboard voice sounds
    def callback(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/Pick_Up.ogg", loop="True", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sound")


label start:
    call variables

    show screen map_screen(main_map)
    #$occupant = main_map.map[10][8].occupant is None
    #"[occupant_flag]"

    $main_map.moveDenizen(player_sprite.x, player_sprite.y, 0, -1)

    #scene bg room
    #
    # show raccoon_idle:
    #     xalign 0.5
    #     yalign 0.5

    raccoon "use arrow keys to walk around"
    raccoon "Well here's a confession"
    raccoon "I didn't have enough time to put everything together"
    raccoon "so I guess just enjoy these visuals..."
    raccoon "and also I guess walk over everything cause of no collisions"
    raccoon "I tried to get it so you can at least walk into the other buildings"
    raccoon "but gotta confess I was having some trouble getting the map to switch"
    raccoon "I challenged myself and learned a lot but guess I couldn't finish"
    raccoon "I'll be working to complete this soon though cause I had fun :)"

    return

label variables:
    define e = Character("Eileen")
    define raccoon = Character("Joe", color = "#ff0000", callback = callback)
    image raccoon_idle = anim.Filmstrip("raccoon_idle.png",(128,128),(2,1),0.5,loop=True)
    $ click_snd = "audio/Place.wav"
    #$ newCard = Card()

    return
