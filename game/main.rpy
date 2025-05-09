
label main_game:
    hide screen sublocation_navigation

    scene bg_black
    show screen city_map

    $ gamemusic.play_per_location(Location.MAP)
    if("event_gym_intro" in flags):
        $ actualgame.block_calls = False
    $ renpy.pause(hard=True)

    jump main_game


label forced_event_base:
    return



