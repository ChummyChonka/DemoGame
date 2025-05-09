
#######################################
############ PHONECALLS ###############
#######################################
transform phonecall_loc:
    xpos 2500
    ypos 100

transform phonecall_wallpaper_loc:
    xpos 2580
    ypos 140
    xsize 706
    ysize 1744

transform phonecall_notification_bar_left:
    xpos 2590
    ypos 140

transform phonecall_notification_bar_right:
    xpos 3040
    ypos 145
    zoom 0.20



#######################################
############## GALLERY ################
#######################################
transform gallery_control_zoom:
    zoom 0.25

transform gallery_control_zoom_small:
    zoom 0.4

transform gallery_zoom:
    #zoom 0.5
    zoom 0.75

# transform gallery_zoom_small:
#     zoom 0.7

transform photo_zoom:
    zoom 0.9

transform photo_zoom_vertical:
    zoom 0.5

transform notification_zoom:
    zoom 0.05

transform photo_preview:
    crop (840,0,2160,2160)
    zoom 0.3

transform app_icon_zoom:
    zoom 1.3

#messages
transform msg_emoji:
    zoom 0.6

transform msg_emoji_old:
    zoom 0.1

transform msg_emoji_old_small:
    zoom 0.25

transform iconzoom:
    zoom 0.25

transform iconzoom_small:
    zoom 0.4

transform messagezoom:
    zoom 0.15

transform messagezoom_small:
    ypos -20
    zoom 0.3

transform messages_photo_small:
    zoom 2

#wallpapers
transform wallpaper_icon_zoom:
    zoom 0.2

# transform wallpaper_icon_zoom_small:
#     zoom 0.35

transform lust_energy_zoom:
    zoom 0.25

transform lust_energy_zoom_small:
    zoom 0.4

transform phonezoom:
    zoom 0.1

transform mobile_phonezoom:
    zoom 0.2

#contacts
transform contactzoom:
    zoom 0.3

transform contactzoom_small:
    zoom 0.4

transform settingszoom:
    zoom 0.1

transform settingszoom_small:
    zoom 0.13

transform contact_big:
    zoom 0.75

#music
transform musicbuttonszoom:
    zoom 0.08

transform musicbuttonszoom_small:
    zoom 0.15

transform phone_background:
    xalign 0.5
    yalign 0.5

transform phone_title:
    xalign 0.5
    yalign 0.1

transform phone_title_small:
    #around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    around (.5, .5) xalign .5 yalign .5
    rotate -90
    yalign 0.5
    xpos 400

transform phone_content:
    xalign 0.5
    ypos 390

transform phone_content_wide:
    #area 800, 370, 2500, 1400
    xpos 850
    ypos 165
    xsize 2140
    ysize 1752

transform phone_content_wide_gallery:
    xpos 850
    ypos 165
    xsize 2140

transform phone_guide_content:
    xpos 850
    ypos 500
    xsize 2140
    ysize 1300

transform phone_guide_checkmarks:
    zoom 0.2

transform phone_msg_content_wide_left:
    #xpos 850
    xpos 810
    ypos 165
    xsize 800
    ysize 1752

transform phone_msg_content_wide_right:
    #xpos 1650
    xpos 1551
    ypos 165
    #xsize 1350
    xsize 1469
    #xsize 1500
    ysize 1752

transform phone_content_wide_left:
    xpos 850
    ypos 200
    xsize 1000
    ysize 1700

transform phone_content_wide_right:
    xpos 1900
    #ypos 200
    ypos 165
    xsize 1100
    #ysize 1700
    ysize 1752

transform phone_widget:
    xalign 0.5
    yalign 0.15

transform phone_weather_widget:
    zoom 0.5
    xalign 0.70
    yalign 0.15


transform phone_button_zoom:
    zoom 0.2

# transform phone_content_gallery:
#     xalign 0.5
#     ypos 50

transform phone_content_small:
    #area 700, 400, 2500, 1400
    xalign 0.5
    #yalign 0.5
    #xsize 2500
    #ysize 1400

transform phone_content_apps:
    xalign 0.5
    #ypos 450
    ypos 750

transform reset_zoom:
    zoom 1.0

# transform notificationbar_left:
#     xpos 1515
#     ypos 313

transform notificationbar_left:
    xpos 850
    ypos 80

# transform notificationbar_right:
#     xpos 2115
#     ypos 324
#     zoom 0.16

transform notificationbar_right:
    xpos 2640
    ypos 90
    zoom 0.25

transform notificationbar_small_left:
    around (.5, .5) xalign .5 yalign .5
    rotate -90
    xpos 590
    ypos 1700

transform notificationbar_small_right:
    around (.5, .5) xalign .5 yalign .5
    rotate -90
    xpos 590
    ypos 500
    #zoom 0.2

transform small_notificationbar_zoom:
    zoom 0.2



#messages
transform phone_content_msgs:
    xpos 1530
    ypos 370
    xsize 800
    ysize 1460

transform phone_content_msgs_small:
    xpos 650
    yalign 0.5
    xsize 2500
    ysize 1400

#smartphone bot controls
transform phone_bottom:
    xalign 0.5
    yalign 0.95

transform phone_bottom_small:
    xpos 3350
    yalign 0.5

transform phone_bot_zoom:
    zoom 0.1

transform phone_bot_zoom_small:
    zoom 0.20

# transform smartphone_stats_small_bars:
#     xfill True
    #xsize 1000
    #xpos 500
    #ypos 50

# Here we are defining the transform. You can use the name you want instead of 'rotation'
# You can also define different transforms for every displayable
transform flipped_left:
    #around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    around (.5, .5) xalign .5 yalign .5
    rotate -90
    zoom 1.8
    #linear 10 rotate 360
    #repeat



transform phone_photo_horizontal:
    zoom 0.54

transform phone_photo_vertical:
    zoom 0.44

transform phone_photo_zoom_button:
    zoom 0.3

transform phone_message_call_button:
    zoom 0.25