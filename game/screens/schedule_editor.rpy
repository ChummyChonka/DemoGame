
style scheduleeditor_text:
    color "#ffffff"
    selected_color "#FF0000"

style scheduleeditor_button_text is scheduleeditor_text:
    hover_color gui.hover_color

style scheduleeditor_radio_text:
    selected_color "#000000"

style scheduleeditorradio_button_text is radio_button_text:
    color "#ffffff"
    selected_color "#FF0000"
    hover_color gui.hover_color


screen schedule_editor():

    modal True
    zorder 10
    style_prefix "scheduleeditor"

    add "images/bg_gray.webp"

    $ locations = get_location_names()

    vbox:
        spacing 100
        xfill True

        hbox:
            ysize 700
            xfill True
            vbox:
                textbutton ("CLOSE"):
                    action Function(close_schedule_editor)

            null width 100

            vbox:
                label ("Character")
                viewport:
                    mousewheel True
                    scrollbars "vertical"
                    xsize 500

                    vbox:
                        style_prefix "scheduleeditorradio"
                        for c in get_sorted_people():
                            textbutton(c):
                                action SetVariable("scheduleeditor.selected_char", c)

            vbox:
                label ("Locations")
                viewport:
                    mousewheel True
                    scrollbars "vertical"

                    xsize 1000

                    vbox:
                        style_prefix "scheduleeditorradio"
                        for loc in locations:
                            textbutton loc:
                                action SetVariable("scheduleeditor.selected_loc", loc)

            vbox:
                label ("Actions")
                textbutton("SAVE FILE - !DANGER!"):
                    text_color "#FF0000"
                    action Function(schedule_editor_do, "save")
                if(scheduleeditor.selected_char is None):
                    text "Select char"
                if(scheduleeditor.selected_loc is None):
                    text "Select location"
                if(scheduleeditor.selected_box == [None, None, None]):
                    text "Select schedule box"
                if(not scheduleeditor.selected_char is None) and (not scheduleeditor.selected_loc is None) and (not scheduleeditor.selected_box == [None, None, None]):
                    textbutton("replace"):
                        action Function(schedule_editor_do, "replace")
                    textbutton("add"):
                        action Function(schedule_editor_do, "add")
                if(not scheduleeditor.selected_char is None) and (not scheduleeditor.selected_box == [None, None, None]):
                    textbutton("remove"):
                        action Function(schedule_editor_do, "remove")



        hbox:
            spacing 50
            null width 100

            vbox:
                #xsize 3300
                label ("Schedule")

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    xfill True
                    ysize 1100

                    grid 5 8:
                        xfill True
                        spacing 10
                        text ""
                        label "morning"
                        label "midday"
                        label "evening"
                        label "night"

                        for weekday in range(1, 8):
                            for daytime in range(5):
                                if(daytime == 0):
                                    label get_weekday_by_nmbr(weekday)[:3]
                                else:
                                    if(scheduleeditor.selected_char is None):
                                        text "-"
                                    else:
                                        $ loc_list = get_specific_location_names_list(scheduleeditor.selected_char, weekday, daytime)
                                        $ counter = 0
                                        hbox:
                                            box_wrap True
                                            style_prefix "scheduleeditorradio"
                                            for loc in loc_list:
                                                textbutton (str(loc)):
                                                    action SetVariable("scheduleeditor.selected_box", [weekday, daytime, counter])
                                                    text_size 50
                                                    if(weekday == actualgame.weekday) and (daytime == actualgame.daytime):
                                                        text_underline True
                                                $ counter += 1


init python:
    import csv

    def get_sorted_people() -> list:
        return sorted(people, key=lambda x: x)

    def get_specific_location_names_list(person_id:str, weekday:int, daytime:int) -> list:
        if(scheduleeditor.schedules is None):
            return
        when = ((weekday - 1) * 4) + daytime - 1

        if(not person_id in scheduleeditor.schedules.keys()):
            return

        string_list = [location.name for location in scheduleeditor.schedules[person_id][when]]
        return string_list


    def set_temp_schedules():
        npc_schedules = read_npc_schedules()
        scheduleeditor.schedules = dict()
        for line in npc_schedules:
            linesplit = line.split(";")
            name = linesplit[0]
            content = list()
            for timeslot in linesplit[1:]:
                timeslot_list = list()
                for entry in timeslot.split(","):
                    timeslot_list.append(get_location_by_name(entry))
                content.append(timeslot_list)

            #if(name in [pers.id for pers in people]):
            if(name in store.people):
                scheduleeditor.schedules[name] = content

        for pers in people:
            if(not pers in scheduleeditor.schedules.keys()):
                pers_schedule = list()
                for i in range(4):
                    for j in range(7):
                        pers_schedule.append([Location.EMPTY])
                scheduleeditor.schedules[pers] = pers_schedule


    def open_schedule_editor():
        renpy.suspend_rollback(True)
        config.rollback_enabled = False

        set_temp_schedules()
        renpy.show_screen("schedule_editor")
        config.developer = False


    def close_schedule_editor():
        renpy.hide_screen("schedule_editor")
        renpy.suspend_rollback(False)
        config.rollback_enabled = True
        config.developer = True
        scheduleeditor.schedules = None


    def schedule_editor_do(action):
        if(scheduleeditor.schedules is None):
            return

        if(action in ["replace", "add", "remove"]):
            location = get_location_by_name(scheduleeditor.selected_loc)
            p_id = scheduleeditor.selected_char

            weekday = scheduleeditor.selected_box[0]
            daytime = scheduleeditor.selected_box[1]
            index = scheduleeditor.selected_box[2]

            when = ((weekday - 1) * 4) + daytime - 1
            content = scheduleeditor.schedules[p_id][when]

            if(action == "replace"):
                if(len(content) == 1):
                    scheduleeditor.schedules[p_id][when] = [location]
                else:
                    scheduleeditor.schedules[p_id][when][index] = location

            elif(action == "remove"):
                if(len(content) == 1):
                    scheduleeditor.schedules[p_id][when] = [Location.EMPTY]
                else:
                    scheduleeditor.schedules[p_id][when].remove(scheduleeditor.schedules[p_id][when][index])

            elif(action == "add"):
                scheduleeditor.schedules[p_id][when].append(location)

        elif(action == "save"):
            schedules_list = list()
            for k,v in scheduleeditor.schedules.items():
                output_line = [k]
                for timeslot in v:

                    timeslot_string = ""
                    for i in range(len(timeslot)):
                        timeslot_string += timeslot[i].name
                        if(not i == len(timeslot) -1):
                            timeslot_string += ","

                    output_line.append(timeslot_string)
                schedules_list.append(output_line)

            with open(config.gamedir + "/extras/npc_schedules.csv", "w") as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=";")
                csv_writer.writerows(schedules_list)

            # trigger schedules reload
            set_daily_schedules()




    def get_weekday_by_nmbr(nmbr:int) -> str:
        if(nmbr == 1):
            return "Monday"
        elif(nmbr == 2):
            return "Tuesday"
        elif(nmbr == 3):
            return "Wednesday"
        elif(nmbr == 4):
            return "Thursday"
        elif(nmbr == 5):
            return "Friday"
        elif(nmbr == 6):
            return "Saturday"
        elif(nmbr == 7):
            return "Sunday"
        else:
            return "LOL"

