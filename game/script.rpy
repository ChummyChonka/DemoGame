
style block2_multiple2_namebox:
    xpos (3840 - gui.name_xpos)
    xalign 1.0

style block1_multiple2_say_dialogue:
    xalign 0.35
    xmaximum 1000

style block2_multiple2_say_dialogue:
    xalign 0.65
    xmaximum 1000

transform kawase_blur:
    shader "wm.kawase_background"
    u_lod_bias 4.0 u_iteration 4.0

transform kawase_blur_darken:
    matrixcolor TintMatrix("#282828")
    shader "wm.kawase_background"
    u_lod_bias 4.0 u_iteration 4.0

define e = Character("Eileen")
default protagonist = Protag("Eileen", money=1735, fitness=7, lust_energy=3, horny=9, confidence=2)

default actualgame.is_demo = True

#contacts
default person.protag = {
    "name" : "Eileen",
    "display_name" : "Eileen",
    "surname" : "Bulbiferum"
    }
default person.bff = {
    "name" : "Aster",
    "surname" : "Lungwort",
    "nickname" : "Bestie",
    "display_name" : "Aster",
    "is_dateable" : True
    }
default person.mom = {
    "name" : "Sophia",
    "display_name" : "Sophia",
    "surname" : "Walker"
    }
default person.cousin = {
    "name" : "Laura",
    "nickname" : "Shortie",
    "display_name" : "Laura",
    "unknown" : True,
    "surname" : "Auratum"
    }
default person.aunt = {
    "name" : "Natalie",
    "is_dateable" : True,
    "display_name" : "Natalie",
    "surname" : "Auratum"
    }
default person.stepdad = {
    "name" : "Christopher",
    "nickname" : "Chris",
    "display_name" : "Chris",
    "surname" : "Walker",
    "use_nickname" : True
    }
default person.boss = {
    "name" : "Theodore",
    "nickname" : "Teddy",
    "display_name" : "Teddy",
    "surname" : "Clark",
    "use_nickname" : True,
    "unknown" : True,
    }
default person.jessica = {
    "name" : "Jessica",
    "surname" : "Santos",
    "nickname" : "Jess",
    "display_name" : "Jessica",
    "unknown" : True
    }
default person.emily = {
    "name" : "Emily",
    "display_name" : "Emily",
    "surname" : "King",
    "unknown" : True
    }
default person.sarah = {
    "name" : "Sarah",
    "display_name" : "Sarah",
    "surname" : "Jones",
    "unknown" : True
    }
default person.harper = {
    "name" : "Harper",
    "surname" : "Ranch",
    "nickname" : "Mrs. Ranch",
    "display_name" : "Mrs. Ranch",
    "use_nickname" : True,
    "unknown" : True
    }
default person.olivia = {
    "name" : "Olivia",
    "display_name" : "Olivia",
    "surname" : "Nguyen",
    "unknown" : True
    }
default person.victoria = {
    "name" : "Victoria",
    "nickname" : "Ms. Burke",
    "surname" : "Burke",
    "use_nickname" : True,
    "unknown" : True
    }
default person.bianca = {
    "name" : "Bianca",
    "display_name" : "Bianca",
    "surname" : "Martin",
    "unknown" : True
    }
default person.isabella = {
    "name" : "Isabella",
    "nickname" : "Bella",
    "display_name" : "Isabella",
    "surname" : "Martinez",
    "unknown" : True
    }
default person.patricia = {
    "name" : "Patricia",
    "surname" : "Galvin",
    "display_name" : "Patricia",
    "unknown" : True
    }
default person.gwen = {
    "name" : "Gwendolyn",
    "nickname" : "Gwen",
    "display_name" : "Gwendolyn",
    "surname" : "Wagner",
    "unknown" : True
    }

#("Aster", "Sophia", "Laura", "Natalie", "Christopher", "Theodore", "Jessica", "Sarah")
default people = {
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


default day_schedules = dict()
default messages = dict()

#pet names
default petnames_for_protag = {
    "Natalie" : "sweetie",
    "Aster" : "babe",
    "Sophia" : "honey",
    "Christopher" : "little gremlin",
    "Jessica" : "sexy",
    "Tom" : "queen",
    "Sarah" : "precious",
    "Isabella" : "Mistress",
    "Theodore" : "my dear",
    "Patricia" : "hotshot",
    }

default petnames_from_protag = {
    "Aster" : "sweetcheeks",
    "Isabella" : "maid"
    }

default flags = []
default phonecalls = []
default actualgame.block_calls = False

default extra_char_names = get_extra_char_names()
default replacements = load_replacements_dict()
default quests = []


default main_menu_hovered_option = None
default quick_menu_pref_hidden = False
default good_shit_enabled = False
default phone_say_hidden = False
default phone_hud_hide = False

default actualgame.quickmenuxalign = 0.5
default actualgame.dialogueBoxOpacity = 0.9

#base game stats
default actualgame.cheats_enabled = True
default actualgame.stat_checks_notification = True
default actualgame.weekday = 4 # 1 monday, 2 tuesday, 3 wednesday, 4 thursday, 5 friday, 6 saturday, 7 sunday
default actualgame.weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
default actualgame.daytime = 2 # 1 morning, 2 midday, 3 evening, 4 night
default actualgame.times = ["Morning", "Midday", "Evening", "Night"]
default actualgame.daycount = 0
default actualgame.content_hints = False
default actualgame.extra_symbols = False
default actualgame.current_location = Location.HOME
default actualgame.current_event = None
default actualgame.forced_events = dict()
#default actualgame.registered_labels = [None for x in range(4*7)]
default actualgame.registered_labels = dict()
default actualgame.daily_event_attempt = []
default actualgame.dateable = []
default actualgame.guide_selected_quest = 0
default actualgame.increase_hud_size = True
default actualgame.location_hovered = None
default actualgame.renamer_person = None
default actualgame.heart_overlay = True

# SMARTPHONE
default smartphone.backgrounds = ["black", "frog", "jessica_nude01", "jessica_nude02", "sarah01", "aster_nude01", "laura_pool01", "patricia_lingerie01", "patricia_lingerie02"]
default smartphone.current_bg = "frog"
default smartphone.actualphone = "images/smartphone/smartphone.webp"
default smartphone.overlay = "images/smartphone/smartphone_overlay_main.webp"
default smartphone.app_overlay = "images/smartphone/smartphone_app_overlay.webp"
default smartphone.notificationbar = "images/smartphone/smartphone_notificationbar_translucent.webp"

default smartphone.mini_idle = "images/smartphone/smartphone_idle.webp"
default smartphone.mini_hover = "images/smartphone/smartphone_hover.webp"
default smartphone.mini_ringing_idle = "images/smartphone/smartphone_ringing_idle.webp"
default smartphone.mini_ringing_hover = "images/smartphone/smartphone_ringing_hover.webp"

default smartphone.msg_text_color = "#000000"
default smartphone.msg_age = 0
default smartphone.msg_their_box = "images/smartphone/msgboxes/phonemsg32.webp"
default smartphone.msg_your_box = "images/smartphone/msgboxes/phonemsg33.webp"
default smartphone.date_divider_bar = True
default smartphone.date_divider_upper = False
default smartphone.date_divider_pos = "center"

default smartphone.battery_level = 90
default smartphone.time = "14:12"
default smartphone.clock24hours = True
default smartphone.time_is_pm = True

default smartphone.enabled = False

default smartphone.is_ringing = False
default smartphone.notification = False

default smartphone.content_stack = ["smartphone_apps_new"]
default smartphone.base_screens = ["smartphone", "smartphone_bot_controls"]

default smartphone.photos = [Photo("black"), Photo("frog")]
default smartphone.photo_full = False

default smartphone.hovered_contact = None
default smartphone.selected_contact = "Aster"
default smartphone.choosing_answer = False

default smartphone.guide_hovered_event = None
default smartphone.guide_opened_event = None


#gallery
default app_icons = load_app_icons()
default app_icons_hovered = load_app_icons_hovered()
default apps = load_apps()

default smartphone.overlay_opacity = 0.8
default smartphone.overlay_app_opacity = 0.0

#only contacts are displayed in smartphone
default smartphone.contacts = get_smartphone_contacts()
default smartphone.msg_contacts = get_smartphone_contacts()



default scheduleeditor.selected_char = None
default scheduleeditor.selected_loc = None
default scheduleeditor.selected_box = [None, None, None]
default scheduleeditor.schedules = None

default debug_actions = {
    "schedule editor" : open_schedule_editor
}
default debug_labels = dict()

default gamemusic = GameMusic()

define audio.phone_notification = "audio/phone_notification.comp.ogg"

default gamemap = {
    "escaperoom" : True,
    "photostudio": True
    }
default gamemap_colored_pins = False

# The game starts here.

label start:
    $ quests = load_quests()
    $ finish_event_by_id("event_demo01")
    $ finish_event_by_id("event_demo02")
    $ finish_event_by_id("event_demo03")
    $ get_event_by_id("event_demo07").lock()

    $ check_all_mandatory_names()
    $ conversations = get_all_conversations()
    $ messages = setup_msg_chains()
    #$ apply_initial_conversations()
    #initial_conversations = ["convo_stepdad01", "convo_aunty01", "convo_bff01", "convo_mom01"]
    $ get_conversation_by_id("convo_stepdad01").apply()
    $ get_conversation_by_id("convo_aunty01").apply()
    $ get_conversation_by_id("convo_bff01").apply()
    $ get_conversation_by_id("convo_mom01").apply()
    $ get_conversation_by_id("convo_teddy01").apply()
    $ store.messages["Theodore"].messages[-1].choose_answer(1)
    $ get_conversation_by_id("convo_jessica01").apply()
    $ get_conversation_by_id("convo_sarah01").apply()
    $ get_conversation_by_id("convo_sarah02").apply()
    $ get_conversation_by_id("convo_sarah03").apply()
    $ set_read_all()

    $ get_conversation_by_id("laura_pool_convo01").apply()

    $ make_all_contacts_known()
    $ smartphone.enabled = True

    $ set_daily_schedules()
    $ choose_fixed_location_for_chars()

    $ renpy.block_rollback()

    $ preferences.set_mixer("music", 0.5)
    $ actualgame.current_location = Location.DINER
    if(renpy.loadable("audio/Pleasant_Porridge.mp3")):
        $ gamemusic.play_song("audio/Pleasant_Porridge.mp3")
    scene diner with fade
    show screen navigation_button
    e "Welcome to this demonstration."
    window hide

    show showoff_overlay with dissolve
    pause
    jump location_diner

