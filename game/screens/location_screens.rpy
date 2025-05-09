init python:
    def hide_all_location_screens():
        renpy.suspend_rollback(False)
        config.rollback_enabled = True
        renpy.hide_screen("sublocation_navigation")
        renpy.hide_screen("navigation_button")
        location_stop_sound()


    def location_stop_sound():
        renpy.sound.stop(fadeout=1.0)


    # returns a list of persons which can appear in a certain major location
    def get_location_chars(major_location: Location) -> list:
        if(major_location == Location.GYM):
            return ["Emily", "Harper", "Olivia"]
        elif(major_location == Location.UNI):
            return ["Aster", "Victoria"]
        elif(major_location == Location.MOMS):
            return ["Sophia", "Christopher", "Isabella", "Laura"]
        return list()


    # returns list of persons who are currently in a given sublocation
    def get_sublocation_chars(sublocation: Location) -> list:
        sublocation_char_list = list()
        for c in get_location_chars(get_major_location_by_sublocation(sublocation)):
            if(person_is_char_in(c, sublocation)):
                sublocation_char_list.append(c)
        return sublocation_char_list


    def get_sublocations(major_location: Location) -> dict:
        if(major_location is None):
            return dict()
        elif(major_location == Location.HOME):
            return {"Downstairs" : [Location.HOME_DOWNSTAIRS, "home_downstairs"],
                    "Upstairs" : [Location.HOME_UPSTAIRS, "home_upstairs"],
                    "Bathroom" : [Location.HOME_BATHROOM, "home_bathroom"]
                    }
        elif(major_location == Location.MOMS):
            return {
                    "Living Room" : [Location.MOMS_FIRSTFLOOR, "moms_first_floor"],
                    "Pool" : [Location.MOMS_POOL, "moms_pool"],
                    "Sundeck" : [Location.MOMS_SUNDECK, "moms_sundeck"],
                    "Chris's Room" : [Location.MOMS_DAD, "moms_serverroom"],
                    "Master Bedroom" : [Location.MOMS_MASTER, "moms_master_bedroom"],
                    "Bathroom" : [Location.MOMS_BATHROOM, "moms_bathroom"],
                    "Guestroom" : [Location.MOMS_GUEST, "moms_guestroom"]
                }
        elif(major_location == Location.GYM):
            locations = {
                    "Reception" : [Location.GYM_RECEPTION, "gym_reception"],
                    "Locker Room" : [Location.GYM_LOCKERROOM, "gym_lockerroom"],
                    "Gym" : [Location.GYM_ACTUAL, "gym_actual"]
                }
            locations["Yoga Studio"] = [Location.GYM_YOGA, "gym_yoga_studio"]
            locations["Toilet"] = [Location.GYM_TOILET, "gym_toilet"]
            locations["Office"] = [Location.GYM_OFFICE, "gym_office"]
            locations["Sauna"] = [Location.GYM_SAUNA, "gym_sauna"]
            locations["Showers"] = [Location.GYM_SHOWERS, "gym_showers"]
            return locations
        elif(major_location == Location.UNI) or (major_location == Location.DORMS):
                return {
                    "Main Hall" : [Location.UNI_MAIN, "location_uni"],
                    "Lecture Hall" : [Location.UNI_LECTURE, "uni_lecturehall"],
                    "Dorms" : [Location.DORMS, "location_dorms"]
                }

        return dict()


    def do_sublocation_button(loc=None):
        renpy.suspend_rollback(False)
        config.rollback_enabled = True
        renpy.hide("actions_default")
        renpy.hide_screen("sublocation_navigation")
        location_stop_sound()
        if(not loc is None):
            renpy.jump(loc)
        renpy.show_screen("navigation_button")


    def show_sublocation_navigation():
        renpy.suspend_rollback(True)
        config.rollback_enabled = False
        #renpy.transition(move_in_top)
        renpy.show_screen("sublocation_navigation")
        renpy.hide_screen("navigation_button")
        #pixellate(old_widget="navigation_button", new_widget="sublocation_navigation")



# Locations Screens
####################################

transform sublocation_navigation:
    xpos 450
    ypos 50

transform offscreentop:
    xpos 450
    ypos -500

define move_in_top = MoveTransition(delay=1.0, enter=offscreentop)


transform location_button_default:
    zoom 1.3

transform location_button_zoom:
    zoom 2.0

transform navigation_button:
    zoom 0.5
    ypos -25

style locations_button_text:
    color "#FFFFFF"
    hover_color gui.hover_color

style locations_button:
    background Solid("#000000")

style location_tooltip:
    size 100
    #kerning 50
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

style sublocation_navigation_button_text:
    color "#FFFFFF"
    hover_color "#e06666"
    outlines [(absolute(2), "#000000", absolute(0), absolute(0))]


style sublocation_navigation_button_text:
    variant "small"
    size 65


screen sublocation_navigation():
    #modal True
    zorder 101
    style_prefix "sublocation_navigation"

    #add "images/smartphone/darken.webp" alpha 0.8
    #add renpy.get_showing_tags(sort=True)[0] at kawase_blur_darken

    textbutton "":
        xsize 3840
        ysize 2160
        mouse "default"
        action Function(do_sublocation_button)

    use navigation_button

    frame:
        #background Frame("images/locations/actions/actions_frame_bg.webp", 50,50)
        background Frame("gui/notify.png", 50,50)
        #xalign 0.5
        xpos 500
        ypos 50
        yminimum 685
        xminimum 560

        $ num_cols = min(5, len(get_sublocations(person_get_current_major_location("Eileen"))))

        vpgrid:
            cols num_cols

            for k,v in get_sublocations(person_get_current_major_location("Eileen")).items():
                vbox:
                    xsize 550
                    ysize 550
                    null height 25

                    textbutton "[k]":
                        xsize 500
                        xalign 0.5
                        text_align (0.5, 0.5)
                        if(actualgame.location_hovered == v[1]):
                            text_color gui.hover_color
                        hovered SetVariable("actualgame.location_hovered", v[1])
                        unhovered SetVariable("actualgame.location_hovered", None)
                        action Function(do_sublocation_button, v[1])


                    hbox:
                        #xfill True
                        #yfill True
                        null width 25

                        frame:
                            if(renpy.loadable("images/locations/icons/" + v[1] + "_frame.webp")):
                                if(actualgame.location_hovered == v[1]):
                                    background Composite(
                                        (500, 500),
                                        (0, 0), "images/locations/icons/" + v[1] + "_frame.webp",
                                        (0, 0), "images/locations/icons/frame_border3.webp"
                                        )
                                else:
                                    background Composite(
                                        (500, 500),
                                        (0, 0), "images/locations/icons/" + v[1] + "_frame.webp",
                                        (0, 0), "images/locations/icons/frame_border2.webp"
                                        )
                                    #background Frame("images/locations/icons/" + v[1] + "_frame.webp", 50,50)
                            else:
                                background Frame("images/locations/icons/placeholder_frame.webp", 50,50)
                            #xfill True
                            #yfill True
                            xsize 500
                            ysize 500
                            # imagebutton:
                            #     idle "images/locations/icons/frame_empty.webp"
                            #     hover "images/locations/icons/frame_border.webp"
                            #     action NullAction()
                            textbutton (""):
                                xsize 500
                                ysize 500
                                xpos -35
                                ypos -15
                                hovered SetVariable("actualgame.location_hovered", v[1])
                                unhovered SetVariable("actualgame.location_hovered", None)
                                action Function(do_sublocation_button, v[1])

                            vbox:
                                xfill True
                                yfill True

                                if(len(get_sublocation_chars(v[0])) > 0):
                                    frame:
                                        background Frame("images/locations/actions/actions_frame_bg.webp", 50,50)
                                        xsize 475
                                        #ysize 100
                                        ypos 300

                                        hbox:
                                            for p in get_sublocation_chars(v[0]):
                                                imagebutton:
                                                    xsize 500
                                                    idle person_get_image(p)
                                                    at contactzoom
                                                    hovered SetVariable("actualgame.location_hovered", v[1])
                                                    unhovered SetVariable("actualgame.location_hovered", None)
                                                    #tooltip p.name
                                                    action NullAction()
                                                    #ysize 100
                                                    #textbutton(p.name):
                                                    #    xalign 0.5
                                                    #xsize 75
                                                    #text_xalign 0.5
                                                    #background c

                        null width 25

                    null height 25

    # $ tooltip = GetTooltip()
    # if tooltip:
    #     nearrect:
    #         focus "tooltip"
    #         prefer_top True

    #         vbox:
    #             xalign 0.5
    #             text tooltip


transform navigation_button_zoom:
    zoom 0.8

screen navigation_button():
    hbox:
        style_prefix "locations"
        xalign 0.02
        yalign 0.02
        #textbutton("Map"):

        imagebutton:
            tooltip "Map"
            at navigation_button_zoom
            #idle Composite((200,200), (0,0), "images/locations/icons/map.webp", (0,0), "images/locations/icons/map_border_idle.webp")
            #hover Composite((200,200), (0,0), "images/locations/icons/map.webp", (0,0), "images/locations/icons/map_border_hover.webp")
            auto "images/locations/icons/navigation_button_%s.webp"
            action Jump("main_game")

        if(len(get_sublocations(person_get_current_major_location("Eileen"))) > 0):
            imagebutton:
                if(renpy.get_screen("sublocation_navigation")):
                    auto "images/locations/icons/locations_arrow_up_%s.webp"
                    action Function(do_sublocation_button)
                else:
                    auto "images/locations/icons/locations_arrow_%s.webp"
                    action Function(show_sublocation_navigation)
                at navigation_button


screen location_header_buttons(args):
    $ locations = args[0]
    if(len(args) == 2):
        $ chars = args[1]
    else:
        $ chars = dict()

    vbox:
        style_prefix "locations"
        xfill True

        hbox:
            xalign 0.5
            #spacing 20
            for k,v in locations.items():
                vbox:
                    # textbutton(k) action [Function(location_stop_sound), Jump(v[1])]:
                    #     if(v[0] == actualgame.current_location):
                    #         text_color gui.hover_color
                    #xsize 250

                    #null height 10
                    xsize 250

                    imagebutton:
                        #idle "images/locations/icons/" + v[1] + ".webp"
                        #idle Composite((200,200), (0,0), "images/locations/icons/" + v[1] + ".webp", (0,0), "images/locations/icons/border_idle.webp")
                        if(renpy.loadable("images/locations/icons/" + v[1] + ".webp")):
                            idle "images/locations/icons/" + v[1] + ".webp"
                        else:
                            idle "images/locations/icons/tester.webp"
                        hovered SetVariable("actualgame.location_hovered", v[1])
                        unhovered  SetVariable("actualgame.location_hovered", None)
                        if(actualgame.location_hovered == v[1]):
                            at location_button_zoom
                        else:
                            at location_button_default
                        #hover Composite((200,200), (0,0), "images/locations/icons/" + v[1] + ".webp", (0,0), "images/locations/icons/border_hover.webp")
                        tooltip k
                        xalign 0.5
                        action [Function(location_stop_sound), Jump(v[1])]
                    hbox:
                        for p,c in chars.items():
                            if(person_is_char_in(p, v[0])):
                                textbutton(p[:1]):
                                    xsize 75
                                    text_xalign 0.5
                                    background c

    $ tooltip = GetTooltip("location_header_buttons")
    if tooltip:
        nearrect:
            focus "tooltip"
            #prefer_top True

            vbox:
                xalign 0.5
                text tooltip:
                    style "location_tooltip"
                    # $ tooltip = GetTooltip()
                    # if(tooltip == k):
                    #     text "[tooltip]":
                    #         style "location_tooltip"
                    #         xalign 0.5




# Actions Screen
##########################################

style tooltip_text:
    outlines [(absolute(3), "#000000", absolute(0), absolute(0))]
    color "#ffffff"
    size 100


screen actions_default(args=None):
    #modal True

    #$ image = args[0]
    if(not args is None):
        $ tooltips = args[0]
        $ actions = args[1]
        $ do_function = args[2]

        if(len(actions) > 0):
            #add "[image]" 

            vbox:
                xalign 0.5
                ypos 1700
                #xsize 150*len(tooltips.keys())
                #ysize 350
                #ysize 200

                frame:
                    background Frame("images/locations/actions/actions_frame_bg.webp", 50,50)
                    ysize 350
                    #yfill True

                    hbox:
                        for k,v in actions.items():
                            # if(actualgame.daytime >= 4) and (not k in ["up", "out"]):
                            #     continue
                            vbox:
                                ypos -5
                                imagebutton:
                                    auto "images/locations/actions/actions_bg_%s.webp"
                                    tooltip tooltips[k]
                                    action [Hide("actions_default"), Function(do_function, k)]

                                add Image("images/locations/actions/" + v + ".svg", dpi=30):
                                    ypos -320
                                    xpos 20


    $ tooltip = GetTooltip("actions_default")
    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True

            vbox:
                style_prefix "tooltip"
                xalign 0.5
                text tooltip


