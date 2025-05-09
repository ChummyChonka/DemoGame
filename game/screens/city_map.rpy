default map.hover_gym = False
default map.hover_home = False

transform markerzoom:
    zoom 0.15


style map_button_text:
    color "#FFFFFF"
    hover_color "#e67132"
    outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]


init python:
    from enum import Enum

    class MarkerColor(Enum):
        BASE = 0
        GREEN = 1
        BLUE = 2
        CYAN = 3
        ORANGE = 4
        PINK = 5
        PURPLE = 6
        RED = 7
        YELLOW = 8




screen city_map():
    modal True
    style_prefix "map"

    vbox:
        style_prefix "map"
        xalign 1.0
        yalign 0.98

    $ markers = setup_map_markers()

    for marker in markers:
        if marker.enabled:
            vbox:
                xsize 500
                style_prefix "marker"
                xpos marker.position[0]
                ypos marker.position[1]

                vbox:
                    xalign 0.5

                    imagebutton:
                        xalign 0.5
                        tooltip marker.name
                        if(marker.location.name in actualgame.current_location.name):
                            idle "images/map/marker_empty_hover.webp"
                            if(actualgame.daytime in marker.open_times):
                                action [Hide("city_map"), Jump("location_" + marker.label)]
                        else:
                            if(gamemap_colored_pins):
                                if(marker.marker_color == MarkerColor.GREEN):
                                    idle "images/map/marker_empty_green_idle.webp"
                                elif(marker.marker_color == MarkerColor.BLUE):
                                    idle "images/map/marker_empty_blue_idle.webp"
                                elif(marker.marker_color == MarkerColor.CYAN):
                                    idle "images/map/marker_empty_cyan_idle.webp"
                                elif(marker.marker_color == MarkerColor.ORANGE):
                                    idle "images/map/marker_empty_orange_idle.webp"
                                elif(marker.marker_color == MarkerColor.RED):
                                    idle "images/map/marker_empty_red_idle.webp"
                                elif(marker.marker_color == MarkerColor.PURPLE):
                                    idle "images/map/marker_empty_purple_idle.webp"
                                elif(marker.marker_color == MarkerColor.PINK):
                                    idle "images/map/marker_empty_pink_idle.webp"
                                elif(marker.marker_color == MarkerColor.YELLOW):
                                    idle "images/map/marker_empty_yellow_idle.webp"
                                else:
                                    idle "images/map/marker_empty_idle.webp"
                            else:
                                idle "images/map/marker_empty_idle.webp"
                                hover "images/map/marker_empty_hover.webp"
                                action [Hide("city_map"), Jump("location_" + marker.label)]
                        at markerzoom

                    add Image("images/map/symbols/" + marker.svg + ".svg", dpi=600):
                        ypos -400
                        xalign 0.5


    vbox:
        xalign 0.05
        yalign 0.02
        textbutton ("Colored Map Markers"):
            if gamemap_colored_pins:
                background Frame("images/notify_filled.png", 50,50)
            else:
                background Frame("images/notify.png", 50,50)
            action ToggleVariable("gamemap_colored_pins", true_value=True, false_value=False)


    $ tooltip = GetTooltip("city_map")
    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            vbox:
                xalign 0.5
                text tooltip:
                    kerning 2
                    outlines [(absolute(3), "#000000", absolute(0), absolute(0))]
                    color "#ffffff"



init python:
    class Marker:
        def __init__(self, name, label, position, location, svg, enabled, open_times=[1,2,3,4], marker_color=MarkerColor.BASE):
            self.name = name
            self.label = label
            self.position = position
            self.location = location
            self.svg = svg
            self.enabled = enabled
            self.open_times = open_times
            self.marker_color = marker_color


    def setup_map_markers() -> list:
        markers = list()
        markers.append(Marker(
            name="Cafe",
            label="cafe",
            position=[1850,920],
            location=Location.CAFE,
            svg="cafe",
            enabled=True,
            open_times=[1,2,3],
            marker_color=MarkerColor.ORANGE
        ))
        markers.append(Marker(
            name="Home",
            label="home",
            position=[530,205],
            location=Location.HOME,
            enabled=True,
            svg="home",
            marker_color=MarkerColor.BASE
        ))
        markers.append(Marker(
            name="Moms",
            label="moms",
            position=[70,1290],
            location=Location.MOMS,
            enabled=True,
            svg="woman",
            marker_color=MarkerColor.PURPLE
        ))
        markers.append(Marker(
            name="Gym",
            label="gym",
            position=[2970,780],
            location=Location.GYM,
            enabled=True,
            svg="gym",
            open_times=[1,2,3],
            marker_color=MarkerColor.RED
        ))
        markers.append(Marker(
            name="Escape Room",
            label="escaperoom",
            position=[2320,150],
            location=Location.ESCAPEROOM,
            enabled=gamemap["escaperoom"],
            svg="key",
            open_times=[3],
            marker_color=MarkerColor.CYAN
        ))
        markers.append(Marker(
            name="Photo Studio",
            label="studio",
            position=[2450,1300],
            location=Location.STUDIO,
            enabled=gamemap["photostudio"],
            svg="photo",
            open_times=[1,2,3],
            marker_color=MarkerColor.YELLOW
        ))
        markers.append(Marker(
            name="University",
            label="uni",
            position=[950,1350],
            location=Location.UNI,
            enabled=True,
            svg="school",
            open_times=[1,2,3],
            marker_color=MarkerColor.BLUE
        ))
        markers.append(Marker(
            name="Dorms",
            label="dorms",
            position=[1150,1500],
            location=Location.DORMS,
            enabled=True,
            svg="dorms",
            open_times=[1,2,3],
            marker_color=MarkerColor.PINK
        ))
        markers.append(Marker(
            name="Park",
            label="park",
            position=[3350,700],
            location=Location.PARK,
            enabled=True,
            svg="park",
            marker_color=MarkerColor.GREEN
        ))
        return markers

