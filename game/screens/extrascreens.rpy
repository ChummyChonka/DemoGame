style succubus_button_text:
    hover_color "#ff0008"
    idle_color "#FFFFFF"
    # (size, color, xoffset, yoffset) 
    outlines [ (absolute(0), "#000", absolute(3), absolute(3)) ]

style succubus_text:
    outlines [ (absolute(0), "#000", absolute(3), absolute(3)) ]

style credits_text:
    text_align 0.0
    size 65

style to_be_continued_button:
    padding (50, 25)

style to_be_continued_button_text is button_text:
    color gui.text_color
    hover_color gui.hover_color
    size gui.text_size



screen photo_taking(vertical, img):
    modal True
    imagebutton:
        idle "images/smartphone/camera/taking_photo_idle.webp"
        xalign 0.5
        yalign 0.5
    imagebutton:
        auto "images/smartphone/camera/photo_button_%s.webp"
        action Function(take_photo, img)
        if vertical:
            xalign 0.5
            yalign 0.97
        else:
            xalign 0.9
            yalign 0.5


screen skip_workout():
    style_prefix "succubus"
    textbutton _("Skip Workout"):
        xalign 1.0
        yalign 0.05
        action Jump("intro_skipped_workout")


screen credits():
    tag menu

    use game_menu(_("Credits"), scroll="viewport"):
        vbox:
            style_prefix "credits"
            text _("Various Credits\n"):
                size 100
                underline True
            for line in read_credits("other"):
                if(line.startswith("http")):
                    text ("{a=[line]}" + line + "{/a}")
                else:
                    text line

            text _("\nSounds Credits\n"):
                size 100
                underline True
            for line in read_credits("sounds"):
                if(line.startswith("http")):
                    text ("{a=[line]}" + line + "{/a}")
                else:
                    text line

            text _("\nMusic Credits\n"):
                size 100
                underline True
            for line in read_credits("music"):
                if(line.startswith("http")):
                    text ("{a=[line]}" + line + "{/a}")
                else:
                    text line


screen to_be_continued():
    modal True
    style_prefix "to_be_continued"
    add "bg_black.webp"
    vbox:
        xalign 0.5
        yalign 0.7
        text "TO BE CONTINUED":
            xalign 0.5
            size 150

        null height 100

        text "The story will continue with your support":
            xalign 0.5
        null height 25
        textbutton ("Open Linktree"):
            xalign 0.5
            background Frame("gui/notify.png", 50,50)
            action OpenURL("https://linktr.ee/chummychonka")

        null height 300
        text "Then click here and remember to save afterwards:":
            xalign 0.5
        null height 25
        textbutton ("Continue playing"):
            xalign 0.5
            background Frame("gui/notify.png", 50,50)
            #action Hide("to_be_continued")
            action [Hide("to_be_continued"), Jump("main_game")]


screen otf_name_change(p_id):
    #style_prefix "input"
    style_prefix "smartphone"
    modal True

    frame:
        #background Transform(Frame("gui/frame_big.png", 50,50), alpha=0.9)
        background Transform(Frame("gui/notify.png", 50,50), alpha=0.95)
        xminimum 2000
        xmaximum 3500
        ysize 1400
        xalign 0.5
        yalign 0.1

        has vbox:
            spacing 30
            xalign 0.5
            yalign 0.5

            null height 50

            hbox:
                spacing 30
                add person_get_image(p_id):
                    xalign 0.5

                grid 2 3:
                    yalign 0.5
                    spacing 30
                    text "Name:"
                    if not person_check_name(p_id):
                        textbutton "Not Set":
                            text_underline True
                            action Show("textinput", args=[p_id, "name"])
                    else:
                        textbutton person_get_name(p_id):
                            text_underline True
                            action Show("textinput", args=[p_id, "name"])

                    text "Nickname:"
                    if not person_check_nickname(p_id):
                        textbutton "Not Set":
                            text_underline True
                            action Show("textinput", args=[p_id, "nickname"])
                    else:
                        textbutton person_get_nickname(p_id):
                            text_underline True
                            action Show("textinput", args=[p_id, "nickname"])

                    text "Surname:"
                    if not person_check_surname(p_id):
                        textbutton "Not Set":
                            text_underline True
                            action Show("textinput", args=[p_id, "surname"])
                    else:
                        textbutton person_get_surname(p_id):
                            text_underline True
                            action Show("textinput", args=[p_id, "surname"])

            null height 50

            text "Name to be displayed for dialogue:":
                xalign 0.5
                underline True
            grid 2 1:
                xalign 0.5
                spacing 30
                textbutton "Name":
                    if not person_use_nickname(p_id):
                        text_underline True
                        text_color "#e06666"
                    action Function(person_set_display_name, p_id, False)
                # imagebutton:
                #     yoffset 20
                #     idle "gui/radio_button_left.png"
                #     action NullAction()
                textbutton "Nickname":
                    if person_use_nickname(p_id):
                        text_underline True
                        text_color "#e06666"
                    action Function(person_set_display_name, p_id, True)

            null height 50

            textbutton "Save and continue":
                xalign 0.5
                background Frame("gui/notify.png", 50,50)
                action [Function(check_mandatory_names, p_id), Function(update_replacements_dict), Hide("otf_name_change")]

            null height 50

    use say_demo(person_get_display_name(p_id), "This is a preview text")


screen say_demo(who, what):
    style_prefix "say"

    window:
        style "window"
        window background Transform(Frame("gui/textbox_test3.png", left=50, top=50), alpha=persistent.dialogueBoxOpacity)
        text what:
            size gui.text_size
            outlines [(absolute(3), "#000000", absolute(2), absolute(2))]
            xpos 700
            ypos 20

        window:
            background Transform(Frame("gui/namebox_test.png", gui.namebox_borders), alpha=persistent.dialogueBoxOpacity)
            style "namebox"
            text who:
                size gui.name_text_size
                outlines [(absolute(3), "#000000", absolute(2), absolute(2))]
                kerning 0

