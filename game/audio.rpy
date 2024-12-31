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
define audio.sad = "audio/music/mus_sad.ogg"
define audio.xmas = "audio/music/mus_krimus.ogg"
define audio.oof = "audio/music/mus_oof.ogg"

## Ambience
define amb_bad1 = "audio/ambience/amb_bad1.ogg"
define amb_bad1_wovoice = "audio/ambience/amb_bad1wovoice.ogg"
define amb_bad2 = "audio/ambience/amb_bad2.ogg"
define amb_bear = "audio/ambience/amb_bear.ogg"
define amb_bear_wonoise = "audio/ambience/amb_bearwonoise.ogg"
define amb_campday = "audio/ambience/amb_campday.ogg"
define amb_intcampday = "audio/ambience/amb_intcampday.ogg"
define amb_campnight = "audio/ambience/amb_campnight.ogg"
define amb_intcampnight = "audio/ambience/amb_intcampnight.ogg"
define amb_rc = "audio/ambience/amb_rc.ogg"
define amb_village = "audio/ambience/amb_village.ogg"
define amb_campnight_wofire = "audio/ambience/amb_campnightwofire.ogg"
define amb_snowmobile = "audio/ambience/amb_snowmobile.ogg"
define amb_snowmobilewind = "audio/ambience/amb_snowmobilewind.ogg"
define amb_stronkwind = "audio/ambience/amb_stronkwind.ogg"


## SFX
define audio.avalanche  = "audio/sfx/avalanche.ogg"
define audio.backpack  = "audio/sfx/backpack.ogg"
define audio.backpacktoss  = "audio/sfx/backpacktoss.ogg"
define audio.bandage1  = "audio/sfx/bandage1.ogg"
define audio.bandage1  = "audio/sfx/bandage1.ogg"
define audio.beargrowl = "audio/sfx/beargrowl.ogg"
define audio.beep  = "audio/sfx/beep.ogg"
define audio.birdyeet = "audio/sfx/birdyeet.ogg"
define audio.blanket = "audio/sfx/blanket.ogg"
define audio.boom  = "audio/sfx/boom.ogg"
define audio.bookclose = "audio/sfx/bookclose.ogg"
define audio.cabinclose  = "audio/sfx/cabinclose.ogg"
define audio.cabinopen  = "audio/sfx/cabinopen.ogg"
define audio.camera1  = "audio/sfx/camera1.ogg"
define audio.camera2  = "audio/sfx/camera2.ogg"
define audio.camera3  = "audio/sfx/camera3.ogg"
define audio.cardoor  = "audio/sfx/cardoor.ogg"
define audio.clang  = "audio/sfx/clang.ogg"
define audio.cloth  = "audio/sfx/cloth.ogg"
define audio.DavosLaugh = "audio/sfx/DavosLaugh.ogg" #J24 if everything's OK
define audio.dial  = "audio/sfx/dial.ogg"
define audio.ding  = "audio/sfx/ding.ogg"
define audio.dirtbag  = "audio/sfx/dirtbag.ogg"
define audio.fall  = "audio/sfx/fall.ogg"
define audio.flash  = "audio/sfx/flash.ogg"
define audio.flashlight  = "audio/sfx/flashlight.ogg"
define audio.gloves  = "audio/sfx/gloves.ogg"
define audio.grab  = "audio/sfx/grab.ogg"
define audio.GregoryLaugh  = "audio/sfx/GregoryLaugh.ogg" #J16 use
define audio.hug  = "audio/sfx/hug.ogg"
define audio.icebox  = "audio/sfx/icebox.ogg"
define audio.j28stab = "audio/sfx/j28stab.ogg"
define audio.jacket  = "audio/sfx/jacket.ogg"
define audio.kick = "audio/sfx/kick.ogg"
define audio.knock  = "audio/sfx/knock.ogg"
define audio.labdoor  = "audio/sfx/labdoor.ogg"
define audio.lobeargrowl  = "audio/sfx/lobeargrowl.ogg"
define audio.LorenzoLaugh  = "audio/sfx/LorenzoLaugh.ogg" #J19 use if fit's hit the shan
define audio.meep  = "audio/sfx/meep.ogg"
define audio.page  = "audio/sfx/page.ogg"
define audio.pen  = "audio/sfx/pen.ogg"
define audio.phonebuz  = "audio/sfx/phonebuzz.ogg" #Note that this is misspelled
define audio.phonesnatch  = "audio/sfx/phonesnatch.ogg"
define audio.pistol  = "audio/sfx/pistol.ogg"
define audio.radio  = "audio/sfx/radio.ogg"
define audio.radiotower  = "audio/sfx/radiotower.ogg"
define audio.rifle  = "audio/sfx/rifle.ogg"
define audio.rumble  = "audio/sfx/rumble.ogg"
define audio.rustle1  = "audio/sfx/rustle1.ogg"
define audio.rustle  = "audio/sfx/rustle2.ogg"
define audio.scoop1  = "audio/sfx/scoop1.ogg"
define audio.scoop2  = "audio/sfx/scoop2.ogg"
define audio.scribble  = "audio/sfx/scribble.ogg"
define audio.shovel  = "audio/sfx/shovel.ogg"
define audio.sleeve  = "audio/sfx/sleeve.ogg"
define audio.slip  = "audio/sfx/slip.ogg"
define audio.snowground  = "audio/sfx/snowground.ogg"
define audio.snowmobile  = "audio/sfx/snowmobile.ogg"
define audio.snowrun  = "audio/sfx/snowrun.ogg"
define audio.snowstorm  = "audio/sfx/snowstorm.ogg"
define audio.snuggle = "audio/sfx/snuggle.ogg"
define audio.stone = "audio/sfx/stone.ogg"
define audio.tinybox = "audio/sfx/tinyboxopen.ogg"
define audio.toolrack  = "audio/sfx/toolrack.ogg"
define audio.tools = "audio/sfx/tool.ogg"
define audio.toss = "audio/sfx/toss.ogg"
define audio.treemove  = "audio/sfx/treemove.ogg"
define audio.WilburCry = "audio/sfx/WilburCry" #J30 but it's BAD bad :(
define audio.wind1  = "audio/sfx/wind1.ogg"
define audio.wind2 = "audio/sfx/wind2.ogg"
define audio.wrr = "audio/sfx/wrr.ogg"
define audio.zipclose  = "audio/sfx/zipclose.ogg"
define audio.zipopen  = "audio/sfx/zipopen.ogg"

