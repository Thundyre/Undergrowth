##Splashscreen
image spooklogo:
    "spooktoberlogo.png"
    zoom 0.8

label splashscreen:
    scene black
    with Pause(1.0)

    show text "This demo was made for" with dissolve:
        ypos 200
    with Pause(0.5)
    
    show spooklogo with dissolve:
        xalign 0.5
        yalign 0.5
    with Pause(1.0)

    scene black with dissolve

    
    return

