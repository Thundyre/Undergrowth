##Splashscreen
image spooklogo:
    "images/spooktoberlogo.png"
    zoom 0.8

label splashscreen:
    scene black
    with Pause(1.0)
    show text "Please play with headphones on for the best experience." with dissolve:
        ypos 0.5
    with Pause(1.0)
    hide text with dissolve

    show text "This demo was made for" with dissolve:
        ypos 200
    with Pause(0.5)
    
    show spooklogo with dissolve:
        xalign 0.5
        yalign 0.5
    with Pause(1.0)

    scene black with dissolve

    
    return

