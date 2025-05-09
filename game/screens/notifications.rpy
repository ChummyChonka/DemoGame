
style centered_style:
    xalign 0.5
    yalign 0.5
    spacing 5

style fitnessxp_text:
    color "#FFFFFF"
    outlines([ (absolute(2), "#000000", absolute(0), absolute(0)) ])

style fitnessxp_button_text is fitnessxp_text:
    hover_color gui.hover_color


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

transform xp_bar_zoom:
    zoom 0.3


screen hbox_screen(buttons=["Test"], text_size=30):
    hbox:
        style "centered_style"
        spacing 10
        xmaximum 300
        box_wrap True
        for button in buttons:
            textbutton button:
                action Null
                text_size text_size


screen dismiss_test():
    dismiss action Return()

    frame:
        modal True

        align (.5, .3)
        padding (20, 20)

        has vbox

        text "This is a very important message.":
            xalign 0.5
            textalign 0.5

        # Dismiss can be confusing on its own, so we'll add a button as well.
        textbutton "Dismiss":
            xalign 0.5
            action Return()


screen notify(message):
    zorder 100
    style_prefix "notify"

    vbox:
        xalign 0.99
        #yalign 0.15
        ypos 400
        frame at notify_appear:
            background Frame("gui/notify.png", 50,50)
            padding(50,50)
            text "[message!tq]"

    timer 3.25 action Hide('notify')


screen fitness_xp_bar(args):
    zorder 100
    style_prefix "fitnessxp"

    $ sections = args[0]
    $ fitness_xp = args[1]
    $ fitness_xp_next = args[2]

    vbox:
        xalign 0.99
        ypos 600


        frame at notify_appear:
            #background Frame("gui/xp_bar/xp_bar_frame.png", 50,50)
            background Frame("gui/notify.png", 50,50)
            padding(50,50)
            ysize 450
            vbox:
                vbox:
                    xalign 0.5
                    if(sections == 10):
                        vbox:
                            xalign 0.5
                            text "LEVEL UP"
                            text "Fitness: " + str(protagonist.get_stat(Stats.FITNESS))
                    else:
                        vbox:
                            xalign 0.5
                            text "Fitness XP to next level:"
                            text "[fitness_xp] | [fitness_xp_next]":
                                xalign 0.5
                vbox:
                    xalign 0.5
                    if(sections<10):
                        add "gui/xp_bar/sections_white/xp_bar_section0" + str(sections) + ".png" at xp_bar_zoom
                    else:
                        add "gui/xp_bar/sections_white/xp_bar_section10.png" at xp_bar_zoom
                    add "gui/xp_bar/xp_bar_empty.png" at xp_bar_zoom:
                        yoffset -150
    timer 3.25 action Hide("fitness_xp_bar")
                    # textbutton _("Confirm"):
                    #     xalign 0.5
                    #     yoffset -150
                    #     action Hide("fitness_xp_bar")
