
################
# Base Screens #
################
screen smartphone(for_phonecall=False):
    modal True
    style_prefix "smartphone"
    if for_phonecall:
        add "images/smartphone/phone_new_folded.webp" at phonecall_loc
        add Crop((1567,208,706,1744), "images/smartphone/wallpaper/" + smartphone.current_bg + ".webp") at phonecall_wallpaper_loc
        add "images/smartphone/smartphone_overlay.webp" alpha (1-smartphone.overlay_opacity) at phonecall_loc
        add "images/smartphone/smartphone_overlay.webp" alpha 0.8 at phonecall_loc
        #add "images/smartphone/smartphone_overlay_top.webp" alpha 0.8 at phonecall_loc
    else:
        add renpy.get_showing_tags(sort=True)[0] at kawase_blur_darken
        add "images/smartphone/phone_new.webp"
        add "images/smartphone/wallpaper/" + smartphone.current_bg + ".webp"
        add "images/smartphone/smartphone_overlay_wide.webp" alpha (1-smartphone.overlay_opacity)
        add "images/smartphone/phone_app_overlay.webp" alpha smartphone.overlay_app_opacity


    if(len(smartphone.content_stack) > 0):
        if for_phonecall:
            text (actualgame.weekdays[actualgame.weekday-1]) at phonecall_notification_bar_left:
                size 35
            hbox:
                at phonecall_notification_bar_right
                imagebutton idle "images/smartphone/notificationbar/phone_empty.webp" action NullAction() style "smartphone_button_inactive"
                null width 20
                imagebutton idle "images/smartphone/notificationbar/phone_silent_off.webp" action NullAction() style "smartphone_button_inactive"
                null width 20
                imagebutton idle "images/smartphone/notificationbar/wifi_connection_full.webp" action NullAction() style "smartphone_button_inactive"
                imagebutton idle "images/smartphone/notificationbar/mobile_connection_full.webp" action NullAction() style "smartphone_button_inactive"

            text ("[smartphone.battery_level]%"):
                if(smartphone.battery_level < 5):
                    color "#D90000"
                xpos 3210
                ypos 145
                size 35

        else:
            text (actualgame.weekdays[actualgame.weekday-1]) at notificationbar_left:
                size 50
            hbox:
                # if(not for_phonecall):
                at notificationbar_right
                # else:
                    #at notificationbar_right_phonering

                #imagebutton idle "images/smartphone/notificationbar/phone_alarm.webp" action NullAction()
                imagebutton idle "images/smartphone/notificationbar/phone_empty.webp" action NullAction() style "smartphone_button_inactive"
                null width 20
                imagebutton idle "images/smartphone/notificationbar/phone_silent_off.webp" action NullAction() style "smartphone_button_inactive"
                null width 20
                imagebutton idle "images/smartphone/notificationbar/wifi_connection_full.webp" action NullAction() style "smartphone_button_inactive"
                imagebutton idle "images/smartphone/notificationbar/mobile_connection_full.webp" action NullAction() style "smartphone_button_inactive"

                #battery icon
                imagebutton:
                    if(smartphone.battery_level >= 90):
                        idle "images/smartphone/notificationbar/battery_90.webp"
                    elif(smartphone.battery_level >= 65):
                        idle "images/smartphone/notificationbar/battery_70.webp"
                    elif(smartphone.battery_level >= 25):
                        idle "images/smartphone/notificationbar/battery_40.webp"
                    elif(smartphone.battery_level >= 5):
                        idle "images/smartphone/notificationbar/battery_10.webp"
                    else:
                        idle "images/smartphone/notificationbar/battery_0.webp"
                    action NullAction()
                    style "smartphone_button_inactive"

            text ("[smartphone.battery_level]%"):
                if(smartphone.battery_level < 5):
                    color "#D90000"
                xpos 2900
                ypos 85
                size 50


screen smartphone_bot_controls():
    style_prefix "smartphone"
    #zorder 100
    hbox at phone_bottom:
        spacing 150
        imagebutton:
            auto "images/smartphone/triangle_%s.webp"
            #action [Hide("smartphone"), Show("smartphone")]
            action Function(smartphone_screen_pop)
            at phone_bot_zoom
        imagebutton:
            auto "images/smartphone/circle_%s.webp"
            #action [Hide("smartphone"), Show("smartphone")]
            action Function(smartphone_home)
            at phone_bot_zoom
        imagebutton:
            auto "images/smartphone/square_%s.webp"
            action Function(do_mini_phone)
            at phone_bot_zoom


screen smartphone_apps_new():
    style_prefix "smartphone"
    #text "Apps" at phone_title
    hbox:
        xalign 0.5
        yalign 0.2
        spacing 20
        text smartphone.time at phone_widget:
            style "smartphone_widget"
        if(not smartphone.clock24hours):
            if smartphone.time_is_pm:
                text "pm":
                    style "smartphone_widget"
            else:
                text "am":
                    style "smartphone_widget"

    hbox:
        at phone_weather_widget
        imagebutton idle "images/smartphone/phone_weather_partly_cloudy.webp" action NullAction()
        vbox:
            xpos 50
            text "Mostly":
                style "smartphone_weather_widget_text"
                xalign 0.5
            text "Sunny":
                style "smartphone_weather_widget_text"
                xalign 0.5
                ypos -60

    grid 5 3 at phone_content_apps:
        #spacing 25
        for app in apps:
            if(not app.disabled and app.function==AppDo.PUSH):
                vbox:
                    #xsize 250
                    xsize 400
                    #ysize 320
                    ysize 400
                    imagebutton:
                        if app.hovered:
                            idle app.get_icon(hovered=True)
                        else:
                            idle app.get_icon()
                        action Function(smartphone_screen_push, app.name)
                        xalign 0.5
                        hovered Function(set_app_hovered, app.name, True)
                        unhovered Function(set_app_hovered, app.name, False)

                    textbutton (app.display_name):
                        hovered Function(set_app_hovered, app.name, True)
                        unhovered Function(set_app_hovered, app.name, False)
                        action Function(smartphone_screen_push, app.name)
                        if(app.hovered):
                            text_style "smartphone_smaller_button_text_hovered"
                        else:
                            text_style "smartphone_smaller_button_text"
                        xalign 0.5
                        ypos -40

        for app in apps:
            if(not app.disabled and app.function==AppDo.URL):
                vbox:
                    #xsize 250
                    #ysize 320
                    xsize 400
                    ysize 400
                    imagebutton:
                        if app.hovered:
                            idle app.get_icon(hovered=True)
                        else:
                            idle app.get_icon()
                        action OpenURL(app.url)
                        xalign 0.5
                        hovered Function(set_app_hovered, app.name, True)
                        unhovered Function(set_app_hovered, app.name, False)


                    textbutton (app.display_name):
                        hovered Function(set_app_hovered, app.name, True)
                        unhovered Function(set_app_hovered, app.name, False)
                        action OpenURL(app.url)
                        if(app.hovered):
                            text_style "smartphone_smaller_button_text_hovered"
                        else:
                            text_style "smartphone_smaller_button_text"
                        xalign 0.5
                        ypos -40


###################
# Content Screens #
###################
screen guide():
    style_prefix "smartphone_guide"
    vbox at phone_content_wide:
        xfill True
        yfill True

        null height 50

        frame:
            background Frame("images/smartphone/msgboxes/phonemsg18.webp", 50,50)
            padding (20,20)
            ysize 200

            hbox:
                xfill True
                xalign 0.5
                yalign 0.5

                # arrow back
                imagebutton:
                    at phone_button_zoom
                    xalign 0.3
                    if(actualgame.guide_selected_quest > 0):
                        auto "images/smartphone/arrow_left_simple_%s.webp"
                        action Function(set_guide_quest_number, increase=False)
                    else:
                        idle "images/smartphone/arrow_simple_empty.webp"
                        action NullAction()
                        style "smartphone_button_inactive"

                vbox:
                    xalign 0.5
                    xsize 1200
                    hbox:
                        xalign 0.5
                        text "[actualgame.guide_selected_quest+1] - "
                        text store.quests[actualgame.guide_selected_quest].name

                # arrow forward
                imagebutton:
                    at phone_button_zoom
                    xalign 0.7
                    if enable_guide_forward_arrow():
                        auto "images/smartphone/arrow_right_simple_%s.webp"
                        action Function(set_guide_quest_number, increase=True)
                    else:
                        idle "images/smartphone/arrow_simple_empty.webp"
                        action NullAction()
                        style "smartphone_button_inactive"

        null height 50

        viewport:
            draggable True
            mousewheel True

            vbox:
                spacing 30

                for event in store.quests[actualgame.guide_selected_quest].events:
                    if event.is_unlocked():
                        hbox:
                            spacing 30
                            box_wrap True

                            frame:
                                if event.done and (smartphone.guide_hovered_event == event.event_id):
                                    background Frame("images/smartphone/msgboxes/phonemsg29.webp", 50,50)
                                elif event.done:
                                    background Frame("images/smartphone/msgboxes/phonemsg22.webp", 50,50)
                                elif event.locked and (smartphone.guide_hovered_event == event.event_id):
                                    background Frame("images/smartphone/msgboxes/phonemsg17.webp", 50,50)
                                elif event.locked:
                                    background Frame("images/smartphone/msgboxes/phonemsg16.webp", 50,50)
                                elif (smartphone.guide_hovered_event == event.event_id):
                                    background Frame("images/smartphone/msgboxes/phonemsg30.webp", 50,50)
                                else:
                                    background Frame("images/smartphone/msgboxes/phonemsg25.webp", 50,50)
                                padding (0,0)
                                #xmaximum 1900
                                xsize 1900
                                yminimum 200

                                vbox:
                                    #xfill True
                                    #yminimum 200
                                    #box_wrap True

                                    spacing 0

                                    if event.done:
                                        textbutton event.guide_name:
                                            xsize 1900
                                            ysize 200
                                            hovered SetVariable("smartphone.guide_hovered_event", event.event_id)
                                            unhovered SetVariable("smartphone.guide_hovered_event", None)
                                            if(smartphone.guide_opened_event == event.event_id):
                                                action SetVariable("smartphone.guide_opened_event", None)
                                            else:
                                                action SetVariable("smartphone.guide_opened_event", event.event_id)

                                        if(smartphone.guide_opened_event == event.event_id):
                                            textbutton get_event_description(event.event_id):
                                                xsize 1900
                                                text_size 65
                                                yminimum 100
                                                hovered SetVariable("smartphone.guide_hovered_event", event.event_id)
                                                unhovered SetVariable("smartphone.guide_hovered_event", None)
                                                action SetVariable("smartphone.guide_opened_event", None)

                                            null height 20

                                    elif event.locked:
                                        textbutton "Event locked":
                                            xfill True
                                            ysize 200
                                            hovered SetVariable("smartphone.guide_hovered_event", event.event_id)
                                            unhovered SetVariable("smartphone.guide_hovered_event", None)
                                            action NullAction()
                                    else:
                                        textbutton "Click here to get a hint...":
                                                hovered SetVariable("smartphone.guide_hovered_event", event.event_id)
                                                unhovered SetVariable("smartphone.guide_hovered_event", None)
                                                ysize 200
                                                xsize 1900
                                                if(smartphone.guide_opened_event == event.event_id):
                                                    action SetVariable("smartphone.guide_opened_event", None)
                                                else:
                                                    action SetVariable("smartphone.guide_opened_event", event.event_id)

                                        if(smartphone.guide_opened_event == event.event_id):
                                            textbutton event.get_guide_info():
                                                text_size 65
                                                hovered SetVariable("smartphone.guide_hovered_event", event.event_id)
                                                unhovered SetVariable("smartphone.guide_hovered_event", None)
                                                xsize 1900
                                                action SetVariable("smartphone.guide_opened_event", None)
                                            null height 20


                            imagebutton:
                                yalign 0.5
                                style "smartphone_button_inactive"
                                at phone_guide_checkmarks
                                if event.done:
                                    idle "images/smartphone/checkmark_filled_idle.webp"
                                elif event.locked:
                                    idle "images/smartphone/checkmark_crossed_idle.webp"
                                else:
                                    idle "images/smartphone/checkmark_empty_idle.webp"
                                action NullAction()


screen renamer():
    style_prefix "smartphone"

    viewport at phone_msg_content_wide_left:
        draggable True
        mousewheel True
        scrollbars "vertical"

        vbox:
            xfill True

            #for p in sorted(store.people, key=lambda pers: pers.name):
            #for p in sorted(people.keys()):
            for p in get_sorted_people_by_display_name():
                if(person_is_unknown(p)):
                    continue
                textbutton person_get_display_name(p):
                    xalign 0.5
                    action SetVariable("actualgame.renamer_person", p)


    viewport at phone_msg_content_wide_right:
        vbox:
            xfill True
            if(actualgame.renamer_person is None):
                null height 300
                text "Select somebody":
                    xalign 0.5
                    yalign 0.5
            else:
                null height 50

                add person_get_image(actualgame.renamer_person):
                    xalign 0.5

                #hbox:
                grid 2 4:
                    xalign 0.5
                    spacing 30

                    text "Name:"
                    if not person_check_name(actualgame.renamer_person):
                        textbutton "Not Set":
                            text_underline True
                            action Show("textinput", args=[actualgame.renamer_person, "name"])
                    else:
                        textbutton person_get_name(actualgame.renamer_person):
                            text_underline True
                            action Show("textinput", args=[actualgame.renamer_person, "name"])

                    text "Nickname:"
                    if not person_check_nickname(actualgame.renamer_person):
                        textbutton "Not Set":
                            text_underline True
                            action Show("textinput", args=[actualgame.renamer_person, "nickname"])
                    else:
                        textbutton person_get_nickname(actualgame.renamer_person):
                            text_underline True
                            action Show("textinput", args=[actualgame.renamer_person, "nickname"])

                    text "Surname:"
                    if not person_check_surname(actualgame.renamer_person):
                        textbutton "Not Set":
                            text_underline True
                            action [SetField(actualgame.renamer_person, "surname", ""), Show("textinput", args=[actualgame.renamer_person, "surname"])]
                    else:
                        textbutton person_get_surname(actualgame.renamer_person):
                            text_underline True
                            action Show("textinput", args=[actualgame.renamer_person, "surname"])

                    if(actualgame.renamer_person in petnames_for_protag):
                        text "Petname:"
                        textbutton petnames_for_protag[actualgame.renamer_person]:
                            text_underline True
                            action [SetField(actualgame.renamer_person, "surname", ""), Show("textinput", args=[petnames_for_protag, "petname", actualgame.renamer_person])]

                null height 100

                text "Used for Dialogue:":
                    underline True
                    xalign 0.5
                grid 2 1:
                    xalign 0.5
                    spacing 30
                    textbutton "Name":
                        if(person_use_nickname(actualgame.renamer_person) == False):
                            text_underline True
                        action Function(person_set_display_name, actualgame.renamer_person, False)
                    textbutton "Nickname":
                        if person_use_nickname(actualgame.renamer_person):
                            text_underline True
                        action Function(person_set_display_name, actualgame.renamer_person, True)


screen textinput(args):
    modal True
    style_prefix "smartphone_textinput"
    frame:
        background Frame("gui/notify.png", 50,50)
        xminimum 2200
        xmaximum 3500
        yminimum 750
        xalign 0.5
        style "name_changer"

        has vbox:
            spacing 30
            xalign 0.5
            yalign 0.5

            hbox:
                spacing 30
                if(args[1] in ["name", "surname", "nickname"]):
                    text args[1].capitalize() + ": "
                    input:
                        value DictInputValue(people[args[0]], args[1])
                elif(args[1] == "petname"):
                    text "Petname:"
                    input:
                        value DictInputValue(args[0], args[2])
                else:
                    text "ERROR"

            textbutton "Save":
                xalign 0.5
                action [Function(person_update_display_name, actualgame.renamer_person), Hide("textinput")]


screen music():
    style_prefix "smartphonemusic"
    text "Music" at phone_title
    vbox at phone_content:
        xsize 780
        hbox:
            spacing 20
            text "Currently Playing:"
            null width 30
            hbox:
                spacing 20
                ypos 15

                #play button
                imagebutton:
                    if(gamemusic.state == 1):
                        idle "images/smartphone/music/music_playing_idle.webp"
                        action NullAction()
                    else:
                        idle "images/smartphone/music/music_play_idle.webp"
                        if(gamemusic.state == 2): #paused
                            action [PauseAudio("music", "toggle"), SetVariable("gamemusic.state", 1)]
                        else: #stopped
                            action [Play("music", gamemusic.currently_playing), SetVariable("gamemusic.state", 1)]
                    at musicbuttonszoom

                #pause button
                imagebutton:
                    if(gamemusic.state == 2): #paused
                        idle "images/smartphone/music/music_paused_idle.webp"
                        action NullAction()
                    else:
                        idle "images/smartphone/music/music_pause_idle.webp"
                        if(gamemusic.state == 0): #stopped
                            action NullAction()
                        else:
                            action [PauseAudio("music", "toggle"), SetVariable("gamemusic.state", 2)]
                    at musicbuttonszoom


                #stop button
                imagebutton:
                    if(gamemusic.state == 0): #stopped
                        idle "images/smartphone/music/music_stopped_idle.webp"
                        action NullAction()
                    else:
                        idle "images/smartphone/music/music_stop_idle.webp"
                        action [Stop("music"), SetVariable("gamemusic.state", 0)]
                    at musicbuttonszoom

        null height 20
        text ">> {u}[gamemusic.currently_playing_short]{/u} <<":
            xalign 0.5
        null height 20
        text "Music Volume:"
        bar value Preference("music volume") #at transform
            #xsize 800
        
        null height 20
        text "{u}Music:{/u}"
        viewport:
            mousewheel True
            scrollbars "vertical"
            draggable True
            xsize 800
            ysize 950
            spacing 10
            vbox:
                #xalign 0.5
                #yalign 0.3
                #xsize 800
                #for track in get_music():
                for track in smartphone.music_list:
                    textbutton(track[25:-4]):
                        action [SetVariable("gamemusic.currently_playing", track), SetVariable("gamemusic.currently_playing_short", track[25:-4]), SetVariable("gamemusic.state", 1), Play("music", track)]
                        #action [Function(set_music_variables(track)), Play("music", track)]


screen photo_view(photo):
    style_prefix "smartphone"
    viewport at phone_content_wide:
        draggable True
        mousewheel True
        scrollbars "both"
        vscrollbar_unscrollable "hide"
        scrollbar_unscrollable "hide"

        imagebutton:
            idle "images/smartphone/photos/" + photo.file + ".webp"
            if(not smartphone.photo_full):
                if photo.vertical:
                    at phone_photo_vertical
                    ypadding 30
                    xpadding 1300
                else:
                    at phone_photo_horizontal
                    ypadding 500
                    xpadding 25
            mouse "default"
            action NullAction()

    hbox:
        xalign 0.75
        yalign 0.1

        if(not smartphone.photo_full):
            imagebutton:
                at phone_photo_zoom_button
                auto "images/smartphone/set_wallpaper_%s.webp"
                action [SetVariable("smartphone.current_bg", photo.file), Notify("Wallpaper changed")]

        imagebutton:
            at phone_photo_zoom_button
            if smartphone.photo_full:
                auto "images/smartphone/stop_fullscreen_%s.webp"
                action SetVariable("smartphone.photo_full", False)
            else:
                auto "images/smartphone/start_fullscreen_%s.webp"
                action SetVariable("smartphone.photo_full", True)


screen gallery():
    style_prefix "smartphone"
    #text "Wallpapers" at phone_title
    vpgrid at phone_content_wide_gallery:
        draggable True
        mousewheel True
        ymaximum 1752

        #grid 3 4:
        cols 4

        top_margin 40
        spacing 40


        #for i in range(len(smartphone.photos)):
        for p in reversed(smartphone.photos):
            imagebutton:
                idle "images/smartphone/photos/thumbnails/" + p.file + ".webp"
                hover Composite((500,500), (0,0), "images/smartphone/photos/thumbnails/" + p.file + ".webp", (0,0), "images/smartphone/camera/photo_preview_overlay.webp")
                #action NullAction()
                action Function(smartphone_screen_push, "photo_view", photo=p)


screen settings():
    style_prefix "smartphone"
    #text "Settings" at phone_title_small
    viewport at phone_content_wide:
        #area 800, 370, 2500, 1400

        vbox:
            xfill True
            #yfill True
            spacing 30
            null width 30
            hbox:
                spacing 40
                text "Enable Quick Menu:"
                if quick_menu:
                    imagebutton:
                        auto "images/smartphone/checkmark_filled_%s.webp"
                        at settingszoom_small
                        action [SetVariable("quick_menu", False), SetVariable("quick_menu_pref_hidden", True)]
                else:
                    imagebutton:
                        auto "images/smartphone/checkmark_empty_%s.webp"
                        at settingszoom_small
                        action [SetVariable("quick_menu", True), SetVariable("quick_menu_pref_hidden", False)]

            hbox:
                text _("Quick Menu Position:")
                null width 40
                if(actualgame.quickmenuxalign == 0.0):
                    imagebutton:
                        idle "images/smartphone/align_left_active_idle.webp"
                        #hover "images/smartphone/align_left_hover.webp"
                        at settingszoom_small
                        mouse "default"
                        action NullAction()
                else:
                    imagebutton:
                        auto "images/smartphone/align_left_%s.webp"
                        at settingszoom_small
                        action SetVariable("actualgame.quickmenuxalign", 0.0)

                if(actualgame.quickmenuxalign == 0.5):
                    imagebutton:
                        idle "images/smartphone/align_center_active_idle.webp"
                        at settingszoom_small
                        mouse "default"
                        action NullAction()
                else:
                    imagebutton:
                        auto "images/smartphone/align_center_%s.webp"
                        at settingszoom_small
                        action SetVariable("actualgame.quickmenuxalign", 0.5)

                if(actualgame.quickmenuxalign == 1.0):
                    imagebutton:
                        idle "images/smartphone/align_right_active_idle.webp"
                        at settingszoom_small
                        mouse "default"
                        action NullAction()
                else:
                    imagebutton:
                        auto "images/smartphone/align_right_%s.webp"
                        at settingszoom_small
                        action SetVariable("actualgame.quickmenuxalign", 1.0)

            hbox:
                spacing 40
                text "Extra Symbols:"
                if actualgame.extra_symbols == True:
                    imagebutton:
                        auto "images/smartphone/checkmark_filled_%s.webp"
                        action SetVariable("actualgame.extra_symbols", False)
                        at settingszoom_small
                else:
                    imagebutton:
                        auto "images/smartphone/checkmark_empty_%s.webp"
                        action SetVariable("actualgame.extra_symbols", True)
                        at settingszoom_small

            vbox:
                spacing 20
                hbox:
                    xfill True
                    spacing 40
                    text _("Wallpaper brightness:")
                    text str(int(smartphone.overlay_opacity*100)) + "%":
                        xalign 1.0
                bar value VariableValue("smartphone.overlay_opacity", 1.0, step=0.05, style="slider"):
                    #xsize 1000
                    xfill True
            vbox:
                xfill True
                spacing 20
                hbox:
                    xfill True
                    spacing 50
                    text _("Dialogue Box opacity:")
                    text str(int(actualgame.dialogueBoxOpacity*100)) + "%":
                        xalign 1.0
                bar value VariableValue("actualgame.dialogueBoxOpacity", 1.0, step=0.05, style="slider"):
                    #xsize 1000
                    xfill True

            hbox:
                spacing 40
                text "12 hour clock:"
                if smartphone.clock24hours:
                    imagebutton:
                        auto "images/smartphone/checkmark_empty_%s.webp"
                        at settingszoom_small
                        action Function(switch_12_hour_clock, True)
                else:
                    imagebutton:
                        auto "images/smartphone/checkmark_filled_%s.webp"
                        at settingszoom_small
                        action Function(switch_12_hour_clock, False)

            if(not "small" in config.variants):
                hbox:
                    spacing 40
                    text "Increase HUD size:"
                    if actualgame.increase_hud_size:
                        imagebutton:
                            auto "images/smartphone/checkmark_filled_%s.webp"
                            at settingszoom_small
                            action SetVariable("actualgame.increase_hud_size", False)
                    else:
                        imagebutton:
                            auto "images/smartphone/checkmark_empty_%s.webp"
                            at settingszoom_small
                            action SetVariable("actualgame.increase_hud_size", True)

            textbutton ("App Settings"):
                xalign 0.5
                action Function(smartphone_screen_push, "app_settings")



screen app_settings():
    viewport at phone_content_wide:
        draggable True
        mousewheel True
        scrollbars "vertical"

        vbox:
            xfill True
            text ("Messages App")
            add "images/smartphone/app_settings_bar.webp"

            text ("Demo:")

            vbox:
                spacing 10
                xsize 1469
                xalign 0.5
                if smartphone.date_divider_bar:
                    add "images/smartphone/date_divider_bar.webp":
                        ypos +70
                else:
                    null height 20

                frame:
                    if(smartphone.date_divider_pos == "left"):
                        xalign 0.1
                    if(smartphone.date_divider_pos == "center"):
                        xalign 0.5
                    if(smartphone.date_divider_pos == "right"):
                        xalign 0.9
                    background Frame("images/smartphone/msgboxes/phonemsg10.webp", 50,50)
                    padding (40,20)
                    if smartphone.date_divider_upper:
                        text "YESTERDAY":
                            size 50
                    else:
                        text "yesterday":
                            size 50

                frame:
                    padding (40,20)
                    #background Frame("images/smartphone/msgboxes/phonemsg32.webp", 50,50)
                    background Frame (smartphone.msg_their_box, 50,50)
                    xpos 0.0
                    xmaximum 1250
                    text ("This is what received messages look like."):
                        style "smartphone_msg_text"

                frame:
                    padding (40,20)
                    #background Frame("images/smartphone/msgboxes/phonemsg33.webp", 50,50)
                    background Frame (smartphone.msg_your_box, 50,50)
                    xalign 1.0
                    xmaximum 1250
                    text("This is what your messages look like."):
                        style "smartphone_msg_text"

            null height 50

            vbox:
                spacing 10
                text ("Their message color:")
                hbox:
                    spacing 10
                    for msgbox in get_msgboxes_list():
                        imagebutton:
                            if(smartphone.msg_their_box == msgbox):
                                idle Composite((200,200), (0,0), msgbox, (0,0), "images/smartphone/msgbox_selected.webp")
                                mouse "default"
                            else:
                                idle msgbox
                            action SetVariable("smartphone.msg_their_box", msgbox)

                text ("Your message color:")
                hbox:
                    spacing 10
                    for msgbox in get_msgboxes_list():
                        imagebutton:
                            if(smartphone.msg_your_box == msgbox):
                                idle Composite((200,200), (0,0), msgbox, (0,0), "images/smartphone/msgbox_selected.webp")
                                mouse "default"
                            else:
                                idle msgbox
                            action SetVariable("smartphone.msg_your_box", msgbox)

                null height 20

                text ("Date Divider")
                vbox:
                    xfill True
                    hbox:
                        spacing 20
                        xalign 0.5
                        textbutton ("Lowercase"):
                            if not smartphone.date_divider_upper:
                                text_underline True
                            action SetVariable("smartphone.date_divider_upper", False)
                        textbutton ("Uppercase"):
                            if smartphone.date_divider_upper:
                                text_underline True
                            action SetVariable("smartphone.date_divider_upper", True)

                        null width 50

                        textbutton ("Bar"):
                            if smartphone.date_divider_bar:
                                text_underline True
                            action SetVariable("smartphone.date_divider_bar", True)

                        textbutton ("No Bar"):
                            if not smartphone.date_divider_bar:
                                text_underline True
                            action SetVariable("smartphone.date_divider_bar", False)

                    null height 50

                    hbox:
                        spacing 20
                        xalign 0.5
                        textbutton ("Left"):
                            if(smartphone.date_divider_pos == "left"):
                                text_underline True
                            action SetVariable("smartphone.date_divider_pos", "left")

                        textbutton ("Center"):
                            if(smartphone.date_divider_pos == "center"):
                                text_underline True
                            action SetVariable("smartphone.date_divider_pos", "center")

                        textbutton ("Right"):
                            if(smartphone.date_divider_pos == "right"):
                                text_underline True
                            action SetVariable("smartphone.date_divider_pos", "right")

            null height 200




screen stats():
    style_prefix "smartphone"
    #text "Stats" at phone_title_small
    #add "images/smartphone/phone_app_overlay.webp"
    #add "images/smartphone/phone_app_overlay_top.webp"
    viewport at phone_content_wide_left:
        #area 700, 370, 2500, 1400
        draggable True
        mousewheel True

        vbox:
            #style "smartphone_area_small"
            #xsize 1200
            xfill True
            #yfill True
            xalign 0.5
            spacing 75

            hbox:
                xfill True
                text "{u}" + person_get_name('Eileen') + "{/u}"
                hbox:
                    xalign 1.0
                    text _("$")
                    text str(protagonist.get_stat(Stats.MONEY))

            null height 20

            vbox:
                spacing 10
                xfill True
                hbox:
                    xfill True
                    text _("Self-Confidence:")
                    text "[protagonist.confidence]":
                        xalign 1.0
                bar value StaticValue(value=protagonist.confidence, range=10)

            vbox:
                spacing 10
                xfill True
                hbox:
                    xfill True
                    text _("Fitness:")
                    text "[protagonist.fitness]":
                        xalign 1.0
                bar value StaticValue(value=protagonist.fitness, range=10)

            vbox:
                spacing 10
                xfill True
                hbox:
                    xfill True
                    text _("Motivation:")
                    text str(protagonist.get_stat(Stats.LUST_ENERGY)):
                        xalign 1.0
                bar value StaticValue(value=protagonist.get_stat(Stats.LUST_ENERGY), range=10)

            vbox:
                spacing 10
                xfill True
                hbox:
                    xfill True
                    text _("Intelligence:")
                    text str(protagonist.get_stat(Stats.HORNY)):
                        xalign 1.0
                bar value StaticValue(value=protagonist.get_stat(Stats.HORNY), range=10)

            # vbox:
            #     spacing 10
            #     xfill True
            #     hbox:
            #         xfill True
            #         text _("Fighting Ability:")
            #         text "[protagonist.fight]":
            #             xalign 1.0
            #     bar value StaticValue(value=protagonist.fight, range=10)


    viewport at phone_content_wide_right:
        mousewheel True
        draggable True
        scrollbars "vertical"

        vbox:
            spacing 10
            for p_id in smartphone.contacts:
                frame:
                    #background Frame("images/smartphone/msgboxes/phonemsg31.webp", 50,50)
                    background Frame("gui/notify.png", 50,50)

                    padding (0,50)

                    has hbox:
                        #xfill True
                        xsize 1000
                        ysize 200
                        #spacing 20

                        imagebutton:
                            yalign 0.5
                            xpos 20
                            idle person_get_image(p_id)
                            at contactzoom_small
                            mouse "default"
                            action NullAction()
                            #action Function(set_current_contact, contact)

                        vbox:
                            text (person_get_name(p_id)):
                                yalign 0.5
                                #xpos -10
                                underline True
                                #action Function(set_current_contact, contact)

                            #text _("Relationship")
                            #text "[smartphone.small_selected_contact.relationship]/[smartphone.small_selected_contact.relationship_max]":
                            text "Relationship: [person_get_relationship(p_id)]/[RELATIONSHIP_MAX]":
                                size 80


screen tictactoe():
    style_prefix "smartphone"
    text "TicTacToe" at phone_title
    vbox:
        xalign 0.5
        yalign 0.2
        hbox:
            spacing 20
            text "Winner:"
            if(tictactoe.winner == 1):
                text "X"
            elif(tictactoe.winner == 2):
                text "O"
            else:
                text "-"

    grid 3 3:
        xalign 0.5
        yalign 0.4
        spacing 20
        $ counter = 0
        for field in tictactoe.game:
            if(field == 0):
                if(tictactoe.winner == 0):
                    imagebutton:
                        auto "images/smartphone/games/tictactoe_empty_%s.webp" at iconzoom
                        #action [Function(set_tictactoe, counter), Function(check_tictactoe_winner_no_return), Function(tictactoe_ai)]
                        action [Function(set_tictactoe, counter), Function(tictactoe_ai)]
                else:
                    imagebutton:
                        idle "images/smartphone/games/tictactoe_empty_idle.webp" at iconzoom
                        action NullAction()
            elif(field == 1):
                imagebutton:
                    auto "images/smartphone/games/tictactoe_cross_%s.webp" at iconzoom
                    action NullAction()
            elif(field == 2):
                imagebutton:
                    auto "images/smartphone/games/tictactoe_circle_%s.webp" at iconzoom
                    action NullAction()
            $ counter += 1
    text "[tictactoe.game]"
    textbutton("Reset"):
        xalign 0.5
        yalign 0.8
        action Function(reset_tictactoe)


screen games():
    style_prefix "smartphone"
    text "Games" at phone_title
    vbox at phone_content:
        hbox:
            textbutton("TicTacToe") action Function(smartphone_screen_push, "tictactoe") #action [Hide("games"), Show("tictactoe")]


screen answer_options(contact, msg):
    style_prefix "smartphone"
    frame:
        background Frame("images/smartphone/msgboxes/phonemsg32.webp", 50,50,50,50)
        xalign 0.85
        yalign 0.7
        hbox:
            null width 50
            vbox:
                if("small" in config.variants):
                    text _("{size=100}{u}Choose your answer:{/u}{/size}")
                else:
                    text _("{u}Choose your answer:{/u}")
                null height 50
                spacing 30
                #for option in msg.answer_options.player_answers:
                for option in msg.answer_options:
                    frame:
                        padding (20,20)
                        background Frame("images/smartphone/msgboxes/phonemsg33.webp", 50,50,50,50)
                        #textbutton (option[0].content) action Function(handle_new_answer, msg, option)
                        textbutton (get_conversation_by_id(option).messages[0].content):
                            action [Function(handle_new_answer, contact, msg, option), Hide("answer_options")]
                null height 50
            null width 50


screen messages():
    style_prefix "smartphone"
    viewport at phone_msg_content_wide_left:
        mousewheel True
        draggable True

        vbox:
            for p_id in smartphone.msg_contacts:
                frame:
                    ysize 260
                    xsize 740

                    if(messages[p_id].unread):
                        if(smartphone.hovered_contact == p_id):
                            background Frame("images/smartphone/messages_frame_unread_hover.webp", 50,50)
                        else:
                            background Frame("images/smartphone/messages_frame_unread.webp", 50,50)
                    else:
                        if(smartphone.hovered_contact == p_id):
                            background Frame("images/smartphone/messages_frame_hovered.webp", 50,50)
                        else:
                            background Frame("images/smartphone/messages_frame.webp", 50,50)

                    hbox:
                        ypos -10
                        vbox:
                            yfill True
                            xsize 120

                            imagebutton:
                                #xsize 200
                                yfill True
                                xalign 0.5
                                yalign 0.5
                                idle person_get_small_image(p_id)
                                hovered SetVariable("smartphone.hovered_contact", p_id)
                                unhovered SetVariable("smartphone.hovered_contact", None)
                                action [Function(set_read, p_id), SetVariable("smartphone.selected_contact", p_id), Function(reset_message_screen)]
                        vbox:
                            ypos -20
                            xfill True
                            hbox:
                                xfill True
                                if person_is_unknown(p_id):
                                    textbutton ("Unknown"):
                                        if(smartphone.hovered_contact == p_id):
                                            text_color gui.hover_color
                                        xfill True
                                        text_bold True
                                        text_kerning 7
                                        hovered SetVariable("smartphone.hovered_contact", p_id)
                                        unhovered SetVariable("smartphone.hovered_contact", None)
                                        action [Function(set_read, p_id), SetVariable("smartphone.selected_contact", p_id), Function(reset_message_screen)]
                                else:
                                    textbutton person_get_display_name(p_id):
                                        if(smartphone.hovered_contact == p_id):
                                            text_color gui.hover_color
                                        xfill True
                                        text_bold True
                                        text_kerning 7
                                        hovered SetVariable("smartphone.hovered_contact", p_id)
                                        unhovered SetVariable("smartphone.hovered_contact", None)
                                        action [Function(set_read, p_id), SetVariable("smartphone.selected_contact", p_id), Function(reset_message_screen)]

                                if messages[p_id].unread:
                                    add "images/smartphone/message_unread_marker.webp" yalign 0.5 xpos -100

                            if(not messages[p_id].last_message is None):
                                #manipulate_text_in_brackets_dict
                                textbutton (manipulate_text_in_brackets_dict([messages[p_id].get_last_message_content(55)])[0]):
                                    style_prefix "smartphone_last_msg"
                                    xpos +20
                                    #xsize 550
                                    xfill True
                                    ysize 100
                                    ypos -10
                                    hovered SetVariable("smartphone.hovered_contact", p_id)
                                    unhovered SetVariable("smartphone.hovered_contact", None)
                                    action [Function(set_read, p_id), SetVariable("smartphone.selected_contact", p_id), Function(reset_message_screen)]

    use msg_chain


screen msg_chain():
    vbox at phone_msg_content_wide_right:
        if(smartphone.selected_contact is None):
            null height 100
        else:
            $ set_read(smartphone.selected_contact)
            $ reset_msg_age()
            vbox:
                xfill True

                frame:
                    background Frame("images/smartphone/msg_chain_top_frame.webp", 50,50)
                    xfill True
                    xpadding 50

                    hbox:
                        xfill True
                        ysize 100

                        hbox:
                            xalign 0.0
                            spacing 30
                            add person_get_image(smartphone.selected_contact) at contactzoom
                            if person_is_unknown(smartphone.selected_contact):
                                text "Unknown":
                                    yalign 0.5
                            else:
                                text person_get_display_name(smartphone.selected_contact):
                                    yalign 0.5


                hbox:
                    xfill True
                    null width 30

                    viewport id "msg_chain":
                        mousewheel True
                        draggable True
                        #yadjustment initialize_adjustment(smartphone.selected_contact)
                        yadjustment initialize_adjustment()

                        vbox:
                            xfill True
                            spacing 10

                            null height 20

                            if smartphone.date_divider_bar:
                                add "images/smartphone/date_divider_bar.webp":
                                    ypos +70
                            else:
                                null height 20
                            frame:
                                if(smartphone.date_divider_pos == "left"):
                                    xalign 0.1
                                if(smartphone.date_divider_pos == "center"):
                                    xalign 0.5
                                if(smartphone.date_divider_pos == "right"):
                                    xalign 0.9
                                background Frame("images/smartphone/msgboxes/phonemsg10.webp", 50,50)
                                padding (40,20)
                                text get_msg_age_text(messages[smartphone.selected_contact].messages[0]):
                                    size 50
                                $ set_msg_divider_age(messages[smartphone.selected_contact].messages[0])


                            for msg in messages[smartphone.selected_contact].messages:
                                if put_day_divider(msg):
                                    null height 20

                                    if smartphone.date_divider_bar:
                                        add "images/smartphone/date_divider_bar.webp":
                                            ypos +70
                                    else:
                                        null height 20
                                    frame:
                                        if(smartphone.date_divider_pos == "left"):
                                            xalign 0.1
                                        if(smartphone.date_divider_pos == "center"):
                                            xalign 0.5
                                        if(smartphone.date_divider_pos == "right"):
                                            xalign 0.9
                                        background Frame("images/smartphone/msgboxes/phonemsg10.webp", 50,50)
                                        padding (40,20)
                                        text get_msg_age_text(msg):
                                            size 50

                                frame:
                                    padding (40,20)
                                    if(msg.author_id == "Eileen"):
                                        #background Frame("images/smartphone/msgboxes/phonemsg33.webp", 50,50)
                                        background Frame(smartphone.msg_your_box, 50,50)
                                        xalign 1.0
                                    else:
                                        #background Frame("images/smartphone/msgboxes/phonemsg32.webp", 50,50)
                                        background Frame(smartphone.msg_their_box, 50,50)
                                        xpos 0.0
                                    xmaximum 1250

                                    vbox:
                                        if(not msg.img is None) and (renpy.loadable("images/smartphone/photos/thumbnails/" + msg.img + ".webp")):
                                            hbox:
                                                imagebutton:
                                                    padding (20,20)
                                                    idle "images/smartphone/photos/thumbnails/" + msg.img + ".webp"
                                                    hover Composite((500,500), (0,0), "images/smartphone/photos/thumbnails/" + msg.img + ".webp", (0,0), "images/smartphone/camera/photo_preview_overlay.webp")
                                                    #action Function(smartphone_screen_push, "photo_view", contact, msg.img, msg.vertical, msg.wallpaper)
                                                    action Function(smartphone_screen_push, "photo_view", photo=Photo(msg.img, msg.vertical))
                                                    xalign 0.5
                                                #text("[msg.content]"):
                                                text(manipulate_text_in_brackets_dict([msg.content])[0]):
                                                    style "smartphone_msg_text"
                                                    if(msg.author_id == "Eileen"):
                                                        text_align 0.0
                                                    else:
                                                        text_align 0.0
                                        else:
                                        #if(not msg.content == ""):
                                            #text("[msg.content]"):
                                            text(manipulate_text_in_brackets_dict([msg.content])[0]):
                                                style "smartphone_msg_text"
                                                if(msg.author_id == "Eileen"):
                                                    text_align 0.0
                                                else:
                                                    text_align 0.0

                                if(msg == messages[smartphone.selected_contact].last_message):

                                    # add to contacts button
                                    if person_is_unknown(smartphone.selected_contact):
                                        frame:
                                            padding (20,20)
                                            background Frame("images/smartphone/msgboxes/phonemsg33.webp", 50,50,50,50)
                                            xalign 1.0
                                            hbox:
                                                null width 100
                                                textbutton _("Add to contacts"):
                                                    #text_hover_color "#000000"
                                                    action Function(contacts_add, smartphone.selected_contact)
                                                null width 100

                                    elif((not msg.answer_options is None) and (not msg.answered)):
                                        # choose answer button
                                        if(not smartphone.choosing_answer):
                                            frame:
                                                padding (20,20)
                                                background Frame("images/smartphone/msgboxes/phonemsg33.webp", 50,50,50,50)
                                                xalign 1.0
                                                hbox:
                                                    null width 100
                                                    textbutton ("choose answer..."):
                                                        #text_hover_color "#000000"
                                                        action [SetVariable("smartphone.choosing_answer", True), Function(scroll_down, smartphone.selected_contact)]
                                                    null width 100

                                        # actual answer options
                                        else:
                                            frame:
                                                background Frame("images/smartphone/msgboxes/phonemsg32.webp", 50,50,50,50)
                                                #xsize 780
                                                xfill True
                                                hbox:
                                                    vbox:
                                                        xfill True
                                                        spacing 30
                                                        text _("Choose your answer:"):
                                                            underline True
                                                            if("small" in config.variants):
                                                                size 100
                                                        for option in msg.answer_options:
                                                            frame:
                                                                padding (20,20)
                                                                xalign 0.5
                                                                background Frame("images/smartphone/msgboxes/phonemsg33.webp", 50,50,50,50)
                                                                textbutton manipulate_text_in_brackets_dict([get_conversation_by_id(option).messages[0].content]):
                                                                    #text_hover_color "#000000"
                                                                    action [Function(handle_new_answer, smartphone.selected_contact, msg, option), SetVariable("smartphone.choosing_answer", False)]

                    null width 100


screen call_confirmation():
    modal True

    add "images/smartphone/darken.webp"

    vbox:
        xalign 0.5
        yalign 0.5

        frame:
            #background Frame("images/smartphone/msg_chain_top_frame.webp", 50,50)
            background Frame("gui/notify.png", 50,50)
            padding (50,50)

            vbox:
                spacing 20
                text "Do you want to call " + person_get_name(smartphone.selected_contact) + "?"

                hbox:
                    xalign 0.5
                    spacing 50

                    imagebutton:
                        idle "images/smartphone/take_call_green.webp"
                        at take_call_icon_zoom
                        action [SetVariable("actualgame.callee_id", smartphone.selected_contact), Jump("phonecalls_base")]

                    imagebutton:
                        idle "images/smartphone/take_call_red.webp"
                        at take_call_icon_zoom
                        action Hide("call_confirmation")


