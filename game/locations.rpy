
label location_diner:
    $ actualgame.current_location = Location.DINER
    scene diner with fade
    show screen navigation_button
    pause
    jump location_diner


label location_cafe:
    $ actualgame.current_location = Location.CAFE
    scene cafe with fade
    show screen navigation_button
    pause
    jump location_cafe


label location_dorms:
    $ actualgame.current_location = Location.DORMS
    scene dorms with fade
    show screen navigation_button
    pause
    jump location_cafe


label location_escaperoom:
    $ actualgame.current_location = Location.ESCAPEROOM
    scene escaperoom with fade
    show screen navigation_button
    pause
    jump location_escaperoom


label location_nightclub:
    scene nightclub with fade
    show screen navigation_button
    pause
    jump location_nightclub


label location_park:
    $ actualgame.current_location = Location.PARK
    scene park with fade
    show screen navigation_button
    pause
    jump location_park


label location_studio:
    $ actualgame.current_location = Location.STUDIO
    scene photostudio with fade
    show screen navigation_button
    pause
    jump location_studio


label location_uni:
    $ actualgame.current_location = Location.UNI_MAIN
    scene uni_main with fade
    show screen navigation_button
    pause
    jump location_uni

label uni_lecturehall:
    $ actualgame.current_location = Location.UNI_MAIN
    scene uni_lecture with fade
    show screen navigation_button
    pause
    jump uni_lecturehall


label location_home:
    $ actualgame.current_location = Location.HOME
    jump home_downstairs


label home_downstairs:
    $ actualgame.current_location = Location.HOME_DOWNSTAIRS
    scene home_downstairs with fade
    show screen navigation_button
    pause
    jump home_downstairs


label home_upstairs:
    $ actualgame.current_location = Location.HOME_UPSTAIRS
    scene home_upstairs with fade
    show screen navigation_button
    pause
    jump home_upstairs


label home_bathroom:
    $ actualgame.current_location = Location.HOME_BATHROOM
    scene home_bathroom with fade
    show screen navigation_button
    pause
    jump home_bathroom


label location_moms:
    jump moms_first_floor


label moms_first_floor:
    $ actualgame.current_location = Location.MOMS_FIRSTFLOOR
    scene moms_firstfloor with fade
    show screen navigation_button
    pause
    jump moms_first_floor

label moms_pool:
    $ actualgame.current_location = Location.MOMS_POOL
    scene moms_pool with fade
    show screen navigation_button
    pause
    jump moms_pool

label moms_sundeck:
    $ actualgame.current_location = Location.MOMS_SUNDECK
    scene moms_sundeck with fade
    show screen navigation_button
    pause
    jump moms_sundeck

label moms_serverroom:
    $ actualgame.current_location = Location.MOMS_DAD
    scene moms_serverroom with fade
    show screen navigation_button
    pause
    jump moms_serverroom

label moms_master_bedroom:
    $ actualgame.current_location = Location.MOMS_MASTER
    scene moms_masterbedroom with fade
    show screen navigation_button
    pause
    jump moms_master_bedroom

label moms_bathroom:
    $ actualgame.current_location = Location.MOMS_BATHROOM
    scene moms_bathroom with fade
    show screen navigation_button
    pause
    jump moms_bathroom

label moms_guestroom:
    $ actualgame.current_location = Location.MOMS_GUEST
    scene moms_guestroom with fade
    show screen navigation_button
    pause
    jump moms_guestroom



label location_gym:
    jump gym_reception

label gym_reception:
    $ actualgame.current_location = Location.GYM_RECEPTION
    scene gym_reception with fade
    show screen navigation_button
    pause
    jump gym_reception

label gym_lockerroom:
    $ actualgame.current_location = Location.GYM_LOCKERROOM
    scene gym_lockers with fade
    show screen navigation_button
    pause
    jump gym_lockerroom

label gym_actual:
    $ actualgame.current_location = Location.GYM_ACTUAL
    scene gym_actual with fade
    show screen navigation_button
    pause
    jump gym_actual

label gym_yoga_studio:
    $ actualgame.current_location = Location.GYM_YOGA
    scene gym_yoga with fade
    show screen navigation_button
    pause
    jump gym_yoga_studio

label gym_toilet:
    $ actualgame.current_location = Location.GYM_TOILET
    scene gym_toilet with fade
    show screen navigation_button
    pause
    jump gym_toilet

label gym_office:
    $ actualgame.current_location = Location.GYM_OFFICE
    scene gym_office with fade
    show screen navigation_button
    pause
    jump gym_office

label gym_sauna:
    $ actualgame.current_location = Location.GYM_SAUNA
    scene gym_sauna with fade
    show screen navigation_button
    pause
    jump gym_sauna

label gym_showers:
    $ actualgame.current_location = Location.GYM_SHOWERS
    scene gym_showers with fade
    show screen navigation_button
    pause
    jump gym_showers
