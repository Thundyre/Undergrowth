init -1 python:
    renpy.music.register_channel("sound_ui", mixer = "sfx_ui", loop=None)
    renpy.music.register_channel("ambience", mixer = "sfx_am", loop=None) 
    renpy.music.register_channel("radio_effect", mixer = "voice", loop=False , stop_on_mute=False)

init python:
    if not persistent.initialized:
        persistent.initialized = True
        preferences.set_volume("sound_ui", 1.0)
        preferences.set_volume("ambience", 1.0)

#define sample_music = 
#define sample_ambience =
#define sample_sound = 
#define sample_soundui = 
#define sample_voice = 

$ sample_radio_on = renpy.random.choice(["audio/ui/radio static/uistatic1.ogg", "audio/ui/radio static/uistatic2.ogg", "audio/ui/radio static/uistatic3.ogg"])
$ sample_radio_off = renpy.random.choice(["audio/ui/radio static/uiclean1.ogg", "audio/ui/radio static/uiclean2.ogg", "audio/ui/radio static/uiclean3.ogg"])

## Music
define audio.light = "audio/music/mus_light.ogg"
define audio.neutral = "audio/music/mus_neutral.ogg"
define audio.anxious = "audio/music/mus_anxious.ogg"
