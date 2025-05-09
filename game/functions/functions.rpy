init python:
    import copy
    import random
    import reprlib
    from enum import Enum

    class FileType(Enum):
        IMAGE = 0
        WALLPAPER = 1
        PHOTO = 2

    config.overlay_screens.append("succubus_menu")
    config.overlay_screens.append("debug")

    preferences.set_mixer("music", 0.35)

    renpy.music.register_channel("sound2", "sfx", loop=False, stop_on_mute=True, 
        tight=True, buffer_queue=True, movie=False, framedrop=True)

    renpy.music.register_channel("sound3", "sfx", loop=False, stop_on_mute=True, 
        tight=True, buffer_queue=True, movie=False, framedrop=True)

    renpy.music.register_channel("sound4", "sfx", loop=False, stop_on_mute=True, 
        tight=True, buffer_queue=True, movie=False, framedrop=True)

    renpy.music.register_channel("ambience", "sfx", loop=True, stop_on_mute=True, 
        tight=True, buffer_queue=True, movie=False, framedrop=True)

    renpy.music.register_channel("ambience2", "sfx", loop=True, stop_on_mute=True, 
        tight=True, buffer_queue=True, movie=False, framedrop=True)

    renpy.music.register_channel("video", "sfx", loop=True, stop_on_mute=True, 
        tight=True, buffer_queue=False, movie=True, framedrop=True)


    def check_can_load_file(filetype, filename):
        if not config.developer:
            return True

        if(filetype is None):
            return False
        elif(filetype == FileType.WALLPAPER):
            if(not renpy.loadable("images/smartphone/wallpaper/" + filename + ".webp")):
                raise Exception("Could not load: images/smartphone/wallpaper/" + filename + ".webp")
            return True
        elif(filetype == FileType.PHOTO):
            file = "images/smartphone/photos/" + filename + ".webp"
            if(not renpy.loadable(file)):
                raise Exception("Could not load: " + file)
            file = "images/smartphone/photos/thumbnails/" + filename + ".webp"
            if(not renpy.loadable(file)):
                raise Exception("Could not load: " + file)
            file = "images/smartphone/wallpaper/" + filename + ".webp"
            if(not renpy.loadable(file)):
                raise Exception("Could not load: " + file)
        return False


    def save_name_change(name):
        store.save_name = name


    def do_main_menu(action):
        # main menu
        if(renpy.get_screen(["preferences"]) is None):
            if(action == "load"):
                renpy.hide_screen("proper_menu")
                renpy.show_screen("load")
            elif(action == "settings"):
                renpy.hide_screen("proper_menu")
                renpy.show_screen("preferences")


    def get_smartphone_contacts() -> list:
        #result_list = list(store.people.keys())
        #result_list.remove("Eileen")
        result_list = ("Aster", "Sophia", "Laura", "Natalie", "Christopher", "Theodore", "Jessica", "Sarah")
        return result_list


    def make_all_contacts_known():
        for k,v in store.people.items():
            store.people[k]["unknown"] = False


    def stop_music_debug():
        gamemusic.stop_music(full_stop=True)


    def proper_round(numb:float) -> int:
        if((numb - int(numb)) >= 0.5):
            return int(numb) + 1
        else:
            return int(numb)


    def debug_chars() -> list:
        chars = [character.protag, character.protag_think, character.bff]
        return chars


    def translate_config_version() -> float:
        if(config.version == "0.1"):
            return 0.1
        elif(config.version == "0.2") or (config.version == "0.2.1") or (config.version == "0.2.2"):
            return 0.2
        elif(config.version == "0.3") or (config.version == "0.3.1"):
            return 0.3


    def config_for_small():
        smartphone.content_stack = ["smartphone_apps_small"]
        smartphone.base_screens = ["smartphone_small", "smartphone_bot_controls_small"]
        smartphone.gallery.photos_per_page = 18


    def config_for_large():
        smartphone.content_stack = ["smartphone_apps_new"]
        smartphone.base_screens = ["smartphone", "smartphone_bot_controls"]
        smartphone.gallery.photos_per_page = 12


    def one_in_hundred() -> bool:
        if(renpy.random.randint(1,100) == 1):
            return True
        return False


    def get_random_list_of_numbers(n):
        numbers = list(range(1, n+1))
        random.shuffle(numbers)
        return numbers


    def phone_notification():
        smartphone.notification = True
        renpy.sound.play(audio.phone_notification)


    def take_photo(image):
        renpy.sound.play(audio.camera_shutter)
        #unlock_wallpaper(image)
        renpy.notify("New wallpaper unlocked")
        renpy.hide_screen("photo_taking")


    def hide_extra_ui(hide=True):
        if hide:
            store.phone_hud_hide = True
            actualgame.extra_symbols = False
        else:
            store.phone_hud_hide = False
            actualgame.extra_symbols = True


    def check_notification():
        #check if there is any notification left
        #for now only unread messages are of interest
        for contact_id in smartphone.msg_contacts:
            if(messages[contact_id].unread):
                smartphone.notification = True
                return
        smartphone.notification = False


    def set_read(contact_id):
        if(contact_id in smartphone.msg_contacts):
            messages[contact_id].unread = False
        check_notification()


    def set_read_all():
        for contact_id in smartphone.msg_contacts:
            messages[contact_id].unread = False
        check_notification()


    def set_read_all_but_unanswered():
        for contact_id in smartphone.msg_contacts:
            store.messages[contact_id].unread = False
            for m in store.messages[contact_id].messages:
                if(hasattr(m, "answer_options")) and (not m.answer_options is None):
                    if(not m.answered):
                        messages[contact_id].unread = True
                        break
        check_notification()


    def get_variable_names(people=False) -> list:
        #import reprlib
        aRepr = reprlib.Repr()
        aRepr.maxstring = 120

        entries = [ ]

        for sn, d in renpy.python.store_dicts.items():
            if sn.startswith("store._"):
                continue

            for vn in d.ever_been_changed:
                if vn.startswith("__00"):
                    continue

                if vn.startswith("_") and not vn.startswith("__"):
                    continue

                if vn not in d:
                    #value = "deleted"
                    continue
                else:
                    value = aRepr.repr(d[vn])

                if vn == "nvl_list":
                    continue

                name = (sn + "." + vn)[6:]

                #entries.append((name, value))
                if people:
                    if(name.startswith("person")):
                        entries.append(name)
                    continue
                else:
                    entries.append([name, value])
        if(not people):
            entries.sort(key=lambda e : e[0])

        return entries


    def contacts_add(contact_id):
        """
        Adds a contact to the phone, if it's not in there already.
        """
        if(contact_id in smartphone.contacts):
            if config.developer:
                raise Exception("Tried to create duplicate entry into smartphone.contacts!")
            return
        if(not contact_id in people):
            if config.developer:
                raise Exception("There is no Person object with that id!")
            return

        people[contact_id]["unknown"] = False
        smartphone.contacts.append(contact_id)
        sort_contacts()
        renpy.notify("New contact added")


    def contacts_move_up(author_id):
        smartphone.msg_contacts = list(smartphone.msg_contacts)
        for i in range(len(smartphone.msg_contacts)):
            if(smartphone.msg_contacts[i] == author_id):
                smartphone.msg_contacts.remove(smartphone.msg_contacts[i])
                smartphone.msg_contacts.insert(0, author_id)


    def sort_contacts():
        #contacts_new = [None] * len(smartphone.contacts)
        contacts_new = []
        names_list = []

        for p in smartphone.contacts:
            names_list.append(people[p]["name"]) # get only the names to sort
        sorted_list = sorted(names_list, key=str.lower) # sort alphabetically

        for name in sorted_list:
            for p in smartphone.contacts:
                if(people[p]["name"] == name):# look for the corresponding person
                    contacts_new.append(p) # add them to our new contacts set
                    break

        smartphone.contacts = contacts_new # overwrite the actual contacts set


    def load_replacements_dict() -> dict:
        update_people_dict()
        replacement_dict = dict()

        for p_id in store.people:
            p_object = p_id.lower()
            if(p_id == "Aster"):
                p_object = "bff"
            elif(p_id == "Eileen"):
                p_object = "protag"
            elif(p_id == "Sophia"):
                p_object = "mom"
            elif(p_id == "Natalie"):
                p_object = "aunt"
            elif(p_id == "Christopher"):
                p_object = "stepdad"
            elif(p_id == "Laura"):
                p_object = "cousin"
            elif(p_id == "Theodore"):
                p_object = "boss"
            elif(p_id == "Gwendolyn"):
                p_object == "gwen"
            else:
                p_object = p_id.lower()

            key_base = "person." + p_object
            key = ""
            for addendum in ["name", "nickname", "display_name", "surname"]:
                key = key_base + "." + addendum
                replacement_dict[key] = store.people[p_id][addendum]


        extras = {
            "petnames_protag(aunt)" : petnames_for_protag["Natalie"],
            "petnames_protag(bff)" : petnames_for_protag["Aster"],
            "petnames_protag(mom)" : petnames_for_protag["Sophia"],
            "petnames_protag(stepdad)" : petnames_for_protag["Christopher"],
            "petnames_protag(jessica)" : petnames_for_protag["Jessica"],
            "petnames_protag(tom)" : petnames_for_protag["Tom"],
            "petnames_protag(sarah)" : petnames_for_protag["Sarah"],
            "petnames_protag(isabella)" : petnames_for_protag["Isabella"],
            "petnames_protag(boss)" : petnames_for_protag["Theodore"],
            "petnames_protag(patricia)" : petnames_for_protag["Patricia"],

            "character.tom" : extra_char_names['tom']
        }

        return replacement_dict | extras


    def load_single_event_from_list(event:list) -> None:
        force = False
        player_hint = None
        quest_id = "testing"
        reqs = None

        if(event[4] != ""):
            force = True
            player_hint = event[12]
            renpy.notify(player_hint)

        #days	weekday	time	events	char	location
        if(event[5] != ""): #has requirements
            reqs = Requirements()

            #min game days -> single value
            if(not event[6] == ""):
                reqs.set_required_gamedays(int(event[6]))

            #weekdays -> can be multiple
            if(not event[7] == ""):
                weekdays_split = event[7].split(",")
                for i in range(len(weekdays_split)):
                    weekdays_split[i] = int(weekdays_split[i])
                reqs.add_required_weekdays(weekdays_split)

            #daytimes -> can be multiple
            if(not event[8] == ""):
                daytimes_split = event[8].split(",")
                for i in range(len(daytimes_split)):
                    daytimes_split[i] = int(daytimes_split[i])
                reqs.add_required_daytimes(daytimes_split)

            #events -> can be multiple
            if(not event[9] == ""):
                events_split = event[9].split(",")
                reqs.add_required_previous_events(events_split)

            #chars -> can be multiple
            if(not event[10] == ""):
                chars_split = event[10].split(",")
                chars = []
                for char in chars_split:
                    chars.append(char)
                reqs.add_required_chars(chars)

            #location -> single value
            if(not event[11] == ""):
                loc = get_location_by_name(event[11])
                reqs.set_required_location(loc)

        return Event(event[2], quest_id, force, player_hint, reqs)


    def read_credits(credits:str) -> list:
        """
        Reads one specific credits file and returns the content as a list.
        """
        credits_file = "credits/" + credits + "_credits.txt"
        if(renpy.loadable(credits_file)):
            opened_file = renpy.open_file(credits_file)
            file_data = opened_file.read()
            byte_list = file_data.split(b"\n")
            data_list = []
            for line in byte_list:
                data_list.append(line.decode('ascii'))
            return data_list
        return_list = ["Could not load credits file: " + credits_file,
            "Sorry...  😔\n\n"]
        return return_list


    def get_csv_as_list(filename: str) -> list:
        if(renpy.loadable(filename)):
            opened_file = renpy.open_file(filename)
            file_data = opened_file.read()
            byte_list = file_data.split(b"\n")
            data_list = []
            for line in byte_list:
                # for some reason when saving the schedule it puts \r at the end of each line
                # rstrip gets rid of that
                data_list.append(line.decode('utf8').rstrip())
            return data_list
        raise Exception("File:" + filename + " could not be read!")
        return None


    #reads npc_schedules.csv and returns that data as a list
    def read_npc_schedules() -> list:
        schedule_file = "extras/npc_schedules.csv"
        return get_csv_as_list(schedule_file)


    def stat_check_relationship(p_id:str, needed:int) -> bool:
        if(not p_id in store.people.keys()):
            return False
        if(people[p_id]["relationship"] >= needed):
            renpy.notify("Stat check passed:\nRelationship " + person_get_display_name(p_id))
            return True
        renpy.notify("Stat check failed:\nRelationship " + person_get_display_name(p_id))
        return False


    def stat_check(stat:Stats, needed:int, invert:bool=False, silent:bool=False, silent_on_pass=False) -> bool:
        made = False
        if invert:
            made = protagonist.get_stat(stat) < needed
        else:
            made = protagonist.get_stat(stat) >= needed
        output_string = ""
        if made:
            output_string += "Stat check passed:\n"
        else:
            output_string += "Stat check failed:\n"

        output_string += protagonist.get_stat_name(stat)

        if not silent and actualgame.stat_checks_notification:
            if made and silent_on_pass:
                return made

            renpy.notify(output_string)

        return made


    def load_apps() -> list:
        return [
            App("contacts", "Contacts", disabled=True),
            App("guide", "Guide"),
            App("gallery", "Gallery"),
            App("games", "Games", disabled=True),
            App("messages", "Messages"),
            App("music", "Music", disabled=True),
            App("renamer", "Renamer"),
            App("settings", "Settings"),
            App("stats", "Stats"),
            App("wallpapers", "Wallpapers", disabled=True),

            App("linktree", "Socials", url="https://linktr.ee/chummychonka"),
            App("bluesky", "Bluesky", url="https://bsky.app/profile/chummychonka.bsky.social", disabled=True),
            App("patreon", "Patreon", url="https://www.patreon.com/ChummyChonka", disabled=True),
            App("discord", "Discord", url="https://discord.gg/JFVM553QDv", disabled=True),
            App("itch", "Itch.io", url="https://chummychonka.itch.io/", disabled=True),
            App("twitter", "X", url="https://x.com/ChummyChonka", disabled=True)
        ]

    def load_app_icons() -> dict:
        return {
            "default" : Composite((250,250), (0,0), Frame("images/smartphone/msgboxes/phonemsg06.webp"), (25,25), "images/smartphone/logos/demo_logo.webp"),

            "gallery" : Composite((250,250), (0,0), Frame("images/smartphone/msgboxes/phonemsg05.webp"), (25,25), "images/smartphone/logos/logo_gallery.webp"),

            #"itch" : Composite((250,250), (0,0), Frame("images/smartphone/msgboxes/phonemsg17.webp"), (25,25), "images/smartphone/logos/logo_itch.webp"),

            "messages" : Composite((250,250), (0,0), Frame("images/smartphone/msgboxes/phonemsg04.webp"), (25,25), "images/smartphone/logos/logo_messages.webp"),

            #"music" : Composite((250,250), (0,0), Frame("images/smartphone/msgboxes/phonemsg06.webp"), (25,25), "images/smartphone/logos/logo_music.webp"),

            "guide" : Composite((250,250), (0,0), Frame("images/smartphone/msgboxes/phonemsg12.webp"), (25,25), "images/smartphone/logos/logo_guide.webp"),

            #"patreon" : Composite((250,250), (0,0), Frame("images/smartphone/msgboxes/phonemsg16.webp"), (25,25), "images/smartphone/logos/logo_patreon.webp"),

            "renamer" : Composite((250,250), (0,0), Frame("images/smartphone/msgboxes/phonemsg08.webp"), (25,25), "images/smartphone/logos/logo_contacts.webp"),

            "settings" : Composite((250,250), (0,0), Frame("images/smartphone/msgboxes/phonemsg10.webp"), (25,25), "images/smartphone/logos/logo_settings.webp"),

            "stats" : Composite((250,250), (0,0), Frame("images/smartphone/msgboxes/phonemsg07.webp"), (25,25), "images/smartphone/logos/logo_stats.webp"),

            #"twitter" : Composite((250,250), (0,0), Frame("images/smartphone/msgboxes/phonemsg19.webp"), (25,25), "images/smartphone/logos/logo_twitter.webp"),

            #"wallpapers" : Composite((250,250), (0,0), Frame("images/smartphone/msgboxes/phonemsg09.webp"), (25,25), "images/smartphone/logos/logo_wallpapers.webp"),

            #"bluesky" : Composite((250,250), (0,0), Frame("images/smartphone/msgboxes/phonemsg20.webp"), (25,25), "images/smartphone/logos/logo_bluesky.webp"),

            #"discord" : Composite((250,250), (0,0), Frame("images/smartphone/msgboxes/phonemsg21.webp"), (25,25), "images/smartphone/logos/logo_discord.webp"),

            "linktree" : Composite((250,250), (0,0), Frame("images/smartphone/msgboxes/phonemsg34.webp"), (25,25), "images/smartphone/logos/logo_linktree.webp")
        }

    def load_app_icons_hovered() -> dict:
        return {
            "default" : Composite((270,270), (0,0), Frame("images/smartphone/msgboxes/phonemsg06.webp"), (35,35), "images/smartphone/logos/demo_logo.webp"),

            "gallery" : Composite((270,270), (0,0), Frame("images/smartphone/msgboxes/phonemsg05.webp"), (35,35), "images/smartphone/logos/logo_gallery.webp"),

            #"itch" : Composite((270,270), (0,0), Frame("images/smartphone/msgboxes/phonemsg17.webp"), (35,35), "images/smartphone/logos/logo_itch.webp"),

            "messages" : Composite((270,270), (0,0), Frame("images/smartphone/msgboxes/phonemsg04.webp"), (35,35), "images/smartphone/logos/logo_messages.webp"),

            #"music" : Composite((270,270), (0,0), Frame("images/smartphone/msgboxes/phonemsg06.webp"), (35,35), "images/smartphone/logos/logo_music.webp"),

            "guide" : Composite((270,270), (0,0), Frame("images/smartphone/msgboxes/phonemsg12.webp"), (35,35), "images/smartphone/logos/logo_guide.webp"),

            #"patreon" : Composite((270,270), (0,0), Frame("images/smartphone/msgboxes/phonemsg16.webp"), (35,35), "images/smartphone/logos/logo_patreon.webp"),

            "renamer" : Composite((270,270), (0,0), Frame("images/smartphone/msgboxes/phonemsg08.webp"), (35,35), "images/smartphone/logos/logo_contacts.webp"),

            "settings" : Composite((270,270), (0,0), Frame("images/smartphone/msgboxes/phonemsg10.webp"), (35,35), "images/smartphone/logos/logo_settings.webp"),

            "stats" : Composite((270,270), (0,0), Frame("images/smartphone/msgboxes/phonemsg07.webp"), (35,35), "images/smartphone/logos/logo_stats.webp"),

            #"twitter" : Composite((270,270), (0,0), Frame("images/smartphone/msgboxes/phonemsg19.webp"), (35,35), "images/smartphone/logos/logo_twitter.webp"),

            #"wallpapers" : Composite((270,270), (0,0), Frame("images/smartphone/msgboxes/phonemsg09.webp"), (35,35), "images/smartphone/logos/logo_wallpapers.webp"),

            #"bluesky" : Composite((270,270), (0,0), Frame("images/smartphone/msgboxes/phonemsg20.webp"), (35,35), "images/smartphone/logos/logo_bluesky.webp"),

            #"discord" : Composite((270,270), (0,0), Frame("images/smartphone/msgboxes/phonemsg21.webp"), (35,35), "images/smartphone/logos/logo_discord.webp"),

            "linktree" : Composite((270,270), (0,0), Frame("images/smartphone/msgboxes/phonemsg34.webp"), (35,35), "images/smartphone/logos/logo_linktree.webp")
        }

    def get_extra_char_names() -> dict:
        return {
            "chonka" : "Chonka",
            "miles" : "Miles",
            "harry" : "Harry",
            "michael" : "Michael",
            "barista" : "Barista",
            "pizza_guy": "Pizza Guy",
            "tom" : "Tom",
            "haruko" : "Haruko",
            "calvin" : "Calvin",
            "tara" : "Tara",
            "lilith": "Lilith",
            "anthony" : "Anthony",
            "ms_clemens" : "Ms. Clemens",
            "prof" : "Prof",
            "petra" : "Petra",
            "rebecca" : "Rebecca",
            "landlord" : "Mr. Sullivan",
            "karina" : "Fearless Karina",
            "dominatrix" : "The Dominatrix",
            "big_boss" : "Some guy",
            "big_boss_wife" : "Woman",
            "big_boss_daughter" : "Young girl"
            }


    def get_sorted_people_by_name() -> list:
        #return sorted(store.people.items(), key=lambda item: item[1]["name"])
        return [p_id for p_id, _ in sorted(store.people.items(), key=lambda item: item[1]["name"])]

    def get_sorted_people_by_display_name() -> list:
        temp_dict = dict()
        for pers in store.people:
            if(not pers in ["Emily", "Victoria", "Isabella", "Bianca"]):
                temp_dict[pers] = store.people[pers]
        return [p_id for p_id, _ in sorted(temp_dict.items(), key=lambda item: item[1]["display_name"])]


    def sort_msg_contacts():
        sort_msg_contacts_by_msg_age()
        new_list = list()
        for p_id in smartphone.msg_contacts:
            if store.messages[p_id].unread:
                new_list.append(p_id)
        for p_id in smartphone.msg_contacts:
            if(not p_id in new_list):
                new_list.append(p_id)
        smartphone.msg_contacts = new_list


    def sort_msg_contacts_by_msg_age():
        msg_age_dict = dict()
        for pers in smartphone.msg_contacts:
            msg_age_dict[pers] = store.messages[pers].messages[-1].day
        msg_age_dict = dict(sorted(msg_age_dict.items(), key=lambda item: item[1], reverse=True))
        smartphone.msg_contacts = list(msg_age_dict.keys())


