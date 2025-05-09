init python:
    import re

    class Msg:
        def __init__(self, author_id, content="", img=None, vertical=False, wallpaper=None, emoji=False, day=None, answer_options=None, answered=False, notification=True):
            self.author_id = author_id
            self.content = content
            self.img = img
            self.vertical = vertical
            self.wallpaper = wallpaper
            self.emoji = False
            self.day = day
            self.answer_options = answer_options
            self.answered = answered
            self.notification = notification

            if(config.developer):
                if(author_id is None) or (author_id == ""):
                    raise Exception("Tried to create Msg object without author_id")


        def get_content(self, max_length=None) -> str:
            if(self.content is None):
                return ""
            if(max_length is None) or (len(self.content) <= max_length):
                return self.content
            else:
                return self.content[:max_length] + "..."


        def choose_answer(self, option):
            if config.developer:
                if(option is None):
                    raise Exception("Can't set option to None.")
                if(option+1 > len(self.answer_options)) or (option < 0):
                    raise Exception("That option is not available!")
                if(self.answer_options is None):
                    raise Exception("No answer options available, can't set choice!")
                if(self.answer_options is None):
                    raise Exception("No answer options to choose from! Is None")

            if(not self.answer_options is None) and (len(self.answer_options) > option) and (option >= 0):
                apply_single_conversation(self.answer_options[option])
                self.answered = True


    class AnswerOptions:
        def __init__(self, a_id, player_answers, npc_answers, chosen_answer=None):
            if(a_id is None) or (a_id == ""):
                raise Exception("Tried to create AnswerOptions object without id!")
            if(player_answers is None):
                raise Exception("Tried to create AnswerOptions object without player_answers!")
            if(npc_answers is None):
                raise Exception("Tried to create AnswerOptions object without npc_answers!")

            self.id = a_id
            self.player_answers = player_answers
            self.npc_answers = npc_answers
            self.chosen_answer = chosen_answer

            if(not self.npc_answers is None):
                self.disable_notifications_for_npc_answers()

        def disable_notifications_for_npc_answers(self):
            for i in range(len(self.npc_answers)):
                for j in range(len(self.npc_answers[i])):
                    self.npc_answers[i][j].notification = False


    class MessageChain:
        def __init__(self, contact_id):
            #self.length = 0
            self.contact_id = contact_id
            self.last_message = None
            #self.last_message_shortened = None
            self.messages = []
            self.unread = False
            #https://www.renpy.org/doc/html/screen_python.html#renpy.get_adjustment
            self.scroll_position = 0
            #self.scroll_adjust = ui.adjustment()

            if(self.contact_id is None) or (self.contact_id == ""):
                raise Exception("Tried to create MessageChain object without contact_id.")

        def set_read(self):
            self.unread = False


        def append_msgs(self, new_messages):
            if(new_messages is None):
                raise Exception("Cannot append None to messages!")

            for i in range(len(new_messages)):
                if(new_messages[i].day is None):
                    new_messages[i].day = actualgame.daycount
                self.messages.append(new_messages[i])
                if(not new_messages[i].img is None):
                    add_photo(new_messages[i].img, vertical=new_messages[i].vertical)

            self.last_message = self.messages[-1]
            if(self.last_message.day == actualgame.daycount):
                contacts_move_up(self.contact_id)
            self.unread = True


        def add_msg(self, author_id, content, img=None, vertical=False, wallpaper=None, emoji=False, day=None, answer_options=None, answered=False, notification=True):
            if(day is None):
                day = actualgame.daycount
            if(img is Null): #needed for 0.1 save compatibility???
                img = None
            self.messages.append(Msg(author_id, content, img, vertical, wallpaper, emoji, day, answer_options, answered))
            self.last_message = self.messages[-1]
            self.last_message_shortened = self.last_message.get_shortened()
            #self.length += 1
            #some idiot used Null instead of None previously
            if((not img is None) and (not emoji)):
                #smartphone.pictures.append(img)
                #smartphone.gallery.add_photo(Photo(img))
                if config.developer:
                    raise Exception("Tried to call smartphone.gallery.add_photo with image " + img)
            if(not author_id == "Eileen"):
                contacts_move_up(author_id)
                self.unread = True
                if notification:
                    smartphone.notification = True

        def get_last_message_content(self, max_length=None) -> str:
            if(self.last_message is None):
                return ""
            return self.last_message.get_content(max_length)


        #used after the fact to inject an option into an existing message
        def add_answer_options_to_last_msg(self, options):
            last_msg = len(self.messages) - 1
            self.messages[last_msg].answer_options = options
            self.messages[last_msg].notification = True
            self.unread = True
            phone_notification()


    class Conversation():
        def __init__(self, id, person_id, flags, messages):
            if(id is None) or (person_id is None) or (messages is None):
                raise Exception("Tried to create Conversations object with some none-Type.\n" + self.id + " " + person_id + " " + messages)
            self.id = id
            self.person_id = person_id
            self.flags = flags
            self.messages = messages


        def set_messages(self, msgs: list):
            if(msgs is None):
                raise Exception("Tried to set the messages of conversation: " + self.id + " to None!")
            if(not self.messages is None) and (game_version >= translate_config_version()):
                raise Exception("Tried to overwrite the messages of conversation: " + self.id + "!\nThis is only allowed with a game update!")
            self.messages = msgs

        def apply_flags(self):
            if(not self.flags is None):
                for flag in self.flags:
                    store.flags.append(flag)

        #add all msgs to phone
        def apply(self, old=False):
            self.apply_flags()
            if(not self.person_id in store.messages):
                store.messages[self.person_id] = MessageChain(self.person_id)
            messages[self.person_id].append_msgs(self.messages)


    ############################
    # standalone functions
    ############################

    def get_all_messages() -> list:
        #load the file into a list
        filename = "extras/text_messages.csv"
        msg_list = get_csv_as_list(filename)
        return msg_list


    def get_all_messages_split(to_split=None) -> list:
        if(to_split is None):
            to_split = get_all_messages()
        split_list = []
        for line in to_split:
            line_split = line.split(";")
            split_list.append(line_split)
        return split_list


    def apply_initial_conversations(p_id=None):
        if(conversations is None) or (len(conversations) == 0):
            raise Exception("Conversations not loaded!")

        initial_conversations = ["convo_stepdad01", "convo_aunty01", "convo_bff01", "convo_mom01"]

        if(p_id is None):
            for c in conversations:
                if(c.id in initial_conversations):
                    c.apply()
        else:
            for c in conversations:
                if(c.id in initial_conversations) and (c.person_id == p_id):
                    c.apply()


    def strip_from_list(somelist: list) -> list:
        for i in range(len(somelist)):
            somelist[i] = somelist[i].strip()
        return somelist


    def get_all_conversations():
        #msg_split = get_all_messages_split(manipulate_text_in_brackets_dict(get_all_messages()))
        msg_split = get_all_messages_split(get_all_messages())
        #msg_split = get_all_messages_split()
        #mgs_split = text_replacement(msg_split)
        max_line = len(msg_split) - 1 #csv files got 1 empty line at the end

        columns = {
            "convo_id" : 0,
            "person_id" : 1,
            "day" : 2,
            "sender" : 3,
            "content" : 4,
            "flags" : 5,
            "answers" : 6,
            "image" : 7,
            #"wallpaper" : 8,
            "vertical" : 8
        }

        result_list = []

        for i in range(1, max_line):
            if(msg_split[i][columns['convo_id']] == ""):
                continue

            c_id = msg_split[i][columns['convo_id']]
            p = msg_split[i][columns['person_id']]
            if config.developer and (not p in people):
                raise Exception("No person with id: " + p + " exists.")
            d = msg_split[i][columns['day']]
            if(d == ""):
                d = None
            else:
                d = int(d)
            flags = msg_split[i][columns['flags']]
            if(flags == ""):
                flags = None
            else:
                flags = flags.split(",") #always gets you a list
                flags = strip_from_list(flags)

            n = 1
            messages = []
            while((i+n < max_line) and (msg_split[i+n][columns['sender']] != "")):
                img = msg_split[i+n][columns['image']]
                if(img == ""):
                    img = None
                else:
                    check_can_load_file(FileType.PHOTO, img)

                s = msg_split[i+n][columns['sender']]
                if(s == "") and config.developer:
                    raise Exception("Sender is empty in Line " + str(i+n))
                c = msg_split[i+n][columns['content']]
                a = msg_split[i+n][columns['answers']]
                if(a == ""):
                    a = None
                else:
                    a = a.split(",")
                    a = strip_from_list(a)
                    #a = get_answer_options_by_id(a)
                # w = msg_split[i+n][columns['wallpaper']]
                # if(w == ""):
                #     w = None
                # else:
                #     check_can_load_file(FileType.WALLPAPER, w)

                v = msg_split[i+n][columns['vertical']]
                if(v == ""):
                    v = False
                else:
                    v = True

                messages.append(Msg(
                    author_id=s,
                    content=c,
                    img=img,
                    day=d,
                    answer_options=a,
                    #wallpaper=w,
                    vertical=v
                ))
                n = n + 1
                img = None
                s = None
                c = None

            i = i + n

            result_list.append(Conversation(c_id, p, flags, messages))
            messages = []
        return result_list


    def get_conversation_by_id(convo_id: str):
        for c in store.conversations:
            if(c.id == convo_id):
                return c


    def apply_single_conversation(convo_id: str):
        if(convo_id == ""):
            if config.developer:
                raise Exception("Cannot apply conversation without id!")
            return
        found_none = True
        for c in store.conversations:
            if(c.id == convo_id):
                if(not c.person_id in smartphone.msg_contacts):
                    smartphone.msg_contacts.append(c.person_id)
                c.apply()
                return

        if config.developer:
            raise Exception("No conversation with that ID could be found! id: " + convo_id)


    def manipulate_text_in_brackets_dict(string_list:list, test_mode=False, replacements=None) -> str:
        if(not type(string_list) is list):
            raise Exception("Function needs to be called with a string list, instead got: ", string_list)
        manipulated_list = []
        if(replacements is None):
            replacements = store.replacements


        for line in string_list:
            parts = line.split("[")
            manipulated_line = parts[0]

            for part in parts[1:]:
                # Split at closing bracket
                try:
                    text, remainder = part.split("]", 1)
                except ValueError:
                    raise Exception(string_list)
                replacement = replacements.get(text)
                if config.developer and (replacement is None):
                    raise Exception("Could not find a replacement for " + text)
                manipulated_line += replacement + remainder

            manipulated_list.append(manipulated_line)

        return manipulated_list


    def setup_msg_chains() -> dict:
        messages_dict = dict()
        for k,v in people.items():
            messages_dict[k] = MessageChain(k)
        return messages_dict