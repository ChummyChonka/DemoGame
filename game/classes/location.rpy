init python:
    from enum import Enum

    class Location(Enum):
        ERROR = 0
        EMPTY = 1
        MAP = 2

        HOME = 3
        HOME_DOWNSTAIRS = 4
        HOME_UPSTAIRS = 5
        HOME_BATHROOM = 6

        GYM = 7
        GYM_TOILET = 8
        GYM_OFFICE = 9
        GYM_YOGA = 10
        GYM_ACTUAL = 11
        GYM_SAUNA = 12
        GYM_LOCKERROOM = 13
        GYM_RECEPTION = 14
        GYM_SHOWERS = 15

        CAFE = 16
        ESCAPEROOM = 17
        DELPHI = 18
        PARK = 19
        OFFICE = 20

        UNI = 21
        UNI_MAIN = 22
        UNI_LECTURE = 23
        UNI_VICTORIA = 24
        DORMS = 25
        DORMS_ASTER = 26

        STUDIO = 27

        MOMS = 28
        MOMS_POOL = 29
        MOMS_FIRSTFLOOR = 30
        MOMS_SUNDECK = 31
        MOMS_DAD = 32
        MOMS_MASTER = 33
        MOMS_BATHROOM = 34
        MOMS_GUEST = 35

        NA_HOME = 36
        NA_WORK = 37
        NA_OUT = 38
        NA_GARDEN = 39
        NA_GROCERIES = 40
        NA_SHOPPING = 41

        GASSTATION = 42
        DINER = 43
        CINEMA = 44



    # gym       =>  reception, lockerroom, showers, sauna, toilet, yoga studio
    # home      =>  downstairs, upstairs, bathroom
    # moms      =>  first floor, sundeck, pool
    # cafe      =>  
    # uni       =>  entrance, lecture hall
    # dorms     =>  hall, aster's room
    # park      => 
    # studio    =>
    # club      =>
    # escaper.  =>
    # map       =>



    def get_location_names(sort_list=True) -> list:
        location_list = [location.name for location in Location]
        if sort_list:
            return sorted(location_list)
        return location_list


    def get_major_location_by_sublocation(sublocation:Location) -> Location:
        return get_location_by_name(sublocation.name.split("_")[0])


    def get_location_list() -> list:
        return [location for location in Location]


    def get_location_by_name(name:str) -> Location:
        if(name == "") or (name is None):
            return Location.EMPTY

        location_list = get_location_list()
        for loc in location_list:
            #if(str(loc).split(".")[1] == name):
            if(loc.name == name.upper()):
                return loc
        return Location.ERROR


    def jump_to_current_location():
        jump_to_location(actualgame.current_location)


    def jump_to_location(loc:Location):
        loc_labels = {
            Location.GYM : "location_gym",
            Location.GYM_LOCKERROOM : "gym_lockerroom",
            Location.GYM_YOGA: "gym_yoga_studio",
            Location.GYM_OFFICE : "gym_office",
            Location.GYM_ACTUAL : "gym_actual",
            Location.GYM_RECEPTION : "gym_reception",
            Location.GYM_SAUNA : "gym_sauna",
            Location.GYM_TOILET : "gym_toilet"
        }

        if(not loc in loc_labels.keys()):
            if config.developer:
                raise Exception("Location not implemented yet: " + str(loc.name))
            return
        renpy.jump(loc_labels[loc])


    def does_location_match(target_loc:Location, comp_loc:Location):
        if(comp_loc in [Location.MOMS, Location.GYM, Location.HOME, Location.UNI, Location.DORMS]):
            loc_list = [loc for loc in Location if loc.name.startswith(comp_loc.name) and not loc.name is comp_loc.name]
            if(target_loc in loc_list):
                return True
            return False
        else:
            if(target_loc == comp_loc):
                return True
            return False



