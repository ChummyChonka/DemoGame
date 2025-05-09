init python:
    import time
    last_vp_change = 0

    class OnViewportChange(Action):
        """
        Class for a 'changed' callback for a viewport whose scroll position is to be saved.
        When the viewport position changes, the __call__ function is run.
        """
        def __init__(self):
            pass

        def __call__(self, value):
            store.messages[smartphone.selected_contact].scroll_position = value


    def initialize_adjustment():
        """
        Returns the yadjustment property for a viewport whose scroll position is to be saved.
        """
        return ui.adjustment(range=1, value=get_current_viewport_position(), changed=OnViewportChange())


    def get_current_viewport_position():
        return store.messages[smartphone.selected_contact].scroll_position


    #pressing square button
    def hide_all_phone_screens():
        store_msg_adjustment(smartphone.content_stack[len(smartphone.content_stack) - 1])
        renpy.hide_screen("call_confirmation")
        #smartphone_reset_content()
        smartphone_screen_pop()

        for i in range(len(smartphone.base_screens)):
            renpy.hide_screen(smartphone.base_screens[i])


    def smartphone_reset_content():
        smartphone.overlay_app_opacity = 0.0
        active_content = len(smartphone.content_stack) - 1
        renpy.hide_screen(smartphone.content_stack[active_content])
        #smartphone.content_stack = ["smartphone_apps"]
        smartphone.content_stack = ["smartphone_apps_new"]


    #pressing circle button
    def smartphone_home():
        store_msg_adjustment(smartphone.content_stack[len(smartphone.content_stack) - 1])
        for scr in smartphone.content_stack:
            if(not scr in smartphone.base_screens):
                renpy.hide_screen(scr)
        smartphone.content_stack = ["smartphone_apps_new"]
        renpy.show_screen(smartphone.content_stack[0])
        smartphone.overlay_app_opacity = 0.0


    def do_mini_phone():
        if(smartphone.is_ringing):
            pass
        else:
            #SHOW
            if(renpy.get_screen("smartphone") is None) and (renpy.get_screen("smartphone_small") is None):
                #renpy.call_in_new_context("testing_context")
                renpy.suspend_rollback(True)
                config.rollback_enabled = False
                #config.allow_skipping = False
                #config.keymap["rollforward"].remove("mousedown_5")
                smartphone_update()

            #HIDE
            else:
                hide_all_phone_screens()

                renpy.suspend_rollback(False)
                config.rollback_enabled = True
                #config.allow_skipping = True
                #config.keymap["rollforward"].append("mousedown_5")
                renpy.hide_screen(smartphone.content_stack[0])


    def unhover_apps() -> None:
        for i in range(len(apps)):
            apps[i].hovered = False


    def smartphone_update():
        unhover_apps()
        for i in range(len(smartphone.base_screens)):
            if(not renpy.get_screen(smartphone.base_screens[i])):
                renpy.show_screen(smartphone.base_screens[i])
                #renpy.call_screen(smartphone.base_screens[i])
        active_content = len(smartphone.content_stack) - 1
        renpy.show_screen(smartphone.content_stack[active_content])
        #renpy.call_screen(smartphone.content_stack[active_content])


    def smartphone_screen_push(new_content_screen, contact=None, img=None, vertical=False, wallpaper=None, photo=None):
        smartphone.overlay_app_opacity = 1.0
        if(new_content_screen == "contacts"):
            sort_contacts()
        #if(new_content_screen == "gallery"):
        #    smartphone.gallery.prep_page()
        # if("small" in config.variants):
        #     new_content_screen = new_content_screen + "_small"
        active_content = len(smartphone.content_stack) - 1

        # msg_chain + messages can be open at the same time
        # must make sure there is only ONE msg_chain screen at once
        if(new_content_screen == "msg_chain"):
            if("msg_chain" in smartphone.content_stack):
                #smartphone_screen_pop()
                renpy.hide_screen(smartphone.content_stack[-1])
                smartphone.content_stack.pop(len(smartphone.content_stack) - 1)
            smartphone.content_stack.append(new_content_screen)
            renpy.show_screen(new_content_screen, contact)

        elif(new_content_screen == "photo_view"):
            #renpy.show_screen(new_content_screen, contact, img, vertical, wallpaper)
            renpy.hide_screen("gallery")
            #renpy.hide_screen("msg_chain")
            renpy.hide_screen("messages")
            # if photo.vertical:
            #     renpy.show_screen("photo_view_vertical", photo)
            # else:
            #     renpy.show_screen("photo_view_horizontal", photo)
            renpy.show_screen(new_content_screen, photo)
            smartphone.content_stack.append(new_content_screen)

        else:
            renpy.hide_screen(smartphone.content_stack[active_content])
            smartphone.content_stack.append(new_content_screen)
            renpy.show_screen(new_content_screen)


    def smartphone_screen_pop(param=None):
        if(len(smartphone.content_stack) == 1):
            return

        if("photo_view" in smartphone.content_stack):
            smartphone.photo_full = False
            #renpy.hide_screen("photo_view_horizontal")
            #renpy.hide_screen("photo_view_vertical")
            renpy.hide_screen("photo_view")
            smartphone.content_stack.remove("photo_view")
            if("gallery" in smartphone.content_stack):
                renpy.show_screen("gallery")
            else:
                renpy.show_screen("messages")
                #renpy.show_screen("msg_chain")
            return

        elif("app_settings" in smartphone.content_stack):
            renpy.hide_screen("app_settings")
            smartphone.content_stack.remove("app_settings")
            renpy.show_screen("settings")
            return

        while(True):
            unhover_apps()
            active_content = len(smartphone.content_stack) - 1
            screenname = smartphone.content_stack[active_content]
            store_msg_adjustment(screenname)
            renpy.hide_screen(screenname)
            smartphone.content_stack.pop(active_content)
            active_content = len(smartphone.content_stack) - 1 
            if(param == None):
                renpy.show_screen(smartphone.content_stack[active_content])
            else:
                renpy.show_screen(smartphone.content_stack[active_content], param)
            if(len(smartphone.content_stack) == 1):
                smartphone.overlay_app_opacity = 0.0
                break


    def store_msg_adjustment(screenname):
        if(renpy.get_screen("answer_options")):
            renpy.hide_screen("answer_options")
        #if(screenname == "msg_chain"):
        #    renpy.notify(smartphone.opened_contact.name)


    def set_app_hovered(name, val):
        for i in range(len(apps)):
            if(apps[i].name == name):
                apps[i].hovered = val


    def show_screen_answers(contact, msg):
        if(config.developer):
            renpy.notify(msg.answer_options)
        #renpy.show_screen("answer_options", msg.answer_options)
        renpy.show_screen("answer_options", contact, msg)


    def get_msgboxes_list() -> list:
        msgboxes_list = list()
        #exclude_list = [5, 6, 7]
        msgbox_list = [32, 4, 14, 30, 33, 3, 15, 18, 34, 29]
        for num in msgbox_list:
            if(num < 10):
                num = "0" + str(num)
            num = str(num)
            msgboxes_list.append("images/smartphone/msgboxes/phonemsg" + num + ".webp")
        return msgboxes_list


    def put_day_divider(msg) -> bool:
        msg_age = get_msg_age(msg)
        if(smartphone.msg_age != msg_age):
            smartphone.msg_age = msg_age
            return True
        return False


    def get_msg_age(msg) -> int:
        age = 0
        age = actualgame.daycount - msg.day
        if(age < 0):
            age = 0
        return age


    def get_msg_age_text(msg) -> str:

        age_dict = {
            0: "today",
            1: "yesterday",
            2: "two days ago",
            3: "three days ago",
            4: "four days ago",
            5: "five days ago",
            6: "six days ago",
            7: "one week ago",
            14: "two weeks ago",
            21: "three weeks ago",
            28: "four weeks ago",
            30: "one month ago",
            60: "two months ago",
            90: "three months ago",
            120: "four months ago",
            150: "five months ago",
            180: "half a year ago",
            365: "one year ago",
            730: "two years ago",
            1095: "thee years ago",
            1460: "four years ago",
            1825: "five years ago",
            2000: "in an ancient past"
        }

        msg_age = get_msg_age(msg)
        sorted_keys = sorted(age_dict.keys())
        largest_key = 0
        for key in sorted_keys:
            if key <= msg_age:
                largest_key = key
            else:
                break
        if smartphone.date_divider_upper:
            return age_dict[largest_key].upper()
        return age_dict[largest_key]


    def reset_msg_age():
        smartphone.msg_age = 0


    def set_msg_divider_age(msg):
        smartphone.msg_age = get_msg_age(msg)


    def reset_message_screen():
        '''
        Hides msg_chain screen and shows it again.
        '''
        smartphone_screen_pop()
        smartphone_screen_push("messages")


    def scroll_down(contact, amount=1000):
        '''
        Increases position of viewport for Person.
        '''
        #contact.msgs.scroll_position += amount
        store.messages[contact].scroll_position += amount
        reset_message_screen()
        #messages[contact]["scroll_position"] += amount


    def handle_new_answer(contact, msg, option):
        if(not msg.answer_options is None):
            for i in range(len(msg.answer_options)):
                if(msg.answer_options[i] == option):
                    msg.choose_answer(i)
                    store.messages[contact].set_read()
                    #contact.set_messages_read()
                    scroll_down(contact)
                    return
        #msg.choose_answer(option)
        #msg.answered = True
        #apply_single_conversation(option)


    def set_guide_quest_number(increase=True):
        current_quest = store.quests[actualgame.guide_selected_quest].quest_id
        key_list = list(get_unlocked_quests().keys())
        counter = 0
        for q in key_list:
            if(q == current_quest):
                break
            counter += 1

        if increase:
            counter += 1
        else:
            counter -= 1

        actualgame.guide_selected_quest = [q.quest_id for q in store.quests].index(key_list[counter])


    def enable_guide_forward_arrow() -> bool:
        unlocked_quests = list(get_unlocked_quests().keys())
        the_key = store.quests[actualgame.guide_selected_quest].quest_id

        if(the_key in unlocked_quests):
            index = unlocked_quests.index(the_key)
            return index < len(unlocked_quests) - 1
        else:
            return False



    def switch_12_hour_clock(do_12_hours=False):
        if not do_12_hours and smartphone.clock24hours:
            return
        if do_12_hours and not smartphone.clock24hours:
            return
        hours, minutes = smartphone.time.split(":")
        hours = int(hours)
        minutes = int(minutes)
        # 24h -> 12h
        if do_12_hours:
            smartphone.clock24hours = False
            if(hours > 12):
                hours -= 12
            elif(hours == 0):
                hours = 12
        # 12h -> 24h
        else:
            smartphone.clock24hours = True
            if smartphone.time_is_pm and (hours < 12):
                hours += 12
            else:
                if(hours == 12):
                    hours = 0

        if smartphone.clock24hours and hours < 12:
            smartphone.time = "0" + str(hours) + ":" + str(minutes)
        else:
            smartphone.time = str(hours) + ":" + str(minutes)


    def set_current_contact(p_id: str):
        if(p_id == ""):
            smartphone.selected_contact = None
        else:
            smartphone.selected_contact = p_id

