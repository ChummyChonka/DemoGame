init python:

    RELATIONSHIP_MAX = 20
    RELATIONSHIP_MIN = 0

    class Person:
        def __init__(self):
            pass


    ########################
    # standalone functions #
    ########################


    def set_daily_schedules():
        npc_schedules = read_npc_schedules()
        for i in range(len(npc_schedules)):
            splitline = npc_schedules[i].split(";")
            name = splitline[0]
            if(name == "Eileen"):
                continue

            start_index = ((actualgame.weekday - 1) * 4) + 1

            day_schedule = list() # list with four lists, one for each time slot
            for entry in splitline[start_index:start_index+4]:
                entry_list = list() # list for each time slot, can contain multiple items
                for loc in entry.split(","):
                    entry_list.append(get_location_by_name(loc))
                day_schedule.append(entry_list)
            day_schedules[name] = day_schedule


    def check_incest(p_id) -> bool:
        check_mandatory_names(p_id)
        relation_list = list()
        if(p_id == "Sophia"):
            relation_list = ["Mom", "Mommy", "Mama", "Mami"]
        elif(p_id == "Christopher"):
            relation_list = ["Dad", "Daddy", "Papa", "Papi", "Stepdad"]
        elif(p_id == "Natalie"):
            relation_list = ["Aunt", "Aunti", "Aunty", "Auntie"]
        elif(p_id == "Laura"):
            relation_list = ["Cousin"]

        return any(people[p_id]["nickname"].casefold() == s.casefold() for s in relation_list)


    def person_get_current_major_location(p_id) -> Location:
        current_loc = person_get_current_location(p_id)
        if(does_location_match(current_loc, Location.GYM)):
            return Location.GYM
        elif(does_location_match(current_loc, Location.HOME)):
            return Location.HOME
        elif(does_location_match(current_loc, Location.MOMS)):
            return Location.MOMS
        elif(does_location_match(current_loc, Location.UNI)):
            return Location.UNI
        elif(does_location_match(current_loc, Location.DORMS)):
            return Location.DORMS
        elif(does_location_match(current_loc, Location.STUDIO)):
            return Location.STUDIO
        else:
            return current_loc


    def person_get_current_location(p_id) -> Location:
        if(p_id == "Eileen"):
            return actualgame.current_location
        return day_schedules[p_id][actualgame.daytime-1][0]


    def person_is_char_here(p_id: str) -> bool:
        return person_is_char_in(p_id, actualgame.current_location)


    def person_is_char_in(p_id:str, loc:Location) -> bool:
        if(p_id == "Eileen"):
            loc_list = [actualgame.current_location]
        else:
            loc_list = person_get_specific_location_list(p_id, actualgame.daytime)
        for loc_item in loc_list:
            if(loc.name in loc_item.name):
                return True
        if(loc in loc_list):
            return True
        return False


    def person_get_specific_location_names_list(p_id, daytime) -> list:
        locations_list = person_get_specific_location_list(p_id, daytime)
        names_list = []
        for loc in locations_list:
            names_list.append(str(loc).split(".")[1])
        return names_list


    def person_get_specific_location_list(p_id, daytime) -> list:
        when = max(1, min(4, daytime)) - 1
        location_list = []
        locations = day_schedules[p_id][when]
        for i in range(len(locations)):
            location_list.append(locations[i])
        return location_list


    def person_update_nickname(p_id, nickname, use_nickname):
        people[p_id]["nickname"] = nickname
        people[p_id]["use_nickname"] = use_nickname
        if use_nickname:
            people[p_id]["display_name"] = nickname


    def person_get_phone_name(p_id):
        if("unknown" in people[p_id]) and (people[p_id]["unknown"] == True):
            return "Unknown"
        return person_get_display_name(p_id)

    def person_get_image(p_id:str) -> str:
        if person_is_unknown(p_id):
            return "images/smartphone/contacts/contacts_unknown.webp"
        photo_name = p_id.lower()
        if(not renpy.loadable("images/smartphone/contacts/contacts_" + photo_name + ".webp")):
            raise Exception("Can't load contact photo: " + photo_name)
        return "images/smartphone/contacts/contacts_" + photo_name + ".webp"

    def person_get_small_image(p_id:str) -> str:
        if("unknown" in people[p_id]) and (people[p_id]["unknown"] == True):
            return "images/smartphone/contacts/test/contacts_unknown.webp"
        photo_name = p_id.lower()
        if(not renpy.loadable("images/smartphone/contacts/test/contacts_" + photo_name + ".webp")):
            raise Exception("Can't load contact photo: " + photo_name)
        return "images/smartphone/contacts/test/contacts_" + photo_name + ".webp"


    def person_use_nickname(p_id) -> bool:
        if(not "use_nickname" in people[p_id]):
            return False
        if(not isinstance(people[p_id]["use_nickname"], bool)):
            return False
        return people[p_id]["use_nickname"]


    def check_mandatory_names(p_id: str):
        if(not person_check_nickname(p_id)):
            people[p_id]["nickname"] = people[p_id]["name"]
        if("use_nickname" in people[p_id]) and (people[p_id]["use_nickname"] == True):
            people[p_id]["display_name"] = people[p_id]["nickname"]
        else:
            people[p_id]["display_name"] = people[p_id]["name"]
        if(not person_check_surname(p_id)):
            people[p_id]["surname"] = ""


    def check_all_mandatory_names():
        for p_id in people.keys():
            check_mandatory_names(p_id)


    def person_check_name(p_id:str) -> bool:
        return person_check_specific_name(p_id, "name")

    def person_check_nickname(p_id:str) -> bool:
        return person_check_specific_name(p_id, "nickname")

    def person_check_surname(p_id:str) -> bool:
        return person_check_specific_name(p_id, "surname")

    def person_check_display_name(p_id:str) -> bool:
        return person_check_specific_name(p_id, "display_name")

    def person_check_specific_name(p_id:str, name_to_check:str) -> bool:
        if(not name_to_check in people[p_id]):
            return False
        if(people[p_id][name_to_check] == ""):
            return False
        if(isinstance(people[p_id][name_to_check], str)):
            return True
        return False


    def person_get_name(p_id:str) -> str:
        if person_check_name(p_id):
            return people[p_id]["name"]
        return "NOT SET"

    def person_get_nickname(p_id:str) -> str:
        if person_check_nickname(p_id):
            return people[p_id]["nickname"]
        return "NOT SET"

    def person_get_surname(p_id:str) -> str:
        if person_check_surname(p_id):
            return people[p_id]["surname"]
        return "NOT SET"

    def person_get_display_name(p_id:str) -> str:
        if person_check_display_name(p_id):
            return people[p_id]["display_name"]
        return "NOT SET"


    def person_set_display_name(p_id, use_nick=False):
        if use_nick:
            people[p_id]["use_nickname"] = True
            if person_check_nickname(p_id):
                people[p_id]["display_name"] = people[p_id]["nickname"]
            else:
                people[p_id]["display_name"] = people[p_id]["name"]
        else:
            people[p_id]["use_nickname"] = False
            people[p_id]["display_name"] = people[p_id]["name"]


    def person_update_display_name(p_id):
        if("use_nickname" in store.people[p_id].keys()) and store.people[p_id]["use_nickname"]:
            if person_check_nickname(p_id):
                people[p_id]["display_name"] = people[p_id]["nickname"]
            else:
                people[p_id]["display_name"] = people[p_id]["name"]
        else:
            people[p_id]["display_name"] = people[p_id]["name"]


    def person_get_relationship(p_id) -> int:
        person_check_relationship(p_id)
        return people[p_id]["relationship"]


    def person_check_relationship(p_id):
        if(not p_id in people):
            raise Exception("No Person with id: " + p_id)

        if(not "relationship" in people[p_id]):
            people[p_id]["relationship"] = RELATIONSHIP_MIN
        if(not isinstance(people[p_id]["relationship"], int)):
            people[p_id]["relationship"] = RELATIONSHIP_MIN
        if(people[p_id]["relationship"] < RELATIONSHIP_MIN):
            people[p_id]["relationship"] = RELATIONSHIP_MIN


    def person_update_relationship(p_id:str, val:int):
        person_check_relationship(p_id)

        people[p_id]["relationship"] += val
        people[p_id]["relationship"] = max(min(people[p_id]["relationship"], RELATIONSHIP_MAX), RELATIONSHIP_MIN)
        display_name = people[p_id]["display_name"]
        if(val > 0):
            renpy.notify("Relationship " + display_name + ": +" + str(val))
        else:
            renpy.notify("Relationship " + display_name + ": " + str(val))


    def person_is_unknown(p_id:str) -> bool:
        if(not p_id in store.people):
            raise Exception("No person with id: " + p_id)
        if("unknown" in people[p_id]) and people[p_id]["unknown"]:
            return True
        return False


    def person_make_known(p_id:str):
        if(not p_id in people):
            raise Exception("No person with id: " + p_id)
        people[p_id]["unknown"] = False


    def person_add_to_contacts(p_id:str):
        if(p_id in smartphone.contacts):
            return
        person_make_known(p_id)
        smartphone.contacts.append(p_id)
        sort_contacts()
        renpy.notify("New contact added")


    def person_set_current_location(p_id:str, new_loc:Location):
        day_schedules[p_id][actualgame.daytime-1] = [new_loc]


    def person_set_current_major_location(p_id:str, new_loc:Location, exclude_list:list=None):
        if(new_loc == Location.MOMS):
            possible_locations = [loc for loc in Location if loc.name.startswith("MOMS") and loc.name != "MOMS"]
        elif(new_loc == Location.GYM):
            possible_locations = [loc for loc in Location if loc.name.startswith("GYM") and loc.name != "GYM"]
        else:
            return

        if(not exclude_list is None):
            for entry in exclude_list:
                if(entry in possible_locations):
                    possible_locations.remove(entry)
        person_set_current_location(p_id, possible_locations[renpy.random.randint(0, len(possible_locations)-1)])


    def person_is_in_game_location(p_id) -> bool:
        if(person_get_current_location(p_id) in [Location.EMPTY, Location.ERROR]):
            return False
        return True


    def update_msg_author_to_id(messages: list, p_id:str, pers:Person):
        for i in range(len(messages.messages)):
            if(not hasattr(messages.messages[i], "author")):
                continue

            author_id = None
            if(messages.messages[i].author == pers):
                author_id = p_id
            else:
                author_id = "Eileen"

            content = messages.messages[i].content
            img = messages.messages[i].img
            vertical = messages.messages[i].vertical
            wallpaper = messages.messages[i].wallpaper
            #answer_options = messages.messages[i].answer_options
            day = messages.messages[i].day
            answered = messages.messages[i].answered

            if(img == "hearteyes"):
                img = None
                content += "😍"
            elif(img == "annoyed"):
                img = None
                content += "😒"
            elif(img == "bottom_eyes"):
                img = None
                content += "🥺"
            elif(img == "tongue_wink"):
                img = None
                content += "😜"

            messages.messages[i] = Msg(
                author_id,
                content,
                img,
                vertical,
                wallpaper,
                #answer_options=answer_options,
                day=day,
                answered=answered
                )


    def update_people_dict():
        if(isinstance(person.protag, Person)):
            store.messages["Eileen"] = person.protag.msgs
            person.protag = {
                "name" : "Eileen",
                "display_name" : "Eileen",
                "surname" : "Bulbiferum"
                }
        if(isinstance(person.bff, Person)):
            store.messages["Aster"] = person.bff.msgs
            update_msg_author_to_id(store.messages["Aster"], "Aster", person.bff)
            person.bff = {
                "name" : "Aster",
                "surname" : "Lungwort",
                "nickname" : "Bestie",
                "display_name" : "Aster",
                "is_dateable" : True,
                "relationship" : person.bff.relationship,
                "unknown" : person.bff.unknown
                }
        if(isinstance(person.mom, Person)):
            store.messages["Sophia"] = person.mom.msgs
            update_msg_author_to_id(store.messages["Sophia"], "Sophia", person.mom)
            person.mom = {
                "name" : "Sophia",
                "display_name" : "Sophia",
                "relationship" : person.mom.relationship,
                "surname" : "Walker",
                "unknown" : person.mom.unknown
                }
        if(isinstance(person.cousin, Person)):
            store.messages["Laura"] = person.cousin.msgs
            update_msg_author_to_id(store.messages["Laura"], "Laura", person.cousin)
            person.cousin = {
                "name" : "Laura",
                "nickname" : "Shortie",
                "display_name" : "Laura",
                "surname" : "Auratum",
                "unknown" : True,
                "relationship" : person.cousin.relationship,
                "unknown" : person.cousin.unknown
                }
        if(isinstance(person.aunt, Person)):
            store.messages["Natalie"] = person.aunt.msgs
            update_msg_author_to_id(store.messages["Natalie"], "Natalie", person.aunt)
            person.aunt = {
                "name" : "Natalie",
                "is_dateable" : True,
                "display_name" : "Natalie",
                "surname" : "Auratum",
                "relationship" : person.aunt.relationship,
                "unknown" : person.aunt.unknown
                }
        if(isinstance(person.stepdad, Person)):
            store.messages["Christopher"] = person.stepdad.msgs
            update_msg_author_to_id(store.messages["Christopher"], "Christopher", person.stepdad)
            person.stepdad = {
                "name" : "Christopher",
                "nickname" : "Chris",
                "display_name" : "Christopher",
                "surname" : "Walker",
                "relationship" : person.stepdad.relationship,
                "unknown" : person.stepdad.unknown
                }
        if(isinstance(person.boss, Person)):
            store.messages["Theodore"] = person.boss.msgs
            update_msg_author_to_id(store.messages["Theodore"], "Theodore", person.boss)
            person.boss = {
                "name" : "Theodore",
                "nickname" : "Teddy",
                "display_name" : "Theodore",
                "surname" : "Clark",
                "unknown" : True,
                "relationship" : person.boss.relationship,
                "unknown" : person.boss.unknown
                }
        if(isinstance(person.jessica, Person)):
            store.messages["Jessica"] = person.jessica.msgs
            update_msg_author_to_id(store.messages["Jessica"], "Jessica", person.jessica)
            person.jessica = {
                "name" : "Jessica",
                "surname" : "Santos",
                "nickname" : "Jess",
                "display_name" : "Jessica",
                "unknown" : True,
                "relationship" : person.jessica.relationship,
                "unknown" : person.jessica.unknown
                }
        if(isinstance(person.emily, Person)):
            store.messages["Emily"] = person.emily.msgs
            update_msg_author_to_id(store.messages["Emily"], "Emily", person.emily)
            person.emily = {
                "name" : "Emily",
                "display_name" : "Emily",
                "surname" : "King",
                "unknown" : True,
                "relationship" : person.emily.relationship,
                "unknown" : person.emily.unknown
                }
        if(isinstance(person.sarah, Person)):
            store.messages["Sarah"] = person.sarah.msgs
            update_msg_author_to_id(store.messages["Sarah"], "Sarah", person.sarah)
            person.sarah = {
                "name" : "Sarah",
                "display_name" : "Sarah",
                "surname" : "Jones",
                "unknown" : True,
                "relationship" : person.sarah.relationship,
                "unknown" : person.sarah.unknown
                }
        if(isinstance(person.harper, Person)):
            store.messages["Harper"] = person.harper.msgs
            update_msg_author_to_id(store.messages["Harper"], "Harper", person.harper)
            person.harper = {
                "name" : "Harper",
                "surname" : "Ranch",
                "nickname" : "Mrs. Ranch",
                "display_name" : "Mrs. Ranch",
                "use_nickname" : True,
                "unknown" : True,
                "relationship" : person.harper.relationship,
                "unknown" : person.harper.unknown
                }
        if(isinstance(person.olivia, Person)):
            store.messages["Olivia"] = person.olivia.msgs
            update_msg_author_to_id(store.messages["Olivia"], "Olivia", person.olivia)
            person.olivia = {
                "name" : "Olivia",
                "display_name" : "Olivia",
                "surname" : "Nguyen",
                "unknown" : True,
                "relationship" : person.olivia.relationship,
                "unknown" : person.olivia.unknown
                }
        if(isinstance(person.victoria, Person)):
            store.messages["Victoria"] = person.victoria.msgs
            update_msg_author_to_id(store.messages["Victoria"], "Victoria", person.victoria)
            person.victoria = {
                "name" : "Victoria",
                "nickname" : "Ms. Burke",
                "surname" : "Burke",
                "use_nickname" : True,
                "unknown" : True,
                "relationship" : person.victoria.relationship,
                "unknown" : person.victoria.unknown
                }
        if(isinstance(person.bianca, Person)):
            store.messages["Bianca"] = person.bianca.msgs
            update_msg_author_to_id(store.messages["Bianca"], "Bianca", person.bianca)
            person.bianca = {
                "name" : "Bianca",
                "display_name" : "Bianca",
                "surname" : "Martin",
                "unknown" : True,
                "relationship" : person.bianca.relationship,
                "unknown" : person.bianca.unknown
                }
        if(isinstance(person.isabella, Person)):
            store.messages["Isabella"] = person.isabella.msgs
            update_msg_author_to_id(store.messages["Isabella"], "Isabella", person.isabella)
            person.isabella = {
                "name" : "Isabella",
                "nickname" : "Bella",
                "display_name" : "Isabella",
                "surname" : "Martinez",
                "unknown" : True,
                "relationship" : person.isabella.relationship,
                "unknown" : person.isabella.unknown
                }
        if(isinstance(person.patricia, Person)):
            store.messages["Patricia"] = person.patricia.msgs
            update_msg_author_to_id(store.messages["Patricia"], "Patricia", person.patricia)
            person.patricia = {
                "name" : "Patricia",
                "surname" : "Galvin",
                "display_name" : "Patricia",
                "unknown" : True,
                "relationship" : person.patricia.relationship,
                "unknown" : person.patricia.unknown
                }
        if(isinstance(person.gwen, Person)):
            store.messages["Gwendolyn"] = person.gwen.msgs
            update_msg_author_to_id(store.messages["Gwendolyn"], "Gwendolyn", person.gwen)
            person.gwen = {
                "name" : "Gwendolyn",
                "nickname" : "Gwen",
                "display_name" : "Gwendolyn",
                "surname" : "Wagner",
                "unknown" : True,
                "relationship" : person.gwen.relationship,
                "unknown" : person.gwen.unknown
                }

        # refresh last messages to handle emoji
        for p_id in store.messages.keys():
            if(not store.messages[p_id] is None) and (len(store.messages[p_id].messages) > 0):
                store.messages[p_id].last_message = store.messages[p_id].messages[-1]

        store.people = {
            "Eileen" : person.protag,
            "Aster" : person.bff,
            "Sophia" : person.mom,
            "Laura" : person.cousin,
            "Natalie" : person.aunt,
            "Christopher" : person.stepdad,
            "Theodore" : person.boss,
            "Jessica" : person.jessica,
            "Emily" : person.emily,
            "Sarah" : person.sarah,
            "Harper" : person.harper,
            "Olivia" : person.olivia,
            "Victoria" : person.victoria,
            "Bianca" : person.bianca,
            "Isabella" : person.isabella,
            "Patricia" : person.patricia,
            "Gwendolyn" : person.gwen
            }

        check_all_mandatory_names()