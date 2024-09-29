################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    color "#b3b3b3"
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    yoffset -80
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos 315
    ypos 35
    padding gui.namebox_borders.padding

style say_label:
    size 48
    xalign gui.name_xalign
    yalign 0.5
    outlines [(absolute(1), "#000000", absolute(1), absolute(1))]

style say_dialogue:
    xpos 400
    xsize 1040
    ypos 85
    outlines [(absolute(1), "#000000", absolute(1), absolute(1))]
    line_spacing 15

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        if len(items)>4:
            box_wrap True
            ymaximum 450
            style_prefix "choicesmall"
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    yminimum 81
    padding (30,20)

style choice_button_text:
    yalign 0.5
    xalign 0.5
    color "f3f3f3"

style choicesmall_vbox is choice_vbox
style choicesmall_button_text is choice_button_text
style choicesmall_button is choice_button:
    xmaximum 640
    xmargin 15



# style choicebubble


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            spacing 25
            xalign 0.5
            yalign 1.0
            yoffset -25

            textbutton _("Back") action Rollback()
            imagebutton auto "gui/quickmenu/auto_%s.png" action Preference("auto-forward", "toggle")
            imagebutton auto "gui/quickmenu/skip_%s.png" action Skip() alternate Skip(fast=True, confirm=True)
            imagebutton auto "gui/quickmenu/save_%s.png" action ShowMenu('save') 
            imagebutton auto "gui/quickmenu/hide_%s.png" action HideInterface()
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            imagebutton auto "gui/quickmenu/settings_%s.png" action ShowMenu('settings')
            imagebutton auto "gui/quickmenu/log_%s.png" action ShowMenu('history')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    if renpy.get_screen("main_menu"):
        hbox:
            style_prefix "title"
            xalign 0.5
            yalign 1.0
            yoffset -30

            spacing 40

            textbutton _("START") action Start()
            textbutton _("CONTINUE") action ShowMenu("load")
            textbutton _("SETTINGS") action ShowMenu("settings")
            textbutton _("EXTRAS") action ShowMenu("gallery")
            textbutton _("QUIT") action Quit(confirm=not main_menu)
    else:
        vbox:
            style_prefix "navigation"
            yalign 0.6
            xalign 0.2
            yoffset 10
            xoffset -4

            spacing 5

            if main_menu:

                textbutton _("Start") action Start()

            else:

                #textbutton _("History") action ShowMenu("history")

                textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")

            textbutton _("Settings") action ShowMenu("settings")

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)

            elif not main_menu:

                textbutton _("Title") action MainMenu()

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                ## Help isn't necessary or relevant to mobile devices.
                textbutton _("Controls") action ShowMenu("controls")

            #textbutton _("About") action ShowMenu("about")

            if renpy.variant("pc") and renpy.get_screen("main_menu"):

                ## The quit button is banned on iOS and unnecessary on Android and
                ## Web.
                textbutton _("Quit") action Quit(confirm=not main_menu)
            
            textbutton _("Return") action Return()


style navigation_button:
    xysize (280,86)
    hover_background "gui/navigation/button_idle_hover.png"
    selected_hover_background "gui/navigation/button_selected_hover.png"
    selected_idle_background "gui/navigation/button_selected_idle.png"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    size 50
    xalign 0.5
    yalign 0.6
    color "#FFF"
    properties gui.text_properties("navigation_button")

style title_button:
    xysize (276,90)
    background "gui/navigation/main_button_idle.png"
    hover_background "gui/navigation/main_button_hover.png"

style title_button_text:
    size 35
    xalign 0.5
    yalign 0.55
    color "#FFF"

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background# at sepia
    
    #add "snow"
    
    add "gui/navigation/logo.png":
        xysize (900,250)
        xalign 0.5
        yalign 0.2

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:
            xpos 634
            ypos 288
            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    vbox:
                        spacing spacing

                        transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    spacing spacing

                    transclude

            else:

                transclude

    use navigation

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty

style game_menu_outer_frame:
    background "gui/overlay/game_menu.png"


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    add "gui/overlay/game_menu.png"
    use navigation

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    
    vbox:
        xpos 634
        ypos 193
        xysize (958, 720)
        ## Buttons to access other pages.
        vbox:
            style_prefix "page"

            xalign 0.5
            yalign 1.0

            hbox:
                spacing 50
                yoffset 10                
                #textbutton _("<") action FilePagePrevious()
                hbox:
                    if config.has_autosave:
                        textbutton _("{#auto_page}Auto") action FilePage("auto")

                    #if config.has_quicksave:
                    #    textbutton _("{#quick_page}Q") action FilePage("quick")

                hbox:
                    spacing gui.page_spacing
                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 9):
                        textbutton "[page]" action FilePage(page)

                #textbutton _(">") action FilePageNext()

        fixed:
            ysize 634
            yalign 1.0
            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            #button:
            #    style "page_label"

            #    key_events True
            #    xalign 0.5
            #    action page_name_value.Toggle()

                #input:
                #    style "page_label_text"
                #    value page_name_value

            ## The grid of file slots.
            grid 2 2:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(4):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox
                        xalign 0.5
                        spacing 12
                        add FileScreenshot(slot)

                        text FileSaveName(slot):
                            style "slot_name_text"

                        text FileTime(slot, format=_("%d %B %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        xoffset 1 yoffset 14
                        key "save_delete" action FileDelete(slot)

    #if config.has_sync:
    #    if CurrentScreenName() == "save":
    #        textbutton _("Upload Sync"):
    #            style_prefix "sync"
    #            action UploadSync()
    #    else:
    #        textbutton _("Download Sync"):
    #            style_prefix "sync"
    #            action DownloadSync()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    padding (20,10)
    hover_background Frame("gui/navigation/button_s_idle_hover.png", 10, 10)
    selected_hover_background  Frame("gui/navigation/button_s_selected_hover.png", 10, 10)
    selected_idle_background  Frame("gui/navigation/button_s_selected_idle.png", 10, 10)
    ysize 70
    xminimum 70

style page_button_text:
    properties gui.text_properties("page_button")
    color "#FFF"
    size 40
    xalign 0.5

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    color "#FFF"
    size 20
    xalign 0.5

style sync_button:
    padding (30,10)
    background Frame("gui/navigation/button_s_idle_hover.png", 30, 10)
    hover_background Frame("gui/navigation/button_s_selected_idle.png", 30, 10)
    ysize 70

style additional_button_text:
    size 30
    xalign 0.5
    yalign 0.6
    color "#FFF"

## settings screen ##########################################################
##
## The settings screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#settings

default set_submenu = "gameplay"

screen settings():
    add "gui/overlay/game_menu.png"
    use navigation
    tag menu
    hbox:
        xpos 724
        ypos 183
        spacing 65
        style_prefix "submenu"
        textbutton _("Gameplay") action SetVariable("set_submenu", "gameplay") 
        textbutton _("Visual") action SetVariable("set_submenu", "visual")
        textbutton _("Audio") action SetVariable("set_submenu", "audio")

    #use game_menu:
    vbox:
        xpos 678
        ypos 347
        if set_submenu == "gameplay":
            use settings_gameplay
        if set_submenu == "visual":
            use settings_visual
        if set_submenu == "audio":
            use settings_audio

screen settings_gameplay():
    tag submenu
    vbox:
        spacing 100
        hbox:
            #spacing 130
            style_prefix "check"
            label _("Skip")
            hbox:
                spacing 10
                xpos 130
                textbutton _("Unseen Text") action Preference("skip", "toggle")
                textbutton _("After Choices") action Preference("after choices", "toggle")
                textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
        vbox:
            style_prefix "additional"
            spacing 20
            textbutton _("Content Warnings") action ShowMenu("warning") xoffset -30
            textbutton _("Advanced Accessibility Settings") action Show("_accessibility") xoffset -30

screen settings_visual():
    tag submenu
    vbox:
        spacing 35
        box_wrap True

        if renpy.variant("pc") or renpy.variant("web"):
            
            hbox:
                style_prefix "radio"
                vbox:
                    spacing 40
                    label _("Display")
                    label _("Font Type")
                vbox:
                    xsize 685
                    xalign 0.0
                    xoffset -50
                    spacing 10
                    hbox:
                        spacing 20
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    hbox:
                        spacing 5
                        textbutton _("Josefin Sans"):
                            action gui.SetPreference("font", "fonts/JosefinSans-VariableFont_wght.ttf")
                            text_font "fonts/JosefinSans-VariableFont_wght.ttf"
                        textbutton _("Atkinson Hyperlegible"):
                            action gui.SetPreference("font", "fonts/AtkinsonHyperlegible-Regular.ttf")
                            text_font "fonts/AtkinsonHyperlegible-Regular.ttf"
        vbox:
            spacing 50
            style_prefix "slider"
            box_wrap True

            hbox:
                spacing 50
                label _("Text Display Speed")
                hbox:
                    yoffset 7
                    spacing 10
                    add "tortoise" 
                    bar:
                        value Preference("text speed")
                        released Show("text_test")
                    add "rabbit"

            frame:
                style_prefix "preview"
                if not renpy.get_screen("text_test"):
                    text "This is a preview of Text Display Speed"        

            hbox:
                spacing 48
                label _("Auto-Forward Time")
                hbox:
                    yoffset 7
                    spacing 10
                    add "tortoise"  
                    bar value Preference("auto-forward time") at rotate_bar
                    add "rabbit"

screen settings_audio():
    tag submenu
    hbox:
        style_prefix "volume"
        vbox:
            spacing 80
            vbox:
                spacing 42
                label _("Music")

                label _("Ambience")

                label _("Sounds FX")

                label _("UI Sounds")
                
                label _("Voice")

            vbox:
                spacing 20
                #if config.has_music or config.has_sound or config.has_voice:
                hbox:
                    spacing 90
                    label _("Mute all")
                    imagebutton auto "gui/settings/check_%s.png" action Preference("all mute", "toggle")
                hbox:
                    spacing 27
                    label _("Radio Static")
                    imagebutton auto "gui/settings/check_%s.png" action ToggleVariable("radio_static", "static", "clean")
                    textbutton _("Test"):
                        if radio_static == "static":
                            action Play("radio_effect", renpy.random.choice(["audio/ui/radio static/uistatic1.ogg", "audio/ui/radio static/uistatic2.ogg", "audio/ui/radio static/uistatic3.ogg"]))
                        else:
                            action Play("radio_effect", renpy.random.choice(["audio/ui/radio static/uiclean1.ogg", "audio/ui/radio static/uiclean2.ogg", "audio/ui/radio static/uiclean3.ogg"]))
                        pos (20,-20)
    
        vbox:
            xoffset -220
            yoffset -10
            spacing 30
            hbox:
                add "volminus"
                bar value Preference("music volume")
                add "volplus"
                #textbutton _("Test") action Play("music", sample_music)
                    
            hbox:
                add "volminus"
                bar value Preference("ambience volume")
                add "volplus"
                #textbutton _("Test") action Play("ambience", sample_ambience)

            hbox:
                add "volminus"
                bar value Preference("sound volume")
                add "volplus"
                #textbutton _("Test") action Play("sound", sample_sound)

            hbox:
                add "volminus"
                bar value Preference("sound_ui volume")
                add "volplus"
                #textbutton _("Test") action Play("sound_ui", sample_soundui)

            hbox:
                add "volminus"
                bar value Preference("voice volume")
                add "volplus"
                #textbutton _("Test") action Play("voice", sample_voice)

screen text_test:
    frame:
        xpos 678
        ypos 646
        style_prefix "preview"
        
        text "This is a preview of Text Display Speed" slow_cps True
        
    timer 2.0 action Hide("text_test")

transform rotate_bar:
    xzoom -1

image rabbit:
    "gui/settings/rabbit.png"
    yoffset 7

image tortoise:
    "gui/settings/tortoise.png"
    yoffset 10

image volplus:
    "gui/settings/volplus.png"
    yoffset 5

image volminus:
    "gui/settings/volminus.png"
    yoffset 5

style volume_slider is slider_slider
style volume_label_text is pref_label_text

style volume_hbox:
    spacing 15

style volume_button is additional_button
style volume_button_text is additional_button_text

style preview_text:
    xalign 0.5
    yalign 0.5
    color "#FFF"
    size 30

style preview_frame:
    background "#242b4f"
    xysize (842, 47)

style submenu_button:
    padding (30,10)
    hover_background Frame("gui/navigation/button_s_idle_hover.png", 30, 10)
    selected_hover_background  Frame("gui/navigation/button_s_selected_hover.png", 30, 10)
    selected_idle_background  Frame("gui/navigation/button_s_selected_idle.png", 30, 10)
    ysize 80

style submenu_button_text:
    size 45
    xalign 0.5
    yalign 0.6
    color "#FFF"

style additional_button:
    padding (30,10)
    background Frame("gui/navigation/button_s_idle_hover.png", 30, 10)
    hover_background Frame("gui/navigation/button_s_selected_idle.png", 30, 10)
    ysize 75

style additional_button_text:
    size 40
    xalign 0.5
    yalign 0.6
    color "#FFF"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    color "#FFF"
    size 35

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    padding (30,10)
    properties gui.button_properties("radio_button")
    hover_background Frame("gui/navigation/button_s_idle_hover.png", 30, 10)
    selected_hover_background Frame("gui/navigation/button_s_selected_hover.png", 30, 10)
    selected_idle_background Frame("gui/navigation/button_s_selected_idle.png", 30, 10)
    ysize 70

style radio_button_text:
    xalign 0.5
    yalign 0.5
    size 30
    color "#FFF"


style check_button:
    padding (30,10)
    properties gui.button_properties("check_button")
    hover_background Frame("gui/navigation/button_s_idle_hover.png", 30, 10)
    selected_hover_background  Frame("gui/navigation/button_s_selected_hover.png", 30, 10)
    selected_idle_background  Frame("gui/navigation/button_s_selected_idle.png", 30, 10)
    ysize 70

style check_button_text:
    xalign 0.5
    yalign 0.5
    size 30
    color "#FFF"

style slider_slider:
    xsize 380

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")



## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    add "gui/settings/overlay.png"

    style_prefix "history"

    vbox:
        xalign 0.5
        ypos 20
        fixed:
            add "gui/other/log_bg.png" xysize (1330, 980)
            xysize (1330, 980)
            vbox:
                spacing 4
                ypos 45
                add "gui/settings/arrow_up.png" xalign 1.0 xoffset -3 ypos -2
                viewport:
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    xysize (1280, 840)
                    vbox:
                        xsize 950
                        spacing 35
                        for h in _history_list:

                            window:
                                ## This lays things out properly if history_height is None.
                                has fixed:
                                    yfit True

                                if h.who:

                                    label h.who:
                                        style "history_name"
                                        substitute False

                                        ## Take the color of the who text from the Character, if
                                        ## set.
                                        if "color" in h.who_args:
                                            text_color h.who_args["color"]

                                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                                text what:
                                    substitute False

                        if not _history_list:
                            label _("The dialogue history is empty.")

                add "gui/settings/arrow_down.png" xalign 1.0 xoffset -3

        textbutton _("Return") action Return() xalign 0.5


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is history_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_name:
    xalign 0.0
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    xalign 1.0
    size 40

style history_text:
    size 30
    xpos 270
    ypos 5
    line_spacing 5
    

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

style history_button:
    background Frame("gui/button/choice_idle_background.png", 30, 10)
    hover_background Frame("gui/button/choice_hover_background.png", 30, 10)
    ysize 60
    xsize 345
    
style history_button_text:
    size 30
    color "#FFF"
    xalign 0.5

style history_vscrollbar is controls_vscrollbar
## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen controls():

    tag menu

    default device = "keyboard"
    add "gui/overlay/game_menu.png"
    use navigation
    style_prefix "controls"
    hbox:
        xpos 724
        ypos 183
        spacing 65
        style_prefix "submenu"
        textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
        textbutton _("Mouse") action SetScreenVariable("device", "mouse")

        if GamepadExists():
            textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

    vbox:
        xpos 678
        ypos 347
        spacing 15
        if device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        elif device == "gamepad":
            use gamepad_help


screen keyboard_help():
    vbox:
        ypos -20
        ysize 530
        spacing 4
        add "gui/settings/arrow_up.png" xalign 1.0 xoffset -3 ypos -2
        viewport:
            xsize 870
            ysize 490
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                spacing 15
                hbox:
                    label _("Enter")
                    text _("Advances dialogue and activates the interface.")

                hbox:
                    label _("Space")
                    text _("Advances dialogue without selecting choices.")

                hbox:
                    label _("Arrow Keys")
                    text _("Navigate the interface.")

                hbox:
                    label _("Escape")
                    text _("Accesses the game menu.")

                hbox:
                    label _("Ctrl")
                    text _("Skips dialogue while held down.")

                hbox:
                    label _("Tab")
                    text _("Toggles dialogue skipping.")

                hbox:
                    label _("Page Up")
                    text _("Rolls back to earlier dialogue.")

                hbox:
                    label _("Page Down")
                    text _("Rolls forward to later dialogue.")

                hbox:
                    label "H"
                    text _("Hides the user interface.")

                hbox:
                    label "S"
                    text _("Takes a screenshot.")

                hbox:
                    label "V"
                    text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

                hbox:
                    label "Shift+A"
                    text _("Opens the accessibility menu.")

        add "gui/settings/arrow_down.png" xalign 1.0 xoffset -3

screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates\nthe interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate():
        style_prefix "additional"
        xpos 620
        ypos 100


style controls_vscrollbar:
    xsize 25
    
style controls_label_text:
    color "#cfcfcf"
    size 30

style controls_text:
    size 30

style controls_hbox:
    spacing 50


################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen
```
screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")
```


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):
    if nvl_mode == "phone":

        use PhoneDialogue(dialogue, items)
    else:
        window:
            style "nvl_window"

            has vbox:
                spacing gui.nvl_spacing

            ## Displays dialogue in either a vpgrid or the vbox.
            if gui.nvl_height:

                vpgrid:
                    cols 1
                    yinitial 1.0

                    use nvl_dialogue(dialogue)

            else:

                use nvl_dialogue(dialogue)

            ## Displays the menu, if given. The menu may be displayed incorrectly if
            ## config.narrator_menu is set to True.
            for i in items:

                textbutton i.caption:
                    action i.action
                    style "nvl_button"

        add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

default hidebubbles = False

screen bubble(who, what):
    style_prefix "bubble"
    if hidebubbles==False:
        window:
            id "window"

            if who is not None:

                window:
                    id "namebox"
                    style "bubble_namebox"

                    text who:
                        id "who"

            text what:
                id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
