
init python:
    # keyboard voice sounds
    def callback(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/keytap.wav", loop="True", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="sound")


label start:
    call variables

    show screen map_screen(main_map)
    $occupant = kotachis_house.map[10][8].occupant is None
    "[occupant_flag]"

    #scene bg room
    #
    # show raccoon_idle:
    #     xalign 0.5
    #     yalign 0.5


    e "You've created a new Ren'Py game."

    raccoon "Once you add a story, pictures, and music, you can release it to the world!"

    return

label variables:
    define e = Character("Eileen")
    define raccoon = Character("Rick", color = "#ff0000", callback = callback)
    image raccoon_idle = anim.Filmstrip("raccoon_idle.png",(128,128),(2,1),0.5,loop=True)
    $ click_snd = "audio/keytap.wav"
    $ newCard = Card()

    return
