init python:
    from enum import Enum

    class AppDo(Enum):
        PUSH = 1
        URL = 2

    class App:
        def __init__(self, name, display_name, disabled=False, url=None):
            self.name = name
            self.display_name = display_name
            self.disabled = disabled
            self.hovered = False
            if(not url is None):
                self.function=AppDo.URL
            else:
                self.function=AppDo.PUSH
            self.url = url

            if config.developer:
                if(name is None) or (name == ""):
                    raise Exception("Can't create App object without a name!")
                if(display_name is None) or (display_name == ""):
                    raise Exception("Can't create App object without a display_name!")

        def enable(self):
            self.disabled = False

        def get_icon(self, hovered=False):
            if(hovered):
                return app_icons_hovered[self.name]
            else:
                return app_icons[self.name]


    # standalone functions
    ###############################################

    def get_app_by_name(app_name):
        for i in range(len(apps)):
            if(apps[i].name == app_name):
                return apps[i]
