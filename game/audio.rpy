init -1 python:
    renpy.music.register_channel("sound_ui", mixer = "sound_ui", loop=None)
    renpy.music.register_channel("ambience", mixer = "ambience", loop=None)

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

## Ambience
define amb_bad1 = "audio/ambience/amb_bad1.ogg"
define amb_bad1_wovoice = "audio/ambience/amb_bad1wovoice.ogg"
define amb_bad2 = "audio/ambience/amb_bad2.ogg"
define amb_bear = "audio/ambience/amb_bear.ogg"
define amb_bear_wonoise = "audio/ambience/amb_bearwonoise.ogg"
define amb_campday = "audio/ambience/amb_campday.ogg"
define amb_campnight = "audio/ambience/amb_campnight.ogg"
define amb_rc = "audio/ambience/amb_rc.ogg"
define amb_village = "audio/ambience/amb_village.ogg"
define amb_campnight_wofire = "audio/ambience/amb_campnightwofire.ogg"

#some of these aren't used anymore ^

## SFX
define audio.ReceiveText  = "audio/sfx/ReceiveText.ogg"
