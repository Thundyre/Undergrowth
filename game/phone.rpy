# Here's the code for the phone!

define nvl_mode = "phone"  ##Allow the NVL mode to become a phone conversation
define MC_Name = "Morgan" ##The name of the main character, used to place them on the screen

init -1 python:
    phone_position_x = 0.3
    phone_position_y = 0.5

    def Phone_ReceiveSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/ReceiveText.ogg")
    def Phone_SendSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/SendText.ogg")

default message_icon = None

transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

transform phone_appear:
    alpha 0.0
    ease 0.5 alpha 1.0
    
transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0
    

transform message_narrator:
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

default pancake = False

screen walkie_talkie():
    add "gui/settings/overlay.png"
    fixed:
        if pancake:
            add "gui/radio/satphone.png":
                xalign 0.95
                yalign 1.0
        else:
            add "gui/radio/walkie.png":
                xalign 0.95
                yalign 1.0
            
screen PhoneDialogue(dialogue, items=None):
    use walkie_talkie
    fixed:
        xalign 0.3
        yalign 0.5
        xsize 1170
        ysize 800
        if len(dialogue) == 1:
            at phone_appear
        viewport:
            xsize 1170
            ysize 800
            draggable True
            mousewheel True
            # cols 1
            yinitial 1.0
            # scrollbars "vertical"
            vbox:
                spacing 50
                null height 20
                use nvl_phonetext(dialogue)
                null height 100


screen nvl_phonetext(dialogue):
    style_prefix None

    $ previous_d_who = None
    for id_d, d in enumerate(dialogue):
        if d.who == None: # Narrator
            text d.what:
                    xpos -335
                    ypos 0.0
                    xsize 1170
                    text_align 0.5
                    italic True
                    size 28
                    slow_cps False
                    id d.what_id
                    if d.current:
                        at message_narrator
        else:
            if d.who == MC_Name:
                $ message_frame = "gui/radio/bubble_right.png"
            else:
                $ message_frame = "gui/radio/bubble_left.png"

            hbox:
                spacing 15
                if d.who == MC_Name:
                    xoffset 15
                    box_reverse True

                #show an icon
                if d.who == MC_Name:
                    $ message_icon = None
                elif d.who == "Cassie":
                    $ message_icon = "[chibi_cassie]"
                elif d.who == "Davos":
                    $ message_icon = "[chibi_davos]"
                elif d.who == "Eva":
                    $ message_icon = "[chibi_eva]"
                elif d.who == "Isaak":
                    $ message_icon = "[chibi_isaak]"
                elif d.who == "Jax":
                    $ message_icon = "[chibi_jax]"
                elif d.who == "Koda":
                    $ message_icon = "[chibi_koda]"
                elif d.who == "Ruran":
                    $ message_icon = "[chibi_ruran]"
                elif d.who == "Wilbur":
                    $ message_icon = "[chibi_wilbur]"

                add message_icon:
                    yalign 0.5
                    yoffset 10
                    if d.current:
                        at message_appear_icon()


                vbox:
                    style_prefix "phonename"
                    yalign 1.0
                    if d.who != MC_Name:
                        text d.who xoffset 50
                    else:
                        text d.who xalign 1.0 xoffset -70

                    frame:
                        if d.who != MC_Name:
                            padding (155,30,30,60)
                            background Frame(message_frame, 60,30,30,30)
                        else:
                            padding (30,30,30,60)
                            background Frame(message_frame, 30,30,60,30)
                        
                        xsize 800

                        if d.current:
                            if d.who == MC_Name:
                                at message_appear(1)
                            else:
                                at message_appear(-1)

                        text d.what:
                            pos (0,10)
                            xsize 800
                            slow_cps False
                            
                            if d.who == MC_Name :
                                text_align 0.0
  
                            id d.what_id
                
                fixed:
                    xysize (128,128) 
        $ previous_d_who = d.who

style phonename_text:
    color "#f3f3f3"

default chibi_cassie = "images/chibi/cassie_neutral.png"
default chibi_davos = "images/chibi/davos_neutral.png"
default chibi_eva = "images/chibi/eva_neutral.png"
default chibi_isaak = "images/chibi/isaak_neutral.png"
default chibi_jax = "images/chibi/jax_neutral.png"
default chibi_koda = "images/chibi/koda_neutral.png"
default chibi_ruran = "images/chibi/ruran_neutral.png"
default chibi_wilbur = "images/chibi/wilbur_neutral.png"