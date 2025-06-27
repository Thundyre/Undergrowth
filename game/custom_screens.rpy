## Custom mouse cursor 🐁 ################################################################
##
define config.mouse = { }
define config.mouse['default'] = [ ( "gui/cursor.png", 0, 0) ]
define config.mouse['button'] = [ ( "gui/cursor_button.png", 0, 0) ]
define config.mouse['pressed_button'] = [ ( "gui/cursor_button.png", 0, 0) ]

## Content Warnings screen ################################################################
##
## This screen shows all the content warnings about the game

screen warning:
    tag menu
    zorder 100
    key "K_ESCAPE" action ShowMenu("settings")
    add "gui/overlay/overlay.png"

    fixed:

        style_prefix "warning"
        xysize(1377,857)
        xalign 0.5
        yalign 0.5
        yoffset 15
        add "gui/other/contentwarning.png"

        vbox:
            spacing 60
            yalign 0.4
            xalign 0.5
            xsize 1000
            text "Content Warnings":
                size 80
                xalign 0.5
            text "Please keep in mind that Undergrowth is a {b}Psychological Horror{/b} Visual Novel game and that the final game will likely contain themes of the following:\n\n{b}Profanity, Death, Hallucinations, Virus Spread, Blood, Violence, Abduction, References of Experimentations on Animals and Humans{/b}"
            textbutton "Dismiss" action ShowMenu("settings"):
                xalign 0.5
                yoffset 40


style warning_button is additional_button
style warning_button_text is additional_button_text
style warning_text:
    size 40
    text_align 0.5


## Extras screen ################################################################
##
## This screen manages all of other extras screens

screen extras():
    vbox:
        style_prefix "navigation"
        yalign 0.5
        xpos 92
        yoffset 10

        textbutton _("Gallery") action ShowMenu("gallery")

        textbutton _("Music") action ShowMenu("music_room")

        textbutton _("Credits") action ShowMenu("credits")

        textbutton _("Title") action Return()

## Credits screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.

screen credits():
    tag menu
    add "gui/extras/extras_background.png"
    use extras

    vbox:
        style_prefix "extras"
        xpos 500
        ypos 140
        ysize 820
        spacing 4
        add "gui/settings/arrow_up.png" xalign 1.0 xoffset -3
        viewport:
            xsize 1240
            ysize 780
            draggable True
            mousewheel True
            scrollbars "vertical"
            vbox:
                spacing 60
                hbox:
                    xsize 1200
                    vbox:
                        spacing 20
                        label _("Crew") text_size 60
                        label "" text_size 10

                        label _("Director, Writer")
                        label _("Narrative Consultant, Art Director")
                        label _("Lead Programmer")
                        label _("Character Artist, UI Designer,\nAssistant Programmer ")
                        label _("Character Artist")

                        #label _("Animator")
                        label _("Composer")
                        label _("Voice Director, Script Editor")

                        label "" text_size 10
                        label _("Cast") text_size 60
                        label "" text_size 10

                        label _("Morgan")
                        label _("Colin")
                        label _("Hilda")
                        label _("Gregory")
                        label _("Pearl")
                        label _("Lorenzo")
                        label _("Aston")
                        label _("Kyle")
                        label _("Wilbur")
                        label _("Davos")
                        label _("Ruran")
                        label _("Cassie")
                        label _("Jax")
                        label _("Koda")
                        label _("Eva")
                        label _("Isaak")
                        label _("Elliot")
                        label _("Ferdinand, Matt")
                        label _("Ethan, Stephen")

                    vbox:
                        xalign 1.0
                        spacing 20
                        text "" size 90

                        text "{a=https://azufx.bsky.social}Kylie Siaw{/a}"
                        text "{a=https://huurreprinssi.itch.io/}Elina Heino{/a}"
                        text "{a=https://f1reshark.itch.io/}Karolina \"F1reshark\" Mendel{/a}"
                        text "{a=https://ruminio.itch.io/}Ruminio{/a}"
                        text "" size 15
                        text "{a=https://bsky.app/profile/iamthoe.bsky.social}Thoe{/a}"

                        #text "{a=https://candycornskull.itch.io/}Candycornskull{/a}"

                        text "{a=https://henkkastorm.bsky.social}Henri Tikkala{/a}"
                        text "{a=https://jettbarker.bsky.social}Jett Barker{/a}"

                        text "" size 120

                        text "{a=https://xmgrantvo.carrd.co/}Xander M. Grant{/a}"
                        text "{a=https://twitter.com/MahoganyVoice}James Rudolph{/a}"
                        text "{a=https://vanessabenvo.bsky.social}Vanessa Benoit{/a}"
                        text "{a=https://tpvoiceworks.com/}Tyler Pasquarella{/a}"
                        text "{a=https://zyrabisquera.bsky.social}Zyra Bisquera{/a}"
                        text "{a=https://bsky.app/profile/j-cuevas.com}J Cuevas{/a}"
                        text "{a=https://wiwyums.bsky.social}Lee Williams{/a}"
                        text "{a=https://brandonpjenkinsvo.bsky.social}Brandon P. Jenkins{/a}"
                        text "{a=https://joshbeardvo.bsky.social}Josh Beard{/a}"
                        text "{a=https://patternscreamer.bsky.social}Kyle Randal{/a}"
                        text "{a=https://itsnotmika.carrd.co/}Mika Nerida{/a}"
                        text "{a=https://breefrankelvo.bsky.social}Bree Frankel{/a}"
                        text "{a=https://noahbelachew.bsky.social}Noah Belachew{/a}"
                        text "{a=https://amadamana.bsky.social}Dante Amada{/a}"
                        text "{a=https://stephswanquills.bsky.social}Stephanie Tobin{/a}"
                        text "{a=https://jettbarker.bsky.social}Jett Barker{/a}"
                        text "{a=https://taylorfvoiceover.com/}Taylor Fernandez{/a}"
                        text "{a=https://jj11818.bsky.social}Jason Hall{/a}"
                        text "{a=https://myaturii.bsky.social}Nate Fernandez{/a}"

                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
        add "gui/settings/arrow_down.png" xalign 1.0 xoffset -2
style extras_text:
    size 40
    xalign 1.0

style extras_label_text:
    color "#FFF"
    size 40

style extras_vscrollbar is controls_vscrollbar

## Gallery screen ######################################################
##
## Gallery blah blah blah

init python:
    g = Gallery()

    # CGs buttons

    g.button("christmas")
    g.condition("persistent.gallery_christmas")
    g.image("cg christmas")

    g.button("findinglorenzo")
    g.condition("persistent.gallery_findinglorenzo")
    g.image("cg findinglorenzo")

    g.button("frozenbody")
    g.condition("persistent.gallery_frozenbody")
    g.image("cg frozenbody")

    g.button("meeting")
    g.condition("persistent.gallery_meeting")
    g.image("cg meeting")

    g.button("pearldeath")
    g.condition("persistent.gallery_pearldeath")
    g.image("cg pearldeath")

    g.button("rash")
    g.condition("persistent.gallery_rash")
    g.image("cg rash")

    g.button("tomatosoup")
    g.condition("persistent.gallery_tomatosoup")
    g.image("cg tomatosoup")

    g.button("meetingkyle")
    g.condition("persistent.gallery_meetingkyle")
    g.image("cg meetingkyle")

    g.button("bearwindow")
    g.condition("persistent.gallery_bearwindow")
    g.image("cg bearwindow1")
    g.image("cg bearwindow2")
    g.image("cg bearwindow3")

    # g.button("avalanche")
    # g.condiition("persistent.gallery_avalanche")
    # g.image("cg avalanche")

    # g.button("morganhome")
    # g.condiition("persistent.gallery_morganhome")
    # g.image("cg morganhome1")
    # g.image("cg morganhome2")

    # g.button("memory")
    # g.condiition("persistent.gallery_memory")
    # g.image("cg memory")


screen gallery():

    tag menu
    add "gui/extras/extras_background.png"
    use extras

    fixed:
        style_prefix "gallery"
        xsize 1240
        ysize 780
        xpos 500
        ypos 140
        grid 3 3:

            xfill True
            yfill True

            add g.make_button("meeting", "gal cg meeting", locked = "locked", hover_border = "cg_hover", xalign=0.5, yalign=0.5)
            add g.make_button("tomatosoup", "gal cg tomatosoup", locked = "locked", hover_border = "cg_hover", xalign=0.5, yalign=0.5)
            add g.make_button("meetingkyle", "gal cg meetingkyle", locked = "locked", hover_border = "cg_hover", xalign=0.5, yalign=0.5)

            add g.make_button("rash", "gal cg rash", locked = "locked", hover_border = "cg_hover", xalign=0.5, yalign=0.5)
            add g.make_button("bearwindow", "gal cg bearwindow", locked = "locked", hover_border = "cg_hover", xalign=0.5, yalign=0.5)
            add g.make_button("findinglorenzo", "gal cg findinglorenzo", locked = "locked", hover_border = "cg_hover", xalign=0.5, yalign=0.5)

            add g.make_button("christmas", "gal cg christmas", locked = "locked", hover_border = "cg_hover",  xalign=0.5, yalign=0.5)
            add g.make_button("pearldeath", "gal cg pearldeath", locked = "locked", hover_border = "cg_hover", xalign=0.5, yalign=0.5)
            add g.make_button("frozenbody", "gal cg frozenbody", locked = "locked", hover_border = "cg_hover", xalign=0.5, yalign=0.5)


## Music Room screen ######################################################
##
## Music :3

define track1 = "audio/music/mus_light.ogg"
define track2 = "audio/music/mus_neutral.ogg"
define track3 = "audio/music/mus_anxious.ogg"
define track4 = "audio/music/mus_sad.ogg"
define track5 = "audio/music/mus_oof.ogg"

init python:

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Step 2. Add music files.
    mr.add("audio/music/mus_neutral.ogg", action=SetScreenVariable("current_track", 1))
    mr.add("audio/music/mus_light.ogg", action=SetScreenVariable("current_track", 2))
    mr.add("audio/music/mus_anxious.ogg", action=SetScreenVariable("current_track", 3))
    mr.add("audio/music/mus_sad.ogg", action=SetScreenVariable("current_track", 4))
    mr.add("audio/music/mus_oof.ogg", action=SetScreenVariable("current_track", 5))

default current_track = 1

screen music_room():

    tag menu
    add "gui/extras/musicbg.png"
    use extras

    style_prefix "music"

    hbox:
        pos (420,85)
        spacing 140
        vbox:
            pos (50,50)
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                xysize (800,815)
                vbox:
                    textbutton "Track 1" action mr.Play("audio/music/mus_neutral.ogg")
                    textbutton "Track 2" action mr.Play("audio/music/mus_light.ogg")
                    textbutton "Track 3" action mr.Play("audio/music/mus_anxious.ogg")
                    textbutton "Track 4" action mr.Play("audio/music/mus_sad.ogg")
                    textbutton "Track 5" action mr.Play("audio/music/mus_oof.ogg")
        vbox:
            spacing 40
            xsize 440
            xalign 0.5
            label _("Now Playing")
            add "gui/extras/albumart.png" xalign 0.5
            label "Track [current_track]"
            text "Henri Tikkala" ypos -25
            vbox:
                xalign 0.5
                bar value AudioPositionValue(channel='music') xalign 0.5
                hbox:
                    xalign 0.5
                    spacing 125
                    imagebutton auto "gui/extras/previtrack_%s.png" action mr.Previous()
                    imagebutton auto "gui/extras/pause_%s.png" action mr.TogglePause()
                    imagebutton auto "gui/extras/nexttrack_%s.png" action mr.Next()
            hbox:
                xalign 0.5
                spacing 10
                add "volminus"
                bar value Preference("music volume")
                add "volplus"

    on "replace" action mr.Play("audio/music/mus_neutral.ogg")
    on "replaced" action Play("music", "audio/music/mus_neutral.ogg")

style music_label:
    xalign 0.5

style music_label_text is extras_label_text

style music_text:
    xalign 0.5

style music_bar:
    right_bar "gui/extras/music_bar_bg.png"
    left_bar "gui/extras/music_bar_fill.png"

style music_button:
    padding (30,10)
    hover_background Frame("gui/navigation/button_s_idle_hover.png", 30, 10)
    selected_hover_background  Frame("gui/navigation/button_s_selected_hover.png", 30, 10)
    selected_idle_background  Frame("gui/navigation/button_s_selected_idle.png", 30, 10)

style music_button_text is additional_button_text:
    insensitive_color "#b8b8b8"

## Pre-game options screen ######################################################
##
## Additional options selectable only once, at the start of a new game


#default radio_static = "static"

default persistent.screenshake = True

screen add_options():
    add "bg forest1" at sepia
    fixed:
        xalign 0.5
        yalign 0.5
        xysize (1345, 1002)
        add "gui/other/log_bg.png"
        hbox:
            style_prefix "radio"
            vbox:
                spacing 40

                #label _("Radio Static")
                label _("Screenshake")

## Save names for dates ############
##

init python:

    def current_date(arc, day):
        renpy.restart_interaction()
        return arc+": "+day

## Date label #################################
##
## label with current in-game day

default current_day = None
screen date_label():
    frame :
        xalign 1.0
        xysize (400,100)
        background Frame("gui/frame.png", 20, 20)
        text current_day:
            xalign 0.5
            yalign 0.5
    timer 2.5 action [Hide("date_label", transition=Dissolve(0.5))]
