init python:
    import sys
    from types import ModuleType, FunctionType
    from gc import get_referents

    def setup_register_label_test():
        actualgame.current_event = None
        register_label("test1", actualgame.daycount+1, 1)
        register_label("test2", actualgame.daycount+1, 1)


    def load_quests_debug():
        quests_file = "extras/quests.csv"
        if(renpy.loadable(quests_file)):
            opened_file = renpy.open_file(quests_file)
            file_data = opened_file.read()
            byte_list = file_data.split(b"\n")
            data_list = []
            for line in byte_list:
                data_list.append(line.decode('utf-8'))
            #return data_list

            result_list = list()
            for line in data_list:
                linesplit = line.split(";")
                if(len(linesplit) > 2) and (linesplit[2].startswith("event")):
                    #result_list.append(linesplit[2])
                    result_list.append(linesplit)
            return result_list


    def apply_single_conversation_debug(convo_id: str):
        for c in conversations:
            if(c.id == convo_id):
                return c


    def getsize(obj):
        BLACKLIST = type, ModuleType, FunctionType
        """sum size of object & members."""
        if isinstance(obj, BLACKLIST):
            raise TypeError('getsize() does not take argument of type: '+ str(type(obj)))
        seen_ids = set()
        size = 0
        objects = [obj]
        while objects:
            need_referents = []
            for obj in objects:
                if not isinstance(obj, BLACKLIST) and id(obj) not in seen_ids:
                    seen_ids.add(id(obj))
                    size += sys.getsizeof(obj)
                    need_referents.append(obj)
            objects = get_referents(*need_referents)
        return size



    # check all embedded variables in text messages
    def check_conversation_replacements():
        string_list = list()
        for conversation in store.conversations:
            for msg in conversation.messages:
                string_list.append(msg.content)

        for p_id in store.messages.keys():
            for msg in store.messages[p_id].messages:
                string_list.append(msg.content)

        manipulate_text_in_brackets_dict(string_list)


    # check if all contact images can be loaded
    def check_images_loadable():
        check_list = [
            "images/smartphone/contacts/contacts_unknown.webp",
            "images/smartphone/contacts/test/contacts_unknown.webp"
            ]
        for p_id in store.people:
            photo_name = p_id.lower()
            check_list.append("images/smartphone/contacts/contacts_" + photo_name + ".webp")
            check_list.append("images/smartphone/contacts/test/contacts_" + photo_name + ".webp")

        for item in check_list:
            if(not renpy.loadable(item)):
                raise Exception("Can't load: ", item)


    # check that name, nickname, surname and display_name have been set
    def check_all_names_forcefully():
        for p_id in store.people:
            if not person_check_name(p_id):
                raise Exceptions("Name error with: ", p_id)
            if not person_check_nickname(p_id):
                raise Exceptions("Nickname error with: ", p_id)
            if not person_check_surname(p_id):
                raise Exceptions("Surname error with: ", p_id)
            if not person_check_display_name(p_id):
                raise Exceptions("Display Name error with: ", p_id)


    # check if there is guide info for each event
    def check_all_guide_info():
        for quest in store.quests:
            for event in quest.events:
                get_event_description(event.event_id)


    # output a list of the day property of all received messages
    def check_msgs_age():
        output_list = list()
        for pers in store.messages:
            for msg in store.messages[pers].messages:
                output_list.append(msg.day)
        return output_list

