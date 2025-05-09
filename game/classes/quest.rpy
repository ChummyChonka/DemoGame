init python:
    from enum import Enum

    class ForcedReason(Enum):
        TODAY = 0
        WEEKDAY = 1


    class Requirements():
        def __init__(self):
            #simple attributes
            self.min_days = None    #min number of days the player spent in the game
            self.location = None    #location where the event has to be triggered

            #sets
            self.daytimes = None    #morning, midday, evening, night -> as set for multiple times
            self.weekdays = None    #mon,tue,wed,... -> as set
            self.events = None      #set -> no duplicates
            self.chars = None       #char_ids of chars that have to be present

        def set_required_gamedays(self, min_days) -> None:
            if(min_days > 0):
                self.min_days = min_days

        def set_required_location(self, location) -> None:
            self.location = location

        def add_required_daytimes(self, daytimes) -> None:
            if(self.daytimes is None):
                self.daytimes = set()
            ##1 morning, 2 midday, 3 evening, 4 night
            for time in daytimes:
                if((time > 0) and (time <= 4)):
                    self.daytimes.add(time)

        def add_required_weekdays(self, weekdays) -> None:
            if(self.weekdays is None):
                self.weekdays = set()
            ##1 monday, 2 tuesday, 3 wednesday, 4 thursday, #5 friday, 6 saturday, 7 sunday
            for day in weekdays:
                if(day < 1):
                    continue
                if(day > 7):
                    day -= 7
                self.weekdays.add(day)

        def add_required_previous_events(self, events) -> None:
            if(self.events is None):
                self.events = set()
            self.events.update(events)

        def add_required_chars(self, chars) -> None:
            if(self.chars is None):
                self.chars = set()
            self.chars.update(chars)

        def has_requirement(self) -> bool:
            if(self.location is None) and (self.daytimes is None) and (self.weekdays is None) and (self.events is None) and (self.chars is None):
                return False
            return True


    class ForcedEvents():
        def __init__(self):
            pass



    class Event():
        def __init__(self, event_id, quest_id, force_player=False, player_hint=None, guide_info=None, guide_name=None, requirements=None, manual=False):
            self.event_id = event_id                #id for this specific event, is identical to ingame label
            self.quest_id = quest_id                #id for quest this event belongs to
            self.done = False                       #flag to show if event has been completed
            self.player_hint = player_hint          #message that display when player gets forced
            self.guide_info = guide_info            #info text for guide app on phone
            self.guide_name = guide_name            #name for the event used in guide app
            self.force_player = force_player        #stop player in his tracks and force him to do this event
            self.requirements = requirements
            self.locked = False                     #disables event for the rest of the game
            self.manual = manual


            if(config.developer):
                #if(not renpy.has_label(event_id)):
                #    raise Exception("There is no label to match the event_id: " + event_id + " when trying to create an Event object.")
                if(self.event_id is None) or (self.event_id == ""):
                    raise Exception("Tried to create Event without event_id.")
                if(self.quest_id is None) or (self.quest_id == ""):
                    raise Exception("Tried to create Event without corresponding quest_id.")
                if(not self.requirements is None):
                    if(not self.requirements.has_requirement()):
                        raise Exception("Tried to create Event object with Requirements, but no requirement has been set.")

        # if all required events are done, this event counts as "unlocked"
        def is_unlocked(self) -> bool:
            # want to show locked events in the guide??
            #if self.locked:
            #    return False
            if(self.requirements is None):
                return True
            if(self.requirements.events is None):
                return True
            for event_id in self.requirements.events:
                if(not event_id.strip() in flags):
                    return False
            return True

        def force_weekday(self, weekday):
            if(weekday >= 1) and (weekday <= 7):
                self.requirements.add_required_weekdays([weekday])
                add_forced_event(self.event_id, ForcedReason.WEEKDAY)
            else:
                if config.developer:
                    raise Exception("Cannot set weekday: " + str(weekday) + " as required!")

        def force_tomorrow(self):
            self.requirements.add_required_weekdays([actualgame.weekday + 1])
            add_forced_event(self.event_id, ForcedReason.WEEKDAY)

        def force_today(self):
            add_forced_event(self.event_id, ForcedReason.TODAY)

        def requirements_debug(self, what):
            if(what == "days"):
                return self.requirements.min_days
            elif(what == "loc"):
                return self.requirements.location
            elif(what == "times"):
                return self.requirements.daytimes
            elif(what == "weekdays"):
                return self.requirements.weekdays
            elif(what == "events"):
                return self.requirements.events
            elif(what == "chars"):
                return self.requirements.chars

        def are_requirements_met(self, forced_event=False, error_out=False) -> bool:
            if(self.locked or self.done or self.event_id in flags):
                if error_out:
                    raise Exception("Event is locked or done already!")
                return False

            if(not self.requirements.daytimes is None):
                got_match = False
                for time in self.requirements.daytimes:
                    if(time == actualgame.daytime):
                        got_match = True
                        break
                if(not got_match):
                    if error_out:
                        raise Exception("Current daytime is not correct!")
                    return False

            if(not self.requirements.weekdays is None):
                got_match = False
                for day in self.requirements.weekdays:
                    if(day == actualgame.weekday):
                        got_match = True
                        break
                if(not got_match):
                    if error_out:
                        raise Exception("Current weekday is not correct!")
                    return False

            # don't check these if event is forced
            if not forced_event:
                if(not self.requirements.min_days is None):
                    if(actualgame.daycount < self.requirements.min_days):
                        if error_out:
                            raise Exception("Min days have not been reached!")
                        return False

                if(not self.requirements.location is None):
                    if(isinstance(self, Phonecall)):
                        #call partner has to be in a certain location
                        if(not self.requirements.chars is None):
                            for char in self.requirements.chars:
                                if(not person_is_char_in(char, self.requirements.location)):
                                    if error_out:
                                        raise Exception("Callee not in correct location!")
                                    return False
                    else:
                        #if(not actualgame.current_location == self.requirements.location):
                        if(not person_is_char_in("Eileen", self.requirements.location)):
                            if error_out:
                                raise Exception("Player not in correct location!")
                            return False

                if(not self.requirements.chars is None) and (not isinstance(self, Phonecall)):
                    for char in self.requirements.chars:
                        if(not person_is_char_here(char)):
                            if error_out:
                                raise Exception("Required char is not present!")
                            return False

                if(not self.requirements.events is None):
                    for event_id in self.requirements.events:
                        if(not event_id.strip() in store.flags):
                            if error_out:
                                raise Exception("Required events are not done!: " + event_id)
                            return False

            return True

        def finish_event(self) -> bool:
            if(not self.event_id in flags):
                flags.append(self.event_id)
            self.done = True
            actualgame.current_event = None
            if(self.force_player):
                remove_forced_event(self.event_id)

            loc = None
            del_list = False

            #remove Event from events_per_location dict
            for location, the_list in store.events_per_location.items():
                if(self.event_id in the_list):
                    the_list.remove(self.event_id)
                if(len(the_list) == 0):
                    del_list = True
                    loc = location
            if del_list:
                events_per_location.pop(loc)
            #renpy.notify(self.event_id + " finished!")
            return True

        def set_as_current(self) -> None:
            #if config.developer and (not actualgame.current_event is None):
                #raise Exception("Cannot set actualgame.current_event as there appears to be already an Event underway.")
            actualgame.current_event = self.event_id

        def jump(self) -> None:
            self.set_as_current()
            renpy.jump(self.event_id)


        # lock event and remove it from events_per_location dictionary
        # add event_id _locked to flags to restore locked events after load
        def lock(self) -> None:
            self.locked = True
            #remove this event from the dict -> set for that location
            if(self.requirements is None):
                return
            loc = self.requirements.location
            if(loc is None):
                return
            if(not events_per_location[loc] is None):
                events_per_location[loc].remove(self.event_id)
            flags.append(self.event_id + "_locked")


        def get_guide_info(self) -> str:
            guide_text = manipulate_text_in_brackets_dict([self.guide_info])
            if(self.requirements is None):
                return guide_text
            if(not self.requirements.min_days is None) and (actualgame.daycount < self.requirements.min_days):
                guide_text == "Wait a few more days."
            return guide_text


    class Phonecall(Event):
        def __init__(self, event_id, quest_id, force_player=False, player_hint=None, guide_info=None, guide_name=None, requirements=None):
            super().__init__(event_id, quest_id, force_player, player_hint, guide_info, guide_name, requirements)

            if(self.requirements.chars is None) and config.developer:
                raise Exception("Tried to create Phonecall object with no character to call.")
            phonecalls.append(self.event_id)


    class Quest():
        def __init__(self, quest_id, name, events):
            self.quest_id = quest_id    #for internal reference
            self.name = name            #to be displayed for user
            self.done = False           #flag to show if this quest has been completed
            self.active = False         #has this quest been started?
            self.events = events        #list of event objects that make up the quest

            if config.developer:
                if(self.quest_id is None) or (self.quest_id == ""):
                    raise Exception("Tried to create Quest without quest_id.")
                if(self.name is None) or (self.name == ""):
                    raise Exception("Tried to create Quest without a name.")
                if(self.events is None) or (len(self.events) == 0):
                    raise Exception("Tried to create Quest without any Events.")

        def finish_quest(self) -> None:
            self.done = True

        def is_unlocked(self) -> bool:
            if(self.quest_id == "exclusives") and (not renpy.has_label("start_select")):
                return False
            for event in self.events:
                if(event.is_unlocked()):
                    return True
            return False

        # def get_guide_info(self) -> str:
        #     for event in self.events:
        #         if(not event.done) and (not event.locked):
        #             return event.get_guide_info()
        #     return "Quest has been completed"


########################
# standalone functions #
########################

    def lock_event_by_id(event_id:str):
        ev = get_event_by_id(event_id)
        if(not ev is None):
            ev.lock()


    def get_unlocked_quests() -> dict:
        return {quest.quest_id: quest.name for quest in store.quests if quest.is_unlocked()}


    def lock_current_event():
        if(actualgame.current_event is None):
            if config.developer:
                raise Exception("Cannot lock current event, as there seems to be no Event ongoing.")
            pass
        else:
            get_event_by_id(actualgame.current_event).lock()
            actualgame.block_calls = False
            phone_hud_hide = False


    def finish_current_event():
        if(actualgame.current_event is None):
            if config.developer:
                renpy.notify("ERROR: Could not finish event -> No event ongoing!")
                #raise Exception("Cannot finish current event, as there seems to be no Event ongoing.")
            pass
        else:
            event_id = actualgame.current_event
            if(isinstance(actualgame.current_event, Event)):
                event_id = actualgame.current_event.event_id
            if(not get_event_by_id(event_id).finish_event()):
                raise Exception("finish_current_event(): could not actually finish the event.")
            actualgame.block_calls = False
            phone_hud_hide = False


    def finish_event_by_id(event_id:str):
        ev = get_event_by_id(event_id)
        if(ev is None) and config.developer:
            raise Exception("Cannot find Event with id: " + event_id)
        ev.finish_event()
        actualgame.block_calls = False


    def trigger_next_event():
        #check for any events
        #if one event possible -> jump to label
        set_of_events = store.events_per_location.get(actualgame.current_location)
        if(set_of_events is None):
            return
        for event_id in set_of_events:
            event = get_event_by_id(event_id)
            if event.manual:
                continue
            if(event.event_id in actualgame.daily_event_attempt):
                continue
            if event.are_requirements_met():
                actualgame.block_calls = True
                hide_all_location_screens()
                renpy.show_screen("actions_default")
                event.jump()


    #takes event_id and sets that event as current_event
    def set_current_event(event_id:str) -> None:
        actualgame.block_calls = True
        event = get_event_by_id(event_id)
        #if(not event is None):
        event.set_as_current()
            #if(hide_phone_ui_during_events):
            #    phone_hud_hide = True
            #renpy.notify(event.event_id + " started!")


    #returns event object that matches event_id
    def get_event_by_id(event_id:str) -> Event:
        for i in range(len(quests)):
            for j in range(len(quests[i].events)):
                if(quests[i].events[j].event_id == event_id):
                    return quests[i].events[j]
        return None


    def load_quests() -> list:
        store.events_per_location = dict()

        quests_file = "extras/quests.csv"
        if(renpy.loadable(quests_file)):
            opened_file = renpy.open_file(quests_file)
            file_data = opened_file.read()
            byte_list = file_data.split(b"\n")
            data_list = []
            for line in byte_list:
                data_list.append(line.decode('utf-8'))

            

            quests = []
            for line in range(3, len(data_list)):
                line_split = data_list[line].split(";")
                if(line_split[0] != ""):
                    quest_id = line_split[0]
                    no_events = int(line_split[1])
                    quest_name = line_split[3]

                    events = []
                    for i in range(no_events):
                        line += 1
                        force = False
                        player_hint = None
                        loc = None
                        reqs = None
                        guide_info = None
                        guide_name = None
                        manual = False

                        line_split = data_list[line].split(";")
                        event_id = line_split[2]
                        get_event_description(event_id, debug=True) #will cause error if not developer and a description is missing
                        is_phonecall = False
                        if(event_id.startswith("phonecall_")):
                            is_phonecall = True

                        if(line_split[4] != ""):
                            force = True
                            player_hint = line_split[12]
                            manipulate_text_in_brackets_dict([line_split[12]], test_mode=True)

                        if(line_split[13] != ""):
                            guide_info = line_split[13]
                            manipulate_text_in_brackets_dict([line_split[13]], test_mode=True)

                        if(line_split[14] != ""):
                            guide_name = line_split[14]

                        if(line_split[15] != ""):
                            if(line_split[15] == "TRUE"):
                                manual = True
                            else:
                                manual = False
 

                        #days	weekday	time	events	char	location
                        if(line_split[5] != ""): #has requirements
                            reqs = Requirements()

                            #min game days -> single value
                            if(not line_split[6] == ""):
                                reqs.set_required_gamedays(int(line_split[6]))

                            #weekdays -> can be multiple
                            if(not line_split[7] == ""):
                                weekdays_split = line_split[7].split(",")
                                for i in range(len(weekdays_split)):
                                    weekdays_split[i] = int(weekdays_split[i])
                                reqs.add_required_weekdays(weekdays_split)

                            #daytimes -> can be multiple
                            if(not line_split[8] == ""):
                                daytimes_split = line_split[8].split(",")
                                for i in range(len(daytimes_split)):
                                    daytimes_split[i] = int(daytimes_split[i])
                                reqs.add_required_daytimes(daytimes_split)

                            #events -> can be multiple
                            if(not line_split[9] == ""):
                                events_split = line_split[9].split(",")
                                reqs.add_required_previous_events(events_split)

                            #chars -> can be multiple
                            if(not line_split[10] == ""):
                                chars_split = line_split[10].split(",")
                                chars = []
                                for char in chars_split:
                                    chars.append(char)
                                reqs.add_required_chars(chars)

                            #location -> single value
                            if(not line_split[11] == ""):
                                loc = get_location_by_name(line_split[11])
                                if(not loc is None):
                                    reqs.set_required_location(loc)

                        if is_phonecall:
                            events.append(Phonecall(event_id, quest_id, force, player_hint, guide_info, guide_name, reqs))
                        else:
                            new_event = Event(event_id, quest_id, force, player_hint, guide_info, guide_name, reqs, manual)
                            #events.append(Event(event_id, quest_id, force, player_hint, reqs))
                            events.append(new_event)
                            #print(event_id + " -> " + str(loc))

                            if(not loc is None) and (manual == False):
                                if(store.events_per_location.get(loc) is None):
                                    store.events_per_location[loc] = [new_event.event_id]
                                else:
                                    store.events_per_location[loc].append(new_event.event_id)

                        loc = None

                    quests.append(Quest(quest_id, quest_name, events))
            return quests


    def get_next_call_by_callee(c_id):
        for c in phonecalls:
            ev = get_event_by_id(c)
            if(not ev is None):
                if(c_id in ev.requirements.chars) and (ev.are_requirements_met()):
                    return ev
        return None



###############################################################
######################## FORCED EVENTS ########################
###############################################################
    def add_forced_event(event_id: str, reason: ForcedReason):
        if config.developer:
            if(event_id is None) or (reason is None):
                raise Exception("Tried to add an Event to ForcedEvents without a proper Event or Reason.")
            if not get_event_by_id(event_id).force_player:
                raise Exception("Tried to add an Event to ForcedEvents that is not a forced event.")
        if get_event_by_id(event_id).force_player:
            actualgame.forced_events[event_id] = reason

    def remove_forced_event(event_id:str):
        if(event_id in actualgame.forced_events):
            actualgame.forced_events.pop(event_id)

    def handle_forced_event() -> None:
        for event_id, reason in actualgame.forced_events.items():
            if(event_id == "FORCE_EVENT"):
                continue
            event = get_event_by_id(event_id)
            if(reason is ForcedReason.TODAY):
                if(event.requirements.daytimes is None):
                    continue
                if(event.are_requirements_met(forced_event=True)):
                    actualgame.forced_events["FORCE_EVENT"] = event_id
                    renpy.jump("forced_event_base")
            elif(reason is ForcedReason.WEEKDAY):
                if(event.requirements.weekdays is None):
                    continue
                if(event.are_requirements_met(forced_event=True)):
                    actualgame.forced_events["FORCE_EVENT"] = event_id
                    renpy.jump("forced_event_base")


    def force_jump() -> None:
        if(not "FORCE_EVENT" in actualgame.forced_events):
            if config.developer:
                raise Exception("No forced event currently set!")
            else:
                renpy.jump("main_game")

        event = get_event_by_id(actualgame.forced_events["FORCE_EVENT"])
        actualgame.current_location = event.requirements.location
        event.jump()

