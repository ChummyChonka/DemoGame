
screen succubus_menu():
    zorder 100
    vbox:
        xalign 1.0
        spacing 10

        if not phone_hud_hide:
            hbox:
                style_prefix "succubus"
                text actualgame.times[actualgame.daytime-1]:
                    outlines [(4, "#000000", 2, 2)]
                    kerning 2
                    if("small" in config.variants) or actualgame.increase_hud_size:
                        size 100
                        ypos +30
                    else:
                        ypos +8
                        size 66

                imagebutton:
                    if(smartphone.is_ringing):
                        if(smartphone.notification):
                            idle Composite((1000,1000), (0,0), "images/smartphone/smartphone_ringing_idle.webp", (0,0), "images/smartphone/smartphone_idle_notification.webp")
                            hover Composite((1000,1000), (0,0), "images/smartphone/smartphone_ringing_hover.webp", (0,0), "images/smartphone/smartphone_hover_notification.webp")
                        else:
                            auto "images/smartphone/smartphone_ringing_%s.webp"
                    else:
                        if(not smartphone.enabled):
                            tooltip "Disabled"
                            if(smartphone.notification):
                                idle Composite((1000,1000), (0,0), "images/smartphone/smartphone_disabled_idle.webp", (0,0), "images/smartphone/smartphone_idle_notification.webp")
                            else:
                                idle "images/smartphone/smartphone_disabled_idle.webp"
                        else:
                            if(smartphone.notification):
                                idle Composite((1000,1000), (0,0), "images/smartphone/smartphone_idle.webp", (0,0), "images/smartphone/smartphone_idle_notification.webp")
                                hover Composite((1000,1000), (0,0), "images/smartphone/smartphone_hover.webp", (0,0), "images/smartphone/smartphone_hover_notification.webp")
                            else:
                                auto "images/smartphone/smartphone_%s.webp"
                    if("small" in config.variants) or actualgame.increase_hud_size:
                        at mobile_phonezoom
                    else:
                        at phonezoom
                    if(smartphone.enabled):
                        action Function(do_mini_phone)

        if actualgame.extra_symbols:
            hbox:
                xalign 1.0

                vbox:
                    #LUST ENERGY
                    imagebutton:
                        tooltip "Lust Energy"
                        idle "images/smartphone/extrasymbols/symbol_lust_energy" + str(protagonist.get_stat(Stats.LUST_ENERGY)) + ".webp"
                        # if(not protagonist.lust_energy is None):
                        #     idle "images/smartphone/extrasymbols/symbol_lust_energy" + str(protagonist.get_stat(Stats.LUST_ENERGY)) + ".webp"
                        # else:
                        #     idle "images/smartphone/extrasymbols/symbol_empty_space.webp"
                        if("small" in config.variants) or actualgame.increase_hud_size:
                            at lust_energy_zoom_small
                        else:
                            at lust_energy_zoom

                vbox:
                    #HORNINESS
                    imagebutton:
                        tooltip "Horniness"
                        idle "images/smartphone/extrasymbols/symbol_horniness" + str(protagonist.get_stat(Stats.HORNY)) + ".webp"
                        # if(not protagonist.horny is None):
                        #     idle "images/smartphone/extrasymbols/symbol_horniness" + str(protagonist.get) + ".webp"
                        # else:
                        #     idle "images/smartphone/extrasymbols/symbol_empty_space.webp"
                        if("small" in config.variants) or actualgame.increase_hud_size:
                            at lust_energy_zoom_small
                        else:
                            at lust_energy_zoom



    $ tooltip = GetTooltip("succubus_menu")
    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True

            vbox:
                style_prefix "tooltip"
                xalign 0.5
                text tooltip


