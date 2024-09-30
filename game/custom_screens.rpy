screen warning:
    tag menu
    zorder 100
    key "K_ESCAPE" action ShowMenu("settings")
    add "gui/settings/overlay.png"
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
#TODO content warnings
            text "Please keep in mind that Undergrowth is a {b}Psychological Horror{/b} Visual Novel. \n The current demo contains (insert list of stuff in current demo) \nThe final game will likely contain themes of the following:\n\n{b}Profanity, Death, Hallucinations, Virus Spread, Blood, Violence, Abduction, References of Experimentations on Animals and Humans{/b}"
            textbutton "Dismiss" action ShowMenu("settings"):
                xalign 0.5
                yoffset 40


style warning_button is additional_button
style warning_button_text is additional_button_text
style warning_text:
    size 40
    text_align 0.5

transform sepia:
    matrixcolor TintMatrix(u'#d3d3d3') * SaturationMatrix(0.5, (0.2126, 0.7152, 0.0722))

image snow = SnowBlossom("gui/navigation/snow.png", count=150, fast=True)