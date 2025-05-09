
init python:


    def get_event_description(event_id: str, debug=False) -> str:

        # Intro
        #######################################################################
        if(event_id == "event_demo01"):
            return "You are shocked by the announcement of the king's abdication. What change might come from this?"
        elif(event_id == "event_demo02"):
            return "[person_get_name('Aster')] and you have a wonderful time catching up."
        elif(event_id == "event_demo03"):
            return "[person_get_display_name('Sophia')] keeps going on and on about the many ways [person_get_display_name('Christopher')] is annoying her day after day."
        elif(event_id == "event_demo04"):
            return ""

        # Learn About Self
        ######################################################################
        elif(event_id == "event_demo05"):
            return ""
        elif(event_id == "event_demo06"):
            return ""
        elif(event_id == "event_demo07"):
            return ""


        if config.developer:
            raise Exception("Description missing for Event: " + event_id)
        return "There is no description for this event."

