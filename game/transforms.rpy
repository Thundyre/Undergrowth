define _scene_show_hide_transition = dissolve

transform centerleft:
    xpos 400
    yalign 1.0

transform centerright:
    xpos 900
    yalign 1.0

define sdissolve = Dissolve(0.3)

define longfade= Fade(0.5, 1.0, 0.5)

define slideright = CropMove(0.5, "slideright")
define slideleft = CropMove(0.5, "slideleft")
define slidedown = CropMove(0.5, "slidedown")

define pushupquick = PushMove(0.3, "pushup")

define moveindissolve = ComposeTransition(pushleft, after =dissolve)

# SPACINGS FOR 5 CHARACTERS AT ONCE
    # show pearl happy at left
    # pe "Helloooo! I'm Pearl! This is Aston, Lorenzo, and Gregory!"
    # show ky with move:
    #     xpos 300
    # show gr with move:
    #     xpos 650
    # show lorenzo smile:
    #     xpos 1000
    #     yalign 1.0
    # show ast neutral at right

transform hover_anim:
    on hover:
        linear 0.3 yoffset -5
    on idle:
        linear 0.3 yoffset 0

transform hover_anim2: #smaller hover for quickmenu
    on hover:
        linear 0.3 yoffset -3
    on idle:
        linear 0.3 yoffset 0