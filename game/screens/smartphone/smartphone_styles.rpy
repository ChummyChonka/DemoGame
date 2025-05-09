style smartphone_area_small:
    area (700, 400, 2500, 1400)

style smartphone_link:
    mouse "button"
    color "#00FF00"

style smartphone_text:
    font "gui/fonts/Outfit-VariableFont_wght.ttf"
    size 100

style smartphone_smaller_button_text is smartphone_text:
    hover_color gui.hover_color
    idle_color "#FFFFFF"
    outlines [ (absolute(1), "#000", absolute(1), absolute(1)) ]
    size 75

style smartphone_smaller_button_text_hovered is smartphone_smaller_button_text:
    hover_color "#FFFFFF"


style smartphone_button_text is smartphone_text:
    hover_color gui.hover_color
    idle_color "#FFFFFF"


style smartphone_textinput_button_text is smartphone_button_text:
    size 200

style smartphone_textinput_input:
    size 200

style smartphone_textinput_text:
    size 200



style smartphone_button:
    background None

style smartphone_textbutton_small:
    size 60
    color "#cccccc"


style smartphone_button_contacts:
    background "#b23941"
    hover_background "#D33F49"
    insensitive_background "#444"
    padding (30,15)
    xsize 300

style smartphone_button_contacts_disabled is smartphone_button_contacts:
    background "#4f4f4f"

style smartphone_button_contacts_green is smartphone_button_contacts:
    background "#00a100"
    hover_background "#00c500"

style smartphone_button_contacts_text:
    xalign 0.5

style smartphone_button_contacts_green_text is smartphone_button_contacts_text
style smartphone_button_contacts_disabled_text is smartphone_button_contacts_text


# GUIDE APP
#####################################
style smartphone_guide_text is smartphone_text

style smartphone_guide_button:
    xpadding 50

style smartphone_guide_button_text is smartphone_text

style smartphone_guide_button_text is smartphone_text:
    variant "small"
    size 100



style smartphone_button_inactive:
    mouse "default"

style smartphone_widget:
    color "#ffffff"
    #textshader "linetexture"
    outlines [ (absolute(2), "#000", absolute(2), absolute(2)) ]
    size 200

style smartphone_weather_widget_text is smartphone_widget:
    outlines [ (absolute(3), "#000", absolute(3), absolute(3)) ]

style smartphone_stats_bar:
    #xsize 500
    xalign 1.0

style smartphone_msg_text is smartphone_text:
    prefer_emoji True
    size 66
    color "#ffffff"

style smartphone_msg_text is smartphone_text:
    variant "small"
    prefer_emoji True
    size 80
    color "#ffffff"

style smartphone_last_msg:
    prefer_emoji True
    size 45
    color "#cccccc"
    #justify True
    #line_spacing -10
    kerning +1

style smartphone_last_msg_button_text is smartphone_last_msg


style debug_small_text:
    size 40

style debug_small_button_text:
    size 40


style smartphonesettings_text is smartphone_text:
    size 60

style smartphonemusic_text is smartphone_text:
    size 60

style smartphonemusic_button_text is smartphonemusic_text


style name_changer:
    yalign 0.5

style name_changer:
    variant "small"
    yalign 0.1

