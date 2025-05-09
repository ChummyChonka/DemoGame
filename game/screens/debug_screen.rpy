style debug_text:
    size 50
    idle_color "#ffffff"
    outlines [(5, "#111111", 2, 2)]
    #font "gui/fonts/Lexend-VariableFont_wght.ttf"
    hover_color gui.hover_color

style debug_button_text is debug_text

screen debug():
    zorder 100
    style_prefix "debug"
    if config.developer:

        vbox:
            ypos 400
            spacing -20
            text ("Debug Actions"):
                underline True
            for k,v in debug_actions.items():
                textbutton (k):
                    action Function(v)
            textbutton ("Map"):
                action [Hide("actions_default"), Function(hide_all_location_screens), Jump("main_game")]

        vbox:
            spacing -20
            xalign 0.0
            yalign 1.0
            text ("Debug Jumps:"):
                underline True
            for k,v in debug_labels.items():
                textbutton (v):
                    #action [Function(hide_all_location_screens), Jump(k)]
                    action Function(debug_jump_label, k)



init python:
    def debug_jump_label(label):
        hide_all_location_screens()
        renpy.show_screen("actions_default")

        renpy.jump(label)


