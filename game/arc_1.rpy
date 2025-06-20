label nov_1:
    
    stop music

    #Testing setup for Winter Jam spriting: with all of this commented out, the game will toss you into November as normal!
    #$ aston_safe = True #(False = Aston ded)
    #$ pearl_safe = True #(False = Pearl ded)
    #$ days404testing = True #If enabled, will have noncontiguous 404'd Days skip forward so you can see all of 'em in sequence (not chronological)
    #$ ruran_safe = True #(False = Ruran ded/going to die)
    #$ ru_branch_yoinked = True #(True = Ruran cause of death is by tree-branch yoinkage)
    #jump nov_17
    #jump dec_19
    #jump [whatever label you want here]
    

    #Regular November stuff
    $ current_day = _("November 1st")
    $ save_name = current_date(_("Prologue"), current_day)
    show screen date_label with dissolve
    show cg morganhome1
    $ persistent.gallery_morganhome = True

    play music audio.ad
    #voice "tr_n1_GlowGlow" #always post-processed, no branching needed
    pause(12.1)
    hi "Glow, glow, glow with NuGLO! Let us help you restore your skin's shiny, supple glow! {w=7.6}{nw}"
    
    play sound phonebuzz
    #voice "tr_n1_SoWhat"
    queue music audio.adwohilda
    hi "So what are you waiting for? Grab your very own NuGLO samples at your local stores today!"
    stop music fadeout 5.0

    $ hidebubbles = True
    play sound ding
    scene black
    #Morgan stands up and switches off the TV abruptly, his phone buzzes.

    #Click!
    show cg morganhome2

    voice "tr_n1_Heya"
    mo "Heya."
    #voice "tr_n1_GotEverything"
    if radio_static == "_s":
        voice "tr_n1_GotEverything_s"
    else:
        voice "tr_n1_GotEverything_c"
    co "Got everything you need, Morg?"
    voice "tr_n1_YepJust"
    mo "Yep, just zipping up here and I'm good to go."
    #voice "tr_n1_SureYou"
    if radio_static == "_s":
        voice "tr_n1_SureYou_s"
    else:
        voice "tr_n1_SureYou_c"
    co "Sure you got everything?"
    voice "tr_n1_CantFit"
    mo "Can't fit you in my bag, now, can I?"
    #Morgan zips his backpack.
    #voice "tr_n1_WouldntTry"
    if radio_static == "_s":
        voice "tr_n1_WouldntTry_s"
    else:
        voice "tr_n1_WouldntTry_c"
    co "Wouldn't try to even if you asked. I'd rather not be stuck in that for three days."
    voice "tr_n1_HahaWell"
    mo "Haha, well... I think it's just about time to head off!"
    #voice "tr_n1_AlrightyThen"
    if radio_static == "_s":
        voice "tr_n1_AlrightyThen_s"
    else:
        voice "tr_n1_AlrightyThen_c"
    co "Alrighty, then. Bring him home and stay safe, soldier."
    voice "tr_n1_IWill"
    mo "I will."

    #With one final look at his living room, Morgan swings his backpack onto his shoulder and then leaves his apartment.
label nov_4:
    scene black with dissolve
    with Pause(2)
    $ current_day = _("November 4th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    voice "n4_ImMorgan"
    mo "I'm Morgan. Undercover cop and proud member of the Special Operations Division."
    voice "n4_HereOn"
    mo "Here on a mission to unravel the secrets behind an operation held by Heralign Inc. far out in the snowy mountains."
    voice "n4_AndTo"
    mo "And to find out what happened to my partner in crime."
    voice "n4_HeToo"
    mo "He too was tasked to investigate the company and its operations before he was completely wiped off the radar."
    voice "n4_AndWhat"
    mo "And what does Heralign Inc. do, you may ask?"
    voice "n4_BehindThat"
    mo "Behind that pristine image of a pharmaceutical company lies Heralign Inc.'s poster business lady."
    voice "n4_HildaHilda"
    mo "Hilda. Hilda Heralign. CEO of Heralign, daughter of some billionaire."
    voice "n4_WhyWould"
    mo "Why would a company like that set out an operation so far away from HQ?"
    voice "n4_IGuess"
    mo "I guess I'm here to find out."
    scene black

    voice "n4_WereHere"
    ex1 "We're here."
    voice "n4_WhewAlright"
    mo "Whew, alright!"

    scene bg snowyplain with dissolve
    play ambience amb_campday fadein 1.0
    play sound cardoor
    "A vast stretch of white greets me as I exit the car."
    "The cold wind stings a little as it brushes my cheek. Might take a while before I get used to it."
    voice "n4_HeyThanks"
    mo "Hey, thanks for the ride!"
    voice "n4_NoWorries"
    ex1 "No worries. Gregory should be up ahead waiting for ya."

    "I gaze towards the direction where he pointed. Sure enough, there's an older man waving his hand at me."
    "I slowly make my way towards him. Trudging through the snow is a feat for sure."
    "It also doesn't help that I've been in the car for hours on end."
    show gr neutral with dissolve
    voice "n4_YoureMorgan"
    gr "You're Morgan, yes? I'm Gregory. Hope the ride up here wasn't too much for you to handle."
    voice "n4_WellWalking"
    mo "Well, walking in snow is definitely much more difficult than sitting in a car, I think. It's nice to meet you, Gregory."
    "He gives me a firm handshake."
    show gr happy with sdissolve
    voice "n4_LetsHead"
    gr "Let's head to camp."

    scene bg forest1 with longfade

    "Along the way, Gregory fills me in on the operation and the rest of the people at camp."
    "The mission? Collecting samples from the environment."
    "Be it sources of water, dirt, trees and maybe foliage, once the \nsnow melts."
    "We're basically here to run errands for the scientists here to find new sources of penicillin..."
    "The good stuff in antibiotic medication."
    "A.K.A. things that Heralign Inc. needs."
    "The Camp. Well... There's two camps, actually."
    "Five people in Camp 1 including myself, and five more in Camp 2."
    "There's also a Research Centre down south, where the research team's situated."
    "Talk about big investments, they have functional labs here."
    "I noticed buildings far off into the distance along the way."
    "They don't seem all that modern. A village perhaps?"
    "A large lake. Frozen all over."
    "And then there's a large mountain that we're walking towards."
    "After about an hour of walking, we've finally reached the campsite."
    scene bg camp1_day with dissolve
    "Against the white snow and the grayish brown trees, the pops of red and orange of the tents stand out beautifully."
    show gr happy
    voice "n4_GoodJob"
    gr "Good job keeping up, let me call the others over 'ere."
    play music audio.light
    voice "n4_EveryoneGather"
    gr "Everyone gather round 'ere, we got a new recruit!"
    hide gr
    show cg meeting
    $ persistent.gallery_meeting = True
    "Three people emerge from the tents."

    #camera to PEARL
    window auto hide
    camera:
        subpixel True
        pos (0, 0) zoom 1.0
        linear 0.40 pos (-955, -136) zoom 1.5
    with Pause(0.50)
    camera:
        pos (-955, -136) zoom 1.5
    window auto show

    voice "n4_OhMy"
    pe "Oh my goodness hello! My name is Pearl, it's super nice to meet you!"
    "Pearl. Chipper and welcoming. She looks like she's in her early 20s."

    #camera to LORENZO
    window auto hide
    camera:
        subpixel True
        pos (-955, -136) zoom 1.5
        linear 0.30 pos (1, 0) zoom 2.5
    with Pause(0.50)
    camera:
        pos (1, 0) zoom 2.5
    window auto show

    voice "n4_ImLorenzo"
    lo "I'm Lorenzo! Pleased to meet you!"
    "Lorenzo. He exudes an aura of a gentleman. Looks a little older than me."

    #camera to ASTON
    window auto hide
    camera:
        subpixel True
        pos (1, 0)
        linear 0.45 pos (-2500, -71)
    with Pause(0.55)
    camera:
        pos (-2500, -71)
    window auto show

    voice "n4_HelloImAston"
    ast "Hello, I'm Aston."
    "Aston. Quick and concise. Gregory said we're the same age."

    #camera to MORGAN
    window auto hide
    camera:
        subpixel True
        pos (-2500, -71) zoom 2.5
        linear 0.50 pos (-5, 3) zoom 1.5
    with Pause(0.60)
    camera:
        pos (-5, 3) zoom 1.5
    window auto show

    voice "n4_HelloImMorgan"
    mo "Hello! I'm Morgan, thanks for having me."
    voice "n4_OkayGood"
    gr "Okay... Good! Now that introductions are out of the way... Lorenzo, I need to borrow you for a second to talk about supplies."

    #back to EVERYONE
    window auto hide
    camera:
        subpixel True
        pos (-5, 3) zoom 1.5
        linear 0.60 pos (0, 0) zoom 1.0
    with Pause(0.70)
    camera:
        pos (0, 0) zoom 1.0
    window auto show

    voice "n4_SureThing"
    lo "Sure thing."
    voice "n4_PearlAston"
    gr "Pearl, Aston, go help Morgan out, will ya?"
    voice "n4_YouGot"
    pe "You got it sir! I'll show you around, Morgan!"
    stop ambience fadeout 1.0
    scene bg maintent_day with dissolve

    "I followed them into one of the bigger tents, it is much more spacious than I thought."
    "A small table, a shelf full of equipment and perishables, and some unlit lanterns on the ground."
    show pearl happy at centerleft
    show ast neutral at centerright
    with dissolve
    voice "n4_WelcomeTo"
    pe "Welcome to our little cave! We put lots of our equipment in here."
    show pearl smile with dissolve
    voice "n4_TheRest"
    pe "The rest outside are all personal tents for all your personal stuff."
    voice "n4_TheresExtra"
    pe "There's extra blankets, flare guns and thingies. Aston organizes everything here 'cause I always misplace stuff."
    show pearl confused with dissolve
    voice "n4_IThink"
    pe "... I think that's all we needed to show Morgan, right?"
    voice "n4_WalkieTalkie"
    ast "Walkie talkie, Pearl."
    show pearl happy with dissolve
    voice "n4_OhYes"
    pe "Oh, yes! The Walkie talkie!"
    play sound jacket
    "Pearl whips out a walkie talkie deep in her jacket pockets and hands it to me."
    show ast inthought with dissolve
    voice "n4_WeShould"
    ast "We should probably test it before you head out. Our codes have all been saved, you can reach any one of us anytime."
    voice "n4_TryTalking"
    ast "Try talking to me."

    #radio selection stuff happens here
    voice "n4_TestingTesting"
    wt_mo "Testing testing, hello hello."
    nvl clear
    show ast neutral with dissolve
    show pearl smile with dissolve
    voice "n4_AlrightIt"
    ast "Alright, it works."
    voice "n4_OohMorgan"
    pe "Ooh, Morgan! Do you wanna try reaching people from other camps?"
    voice "n4_SureAnyone"
    mo "Sure, anyone in particular that I should reach out to?"
    show pearl happy with dissolve
    voice "n4_DavosFrom"
    pe "Davos from Camp 2 and Koda from the Research Centre! They're both my best buds. I reminded them today that we have a newcomer so they should pick up instantly!"
    #choice branch start
    #radio selection stuff happens here
    $ pancake = False
    menu n4_call:
        "Call Davos" if not n4_call_da:

            hide ast with dissolve
            $ n4_call_da = True
            $ chibi_morgan = "images/chibi/morgan_happy.png"
            voice "n4_HelloThis"
            wt_mo "Hello this is Morgan, is Davos here?"
            if radio_static == "_s":
                voice "n4_OhHello_s"
            else:
                voice "n4_OhHello_c"
            wt_da "Oh, hello! Morgan, was it? It's nice to meet you!"
            if radio_static == "_s":
                voice "n4_ImIn_s"
            else:
                voice "n4_ImIn_c"
            wt_da "I'm in Camp 2, which is a little down south from where you're at!"
            $ chibi_morgan = "images/chibi/morgan_neutral.png"
            voice "n4_PleasedTo"
            wt_mo "Pleased to meet ya! There's also five of you there, yes?"
            $ chibi_davos = "images/chibi/davos_happy.png"
            if radio_static == "_s":
                voice "n4_HahaYes_s"
            else:
                voice "n4_HahaYes_c"
            wt_da "Haha, yes! I'm here with my pops Wilbur, Cassie, Ruran and Jax. They're kinda busy right now, though."
            if radio_static == "_s":
                voice "n4_DavosCould_s"
            else:
                voice "n4_DavosCould_c"
            wt_wi "Davos? Could you lend me a hand here?"
            $ chibi_davos = "images/chibi/davos_neutral.png"
            if radio_static == "_s":
                voice "n4_OopsGotta_s"
            else:
                voice "n4_OopsGotta_c"
            wt_da "Oops, gotta go! Talk to you next time Morgan!"
            nvl clear
        "Call Koda" if not n4_call_ko:
            hide ast with dissolve
            $ n4_call_ko = True
            $ chibi_morgan = "images/chibi/morgan_happy.png"
            voice "n4_HelloThisKoda"
            wt_mo "Hello, this is Morgan. Is this Koda?"
            $ chibi_koda = "images/chibi/koda_happy.png"
            if radio_static == "_s":
                voice "n4_OhIm_s"
            else:
                voice "n4_OhIm_c"
            wt_ko "Oh! I'm Koda, yes! I heard from Pearl you were arriving today."
            if radio_static == "_s":
                voice "n4_ImOver_s"
            else:
                voice "n4_ImOver_c"
            wt_ko "I'm over here at the RC with Eva and Isaak...they're both scientists. They're also both my supervisors."
            $ chibi_morgan = "images/chibi/morgan_neutral.png"
            voice "n4_AreYou"
            wt_mo "Are you not a scientist yourself, Koda?"
            if radio_static == "_s":
                voice "n4_WellNot_s"
            else:
                voice "n4_WellNot_c"
            wt_ko "Well, not quite yet... But I'm a lab assistant for now!"
            $ chibi_koda = "images/chibi/koda_worried.png"
            if radio_static == "_s":
                voice "n4_OhI_s"
            else:
                voice "n4_OhI_c"
            wt_ko "Oh, I think I have to go now. Isaak is looking for me. Bye Morgan!"
            nvl clear
    #choice branch end
    if not n4_call_da or not n4_call_ko:
        jump n4_call
    #back to Pearl after calling
    show pearl smile with dissolve
    voice "n4_SoHow"
    pe "So, how did it go?"
    voice "n4_WalkieTalkieWorksFor"
    mo "Walkie talkie works for sure. Thanks Pearl... And Aston?"
    show pearl neutral with dissolve
    voice "n4_AstonWent"
    pe "Aston went out to look for Lorenzo and Gregory."
    show pearl happy with dissolve
    voice "n4_ItsGetting"
    pe "It's getting late and the sun is going down, I think all that's left is to show you your tent!"
    show bg camp1_night
    hide pearl
    "Pearl walks me out to an orange tent, ensures I have all my supplies and then heads to her own for the night."

    scene bg morganstent with dissolve

    "Home sweet home. For the next few months."
    "The sleeping tent is much smaller, but it's enough for me."
    "I waited till the sun fully set, and watched the sky turn dark."
    "The others are in their tents all zipped up, which means it's probably time to update Colin on my whereabouts."

    show satphone
    #voice "n4_SoAre"
    if radio_static == "_s":
        voice "n4_SoAre_s"
    else:
        voice "n4_SoAre_c"
    co "So, are you all snuggled in with blankets, Morg?"
    voice "n4_YeahIm"
    mo "Yeah, I'm pretty sure I'll freeze out here if I don't."
    #voice "n4_YeahThat"
    if radio_static == "_s":
        voice "n4_YeahThat_s"
    else:
        voice "n4_YeahThat_c"
    co "Yeah, that won't be ideal, man."
    voice "n4_CoActually"
    mo "Co- Actually, no. You don't get to be him now. Hmm... How about Pancake?"
    #voice "n4_YouAnd"
    if radio_static == "_s":
        voice "n4_YouAnd_s"
    else:
        voice "n4_YouAnd_c"
    co "You and Elly, I swear... He calls me Pangolin and you call me Pancake. Y'all are not creative."
    voice "n4_ItsKinda"
    mo "It's kinda your fault, you know."
    #voice "n4_ItsMy"
    if radio_static == "_s":
        voice "n4_ItsMy_s"
    else:
        voice "n4_ItsMy_c"
    co "It's my kiddo's drawing! Can't pay me to change it."
    #voice "n4_ButAnyway"
    if radio_static == "_s":
        voice "n4_ButAnyway_s"
    else:
        voice "n4_ButAnyway_c"
    co "But anyway, I'm sure you're tired, Morg. Rest up, you hear?"
    voice "n4_AlrightAlright"
    mo "Alright, alright. Goodnight, Pancake. I'll catch you later."
    hide satphone
    stop music

#DONE relabeling N4
label nov_5:
    play music audio.neutral
    scene bg morganstent with longfade
    $ current_day = _("November 5th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    #INT: Morgan's tent

    "I woke up to the sound of Pearl calling for me outside my tent."
    "Man, do I miss the comfort of an actual bed. My back is still sore from all the traveling."

    voice "n5_WakeUp"
    pe "Wake up Morgaaannnn. Gregory's about to start!"

    show bg camp1_day with dissolve

    show pearl smile at center

    "I barely had a second to adjust to the sunlight before Pearl dragged me to the center of the campsite."
    hide pearl with dissolve
    show lorenzo smile at left
    show ast neutral at centerleft
    "Lorenzo and Aston are already up. Looks like they're making breakfast."
    show gr angry at right
    hide lorenzo
    hide ast
    "And Gregory... He looks like he's about to chew me out for being late."
    "Whoops."

    show gr angry:
        subpixel True
        xpos 1.0
        linear 0.50 xpos 0.8
    with Pause(0.60)
    show gr angry:
        xpos 0.8

    voice "n5_AlrightNice"
    gr "Alright nice, you're up. I'll cut you some slack since it's your first day."
    show gr neutral with dissolve
    voice "n5_AndBecause"
    gr "And because it's your first day here, we gotta make sure you understand the rules."

    "He hands me a booklet."
    "'{i}The Camp Guide's Guide{/i}'"
    "That's not a very creative name."

    show pearl confused at centerleft
    voice "n5_IveBeen"
    pe "I've been through this a thousand times, do I still need to be here?"
    voice "n5_YeahBecause"
    gr "{w=1.2}Yeah...because you need reminding every time you attempt to do something reckless."
    show pearl sad with dissolve
    voice "n5_PearlVNVR"
    pe "..."

    hide gr
    hide pearl 
    with dissolve
    "Gregory runs us through the list of basic camp rules."
    "All of which I'm already familiar with."
    "Time to put that 3 months of camp training knowledge to work."
    "\"Do not interact with animals.\""
    "Sure, I can do that."
    "\"Do not consume berries or plants you see without proper identification.\""
    "The closest hospital is 4 hours away, I won't like that ending."
    "\"Do show up for roll call before sundown.\""
    "A necessary routine, yada yada."
    "That is, until Gregory flips the pages and reads the rules specifically for our camp and operations."

    "\"Do not hike alone without supervision.\""
    "\"Do not go out at night.\""
    "Alright, easy stuff."

    "\"Do not attempt to traverse the east side of the mountain alone.\""
    "Oddly specific, but okay?"

    "\"Do not head north to the village.\""
    "Does he mean the village we passed yesterday?"

    "\"Do not attempt to handle animal carcasses without protective gear.\""
    "What kind of gear are we talking about? And why are we handling carcasses?"

    "\"Do not leave camp under any circumstances.\""
    "\"Do not call HQ unless you have permission to.\""
    "Oh lovely, those sound like bright red flags."

    show gr at right
    show pearl at centerleft
    with dissolve

    voice "n5_GotAny"
    gr "Got any questions?"
    voice "n5_YeahUh"
    mo "Yeah, uh... what's with the location specific ones? Wasn't the village to our right yesterday?"
    voice "n5_WellYeah"
    gr "Well yeah, but I just follow HQ's orders. So it's best we don't try anything funny."
    show gr confused with dissolve
    voice "n5_HeardThe"
    gr "Heard the villagers there weren't too keen with this whole makeshift camp base situation we're having here."
    voice "n5_AndWere"
    mo "And we're not supposed to call anyone from HQ? Unless we get permission from...?"
    show gr neutral with dissolve
    voice "n5_ThatWould"
    gr "That would be me. Easier to have one person to gather reports from, they said."

    "Those were pretty vague answers."
    "But I don't think I should push my luck with the questions for now."

    voice "n5_AlrightPearl"
    gr "Alright... Pearl? Any questions from ya?"
    show pearl happy
    voice "n5_IsIt"
    pe "Is it time for breakfast? Cause I smell something!"
    show gr worried with dissolve
    voice "n5_GregoryVNVR"
    gr "..."
    show gr neutral with dissolve
    voice "n5_LetsEat"
    gr "Let's eat, I guess."

    "Aston hands us all our breakfast burritos."
    "Pearl's burrito has a ridiculous amount of tomato sauce."

    "The rest of the day was spent on learning how to use camp gear and equipment."
    "Basic first aid."
    "Little survival skills to brave the cold."
    "Nothing too complicated."

    "The days definitely seem much shorter here."
    "Looks like I'll have to get used to not having much daytime for the time being."
    stop music fadeout 3.0

label nov_6:
    #INT: Morgan's tent
    scene morganstent with longfade
    $ current_day = _("November 6th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    play ambience amb_intcampday fadein 1.0
    "Nice, I woke up on time."
    "Today is sample collection day. Wouldn't want to miss that."
    "Wonder what that's all about?"
    "I should go look for the rest."

    scene bg maintent_day with dissolve
    show lorenzo pondering with dissolve
    "As I entered the tent, I saw a lone Lorenzo scribbling away at his notebook."
    "The rest were outside around the campfire, preparing breakfast."

    voice "n6_SoHow"
    mo "So, how's your morning going?"
    show lorenzo neutral
    voice "n6_JustLiaising"
    lo "Just liaising with the supply crew at HQ. A financier's job never ends until everyone gets supplies."
    voice "n6_AndAs"
    lo "And as you may notice... I'm not exactly fit to be a camp guide. So this is the best I can do."
    voice "n6_NahI"
    mo "Nah, I wouldn't have guessed."
    show lorenzo smile
    voice "n6_YouFlatter"
    lo "You flatter me Morgan. Aston, on the other hand, would've been a much better fit."
    voice "n6_ButHe"
    mo "But he chose to be a field medic?"
    voice "n6_ManyWays"
    lo "Many ways to help others, he said. Plus, being a medic means that we get to spend more time together."
    voice "n6_ThatsAwfully"
    mo "That's awfully cute."
    show lorenzo happy
    "Lorenzo beams at me."
    "I wonder how long they've been together."
    "Our conversation was interrupted by Gregory calling us over to gear up."
    "Alrighty, I guess it's time."
    stop ambience fadeout 3.0

    scene bg forest3 with dissolve
    play ambience amb_campday fadein 1.0
    show gr neutral at centerright with dissolve

    "Gregory begins by going through a long checklist of items to collect for the day."
    play sound tools
    "He hands Pearl and I some bags and tools."
    show pearl neutral at centerleft
    voice "n6_AlrightThe"
    gr "Alright. The plan is simple. We go out, grab dirt samples, and then I'll send them back to the lab."
    voice "n6_TodayLets"
    gr "Today... Let's see... We'll start by gathering some over 'ere."

    "Holding the map up, Gregory points to a location marked by his pens."
    "This is the first time I've seen the full picture. I wish I could get one myself, but it seems like they ran out of maps."
    "The ones in the main tent haven't been updated since summer. The terrain looks entirely different from what we're dealing with now."

    voice "n6_SoI"
    mo "So I reckon Camp 2 does the same?"
    show gr worried
    voice "n6_SameTasks"
    gr "Same tasks, different area. Environmental study or some shit. I'm not exactly the guy to ask, but if that helps the research team, I ain't complaining."
    show pearl smile with sdissolve
    voice "n6_NeverThought"
    pe "Never thought I'd be excited to play with dirt again."
    show gr neutral
    voice "n6_PleaseDont"
    gr "Please don't tarnish the samples with your hands."
    show pearl sad with sdissolve
    voice "n6_Okaaay"
    pe "Okaaay."
    hide gr with dissolve
    hide pearl with dissolve
    "Snow and dirt. Alright, let's see..."
    play sound scoop1
    "Scoop."


    "To my eyes, it looks like plain old dirt."
    "Not gravelly, just wet cold soil with no bugs in it."
    play sound scoop2
    "Two scoops to fill up the bag."
    "That'll do for now."
    "We were also tasked to observe the trees, changes to terrain, weather and such."
    "Honestly this is beginning to sound like a dream job. Get paid looking at trees?"
    "Looking at the checklist in my hands... Let's see here..."

    "\"Tree trunk color?\" Gray brown."
    "\"Leaves present?\" None."
    "\"Flaky tree bark?\" Doesn't seem like it."
    "\"Any growths (ferns, fungi, etc.)?\""
    "No sign of weird growths. Not that I can tell."
    "I don't think ferns or fungi can grow in this harsh weather."
    "\"Roots exposed?\" I don't think so."
    "\"Other observations if any:\""
    "I assume animals have been around here, cause these seem like animal claw marks around the base?"
    "Big enough to be a wolf maybe?"
    "I'm just glad it doesn't smell."

    voice "n6_Morgan"
    pe "Morgan!"
    show pearl happy with sdissolve

    "That made me jump."

    voice "n6_GoodnessYou"
    mo "Goodness, you scared me."
    voice "n6_HehWant"
    pe "Heh, want some water or snacks?"
    voice "n6_ThatWould"
    mo "That would be nice, thanks Pearl."
    show pearl smile with sdissolve
    "She hands me a small box of trail mix and a flask filled with water."

    voice "n6_SoHow"
    mo "So how long have you been here Pearl?"

    voice "n6_ActuallyIve"
    pe "Actually, I've only been here for two months! Just a little later than Davos and Koda at least."
    voice "n6_MetDavos"
    pe "Met Davos at the academy waaaay before and he introduced me to Koda! I kinda miss them now though."
    voice "n6_GregorysUsually"
    pe "Gregory's usually the one in charge of delivering stuff, especially during the stormy season. So I haven't seen them in two weeks."

    voice "n6_YouveNever"
    mo "You've never followed him to the RC?"
    show pearl depressed with sdissolve
    voice "n6_NotReally"
    pe "Not really, I prefer staying at camp than riding the snowmobile. Motion sickness ain't my best friend so..."
    voice "n6_Snowmobile"
    mo "Snowmobile?"
    show pearl happy with sdissolve
    voice "n6_YeahThe"
    pe "Yeah! The one that goes vroom-vroom, but in snow! Gregory has one, I don't remember where he parks it though, it's a tiny walk from camp."

    "That's interesting to know."
    hide pearl with dissolve
    "I finished up the remainder of my trail mix, and got back to work."
    "Gregory seems pleased with my reports."
    "Not bad, Morgan. Maybe I am suited to be a camp guide."
    stop ambience fadeout 1.0

label nov_7_11:
    #7th
    play music audio.light
    scene bg waterbody with longfade
    $ current_day = _("November 7th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve

    "Another sample collection day."
    "Today we're breaking some of the ice at the lake."
    "As we approached the body of frozen water, Pearl almost slipped on the ice."
    "I'm not sure if it's my imagination, but the lake looks like it has a slight tinge of green hues."
    "Science ain't my forte anyway. I guess if the water is green, then the water is green."
    show pearl smile at centerleft
    show gr neutral at centerright
    with dissolve
    voice "n7_PearlCould"
    gr "Pearl, could you get me the-"
    show pearl happy with sdissolve
    voice "n7_ThePick"
    pe "The pick? I got it sir!"
    show gr worried
    voice "n7_NoThe"
    gr "No, the-"
    voice "n7_OHThe"
    pe "OH, the ice saw thingy? Here you go sir!"
    show gr scared
    voice "n7_GregoryVNVR"
    gr "..."
    voice "n7_ActuallyPearl"
    gr "Actually Pearl... I just want the checklist."
    voice "n7_YouGot"
    pe "You got it!"
    show gr neutral
    "Gregory seems like he's having a great time."

    #8th
    #EXT: Camp 1
    scene bg camp1_night with longfade
    $ current_day = _("November 8th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve

    "After a long day, Aston decided that we should have canned soup for tonight."
    "He walks over to Pearl and hovers two different flavors in her face."
    show cg tomatosoup with sdissolve
    $ persistent.gallery_tomatosoup = True
    voice "n8_WeHave"
    ast "We have tomato soup and... {w=0.6}Pea soup. Which one do you want?"
    voice "n8_Hmmmm"
    pe "Hmmmm..."
    voice "n8_PearlVNVR"
    pe "..."
    voice "n8_Well"
    ast "Well?"
    voice "n8_IKinda"
    pe "I kinda want to try pea soup today but..."
    voice "n8_AlrightTomato"
    ast "Alright, tomato it is."
    voice "n8_Hehe"
    pe "Hehe."

    "Judging from his reaction, he hates pea soup, doesn't he?"

    #9th
    #INT: Main tent
    $ current_day = _("November 9th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    scene bg maintent_day with longfade

    "Lunch time. {w=0.6}Time to grab a quick snack from the food shelf."
    "I noticed Lorenzo was in the midst of counting meat and potato meal packets."
    show lorenzo pondering

    voice "n9_4647"
    lo "46... 47... 48..."
    voice "n9_OhWait"
    lo "Oh wait, where did I put my pen...?{w=1.0} Ah!"
    show lorenzo smile

    "Lorenzo found his pen, but at what cost?"
    show lorenzo neutral
    voice "n9_LorenzoVNVR"
    lo "..."
    voice "n9_YouStopped"
    mo "You stopped at 48."
    show lorenzo happy with sdissolve
    voice "n9_OhThank"
    lo "Oh! Thank you, Morgan. {w=0.5}49... 50... 51..."
    show lorenzo pondering with sdissolve
    voice "n9_57Thats"
    lo "57? That's not nearly enough for a month! I'll need to call support."
    voice "n9_Isnt57"
    mo "Isn't 57 plenty?"
    show lorenzo smile with sdissolve
    voice "n9_NotIf"
    lo "Not if Gregory and Aston keep inhaling them so quickly."
    voice "n9_IHave"
    mo "I have to agree that it's probably the best thing we have."
    voice "n9_SiAmico"
    lo "Si amico. So 57 isn't nearly enough."

    #10th
    #EXT: Camp 1
    scene bg camp1_day with longfade
    $ current_day = _("November 10th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    play sound snowmobile loop
    "While walking back to my tent, I spot Gregory. Looks like he's about to go to the RC on his snowmobile."
    show gr neutral
    "Never actually paid attention to how cool it looks."
    "Maybe I should demand one from Colin."

    voice "n10_IsaakSamples"
    gr "Isaak, samples are coming in about 30 minutes. Do you need anything else?"
    voice "n10_NoThatll"
    isa "No, that'll do. I'll have Koda retrieve it for me later."
    voice "n10_YoureReally"
    gr "You're really working that kid to the bone, huh?"
    isa "They're helpful. I don't see why not?"
    show gr angry with sdissolve
    voice "n10_YoureAn"
    gr "You're an ass, you know that?"
    voice "n10_IsaakVNVR"
    isa "..."
    show gr worried with sdissolve
    voice "n10_AlrightIll"
    gr "Alright, I'll be on my way."

    "They're not friends. Noted."
    stop sound

    #11th
    #INT: Main tent
    scene bg maintent_day with longfade
    $ current_day = _("November 11th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve

    "I had some free time on my hands today. According to the numbers that Colin gave me, I have yet to meet the majority of the people here."
    "The weather isn't suitable for walking longer distances. Apparently it's going to get stormy during these few weeks... months, even."
    "And of course I can't possibly use Gregory's snowmobile. I'm still envious."
    "I suppose the Walkie shall suffice for now."
    "Who should I beep first?"

    #choice branch starts
    menu wt_intro:
        "Beep Wilbur":
            if not wt_intro_wi:
                $ wt_intro_wi = True
                $ chibi_wilbur = "images/chibi/wilbur_happy.png"
                if radio_static == "_s":
                    voice "n11_HelloMorgan_s"
                else:
                    voice "n11_HelloMorgan_c"
                wt_wi "Hello Morgan! I heard lots about you from Pearl and Davos!"
                $ chibi_morgan = "images/chibi/morgan_happy.png"
                voice "n11_ImSurprised"
                wt_mo "I'm surprised you already knew about me, they sure are close."
                $ chibi_wilbur = "images/chibi/wilbur_neutral.png"
                if radio_static == "_s":
                    voice "n11_WellYes_s"
                else:
                    voice "n11_WellYes_c"
                wt_wi "Well, yes! News travels fast around here lad! Oh! Ruran, my friend, would you like to say hi?"
                $ chibi_ruran = "images/chibi/ruran_happy.png"
                if radio_static == "_s":
                    voice "n11_IsIt_s"
                else:
                    voice "n11_IsIt_c"
                wt_ru "Is it Morgan? It is nice to meet you, Morgan. I'm Ruran."
                $ chibi_morgan = "images/chibi/morgan_neutral.png"
                voice "n11_OhThe"
                wt_mo "Oh, the other camp medic? Aston told me that you're his mentor."
                if radio_static == "_s":
                    voice "n11_YesI_s"
                else:
                    voice "n11_YesI_c"
                wt_ru "Yes, I am. He's great, and it's always nice to have extra hands in case of emergencies."
                if radio_static == "_s":
                    voice "n11_HopeAston_s"
                else:
                    voice "n11_HopeAston_c"
                wt_wi "Hope Aston will warm up to you soon...that boy has always been a man of few words. Know him long enough, and you'll realize he's a big softie!"
                $ chibi_morgan = "images/chibi/morgan_happy.png"
                voice "n11_AstonAnd"
                wt_mo "'Aston' and 'softie' were two words I never expected in the same sentence, but thank you for telling me."
                $ chibi_morgan = "images/chibi/morgan_neutral.png"
                voice "n11_IllLet"
                wt_mo "I'll let y'all go for now, tell Davos I said hi!"
                if radio_static == "_s":
                    voice "n11_CallUs_s"
                else:
                    voice "n11_CallUs_c"
                wt_ru "Call us anytime, Morgan!"
                if radio_static == "_s":
                    voice "n11_IfOnly_s"
                else:
                    voice "n11_IfOnly_c"
                wt_wi "If only this darn wind would let up, I'd love to meet you in person soon!"
                nvl clear
                jump wt_intro
            else:
                "I don't think I need to do that now."
                jump wt_intro

        "Beep Cassie":
            if not wt_intro_ca:
                $ wt_intro_ca = True
                $ chibi_cassie = "images/chibi/cassie_happy.png"
                if radio_static == "_s":
                    voice "n11_WhatA_s"
                else:
                    voice "n11_WhatA_c"
                wt_ca "What a coincidence! I was just about to beep ya! I'm Cassie!"
                $ chibi_morgan = "images/chibi/morgan_neutral.png"
                voice "n11_ItsNice"
                wt_mo "It's nice meeting you Cassie, I'm Morgan."
                $ chibi_cassie = "images/chibi/cassie_neutral.png"
                if radio_static == "_s":
                    voice "n11_WellI_s"
                else:
                    voice "n11_WellI_c"
                wt_ca "Well, I just want to let you know that I have a map ready for you! The next time Lorenzo or Gregory comes by, I'll have them be our courier pigeon."
                $ chibi_morgan = "images/chibi/morgan_happy.png"
                voice "n11_ThanksI"
                wt_mo "Thanks! I appreciate it!"
                $ chibi_cassie = "images/chibi/cassie_happy.png"
                if radio_static == "_s":
                    voice "n11_AnytimeMorgan_s"
                else:
                    voice "n11_AnytimeMorgan_c"
                wt_ca "Anytime, Morgan!"
                nvl clear
                jump wt_intro
            else:
                "I don't think I need to do that now."
                jump wt_intro

        "Beep Jax":
            if not wt_intro_ja:
                $ wt_intro_ja = True
                if radio_static == "_s":
                    voice "n11_YeahIs_s"
                else:
                    voice "n11_YeahIs_c"
                wt_ja "Yeah, is this the new guy?"
                $ chibi_morgan = "images/chibi/morgan_neutral.png"
                voice "n11_HiJax"
                wt_mo "Hi Jax, I'm Morgan. Just thought I'd check on everyone."
                $ chibi_jax = "images/chibi/jax_happy.png"
                if radio_static == "_s":
                    voice "n11_ThatsNice_s"
                else:
                    voice "n11_ThatsNice_c"
                wt_ja "That's nice of you."
                $ chibi_jax = "images/chibi/jax_neutral.png"
                if radio_static == "_s":
                    voice "n11_JustDoing_s"
                else:
                    voice "n11_JustDoing_c"
                wt_ja "Just doing a routine cleanup on my rifles, nothing much."
                voice "n11_OhNice"
                wt_mo "Oh nice, didn't know we had rifles at camp."
                if radio_static == "_s":
                    voice "n11_YouKnow_s"
                else:
                    voice "n11_YouKnow_c"
                wt_ja "You know how to handle one?"
                $ chibi_morgan = "images/chibi/morgan_happy.png"
                voice "n11_ImA"
                wt_mo "I'm a little out of practice."
                if radio_static == "_s":
                    voice "n11_UsuallyPeople_s"
                else:
                    voice "n11_UsuallyPeople_c"
                wt_ja "Usually, people say that to sound humble."
                $ chibi_morgan = "images/chibi/morgan_neutral.png"
                voice "n11_NahI"
                wt_mo "Nah. I am actually pretty rusty."
                $ chibi_jax = "images/chibi/jax_happy.png"
                if radio_static == "_s":
                    voice "n11_WellHave_s"
                else:
                    voice "n11_WellHave_c"
                wt_ja "We'll have to see about that."
                $ chibi_morgan = "images/chibi/morgan_happy.png"
                voice "n11_Bet"
                wt_mo "Bet."
                nvl clear
                jump wt_intro
            else:
                "I don't think I need to do that now."
                jump wt_intro

        "Beep Isaak":
            $ wt_intro_isa += 1
        #Isaak won't pick up the first or second time
            if wt_intro_isa <= 2:
                "Nothing. There doesn't seem to be any response."
                jump wt_intro

        #beeping Isaak for the third time
            elif wt_intro_isa == 3:
                if radio_static == "_s":
                    voice "n11_ThisBetter_s"
                else:
                    voice "n11_ThisBetter_c"
                wt_is "This better be an emergency."
                $ chibi_morgan = "images/chibi/morgan_worried.png"
                voice "n11_NotReally"
                wt_mo "Not really. I'm just calling to say hi."
                if radio_static == "_s":
                    voice "n11_ImIsaak_s"
                else:
                    voice "n11_ImIsaak_c"
                wt_is "I'm Isaak, you're Morgan. I don't like small talk, nor do I like people who try to make me engage in small talk."
                if radio_static == "_s":
                    voice "n11_Goodbye_s"
                else:
                    voice "n11_Goodbye_c"
                wt_is "Goodbye."
                nvl clear
                jump wt_intro

            elif wt_intro_isa == 4:
                "Isaak stops responding to you."
                "Rude."
                jump wt_intro

            else:
                "I don't think I need to do that now."
                jump wt_intro

        "Beep Eva":
            if not wt_intro_ev:
                $ wt_intro_ev = True
                if radio_static == "_s":
                    voice "n11_Yes_s"
                else:
                    voice "n11_Yes_c"
                wt_ev "Yes?"
                $ chibi_morgan = "images/chibi/morgan_neutral.png"
                voice "n11_ItsMorgan"
                wt_mo "It's Morgan, just thought I'd call to say hello!"
                $ chibi_eva = "images/chibi/eva_happy.png"
                if radio_static == "_s":
                    voice "n11_AhYes_s"
                else:
                    voice "n11_AhYes_c"
                wt_ev "Ah yes, the new guy. I'm Eva, I think Koda already told you."
                $ chibi_eva = "images/chibi/eva_neutral.png"
                if radio_static == "_s":
                    voice "n11_ICant_s"
                else:
                    voice "n11_ICant_c"
                wt_ev "I can't talk for long, though. Gotta run some errands."
                voice "n11_IllLeave"
                wt_mo "I'll leave you to it, then."
                nvl clear
                jump wt_intro
            else:
                "I don't think I need to do that now."
                jump wt_intro

        "Beep Ruran":
            if wt_intro_ru == 0:
                $ wt_intro_ru += 1

                "Oh, well. It looks like her Walkie may be charging right now."
                jump wt_intro

        #beep Ruran after the first beep
            else:
                "Probably still charging."
                jump wt_intro

        #everyone has to be called once, if not the player shouldn't be able to leave the selection screen

        #Next line split/commented out for now because having to hit this button is inconsistent with future comparable menus (e.g. J13); can add back in if desired
        "That's everyone!" if wt_intro_ca and wt_intro_ev and wt_intro_isa >= 1 and wt_intro_ja and wt_intro_ru == 1 and wt_intro_wi:
        #exit radio to end branch
            nvl clear
            jump wt_intro_end
            #choice branch ends
    if not wt_intro_ca or not wt_intro_ev or wt_intro_isa < 1 or not wt_intro_ja or wt_intro_ru < 1 or not wt_intro_wi:
        jump wt_intro

    label wt_intro_end:
        "I think that's all of them."
        "Wilbur, Davos' father. Like Gregory, a senior camp guide. Friendly and welcoming."
        "Ruran. The camp medic. She seems like a nice lady."
        "Cassie. I assume the cartographer. Also nice."
        "Jax. Another senior camp guide, I think. Sounds like he knows his stuff about weapons."
        "Eva. Koda's senior at the RC. She seems busy."
        "Isaak. Also at the RC. That's really all I know for now."
        "That brings us to a total of 12 people here."
        "I should update Colin when I have the chance."
        stop music

label nov_12:
    #EXT: Village
    scene bg village1 with longfade
    $ current_day = _("November 12th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    play ambience amb_village fadein 1.0
    #Kyle's POV
    show ky smile at centerleft with dissolve
    voice "n12_JustOne"
    ky "Just one more shot of y'all together... Yep, that's cute!"
    play sound camera2
    "Click click!"

    voice "n12_OneMore"
    ky "One more... And, done!"

    voice "n12_IWanna"
    v1 "I wanna see, I wanna see!"
    voice "n12_SusiesSo"
    v2 "Susie's so pretty... Thanks for this, Mr. Kyle!"
    show ky happy
    voice "n12_KyleIs"
    ky "Kyle is just fine! And you're welcome!"
    voice "n12_Moo1"
    vs "Moo."
    voice "n12_DoYou"
    ky "Do you want a portrait of just yourself, Susie?"
    voice "n12_Moo2"
    vs "Moo!"
    hide ky with dissolve
    show bg village1_kyle with dissolve

    "Kyle rolled up his sleeves and got to work."
    play sound camera3
    "Click click click!"

    voice "n12_HereYou"
    ky "Here you go Susie!"

    "Kyle tilts his camera towards Susie."

    voice "n12_SusieVNVR"
    vs "..."

    "Susie studies her portrait."

    voice "n12_WhatsWrong"
    v1 "What's wrong, Susie?"

    voice "n12_WasIt"
    ky "Was it... Not to her liking?"
    voice "n12_AreYou"
    v2 "Are you okay?"

    "The kids start petting Susie's back."
    "Kyle reached out to pet Susie's head but before he could even reach her-"

    "CHOMP!"
    show bg village1 with sdissolve
    show ky shaken
    "Susie bit his forearm."

    voice "n12_Moo3"
    vs "Moooo!"
    show ky sad
    voice "n12_Owwie"
    ky "Owwie."
    voice "n12_HahaIt"
    v1 "Haha! It means Susie likes it! She's happy."
    show ky confused
    voice "n12_ImNot"
    ky "I'm not sure if that's normal cow behavior."
    voice "n12_DidIt"
    v2 "Did it hurt, Mr. Kyle?"

    "Gazing down at his forearm, it seems like Susie's bite managed to break the skin."
    "It's red, but it doesn't hurt that much."
    "Simple first aid should do the trick."

    show ky smile
    voice "n12_IThink"
    ky "I think I'll be alright!"
    voice "n12_Moo4"
    vs "Mooo..."
    show ky happy
    voice "n12_ApologyAccepted"
    ky "Apology accepted Susie!"

    "Kyle reaches out again, this time with his sleeves down."
    "Achievement unlocked...{w=0.4} He pets the cow!"
    "After getting his fill of cow scritches, Kyle bids the children goodbye."
    "Susie isn't wild, but a fluffy friend nonetheless."
    "But to Kyle, his mission is far from over."
    "He grips his camera tightly in his hands."
    "His determination, unwavering."
    "Kyle is going to be the best wildlife photographer to ever exist."
    "Or so he tries to tell himself."
    "After the fact he got bitten by a cow of all things."
    stop ambience fadeout 1.0


label nov_13:
    scene bg morganstent with longfade
    $ current_day = _("November 13th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve

    "It's been roughly a week since I've been here."
    "Everything seems normal, perhaps a little too normal."
    "Collected samples again earlier this afternoon."
    "Dinner ended two hours ago and everyone is about to head to bed soon."
    "I don't feel sleepy yet."
    "I think I'll just walk a circle around camp."

    scene bg camp1_night with dissolve

    #SFX snowfoot
    "Night walks are my happy place."
    "The scenery is different than in the city, but at least the air is fresher here."
    "Quiet city to quiet campsite."
    "City lights to the lanterns and stars."
    "My sneakers to snow boots."
    "Only thing different is that Elly isn't here."
    "He'd join me sometimes. I miss that."
    "I wish he'd just-"

    show gr scared

    voice "n13_IUnderstand"
    gr "I understand ma'am, but that's not possible."
    play music audio.anxious


    "Oh, is he on the phone?"

    voice "n13_WellHave"
    gr "We'll have to wait till the lake unfreezes."
    if radio_static == "_s":
        voice "n13_SoNothing_s"
    else:
        voice "n13_SoNothing_c"
    who "So nothing new to report? It's getting pretty boring, Gregory."
    show gr neutral with dissolve
    voice "n13_ICant"
    gr "I can't move mountains nor change the seasons."
    if radio_static == "_s":
        voice "n13_WhatAbout_s"
    else:
        voice "n13_WhatAbout_c"
    who "What about the boy? The coppers would've been onto it by now."

    "Hey, that's me."
    show gr confused with sdissolve
    voice "n13_WhatBoy"
    gr "What boy? What d'ya mean?"
    voice "n13_YouTold"
    gr "You told me to take care of 'em, but Isaak insisted on helping me out."
    if radio_static == "_s":
        voice "n13_AndYouNeverQuestioned_s"
    else:
        voice "n13_AndYouNeverQuestioned_c"
    who "And you never questioned him?"
    show gr angry with dissolve
    voice "n13_LookYou"
    gr "Look, you hired the guy, not me. And you told me to work with him."
    show gr neutral with dissolve
    voice "n13_INever"
    gr "I never had a choice."
    if radio_static == "_s":
        voice "n13_AndYouNeverWill_s"
    else:
        voice "n13_AndYouNeverWill_c"
    who "And you never will until you get this done. Remember what's at stake here, Gregory. I am not repeating myself."
    voice "n13_OkayOkay"
    gr "Okay, okay. If pressure is what you want, I'll do it."
    if radio_static == "_s":
        voice "n13_FindHim_s"
    else:
        voice "n13_FindHim_c"
    who "Find him. I don't want to be the one playing clean up every time."

    "Whoever he's talking to sounds full of themselves."
    show gr angry
    voice "n13_HerPlaying"
    gr "Her? Playing clean up? What a load of bullshit. I'm the one here cleaning up every damn time."

    hide gr

    "I hope he ended the call before he said that."
    "Looks like the night walk did yield some great intel."
    "Someone Gregory and Isaak report to."
    "And a boy... {w=0.4}Elly?"
    "Nope. I'm not gonna think about the worst case scenario just yet."
    "Let's head to bed."
    stop music fadeout 3.0


label nov_14:
    #INT: Morgan's tent
    scene bg morganstent with longfade
    play ambience amb_intcampday fadein 1.0
    $ current_day = _("November 14th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve

    play sound wrr
    "WRRRRRRRR..."

    "What in the world was that?"
    "Is it coming from the radio?"
    stop ambience fadeout 3.0
    #EXT: Camp 1
    scene bg camp1_day with dissolve
    play ambience amb_campday fadein 1.0

    show lorenzo sad with dissolve
    voice "n14_OhMorgan"
    lo "Oh, Morgan. Good morning!"

    "Lorenzo greets me as I crawl out my tent."
    "A worried expression plastered on his face."
    voice "n14_ITake"
    mo "I take it that there's bad news?"
    voice "n14_SnowStorm"
    lo "snowstorm warning. Looks like we have one coming real soon."
    voice "n14_AnyIdea"
    mo "Any idea when that'll be?"
    voice "n14_CouldHappen"
    lo "Could happen in a matter of the next few hours, could happen in a day or two."
    show gr neutral at right
    voice "n14_AnyhowWe"
    gr "Anyhow, we should start preparing ourselves. I'll give Wilbur a call."
    voice "n14_ISuppose"
    mo "I suppose we should also do our part, yeah?"
    show ast neutral at left

    "Aston hands me a hammer and some ropes."

    voice "n14_HelpMe"
    ast "Help me secure the tents to the trees."
    show lorenzo with move:
        xpos 700
    voice "n14_AmoreIve"
    lo "Amore, I've locked the supply crates. Anything else you need me to do?"
    voice "n14_CouldYou"
    ast "Could you help me keep the crockpot away? Thank you."
    show pearl smile at centerright with sdissolve
    voice "n14_ManImagine"
    pe "Man, imagine if the wind blows and we all end up flying. That would be horrible!"
    show lorenzo sick with dissolve
    voice "n14_DontPut"
    lo "Don't put that image in my head, Pearl... That's terrifying!"
    show pearl sad
    voice "n14_Sorry"
    pe "Sorry."
    show lorenzo neutral with dissolve
    scene bg camp1_day with dissolve
    "With the tents fully secured, we went about our day at the campsite."
    "Can't collect samples when there's a storm that could strike at any moment."
    "Roll call happened much earlier today, and everyone went back to their respective tents to hunker down for the night."
    "This would probably be a great time to call Colin for updates."
    stop ambience fadeout 3.0

    scene bg morganstent with fade
    play ambience amb_intcampnight fadein 1.0

    show satphone
    voice "n14_HowsMy"
    mo "How's my Pancake doing?"
    #voice "n14_DoingGreat"
    if radio_static == "_s":
        voice "n14_DoingGreat_s"
    else:
        voice "n14_DoingGreat_c"
    co "Doing great, Morg. Any updates?"
    voice "n14_WellOne"
    mo "Well, one thing's for sure... Gregory reports to someone higher up in Heralign."
    voice "n14_ICant"
    mo "I can't say it's Hilda for sure, but he seems inexplicably respectful. A little out of character."
    #voice "n14_IdSay"
    if radio_static == "_s":
        voice "n14_IdSay_s"
    else:
        voice "n14_IdSay_c"
    co "I'd say it's a possibility, yeah."
    voice "n14_AndIt"
    mo "And it looks like there's a lot more people than when Elly was last here."
    #voice "n14_ABunch"
    if radio_static == "_s":
        voice "n14_ABunch_s"
    else:
        voice "n14_ABunch_c"
    co "A bunch of new faces, eh? Tell me more."

    #players only get one choice to pick
    menu:
        "Tell Colin about the people at Camp 1":
            voice "n14_TheresFiveOfUs"
            mo "There's five of us in C1...think you probably haven't heard of someone named Pearl. She's new, just like me."
            #voice "n14_OhShes"
            if radio_static == "_s":
                voice "n14_OhShes_s"
            else:
                voice "n14_OhShes_c"
            co "Oh, she's definitely new alright."
            voice "n14_ShesA"
            mo "She's a silly one, I doubt she's involved in anything messy."

        "Tell Colin about the people at Camp 2":
            voice "n14_TheresFiveInC2"
            mo "There's five in C2, though I haven't actually met them in person yet. Don't think I'll be able to anytime soon."
            #voice "n14_WeHave"
            if radio_static == "_s":
                voice "n14_WeHave_s"
            else:
                voice "n14_WeHave_c"
            co "We have one new guy, huh? In Elly's notes I've got a Wilbur, a Jax, a Cassie and a Ruran."
            voice "n14_ThatWould"
            mo "That would mean you're missing Davos, Wilbur's kid."

        #choice branch ends
        #phone ends
    play sound rustle1
    "*rustle rustle*"

    "Was that from outside?"

    menu:
        #choice branch starts
        "Tell Colin goodnight":

            voice "n14_AlrightDaddy"
            mo "Alright, daddy's tired. You better go get some sleep too, Pancake. Listen to mommy, okay?"
            voice "n14_Wha"
            if radio_static == "_s":
                voice "n14_Wha_s"
            else:
                voice "n14_Wha_c"
            co "Wha-"

            "I hung up on Colin."
            "Last thing I want is someone eavesdropping on me."
            "I paused to listen, but the sound doesn't seem to happen again."
            "I should text Colin real quick."
            "\"Sorry. I thought I heard someone outside.\""
            play sound ding
            "\"Oh yeah, better be safe than sorry. Updates for another time then.\""
            hide satphone
            "I guess it's time to hit the bed."

        "Check outside":
            hide satphone
            voice "n14_OneMoment"
            mo "One moment."
            stop ambience fadeout 1.0
            play ambience amb_campnight fadein 1.0
            play sound zipopen
            "I unzipped my tent just enough to peer outside."
            show black
            "Pitch black. Can't see shit."

            play sound rustle2
            "*rustle rustle*"

            voice "n14_WhosThere"
            mo "Who's there?!"
            show gr neutral with dissolve
            "Out from the shadows comes Gregory."
            "Crap."

            voice "n14_SorryKid"
            gr "Sorry kid, did I wake ya? Just taking a quick piss."
            voice "n14_NahYoure"
            mo "Nah, you're good. I'm gonna head back to bed."
            hide gr
            hide black
            with dissolve
            stop ambience fadeout 3.0
            play ambience amb_intcampnight fadein 3.0
            play sound zipclose
            "I zipped my tent up quickly."
            "Looks like Colin hung up on me."
            "\"I am okay. Gregory was outside.\""
            play sound ding
            "\"Aight, careful out there Morg.\""
            "I guess it's time to hit the bed."

            #choice branch ends
    stop ambience fadeout 1.0

label nov_15:
    #INT: Morgan's tent
    scene bg morganstent with longfade
    $ current_day = _("November 15th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    play ambience amb_intcampday fadein 1.0

    "Another day, another round of sore backs."
    "I don't think I'll ever get used to sleeping on packed snow."
    "But it looks like the storm didn't hit us last night."
    stop ambience fadeout 1.0

    scene bg camp1_day with dissolve
    play ambience amb_campday fadein 1.0
    #EXT: Camp 1

    "For once, I'm the first one up today."
    "Aston and Lorenzo are usually the earliest."
    "Followed by Gregory."
    "And then it's always a battle between Pearl and me."
    stop ambience fadeout 1.0
    show bg maintent_day
    play ambience amb_intcampday fadein 1.0
    #INT: Main tent

    "I guess I could go snoop around in the main tent for a bit."

    menu:
        "Check the food shelf":
            "Meat and potatoes. Love that."
            "Canned soup. 80\% of these are tomato flavored. I think I already know why."
            "Instant rice meals. Maybe I should request some today."
            "Instant noodles. I eat that way too much at home."
            "Different kinds of jerky. Would love those if they weren't so hard to chew."
            "Freeze-dried fruit and vegetables. Healthy."
            "I'd say this shelf is pretty well stocked."

        "Check the weapon and tool rack":
            "Knives, picks and axes."
            "Pistols and pistol ammo."
            "Flares and... Nothing much."
            "Jax said that they have rifles in C2."
            "Is this unfairness I smell?"

    #choice branch ends
    "I turn to the large table in the middle that we use for meals if we're not outside near the campfire."
    "Think Lorenzo uses it the most if not for meals. Lots of writing and calculations he needs to do for his job."
    stop ambience fadeout 5.0
    "And what do we have here?"
    "There are documents strewn across the table... {w=0.5}They weren't here last night."
    "Huh?"

    play music audio.anxious

    "These are... Everyone's profiles?"
    "Name: Pearl"
    "Age: 24"
    "Gender: Female"
    "Status: Uninfected"
    "Uninfected?"
    "That's an odd way to label someone."
    "Would Elly's copy be in here then?"

    menu:
        "Dig through the documents":
            $ dig_thru_docs= True
            "Name: REDACTED"
            "Age: REDACTED"
            "Gender: REDACTED"
            "Status: Infected"
            "Well, reading that makes me suuuper comfortable."
            "There are multiple people with similar profiles like these, and their pictures have been torn out too."
            "No sign of Elly. I really hope he's not one of them."
            "Better clean this up real quick."

        "Don't dig through them":
            "Someone left it out here, and that someone might find out I'm snooping."
            "It's best to think about it for a second."
    #choice branch ends

    "Whatever those records are, if people at camp have one, then I'll most likely get one too."
    "I'd much rather stay healthy, thanks."

    show ast neutral with sdissolve
    voice "n15_Morgan"
    ast "Morgan?"

    "Crap, that scared me."

    voice "n15_MorningAston"
    mo "Morning, Aston... {w=0.8}Was just thinking about what to eat for breakfast. Slept well?"

    voice "n15_YesWhat"
    ast "Yes. What were you looking at?"

    "Uh oh."

    voice "n15_WellIm"
    mo "Well, I'm not sure who left these here, and I was gonna just keep them away to make space for breakfast."
    show ast inthought
    voice "n15_IThink"
    ast "I think that might be Gregory's. Pearl's still asleep, Lorenzo was with me, and you found them here."

    "Gregory's... Huh. What's he doing with everyone's records?"
    show ast neutral
    voice "n15_IsSomething"
    ast "Is something wrong?"
    voice "n15_NothingI"
    mo "Nothing, I think I just woke up on the wrong side of the bed."

    "Aston takes a moment to read my expression."

    show gr neutral at left with dissolve
    voice "n15_OhUp"
    gr "Oh, up early are we?"

    "Gregory's voice booms from behind Aston."
    show ast confused
    voice "n15_GregoryDid"
    ast "Gregory, did you leave these here?"

    show gr angry
    "Gregory's hurried footsteps give off a slight uneasiness."
    show ast neutral
    voice "n15_WeWere"
    ast "We were just about to go look for you. Morgan and I were deciding what to eat for breakfast."
    show gr neutral
    "Almost instantaneously, Gregory's face softened from relief."
    "Aston covered for me. I shall remember that."
    "He didn't have to lie."

    voice "n15_AnythingYoud"
    mo "Anything you'd like in particular, Gregory?"
    show gr happy
    voice "n15_IllLeave"
    gr "I'll leave it up to you guys."

    # show gr with move:
    #     xpos -200

    hide gr with dissolve
    "He grabbed all the files quickly and went back to his tent."
    "Major alarms are blaring in my head."
    "Aston and I share glances for a moment, before he decides to go on about his daily routine."
    "He doesn't question me, nor does he bring it up again later in the day."
    stop music fadeout 3.0

    scene bg camp1_night with dissolve
    #EXT: Camp 1
    play ambience amb_campnightwfire fadein 1.0

    "The records have been occupying my mind since this morning."
    "At least there's meat and potatoes for tonight...for a temporary distraction."
    "Can't solve cases on an empty stomach."
    show lorenzo sad at centerleft
    voice "n15_MorganAre"
    lo "Morgan, are you feeling alright? You haven't been touching your food."
    voice "n15_TheFoods"
    mo "The food's great, Lorenzo. I just have a headache."
    show pearl smile at centerright
    voice "n15_AstonShould"
    pe "Aston should have some meds for that! I can go get them for-"
    show pearl neutral
    play sound wind1
    "A strong gust of wind begins to pick up, cutting Pearl's sentence short."
    "The campfire embers dance violently around the pit."
    stop ambience fadeout 3.0

    play sound wrr
    "WRRRRRRRRRRRRR!"
    show pearl scared
    show lorenzo scared
    "Oh, that's bad news."
    play sound radio
    "The radio turns on."
    voice "n15_HelloI"
    ev "Hello? I sure hope you guys can hear me."
    voice "n15_SnowstormsHappening"
    ev "Snowstorm's happening. If you're outside, get in - like, RIGHT now."

    "I didn't know Eva did weather reporting too."

    voice "n15_YouHeard"
    gr "You heard her! IN. NOW."
    play sound snowstorm loop


    "Oh, fuck."
    "They weren't kidding when they said snowstorms mean business in these parts."
    scene bg maintent_day with dissolve
    "Each one of us sat in a corner of the main tent... Holding it down with our body weight."
    show gr angry at centerleft
    voice "n15_EveryoneHold"
    gr "Everyone hold tight, lest we start flying!"

    "If anyone were to move, I feel like we would actually start flying upwards."
    "I'm glad we secured the tents yesterday. Getting hit like this without warning? Lethal for sure."
    "But I wonder how those ropes and weighted bags will fare in this storm."
    "It would be a problem if my tent flies... I can't let anyone read my journal."

    stop sound fadeout 3.0
    scene bg maintent_day with dissolve
    with Pause(1.5)

    "I don't know how much time has elapsed."
    "It's still snowing outside, but it would seem that the storm finally decided to calm down."
    show pearl sad at left
    voice "n15_IsEveryone"
    pe "Is everyone okay...? Are we okay?"
    show gr neutral at centerleft
    voice "n15_LooksLike"
    gr "Looks like it... Everyone is still in one piece, aye?"

    play ambience amb_intcampnight fadein 5.0

    "Lorenzo is already on his Walkie, checking in on Camp 2."
    show lorenzo pondering at centerright
    voice "n15_EveryoneOkay"
    lo "Everyone okay? We're safe here, I think!"
    voice "n15_WereAll"
    ru "We're all safe too! Cassie got a tiny cut from falling, but she's okay now."
    voice "n15_ThatWas"
    da "That was some wind, wasn't it? Hope none of your tents flew away."
    show ast inthought at right
    voice "n15_WeShould"
    ast "We should call the RC, too."
    voice "n15_IllDo"
    mo "I'll do just that."
    voice "n15_AlrightIm"
    ast "Alright, I'm going to check outside for a bit."
    hide ast
    hide pearl
    with dissolve
    "Pearl follows Aston outside."
    "I should beep Eva."

    #radio selection stuff
    menu:
        "Beep Eva": #TODO: Do we still want this button here, or go straight into the call?
            $ chibi_morgan = "images/chibi/morgan_worried.png"
            voice "n15_EvaIs"
            wt_mo "Eva! Is everyone at the RC okay?"
            $ chibi_eva = "images/chibi/eva_worried.png"
            if radio_static == "_s":
                voice "n15_TheThree_s"
            else:
                voice "n15_TheThree_c"
            wt_ev "The three of us are fine. We're the ones with a roof here... We should be asking if you're okay."
            $ chibi_morgan = "images/chibi/morgan_neutral.png"
            voice "n15_WereOkay"
            wt_mo "We're okay. And it sounds like Camp 2 is alright too!"
            $ chibi_koda = "images/chibi/koda_worried.png"
            if radio_static == "_s":
                voice "n15_ThankGoodness_s"
            else:
                voice "n15_ThankGoodness_c"
            wt_ko "Thank goodness... Update us if anything happens, okay?"

            voice "n15_NooooooooMy"
            pe "Noooooooo! My tent collapsed."

            "Pearl's voice could be heard coming from the outside."

            voice "n15_WellIf"
            wt_mo "Well... If you heard that, that's the update, I guess. Pearl's tent collapsed."
            $ chibi_koda = "images/chibi/koda_happy.png"
            if radio_static == "_s":
                voice "n15_OohNo_s"
            else:
                voice "n15_OohNo_c"
            wt_ko "O-Oh no, poor Pearl."
            if radio_static == "_s":
                voice "n15_YouDont_s"
            else:
                voice "n15_YouDont_c"
            wt_ev "You don't sound all that sorry for her, Koda."
            $ chibi_eva = "images/chibi/koda_neutral.png"
            if radio_static == "_s":
                voice "n15_IAm_s"
            else:
                voice "n15_IAm_c"
            wt_ko "I am, it's just... It's very Pearl of her."
            $ chibi_eva = "images/chibi/eva_worried.png"
            if radio_static == "_s":
                voice "n15_ItLooks_s"
            else:
                voice "n15_ItLooks_c"
            wt_ev "It looks like the storm actually did some damage."
            $ chibi_eva = "images/chibi/eva_neutral.png"
            if radio_static == "_s":
                voice "n15_AnywayIm_s"
            else:
                voice "n15_AnywayIm_c"
            wt_ev "Anyway, I'm sure you're busy Morgan... Help the girl out, will you?"
            nvl clear
            #radio selection stuff end

    scene black with dissolve

    "The night ended after we did a round of damage inspection."

    scene bg morganstent with dissolve
    "Looks like everything is okay in my tent."
    "Pearl's going to be sleeping in the main tent for the night."
    "Surviving a snowstorm, huh? {w=0.5}Well, that's one check off my extreme bucket list."
    "Now I have a reason to demand a snowmobile from Colin."
    stop ambience fadeout 3.0

label nov_16:
    #EXT: Camp 1
    scene bg camp1_day with longfade
    $ current_day = _("November 16th")
    $ save_name = current_date(_("Arc 1"), current_day)
    play ambience amb_campday fadein 1.0
    show screen date_label with dissolve

    "The next day after the storm, we got to work rebuilding the campsite."
    "Other than fixing Pearl's tent, we've got some shoveling to do, the snow piled up real high and we lost our campfire."
    show pearl sad at centerright
    voice "n16_StillCant"
    pe "Still can't believe it was my tent of all things. Now I need to redecorate again."
    show lorenzo smile at centerleft
    voice "n16_IllHelp"
    lo "I'll help you out, Pearl. Don't worry!"
    show pearl happy
    voice "n16_GrazieLorenzo"
    pe "Grazie, Lorenzo!"

    hide pearl
    hide lorenzo
    with dissolve

    play sound shovel
    "Dig, dig, digging...there is a lot of snow piled up. We'll be here all day."
    "Lorenzo said that everyone once had to deal with fallen trees. It was not a fun experience."
    "Snow is much easier to remove, so I appreciate the lack of trees."
    "Gregory went towards Camp 2 earlier, checking for tree issues. Maybe I should also do the same facing north?"

    show bg forest1 with fade
    "Well no fallen trees, but..."
    "Wait, is that an igloo? It's too perfectly shaped to be natural."

    voice "n16_GuysIm"
    mo "Guys... I'm going to be back real quick. I see something up ahead."

    "Definitely not natural, it even has a little entrance."
    stop ambience fadeout 3.0
    show cg meetingkyle
    $ persistent.gallery_meetingkyle = True
    play music audio.light

    voice "n16_Hello"
    ky "Hello!"

    "An unfamiliar face greets me as I approach the igloo-like structure."

    voice "n16_OhGeez"
    ky "Oh, geez, the snowstorm yesterday was rough, huh? My tent ended up flying away last night!"
    voice "n16_WaitYoure"
    mo "Wait. You're telling me you spent the night in... That?"

    "I gesture towards the igloo."
    hide cg meetingkyle
    show ky smile
    voice "n16_LooksPretty"
    ky "Looks pretty neat, huh? I made it myself! It's cold, but it does the trick."
    show ky sad
    voice "n16_IWouldnt"
    ky "I wouldn't want to do that for another night though."
    show ky smile
    voice "n16_SayDo"
    ky "Say, do you happen to have more tents?"
    voice "n16_ImNot"
    mo "I'm not sure, but I could go check?"
    show ky happy
    voice "n16_ThatWould"
    ky "That would be awesome sauce! Oh, wait, where are my manners? I'm Kyle, nice meeting you out here!"
    voice "n16_MorganNice"
    mo "Morgan. Nice meeting you, too. Why were you out here alone, anyway?"
    voice "n16_LongStory"
    ky "Long story short, I'm a wildlife photographer! I'm on a solo expedition to capture the animals around here."

    "He proudly raises the camera hanging around his shoulder."
    show ky smile
    voice "n16_SoLike"
    ky "So, like, 2 days ago, I was at the village up north. Met the locals, some farm kids, and then I also got bitten by a cow. Pictures turned out great though!"
    voice "n16_ACow"
    mo "A cow? Looks like you had an eventful day. The villagers were friendlier I hope?"
    show ky happy
    voice "n16_OhYes"
    ky "Oh, yes, super friendly - and they actually offered me to stay with them, but I thought it'd be counterintuitive to stay there with farm animals when I'm looking to find wild ones."
    voice "n16_TheyGave"
    ky "They gave me extra blankets as a parting gift! I'd be a goner without them last night."

    "Friendly, huh? Gregory said they didn't like outsiders. Maybe they just hate us in particular?"

    voice "n16_WellIts"
    mo "Well, it's a damn miracle that you're still talking. Wanna follow me back to camp? Can't leave you out here by yourself."
    voice "n16_AwwYeah"
    ky "Aww yeah, thank you! That'll be great!"

    scene bg camp1_day with dissolve
    with Pause(1.0)

    voice "n16_HeyaGuys"
    mo "Heya guys, I'm back with a new friend."
    show ky happy:
        xpos 650
        yalign 1.0
        #with dissolve

    voice "n16_HelloooImKyle"
    ky "Hellooo! I'm Kyle!"
    show gr neutral:
        xpos 1000
        yalign 1.0
        #with dissolve
    "A frown forms almost instantaneously on Gregory's face upon seeing the two of us."
    show pearl happy at left
    voice "n16_HellooooImPearl"
    pe "Helloooo! I'm Pearl! This is Aston, Lorenzo, and Gregory!"
    show ky with move:
        xpos 300
    show gr with move:
        xpos 650
    show lorenzo smile:
        xpos 1000
        yalign 1.0
        #with dissolve
    show ast neutral at right with dissolve

    "I have a feeling Pearl and Kyle will get along just fine."
    show gr confused
    show pearl smile
    with dissolve
    
    voice "n16_WhereDid" 
    gr "Where did you come from, son?"
    show ky smile
    voice "n16_OhJust"
    ky "Oh, just up ahead! I was camping in a tent before it flew away last night."
    show pearl happy
    voice "n16_YESIm"
    pe "YES! I'm not the only- uh I-I mean, {nw}"
    show pearl sad with None
    extend "that really sucks. Where did you end up sleeping?"
    voice "n16_YoureNot"
    mo "You're not gonna believe it."
    show ky happy
    voice "n16_AMan"
    ky "A man made igloo."
    show pearl smile
    show gr neutral
    show ast inthought
    with dissolve
    voice "n16_AllIgloos"
    ast "All igloos are man made."
    show ky smile
    voice "n16_OhDamn"
    ky "Oh damn, you're right. {w=0.7}I took some pictures! Wanna see?"
    show lorenzo sad
    voice "n16_SantoCielo"
    lo "Santo cielo, you survived the night in that?"
    show ky happy
    voice "n16_YeahI"
    ky "Yeah! I was at the village two days ago and they gave me blankets! Thanks to them, I survived the cold!"
    show ky sad
    voice "n16_ThenI"
    ky "Then I also got bitten by a cow named Susie. Which reminds me, do you guys also have extra bandages?"
    show ast confused
    voice "n16_LetMe"
    ast "Let me have a look at it."
    show lorenzo smile with dissolve
    show ast neutral with None
    voice "n16_AstonHere"
    lo "Aston here is our camp medic! He'll fix you right up."
    show gr angry
    voice "n16_SoHow"
    gr "So, how long do you plan on staying?"

    "Gregory asking the important questions here."

    voice "n16_IWas"
    ky "I was wondering if you had extra tents that I could borrow? I wouldn't want to just impose myself here."
    show lorenzo pondering
    voice "n16_IDont"
    lo "I don't think we'll have any extras until next month."
    show gr neutral
    voice "n16_IGuess"
    gr "I guess you'll have to leave, then."
    show ky shaken
    show lorenzo neutral
    voice "n16_OhBut"
    ky "Oh, but please sir Gregory, if I could just have a few days of your time? I really can't afford to leave the mountains when it took so much for me to get up here."
    voice "n16_IJust"
    ky "I just need some time to capture all the wildlife here."
    show pearl happy
    voice "n16_ICan"
    pe "I can give you my tent! Then I could sleep in our main tent."
    show ky happy
    voice "n16_ReallyThank"
    ky "Really? Thank you, Pearl!"
    show gr angry
    voice "n16_IDidnt"
    gr "I didn't even-"
    show ky smile
    show lorenzo smile
    voice "n16_ThankYou"
    ky "Thank you to the rest of you too! Once I get the photos I need, I'll leave the camp. I promise I won't interfere with your... vacation?"
    voice "n16_WereWorking"
    gr "We're working here. It ain't a vacation."
    show ky happy
    voice "n16_CoolCool"
    ky "Cool, cool! If you need anything at all, please do ask. I'd like to be helpful, especially since I'm gonna be crashing here for a while!"
    show ast inthought
    voice "n16_WeShould"
    ast "We should treat the cow bite first."
    show ky shaken
    voice "n16_AhYes"
    ky "Ah yes! Totally forgot about that."

    scene bg camp1_day with dissolve
    "Snow shoveling day turned out to be much more eventful than we expected."
    "But now I'm worried about dragging another civilian into a mess whose depth even I'm unsure of."
    "Sounds like I made a bad choice, but the only other option was to leave him to fend for himself."
    "...{w=1.0} I'm sure it'll be fine for now."
    stop music fadeout 3.0

label nov_17:
    #INT: Main tent
    scene bg maintent_day with longfade
    $ current_day = _("November 17th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    play ambience amb_intcampday fadein 1.0
    "It's been three days since we were stuck at camp."
    "Lorenzo and Gregory said that they'll be sending in new samples together. The batch we accumulated over the days was a little too much for one person to handle."
    "Meanwhile, Aston, Pearl, and I were tasked to reallocate food portions for an extra person and reset camp to its original form."
    "Which means rebuilding the campfire, fixing our crockpot stand, and restabilizing the main tent. Pearl heard creaking in one of the legs last night."
    "Kyle was a freebird. Without a map, it'll be hard for him to navigate around here."
    show ky smile at left
    show gr neutral at centerleft
    with dissolve
    voice "n17_HeyaDo"
    ky "Heya, do you need some help?"
    voice "n17_NoNot"
    gr "No, not really. Go bother someone else, will ya?"
    show ky sad
    voice "n17_ICould"
    ky "I could help you guys with heavy stuff? Delivering? Lifting?"
    show ast neutral at centerright
    show lorenzo smile at right
    with dissolve
    voice "n17_YouCould"
    ast "You could head to Camp 2 and grab us some food, an extra mouth to feed after all."
    show ky happy
    voice "n17_SureLeave"
    ky "Sure! Leave it to me!"
    show ast confused

    voice "n17_Camp2"
    ast "Camp 2 is pretty far by foot. Are you sure?"
    show gr confused
    voice "n17_TheSnowmobile"
    gr "The snowmobile can fit two people, so unless you'd like to be dragged like a ragdoll along with our other supplies, walking is the way."
    show ast neutral
    show lorenzo sad
    voice "n17_IMean"
    ky "I mean, sure! You guys know what's best."

    "The bewilderment on Gregory's face is loud."
    show gr happy
    voice "n17_WellGive"
    gr "We'll give you a lift, then. Come outside in 5."
    show lorenzo smile
    show ast happy
    with dissolve
    voice "n17_ThinkI"
    lo "Think I have everything I need. I'll see you later, amore. {w=0.9}Bye friends!"
    hide lorenzo with dissolve
    hide gr with dissolve
    show ast neutral with move:
        xalign 0.5
    "Lorenzo bids Aston and us farewell and follows Gregory outside."
    show ky shaken
    show pearl smile at right
    with dissolve
    voice "n17_IForgot"
    ky "I forgot to ask if they had helmets."
    voice "n17_ImSure"
    pe "I'm sure you'll be fine, Kyle."

    #INT: Main tent
    show black
    hide ky

    "We made lots of progress within two hours."
    "Tent? Fixed. Crockpot? Fixed."
    "Reorganized the shelves and storage? All done."
    "The camp has been restored to its former glory."
    hide black
    show pearl happy with dissolve

    voice "n17_GreatWork"
    pe "Great work, guys! We did amazing!"
    stop ambience fadeout 3.0
    play music audio.light

    #Cassie beeps you
    play sound beep
    "Beep!"
    "Oh, it looks like I've got a message."
    # $ chibi_walkie = "images/chibi/clearwalkie.png"
    $ chibi_kyle = "images/chibi/kyle_happy.png"
    if radio_static == "_s":
        voice "n17_WoahCassie_s"
    else:
        voice "n17_WoahCassie_c"
    wt_ky "Woah, Cassie, does this mean he \nreceived it?"
    voice "n17_LoudAnd"
    wt_mo "Loud and clear, Kyle."
    if radio_static == "_s":
        voice "n17_HahaHello_s"
    else:
        voice "n17_HahaHello_c"
    wt_ca "Haha! Hello, Morgan! I was just teaching him how the Walkie works. We happened to have a spare!"
    $ chibi_cassie = "images/chibi/cassie_neutral.png"
    if radio_static == "_s":
        voice "n17_AndIt_s"
    else:
        voice "n17_AndIt_c"
    wt_ca "And it looks like we have a different courier pigeon. I'll get Kyle to deliver your map tomorrow!"
    $ chibi_morgan = "images/chibi/morgan_happy.png"
    voice "n17_SweetThanks"
    wt_mo "Sweet! Thanks again, Cassie. Hope that new pigeon doesn't cause you too much trouble."
    if radio_static == "_s":
        voice "n17_OhIm_s"
    else:
        voice "n17_OhIm_c"
    wt_ca "Oh, I'm gonna put him to work. Don't you worry!"
    $ chibi_kyle = "images/chibi/kyle_neutral.png"
    if radio_static == "_s":
        voice "n17_IDont_s"
    else:
        voice "n17_IDont_c"
    wt_ky "I don't have a say in this, do I?"
    if radio_static == "_s":
        voice "n17_NopeeeeThats_s"
    else:
        voice "n17_NopeeeeThats_c"
    wt_ca "Nopeeee, that's what you get for making me do extra work. I have to draw a new map for you!"
    $ chibi_davos = "images/chibi/davos_worried.png"
    if radio_static == "_s":
        voice "n17_YouTwo_s"
    else:
        voice "n17_YouTwo_c"
    wt_da "You two should get a room, it's blinding!"
    voice "n17_SpillThe"
    wt_pe "Spill the tea Davos, what are we \nlooking at?"
    $ chibi_davos = "images/chibi/davos_happy.png"
    if radio_static == "_s":
        voice "n17_YouShouldve_s"
    else:
        voice "n17_YouShouldve_c"
    wt_da "You should've been here just now! \"H-H-Hi, my name is K-Kyle, I think you're c-cute.\""
    $ chibi_kyle = "images/chibi/kyle_worried.png"
    if radio_static == "_s":
        voice "n17_ThatIs_s"
    else:
        voice "n17_ThatIs_c"
    wt_ky "That is not what I said, Davos!"
    $ chibi_jax = "images/chibi/jax_happy.png"
    if radio_static == "_s":
        voice "n17_ItWas_s"
    else:
        voice "n17_ItWas_c"
    wt_ja "It was definitely close enough...\nRight, Cassie?"
    $ chibi_cassie = "images/chibi/cassie_worried.png"
    if radio_static == "_s":
        voice "n17_DDontDrag_s"
    else:
        voice "n17_DDontDrag_c"
    wt_ca "D-Don't drag me into this!"
    voice "n17_WellIt"
    wt_mo "Well, it sounds like you guys are \nhaving fun without us, alright."
    voice "n17_RememberTo"
    wt_ast "Remember to grab food supplies too, Kyle."
    if radio_static == "_s":
        voice "n17_AllPacked_s"
    else:
        voice "n17_AllPacked_c"
    wt_wi "All packed and ready, Aston. He won't starve on my watch!"
    $ chibi_ruran = "images/chibi/ruran_worried.png"
    if radio_static == "_s":
        voice "n17_OhAston_s"
    else:
        voice "n17_OhAston_c"
    wt_ru "Oh Aston, did you also need med supplies? Kyle has a bite on his arm, doesn't he?"
    voice "n17_YesHe"
    wt_ast "Yes, he got bitten by a cow. I think we have enough supplies, though."
    $ chibi_wilbur = "images/chibi/wilbur_happy.png"
    if radio_static == "_s":
        voice "n17_ACow_s"
    else:
        voice "n17_ACow_c"
    wt_wi "A cow? My, you're full of surprises - aren't you, lad?"

    nvl clear
    #beeps end

    "They're such a silly bunch."
    "We all ended up talking for hours and had to swap Walkies multiple times... The batteries kept running out."
    stop music fadeout 3.0

    #Lorenzo's POV
    scene black with longfade
    scene bg isaaklab1 with dissolve
    play ambience amb_rc fadein 1.0

    show lorenzo pondering at centerleft
    voice "n17_HngggghPhew"
    lo "Hnggggh... Phew...{w=0.8} I think that's the last box for Isaak? Koda's usually the one that collects boxes, but I think they're with Gregory and Eva now."
    show lorenzo sad
    voice "n17_IsaakAre"
    lo "Isaaaaak? {w=0.5}Are you there?"
    show lorenzo neutral
    voice "n17_HmmWhy"
    lo "Hmm... Why is the ice box open- {w=0.8}Oh."
    stop ambience fadeout 1.0
    play music audio.anxious fadein 1.0

    "An unidentifiable animal carcass could be found in the box, covered in ice."
    "Looks about the size of a wolf pup or a large bird."
    "There doesn't seem to be any smell."
    show lorenzo sick
    voice "n17_WWellI"
    lo "W-Well... I guess at least it doesn't stink...{w=0.8} Maybe I should close it up, still."

    "Lorenzo closes the lid of the ice box."
    play sound icebox
    show bg isaaklab2
    voice "n17_IllLet"
    lo "I'll let Koda know that his supplies are here, I guess."
    stop music fadeout 5.0
    scene black with fade
    "Unable to shake off the feeling of uneasiness, Lorenzo decides to leave the lab to go look for the others."

label nov_18:
    #EXT: Camp 1
    scene black
    scene  bg camp1_day with dissolve
    play ambience amb_campday fadein 1.0
    $ current_day = _("November 18th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    "The next day, Kyle returns home from Camp 2. Gregory had to pick him up because the ragdoll idea wasn't as great as he thought."

    show pearl happy at centerright
    show ky smile at centerleft
    with dissolve
    voice "n18_YoureFinally"
    pe "You're finally back! Thought you didn't want to leave Cassie."
    show ky happy
    voice "n18_IAm"
    ky "I am a man of my words, Pearl! Gotta send these supplies back here, and this, for you!"

    "Kyle hands me a newly drawn map."
    "Perfect. I should send Colin a shot of this later... This map is unlike the one that Elly had before."
    show lorenzo smile at left
    voice "n18_CassieI"
    lo "Cassie? {w=0.6}I feel like I'm missing some context here."
    show ky flustered with None
    voice "n18_ItsNothing"
    ky "It's nothing Lorenzo, don't listen to Pearl."
    
    scene bg camp1_day with dissolve
    "The day goes on with lots of fun and banter."

    stop ambience fadeout 5.0
    scene bg morganstent with longfade
    play music audio.neutral

    "Night time."
    "First things first, the map."

    play sound ding
    "And...{w=0.5}sent! Colin now has a copy of this."
    show satphone
    voice "n18_HiiiiPancake"
    mo "Hiiii Pancake, I just sent you a picture."
    #voice "n18_NiceOne"
    if radio_static == "_s":
        voice "n18_NiceOne_s"
    else:
        voice "n18_NiceOne_c"
    co "Nice one Morg. So, what have you been up to?"
    voice "n18_ISurvived"
    mo "I survived a snowstorm, my highlight of the week."
    #voice "n18_AreYou"
    if radio_static == "_s":
        voice "n18_AreYou_s"
    else:
        voice "n18_AreYou_c"
    co "Are you serious? Well, I'm glad you're still in one piece, soldier."
    voice "n18_SayDo"
    mo "Say... Do we get bonuses for surviving? I've been eyeing this cool snowmobile that the guys have."
    #voice "n18_WeDont"
    if radio_static == "_s":
        voice "n18_WeDont_s"
    else:
        voice "n18_WeDont_c"
    co "We don't even have snow back home, Morg."
    voice "n18_JustThought"
    mo "Just thought I'd put in a request. Anyway, I think you'd want to hear this."
    voice "n18_ProfilesOf"
    mo "Profiles of the people at camp... Sounds normal enough, yeah? But under all the necessary info, there's a part that lists whether the person is infected."
    #voice "n18_IBeg"
    if radio_static == "_s":
        voice "n18_IBeg_s"
    else:
        voice "n18_IBeg_c"
    co "I beg your pardon? Infected? Those are some glaring red flags if I've ever seen one."

    #IF MORGAN CHOSE TO DIG FURTHER ON DAY N15th he says this
    if dig_thru_docs:
        voice "n18_FlippingThrough"
        mo "Flipping through, I also found profiles with redacted info, with faces torn out. I didn't see any sign of Elly."
    #branch ends

    #voice "n18_DontSuppose"
    if radio_static == "_s":
        voice "n18_DontSuppose_s"
    else:
        voice "n18_DontSuppose_c"
    co "Don't suppose you know who owns 'em?"
    voice "n18_GregoryWouldve"
    mo "Gregory. Would've taken pictures but I was almost caught snooping around."
    #voice "n18_BetterLuck"
    if radio_static == "_s":
        voice "n18_BetterLuck_s"
    else:
        voice "n18_BetterLuck_c"
    co "Better luck next time! But Gregory, huh? Perhaps I should do some digging out here."
    voice "n18_YeahOh"
    mo "Yeah. Oh, we did get another new member, too."
    #voice "n18_NewRecruit"
    if radio_static == "_s":
        voice "n18_NewRecruit_s"
    else:
        voice "n18_NewRecruit_c"
    co "New recruit?"
    voice "n18_NahA"
    mo "Nah, a wildlife photographer! Guy survived the storm in a makeshift igloo."
    #voice "n18_HahHes"
    if radio_static == "_s":
        voice "n18_HahHes_s"
    else:
        voice "n18_HahHes_c"
    co "Hah! He's insane, I like him. If I had a snowmobile, I think he'd deserve it much more than you."
    voice "n18_IThought"
    mo "I thought I was your favorite."
    #voice "n18_ILove"
    if radio_static == "_s":
        voice "n18_ILove_s"
    else:
        voice "n18_ILove_c"
    co "I love everyone the same."
    voice "n18_SureIll"
    mo "Sure, I'll believe it if a snowmobile spawns in my apartment."
    #voice "n18_IllDo"
    if radio_static == "_s":
        voice "n18_IllDo_s"
    else:
        voice "n18_IllDo_c"
    co "I'll do you one better, how about I throw you a welcome back party once this is over?"
    voice "n18_ThatSucks"
    mo "That sucks."
    #voice "n18_ComeOn"
    if radio_static == "_s":
        voice "n18_ComeOn_s"
    else:
        voice "n18_ComeOn_c"
    co "Come on, can't you act a tiny bit grateful?"
    voice "n18_MyMother"
    mo "My mother didn't teach me to lie...but for you, Pancake? I'll tolerate the party."
    #voice "n18_ThatsVery"
    if radio_static == "_s":
        voice "n18_ThatsVery_s"
    else:
        voice "n18_ThatsVery_c"
    co "That's very kind of you."
    #voice "n18_AightGood"
    if radio_static == "_s":
        voice "n18_AightGood_s"
    else:
        voice "n18_AightGood_c"
    co "Aight, good talk. You sleep tight, Morg."
    voice "n18_NightyNight"
    mo "Nighty-night, Pancake."
    hide satphone
    "I fell asleep soon after."
    scene black with dissolve
    stop music fadeout 3.0

label nov_19_23:
    #19th
    scene bg camp1_day with longfade
    play music audio.light
    $ current_day = _("November 19th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve

    "It's my favorite time of the day, meal time."
    "Looks like there's already a crowd gathered in here."

    #INT: Main tent
    show bg maintent_day
    show lorenzo neutral at left
    show ast sad at centerleft
    show pearl confused at centerright
    with dissolve
    voice "n19_AmoreYou"
    lo "Amore, you need to eat more greens!"
    show ast inthought
    voice "n19_IDont"
    ast "I don't eat green vegetables."
    voice "n19_ButWhat"
    pe "But what about corn? Or carrots? Eggplants?"
    show ast neutral with None
    show lorenzo smile with dissolve
    voice "n19_NormallyId"
    ast "Normally I'd choose not to...but I know it's healthy, so I tolerate them."
    show pearl sad
    voice "n19_SoNo"
    pe "So, no to pea soup?"
    voice "n19_NoTo"
    ast "No to pea soup. They're green."

    "Lorenzo notices me walking in."
    show lorenzo happy
    voice "n19_MorganDo"
    lo "Morgan! Do you like vegetables?"
    voice "n19_ILove"
    mo "I love them roasted or stir fried, but not too much if they're boiled."
    show pearl smile
    show ast inthought
    voice "n19_SeeAston"
    pe "See Aston, you're the pickiest!"
    voice "n19_IveSurvived"
    ast "...I've survived this long without vegetables. I can live without it."
    show lorenzo smile
    voice "n19_ThereAre"
    lo "There are two kinds of people, survive to eat, and eat to survive. Amore, I think you're the latter."
    show ast neutral
    voice "n19_HeyIts"
    ast "Hey, it's not like I avoid everything green. I eat basil on pizza."
    voice "n19_WhatAre"
    mo "What are your favorite pizzas?"
    show ast inthought
    voice "n19_AMeatasaurus"
    ast "A meatasaurus. If it has mushrooms and onions it'll smell better, but I'd still prefer meat and nothing else."
    show pearl happy
    voice "n19_HmmmI"
    pe "Hmmm, I like pep and cheese, or... Oh! A margherita with extra tomato!"
    show lorenzo happy
    voice "n19_ILike"
    lo "I like pesto with seafood, paired with wine? Mmm! That would be my ideal dinner night."
    voice "n19_ImNot"
    mo "I'm not that picky but I do love me some extra onions, olives and anchovies. I love stinky stuff."
    voice "n19_WhatAreYourStances"
    pe "What are your stances on pineapple on pizza?"
    show ast neutral
    voice "n19_TolerableIts"
    ast "Tolerable. It's a nice touch."
    show lorenzo sad
    voice "n19_WithPesto"
    lo "With pesto and seafood, absolutely not! With other savory meats...then, yes, I can see the vision!"
    show pearl smile
    voice "n19_WhatAbout"
    pe "What about you, Morgan?"
    voice "n19_ThreeFor"
    mo "Three for three, I love pineapple on pizza. Especially if they're sweet."

    mo "Do you know any pizza places that do delivery here?"
    show lorenzo smile
    show pearl scared
    show ast happy
    with dissolve
    "*gurgle*"
    #SFX stomach
    "Someone's stomach lets out a deafening growl."

    voice "n19_IGuess"
    mo "I guess the answer is no."

    #20th
    #INT: Main tent
    scene bg maintent_day with longfade
    $ current_day = _("November 20th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    "It's my first time seeing someone else using the table other than Gregory or Lorenzo."
    show ky smile
    voice "n20_MorningKyle"
    mo "Morning, Kyle. What are you up to?"
    voice "n20_MorningIm"
    ky "Morning! I'm planning my routes on the map that Cassie gave me."
    voice "n20_SoAre"
    mo "So are you guys a thing yet?"
    show ky flustered
    voice "n20_WWhatI"
    ky "W-What? I mean, I haven't even taken her out to dinner yet...and I don't even know if she's available, you know?"

    "The fluster in his voice is evident...looks like the cat really got his tongue."
    show ky smile
    voice "n20_CassieIs"
    ky "Cassie is really cute, though! She seemed interested when I showed her my album. There's lots of pictures of my previous adventures."
    voice "n20_TheresAlso"
    ky "There's also Susie and all the other farm animals."

    "Kyle has his map laid out openly. It was then that I noticed something different."

    voice "n20_WaitWhy"
    mo "Wait... Why do you have extra drawings on your map?"
    show ky happy
    voice "n20_SheDrew"
    ky "She drew some animals for me! Waypoints for common sightings of animals."
    #TODO Make sure new line read's bounced out to fix vocal "deers" to "deer"
    voice "n20_SoTheres"
    ky "So, there's apparently wolves here, bears here if they are not already hibernating, birds of some kind that gather here, deer everywhere..."

    "Kyle explains everything with a large smile painted across his face."
    "He's such a golden retriever."

    #21st
    #EXT: Camp 1
    scene bg camp1_night with longfade
    $ current_day = _("November 21st")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    play ambience amb_campnightwfire fadein 1.0

    "Mealtime around the campfire!"
    show lorenzo smile at left
    show ast happy:
        xpos 300
        yalign 1.0
    "Lorenzo and Aston are sharing a plate of dried fruit as usual."
    show ky happy:
        xpos 650
        yalign 1.0
    show pearl happy:
        xpos 1000
        yalign 1.0
    "Kyle and Pearl are bantering about trivial things, the matching energy is undeniable."
    show gr neutral at right
    "Gregory sits alone with his eyebrows furrowed."
    "I'm guessing he really doesn't like having double the Pearls."
    hide lorenzo
    hide ast
    hide ky
    hide pearl
    show gr with move:
        xpos 1600

    voice "n21_YouGood"
    mo "You good, Gregory?"
    voice "n21_YesI"
    gr "Yes. I just wasn't expecting to babysit twice the amount of kids all of a sudden."
    voice "n21_GotAny"
    mo "Got any kids of your own, Gregory?"
    show gr worried
    "A flicker of sadness shows on his face."
    voice "n21_IHave"
    gr "I have a daughter, yes. She's about Pearl's age."
    voice "n21_SometimesI"
    gr "Sometimes I wish I didn't have this job."
    voice "n21_WhyWould"
    mo "Why would you think so?"
    show gr neutral
    voice "n21_WellYou"
    gr "Well, you know... More time for family. More time for her."
    voice "n21_ThankfullyIm"
    gr "Thankfully, I'm retiring soon. I hope that she doesn't hate her old man for being away for so long."
    "He recollects himself and continues."
    voice "n21_WhatAbout"
    gr "What about you, got any kids yourself?"
    voice "n21_IActually"
    mo "I actually have a 4 year old running around back at home."
    show gr happy with None
    voice "n21_A4"
    gr "A 4 year old? Hah, your wife must be having a real hard time taking care of the little bugger!"
    show gr happy
    voice "n21_ThatsThe"
    gr "That's the age when they tear your house down."

    scene black with dissolve
    "Colin's face flashes in my mind."
    "Yeah, my 4 year old child."
    stop ambience fadeout 3.0

    #22nd
    #INT: Main tent
    scene bg maintent_day with longfade
    $ current_day = _("November 22nd")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve

    play sound toolrack volume 0.5
    "*crash*"
    "Did I walk into something uninvited?"
    show pearl scared:
        xalign 0.5
        ypos 600
    voice "n22_ImOkay"
    pe "I'm okay!"
    "Pearl fell and accidentally knocked over the tool rack."
    "I rushed over to help her to her feet."
    show pearl smile with move:
        yalign 1.0
    voice "n22_LookingFor"
    mo "Looking for something?"
    voice "n22_YeahMy"
    pe "Yeah... My compass, I don't remember where I put it."

    #choice branch starts
    menu pearl_compass:
        "Ask her to check her pockets" if not pe_check_pockets:
            voice "n22_HaveYou"
            mo "Have you checked your pockets?"
            show pearl happy
            voice "n22_OhYeah"
            pe "Oh, yeah, good idea."
            show pearl confused
            "She thoroughly searches her pockets, but to no avail. Guess it's not there."
            $ pe_check_pockets = True
            jump pearl_compass

        "Check the food shelf" if not pe_check_shelf:
            "Maybe at the food shelf?"
            "I reached over to the tomato soup section."
            show pearl sad
            voice "n22_MorganI"
            pe "Morgan! I know everyone knows that I love tomato soup, but it's not there!"
            "Whoops."
            $ pe_check_shelf = True
            jump pearl_compass

        "Check the storage boxes":
            hide pearl with dissolve
            "Storage with all the important documents. A compass would be too clunky to fit in here."
            "Storage for extra ammo. I doubt she would be flipping through here anyway. We haven't had the need to use guns."
            "Storage with all the small tools... Oh!"
            "A compass with... {w=0.4}A tomato sticker behind it. Classic Pearl."

    #choice branch ends
    show pearl smile
    voice "n22_HereYou"
    mo "Here you go, Pearl. It was with all the screwdrivers and hammers."
    show pearl happy
    voice "n22_OoohThank"
    pe "Oooh! Thank you Morgan, you're the best!"

    "If we're out in the forest, it would be pretty dangerous to leave your compass back at camp."
    "I'll need to make sure I remind her every time, then."
    stop music fadeout 3.0

    #23rd
    scene bg camp1_day with longfade
    $ current_day = _("November 23rd")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    show ky happy at centerleft with dissolve
    voice "n23_AndThen"
    ky "-and then, splash! The otter family all jumped into the river together!"
    voice "n23_GoshI"
    ky "Gosh, I love their little paws."

    "Kyle and I were talking about his otter family encounters."
    "Of course, being the great photographer that he is, he's got a whole album designated for them."
    show ast neutral at centerright
    voice "n23_KyleIts"
    ast "Kyle? It's time."

    "Aston pokes his head out from inside the main tent."
    show ky smile
    voice "n23_OohYeah"
    ky "Ooh yeah, bandage time. Join us, Morgan."

    #INT: Main tent
    show bg maintent_day with sdissolve
    play music audio.neutral

    play sound bandage1
    "Aston skillfully unwraps Kyle's bandage and examines the wound."
    "He turns around and gives Kyle a packet of anti-inflammatory meds."
    show ast inthought
    voice "n23_TheWound"
    ast "The wound closed up long ago, but I'm not sure why it is still red here."
    show ky sad
    voice "n23_ItKinda"
    ky "It kinda hurts when I touch it."
    show ast neutral
    voice "n23_OhWell"
    ast "Oh, well...we'll just monitor the rash for a few more days. If it gets worse, I'm sending you to the hospital."

    "The rash is concerning, considering that the original bite wound was only a quarter of its size."

    voice "n23_CanCows"
    mo "Can cows carry rabies?"
    show ast inthought
    voice "n23_IThink"
    ast "I think so, but I'm pretty sure the farm animals here are all vaccinated against it."
    play sound bandage2
    "Aston swiftly wraps a new bandage around Kyle's forearm."
    show ast neutral
    voice "n23_GoodAs"
    ast "Good as new. Remember to take those meds."
    show ky happy
    voice "n23_SureThing"
    ky "Sure thing. Thanks, Aston!"
    stop music fadeout 5.0

label nov_24:
    #EXT: Camp 1
    scene bg camp1_day with longfade
    $ current_day = _("November 24th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    play music audio.light
    "Today is rest day at camp."
    "Or in Pearl's words, tonight is marshmallow night!"
    "Can't remember the last time I've had a marshmallow, let alone a toasted one."
    "We were just waiting for sundown and for Kyle to come back from his photography session."
    "He seemed pretty excited to put his new map to use this morning."
    "He should be back soon."
    "In the meantime, I should probably mingle around."
    "Who should I approach first?"

    menu nov24_approach:
        "Approach Pearl" if not approach_pe:
            $ approach_pe = True
            show pearl smile
            "Pearl seems to have a 3-way Walkie setup going on right now."
            voice "n24_ImWaiting"
            da "I'm waiting for my second growth spurt. You'll see, Pearl."
            voice "n24_ImGonna"
            da "I'm gonna be as tall as or taller than my pops! Within the next few years... I hope?"
            voice "n24_WeLove"
            pe "We love our short king."
            voice "n24_ImNot"
            ko "I'm not sure we can even beat genetics Davos. That's a high bar to reach."
            show pearl happy
            voice "n24_HighBar"
            pe "High bar to reach... Pfft."
            voice "n24_Hey"
            da "Hey!"
            voice "n24_SoDavos"
            mo "So Davos is short?"
            voice "n24_Hes5"
            ko "He's 5'3\", our beloved short king."
            show pearl smile
            voice "n24_AwwDont"
            da "Aww, don't join them, Morgan."
            voice "n24_YouWin"
            ko "You win some, you lose some Davos. But, hey...at least you have a great sense of direction."
            show pearl confused
            voice "n24_ExcuseMe"
            pe "Excuse me?"
            voice "n24_DidntSay"
            ko "Didn't say who, but I guess you outed yourself Pearl."
            voice "n24_ICan"
            mo "I can confirm that Pearl doesn't do well when we're out collecting."
            show pearl sad
            voice "n24_Morgaaaaaaaaaannnnnn"
            pe "Morgaaaaaaaaaannnnnn."
            voice "n24_RunMorgan"
            da "Run, Morgan, run!"
            nvl clear
            hide pearl

        "Approach Lorenzo" if not approach_lo:
            $ approach_lo = True
            "Lorenzo has his eyes closed, resting against the chair."
            "His face scrunches up every so often."
            "Is he having a nightmare? He looks like he's in pain."
            "I should call Aston over when I see him."
            "For now, I'll cover him up better with the blanket that he has."
    #choice branch ends

    if not approach_pe or not approach_lo:
        jump nov24_approach

    else:
        "I guess it's time to look for the other two in the main tent."

    #INT: Main tent
    scene bg maintent_day with dissolve
    show ast neutral
    "In the main tent, Aston is seen preparing the sticks and marshmallows."
    voice "n24_AstonI"
    mo "Aston, I think Lorenzo is having a nightmare. What do you th-"
    show ast scared
    voice "n24_What"
    ast "What?"
    hide ast
    "Aston doesn't wait for me to finish. He drops everything he's doing onto the table and runs out."
    "With the main tent empty, I've just noticed Gregory isn't anywhere to be found."
    "Would he be in his personal tent now?"

    #EXT Camp 1
    show bg camp1_day
    show ky smile
    "As I was exiting the tent, I bumped into Kyle."
    "He's back early."
    voice "n24_HeyMorgan"
    ky "Hey Morgan! You wouldn't believe what I just saw!"
    show ky happy
    voice "n24_ISaw"
    ky "I saw a wolf! It was a silly one...kept bumping into trees."
    "I suppose I'll have to leave snooping in Gregory's tent for another time."
    "Marshmallow night is about to start soon."


    scene bg camp1_night with longfade
    play ambience amb_campnightwfire fadein 1.0

    "*crackle crackle*"
    "The fire chirps loudly in the midst of the silent snowy plain."
    "Marshmallow in hand, everyone sits in a circle, patiently toasting their marshmallow."
    show lorenzo smile at left
    show ast happy at centerleft
    "Lorenzo is awake, leaning against Aston. He looks like he's feeling a bit better."
    hide lorenzo
    hide ast
    show pearl smile
    "Pearl still has the Walkie setup on and the rest of the folks could be heard through them."
    hide pearl
    show ky flustered at centerright
    "Kyle is... On the Walkie with Cassie? Nice one, I'm rooting for you two."
    hide ky
    show gr happy at right
    "Gregory too seems to be enjoying his time, savoring the toasted goodies."
    hide gr
    "At this moment, it's serene and peaceful."
    "Everyone is having a good time."
    "Despite not knowing them for long...{w=0.8} Their personalities have left an imprint on me."
    "For a while, I let myself bask in the feeling of having new companions."
    "The feelings, however, were short-lived. My intuition had other plans."
    "Like a premonition, I was just waiting for something bad to happen."
    "I don't like this unshakeable feeling of anxiousness."
    "I remind myself of my mission: Elliot still needs me."
    "The smell of something burnt tickles my nose and pauses my train of thought."
    "Whoops. Looks like I burnt mine."
    "I chucked the burnt marshmallow away and replaced it with a new one. Paying more attention to it this time."
    "Right now, with the knowledge I have, I'm inclined to believe that Gregory isn't innocent."
    "There has to be something. Something... or someone else in the picture that I'm not seeing."
    "What is it? Who is it?"
    "I need to gather more info for Colin."
    stop ambience fadeout 5.0
    stop music fadeout 5.0

label nov_25:
    #EXT: Forest
    scene bg waterbody with longfade
    $ current_day = _("November 25th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    play ambience amb_campday fadein 1.0
    "Marshmallow night was a success, I had a great night's sleep."
    "New day, new samples."
    "New samples, from the same old lake."
    "It wasn't my imagination, the lake really is green."
    "Is there something in the water that makes it look green?"

    show pearl confused with dissolve
    voice "n25_IsIt"
    pe "Is it just me, or does the soil feel different?"
    "Pearl calls me over."
    voice "n25_SureIts"
    mo "Sure it's not the melting snow you're feeling?"
    voice "n25_NoLike"
    pe "No, like, I've dug downwards three times, I don't remember the soil being hydrated."
    "Looks like there's a new observation to be made."
    show pearl neutral
    "If the soil is wet, water flow must be present."
    "The ice shouldn't really start melting this early. At least that's what it says in '{i}The Camp Guide's Guide{/i}'."
    show gr neutral at right
    voice "n25_YouFound"
    gr "You found anything?"
    voice "n25_WetterSoilApparently"
    mo "Wetter soil, apparently."
    voice "n25_WetterSoilThat"
    gr "Wetter soil? That can't be right."

    "Gregory removes his glove to feel the moisture."
    voice "n25_YepThats"
    gr "Yep, that's something new to report. Scrap the extra dirt collecting for now and let's head back. We have what we need for today."
    "He looks at me, who's evidently confused, and continues."
    voice "n25_IsaaksOrders"
    gr "Isaak's orders. He needs wet soil more than anything else."
    voice "n25_ToldMe"
    gr "Told me to bring it to him immediately if we found any."
    voice "n25_ItCant"
    mo "It can't be from the lake can it?"
    show gr confused
    voice "n25_WeHave"
    gr "We have to dig pretty deep down before we hit water, remember?"

    "It makes sense...but at the same time, it doesn't make sense to me."
    "I think I need to ask someone with qualifications on this topic."
    "Maybe Eva?"
    stop ambience fadeout 3.0
    scene bg camp1_day with dissolve
    play music audio.neutral

    "We quickly returned to the campsite and Gregory hastily drove his snowmobile to the RC."
    "I guess it will be an early day for Pearl and me."
    "Time to return to my tent."
    scene bg camp1_day with dissolve
    show lorenzo sick
    "I encountered Lorenzo on the way."
    show lorenzo with sdissolve:
        ypos 1100
        xpos 900
    "Suddenly Lorenzo stumbles, almost losing his balance."
    show lorenzo with move:
        xalign 0.5
        yalign 1.0
    "I grabbed onto his shoulders to hold him steady."

    voice "n25_YouAlright"
    mo "You alright?"
    voice "n25_ImIm"
    lo "I'm... I'm alright, amico. Thank you."
    hide lorenzo with dissolve
    "He rushes back into his tent."
    "I'm worried. This is the second time I've seen him acting all weird."
    scene black with fade

    #INT: Morgan's tent
    show bg morganstent with dissolve
    "Alright, better beep Eva."
    menu:
        "Beep Eva":
            if radio_static == "_s":
                voice "n25_WhatsUp_s"
            else:
                voice "n25_WhatsUp_c"
            wt_ev "What's up?"
            $ chibi_morgan = "images/chibi/morgan_neutral.png"
            voice "n25_IHave"
            wt_mo "I have questions, if you're up for it right now. It's about the samples."
            if radio_static == "_s":
                voice "n25_Shoot_s"
            else:
                voice "n25_Shoot_c"
            wt_ev "Shoot."
            voice "n25_GregoryIs"
            wt_mo "Gregory is on his way to deliver wet soil to Isaak, it sounded urgent."
            $ chibi_morgan = "images/chibi/morgan_worried.png"
            voice "n25_WeFound"
            wt_mo "We found it near the lake. Does that mean anything serious?"
            $ chibi_eva = "images/chibi/eva_worried.png"
            if radio_static == "_s":
                voice "n25_WetSoil_s"
            else:
                voice "n25_WetSoil_c"
            wt_ev "Wet soil around the frozen lake? If it's not the snow melting on top of it..."
            if radio_static == "_s":
                voice "n25_ThenThat_s"
            else:
                voice "n25_ThenThat_c"
            wt_ev "Then that would mean the lake is eroding."
            if radio_static == "_s":
                voice "n25_AndIf_s"
            else:
                voice "n25_AndIf_c"
            wt_ev "And if it erodes, that would mean bad news for us."
            if radio_static == "_s":
                voice "n25_WorstCase_s"
            else:
                voice "n25_WorstCase_c"
            wt_ev "Worst case scenario is it dries up or it becomes a threat for geological hazards."
            $ chibi_eva = "images/chibi/eva_neutral.png"
            if radio_static == "_s":
                voice "n25_ItsUnfortunate_s"
            else:
                voice "n25_ItsUnfortunate_c"
            wt_ev "It's unfortunate, but it is a natural occurrence."
            $ chibi_eva = "images/chibi/eva_worried.png"
            if radio_static == "_s":
                voice "n25_AsFor_s"
            else:
                voice "n25_AsFor_c"
            wt_ev "As for why Isaak needs it urgently... I have no clue. He has never brought that up to us."
            $ chibi_eva = "images/chibi/eva_neutral.png"
            if radio_static == "_s":
                voice "n25_PerhapsI_s"
            else:
                voice "n25_PerhapsI_c"
            wt_ev "Perhaps I should grab some from him and have a look at it myself."
            $ chibi_morgan = "images/chibi/morgan_neutral.png"
            voice "n25_WellThanks"
            wt_mo "Well thanks for that Eva, that's good info."
            $ chibi_eva = "images/chibi/eva_happy.png"
            if radio_static == "_s":
                voice "n25_YoureWelcome_s"
            else:
                voice "n25_YoureWelcome_c"
            wt_ev "You're welcome."
            nvl clear
    #beep end

    "Lake erosion, huh?"
    "That does sound bad."
    "But worrying about it won't do anything right now."
    stop music fadeout 3.0

label nov_26:
    #INT: Main tent
    scene bg maintent_day with longfade
    $ current_day = _("November 26th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    play ambience amb_intcampday fadein 1.0
    "Kyle, Lorenzo and I were having a discussion about animals."
    show ky smile at centerleft
    voice "n26_FavoriteAnimal"
    ky "Favorite animal I've photographed? Definitely toucans!"
    show ky happy
    voice "n26_IMean"
    ky "I mean, just look at them. Silly banana beaked birds."
    show lorenzo smile at centerright
    voice "n26_ThenWhat"
    lo "Then...what animal would you like to photograph that you haven't had the opportunity to before?"
    show ky smile
    voice "n26_OhThats"
    ky "Oh, that's such a cool question! I'd love to capture a picture of a Loch Ness monster or a kraken one day."
    voice "n26_AreThey"
    mo "Are they even real?"
    show ky happy
    voice "n26_IDont"
    ky "I don't really know, which makes it the fun part!"
    voice "n26_MaybeThat"
    ky "Maybe that should be my next adventure, and maybe after my arm has healed."
    voice "n26_TheBite"
    mo "The bite from Susie hasn't healed yet?"
    show lorenzo sad
    show ky neutral
    with dissolve
    voice "n26_ItsNot"
    ky "It's not like I haven't been bitten before, but this is the first time that it has gotten this bad."
    voice "n26_ItsAbout"
    ky "It's about time for Aston to help me with a new bandage, anyway. Here, let me show you."
    stop ambience fadeout 3.0
    play music audio.neutral
    play sound bandage1
    "Kyle unwrapped his bandage to show a nasty rash. It hurts just looking at it."
    show cg rash
    $ persistent.gallery_rash = True
    voice "n26_ThatLooks"
    lo "That... Looks bad, Kyle."

    "I caught Lorenzo pulling on his sleeve."
    hide cg
    show ky sad
    voice "n26_IKnow"
    ky "I know, and honestly, I've been feeling a lot groggier recently. Is it the weather or just me?"
    voice "n26_IDontThink"
    mo "I don't think it's a matter of the weather."
    voice "n26_WhatAbout"
    mo "What about you, Lorenzo? Are you feeling alright?"
    voice "n26_ImWorried"
    mo "I'm worried, you nearly collapsed yesterday."
    voice "n26_ImNot"
    lo "I'm not exactly sick, but... I've been having weird dreams recently."
    voice "n26_DoYou"
    mo "Do you want to talk about it?"

    "Lorenzo hesitates for a second."
    show lorenzo neutral with dissolve
    voice "n26_LetMe"
    lo "Let me draw them real quick."

    play sound scribble
    "Lorenzo begins to scribble on his notebook."
    show cg lorenzosdrawing
    "A bear-shaped thing?"

    voice "n26_SeeThis"
    lo "See this... This bear thing, it has been following me night after night."
    show lorenzo sad
    voice "n26_ImSorry"
    lo "I'm sorry if it sounds silly, I just..."
    hide cg

    show ky neutral
    voice "n26_ItsNotSillyLorenzo"
    ky "It's not silly Lorenzo, fears are valid!"
    show ky shaken
    voice "n26_PlusId"
    ky "Plus, I'd be scared shitless if a normal bear was in front of me, let alone this one."
    show ky neutral
    voice "n26_DoesIt"
    mo "Does it act like a normal bear?"
    show lorenzo scared
    voice "n26_OhThatsTheThing"
    lo "Oh, that's the thing! It doesn't. It's always standing on its hind legs."
    voice "n26_ICant"
    lo "I can't read its expression but it doesn't feel like a friendly presence."
    show lorenzo sick
    voice "n26_ImNotEvenSure"
    lo "I'm not even sure if it has fur or some kind of... {w=0.5}Substance? I can't put it into words."
    show lorenzo sad
    voice "n26_ItsBecoming"
    lo "It's becoming a nightly event."
    show ky sad
    voice "n26_ThatSounds"
    ky "That sounds rough, Lorenzo..."


    "Kyle's rash is worrying. Lorenzo's dreams are worrying."
    "That's two things that happened within a week."
    voice "n26_IveWoken"
    lo "I've woken Aston up way too many times during the night. I feel horrible for disrupting his sleep."
    voice "n26_IDoubt"
    mo "I doubt he'd be worrying about his sleep when you're in distress, my friend."
    show ky smile
    voice "n26_YeahHes"
    ky "Yeah, he's doing exactly what a good partner should be doing!"

    "A smile dawned on his face."
    show lorenzo smile
    voice "n26_ImLucky"
    lo "I'm lucky to have him."

    "We pat his back."
    show ky happy
    voice "n26_LetUs"
    ky "Let us know if there's anything we can do to help!"
    voice "n26_ThankYou"
    lo "Thank you, my friends."
    stop music fadeout 3.0
    scene black with longfade

label nov_27:
    #INT: Morgan's tent
    play ambience amb_intcampnight fadein 1.0
    scene bg morganstent with dissolve
    $ current_day = _("November 27th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    "It's time for a check in with my beloved Pancake."
# TODO PHONE
    show satphone
    voice "n27_WhosThe"
    mo "Who's the sweetest Pancake in the world?"
    #voice "n27_HeyMorg"
    if radio_static == "_s":
        voice "n27_HeyMorg_s"
    else:
        voice "n27_HeyMorg_c"
    co "Hey, Morg...I know it's just a nickname, but don't get too used to it, you hear?"
    #voice "n27_IDont"
    if radio_static == "_s":
        voice "n27_IDont_s"
    else:
        voice "n27_IDont_c"
    co "I don't wanna feel like I have to call you my pappy!"
    voice "n27_AwCome"
    mo "Aw, come on, humor me. Who's the sweetest Pancake in the world?"
    #voice "n27_MeeeeeOkay"
    if radio_static == "_s":
        voice "n27_MeeeeeOkay_s"
    else:
        voice "n27_MeeeeeOkay_c"
    co "Meeeee. Okay, done. What's the update?"
    voice "n27_TwoUpdates"
    mo "Two updates. Regarding the well-being of my campmates."

    menu nov27_about:
        "Talk about Lorenzo" if not about_lo:
            $ about_lo = True
            voice "n27_LorenzoHas"
            mo "Lorenzo has been having night terrors, the same recurring nightmare about a bear-like monster."
            #voice "n27_ThatDoesnt"
            if radio_static == "_s":
                voice "n27_ThatDoesnt_s"
            else:
                voice "n27_ThatDoesnt_c"
            co "That doesn't sound fun."
            voice "n27_MyGut"
            mo "My gut tells me that he's not telling me the full picture, but he looks awfully distressed, so I doubt he's lying about the bear."

        "Talk about Kyle" if not about_ky:
            $ about_ky = True
            voice "n27_KyleHas"
            mo "Kyle has a rash on his arm. It's been about two weeks since he got bitten."
            #voice "n27_RashesYou"
            if radio_static == "_s":
                voice "n27_RashesYou_s"
            else:
                voice "n27_RashesYou_c"
            co "Rashes, you say? Describe it to me."
            voice "n27_BiteSite"
            mo "Bite site looks infected. The surrounding areas are red, peeling slightly. Kyle said it hurts to touch but it's also itchy."

    if not about_lo or not about_ky:
        jump nov27_about
        #choice branch ends
    else:
        voice "n27_DidElly"
        mo "Did Elly ever say anything about these symptoms?"
        #voice "n27_NadaMorg"
        if radio_static == "_s":
            voice "n27_NadaMorg_s"
        else:
            voice "n27_NadaMorg_c"
        co "Nada Morg, first I'm hearing of it."
        #voice "n27_ThoughElly"
        if radio_static == "_s":
            voice "n27_ThoughElly_s"
        else:
            voice "n27_ThoughElly_c"
        co "Though, Elly did sound sick when we last talked..."
        #voice "n27_HeNever"
        if radio_static == "_s":
            voice "n27_HeNever_s"
        else:
            voice "n27_HeNever_c"
        co "He never mentioned anything about an animal bite, nor having nightmares."
        #voice "n27_WhichNow"
        if radio_static == "_s":
            voice "n27_WhichNow_s"
        else:
            voice "n27_WhichNow_c"
        co "Which now begs the question: where do you get it from?"
        voice "n27_ThereMust"
        mo "There must be another source, then."

        #SFX snowfoot2
        "Suddenly, I hear footsteps from the outside."

        voice "n27_MorganYou"
        gr "Morgan? You there?"

        "He has the worst possible timing."

        voice "n27_ILove"
        mo "I love you Pancake, but Papa's gotta get back to work. I'll call you back okay? "
        hide satphone
        "I hung up on Colin."
        
        play sound zipopen
        scene camp1night with dissolve
        show gr happy
        voice "n27_YouCall"
        gr "You call your kid Pancake? That's sweet."
        show gr neutral
        voice "n27_SorryFor"
        gr "Sorry for interrupting family time, but I've got a favor to ask of ya."
        voice "n27_Yeah"
        mo "Yeah?"
        show gr worried
        voice "n27_WellIm"
        gr "Well, I'm just worried about Lorenzo. You think he's down with a cold or something?"

    #choice branch starts, one choice only
    menu:
        "Lie":
            voice "n27_SickNah"
            mo "Sick? Nah, I don't think so. Maybe he just lacks some sleep."

        "Tell the truth":
            $ greg_sus += 1
            voice "n27_WellMaybe"
            mo "Well... Maybe, yes. Lorenzo told me that he has been having nightmares, but that's about it."
    #choice branch ends

    show gr neutral
    voice "n27_HmmmOh"
    gr "Hmmm... Oh, well. Just keep an eye out, will ya?"
    voice "n27_LetMe"
    gr "Let me know if you notice anything different about him. Thanks, Morg."
    hide gr with dissolve
    voice "n27_YesSir"
    mo "Yes sir."
    play sound zipclose
    scene black with dissolve
    "Now that was a peculiar request. I didn't like the sound of that."
    "Anyhow, I should look out for Lorenzo."
    "I sincerely hope that his nightmares subsides soon."
    stop ambience fadeout 3.0
    scene black with longfade
    jump nov_28

label nov_30:
    #INT: Main tent
    scene bg maintent_day with dissolve
    $ current_day = _("November 30th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    play ambience amb_intcampday fadein 1.0
    "The past few days have just been the usual routine."
    "Wake up. Eat. Collect samples. Repeat."
    "Today was no different, but as we were about to hunker down for the night, the radio buzzed."
    play sound radio
    #radio goes brrr connects to camp 1 and 2
    stop ambience fadeout 3.0
    play music audio.neutral
    if radio_static == "_s":
        voice "n30_HelloCampers_s"
    else:
        voice "n30_HelloCampers_c"
    wt_ev "Hello campers, is now a good time?"
    $ chibi_jax = "images/chibi/jax_neutral.png"
    if radio_static == "_s":
        voice "n30_AnotherWeather_s"
    else:
        voice "n30_AnotherWeather_c"
    wt_ja "Another weather report, Eva? Camp 2's all here."
    # TODO If all are hidden, no stutter. Otherwise, stutters on entrance and exit. Stutter OK?
    show pearl smile at left
    show gr neutral:
        xpos 300
        yalign 1.0
    show ky smile:
        xpos 600
        yalign 1.0
    show lorenzo smile at right
    show ast neutral:
        xpos 1000
        yalign 1.0
    
    voice "n30_WereAll"
    wt_pe "We're all here, too!"
    hide ky
    hide gr
    hide pearl
    hide lorenzo
    hide ast
    with dissolve
    if radio_static == "_s":
        voice "n30_AlrightGood_s"
    else:
        voice "n30_AlrightGood_c"
    wt_ev "Alright, good...but it's not about the weather, though."
    $ chibi_eva = "images/chibi/eva_neutral.png"
    if radio_static == "_s":
        voice "n30_IHave_s"
    else:
        voice "n30_IHave_c"
    wt_ev "I have bad news and bad news."
    if radio_static == "_s":
        voice "n30_TheOther_s"
    else:
        voice "n30_TheOther_c"
    wt_ev "The other day, Camp 1 found abnormal amounts of moist dirt."
    if radio_static == "_s":
        voice "n30_WeHave_s"
    else:
        voice "n30_WeHave_c"
    wt_ev "We have confirmed that the lake bed is probably giving way. The contents of the water do match up."
    $ chibi_eva = "images/chibi/eva_worried.png"
    if radio_static == "_s":
        voice "n30_WhichUltimately_s"
    else:
        voice "n30_WhichUltimately_c"
    wt_ev "Which ultimately means that the lake might dry up over time."
    $ chibi_davos = "images/chibi/davos_worried.png"
    if radio_static == "_s":
        voice "n30_SoThe_s"
    else:
        voice "n30_SoThe_c"
    wt_da "So the first bad news is that the lake is just gonna go poof on us?"
    if radio_static == "_s":
        voice "n30_BasicallyYes_s"
    else:
        voice "n30_BasicallyYes_c"
    wt_ev "Basically yes, Davos. We doubt it will happen anytime soon though."
    $ chibi_morgan = "images/chibi/morgan_worried.png"
    voice "n30_WhatsThe"
    wt_mo "What's the other bad news?"
    if radio_static == "_s":
        voice "n30_TheLakes_s"
    else:
        voice "n30_TheLakes_c"
    wt_is "The lake's water has an unknown strand of fungi-like contaminants."
    if radio_static == "_s":
        voice "n30_ButIt_s"
    else:
        voice "n30_ButIt_c"
    wt_is "But it may just be what Heralign Inc. needs."
    $ chibi_koda = "images/chibi/koda_happy.png"
    if radio_static == "_s":
        voice "n30_TheBest_s"
    else:
        voice "n30_TheBest_c"
    wt_ko "The best case scenario is that we'll find a new source to gather something like penicillin."
    if radio_static == "_s":
        voice "n30_FungiAnd_s"
    else:
        voice "n30_FungiAnd_c"
    wt_ko "Fungi and the like are important ingredients for antibiotic medication!"
    if radio_static == "_s":
        voice "n30_ImSure_s"
    else:
        voice "n30_ImSure_c"
    wt_is "I'm sure you all know survival rules, but I'll just say this."
    if radio_static == "_s":
        voice "n30_DoNot_s"
    else:
        voice "n30_DoNot_c"
    wt_is "Do not, under any circumstances, drink the lake water."
    if radio_static == "_s":
        voice "n30_UnlessYoud_s"
    else:
        voice "n30_UnlessYoud_c"
    wt_is "Unless you'd like to find out why...in which case, be my guest."
    $ chibi_koda = "images/chibi/koda_worried.png"
    if radio_static == "_s":
        voice "n30_LLetsStay_s"
    else:
        voice "n30_LLetsStay_c"
    wt_ko "L-Let's stay with the boiled fresh snow and bottled water to be safe."
    $ chibi_jax = "images/chibi/jax_worried.png"
    if radio_static == "_s":
        voice "n30_SoTheWatersDeemed_s"
    else:
        voice "n30_SoTheWatersDeemed_c"
    wt_ja "So the water's deemed undrinkable, then."
    $ chibi_jax = "images/chibi/jax_neutral.png"
    if radio_static == "_s":
        voice "n30_AnyIdea_s"
    else:
        voice "n30_AnyIdea_c"
    wt_ja "Any idea how it would affect the wildlife here once the lake fully melts?"
    $ chibi_jax = "images/chibi/jax_worried.png"
    if radio_static == "_s":
        voice "n30_IdHate_s"
    else:
        voice "n30_IdHate_c"
    wt_ja "I'd hate it if something were to happen to them."
    $ chibi_koda = "images/chibi/koda_neutral.png"
    if radio_static == "_s":
        voice "n30_ThatsDefinitely_s"
    else:
        voice "n30_ThatsDefinitely_c"
    wt_ko "That's definitely something to look out for now while we figure out what we have on our end."
    if radio_static == "_s":
        voice "n30_GregoryWilbur_s"
    else:
        voice "n30_GregoryWilbur_c"
    wt_is "Gregory, Wilbur and the rest. You have a new extra task - observe the behaviour of the wildlife."
    if radio_static == "_s":
        voice "n30_GetPictures_s"
    else:
        voice "n30_GetPictures_c"
    wt_is "Get pictures if possible."
    stop music fadeout 3.0
    "Gregory looks at Kyle, and Kyle points to his camera expectantly."
    show gr neutral with dissolve
    voice "n30_KyleHas"
    gr "Kyle has a camera we can use."
    $ chibi_wilbur = "images/chibi/wilbur_happy.png"
    if radio_static == "_s":
        voice "n30_HahIt_s"
    else:
        voice "n30_HahIt_c"
    wt_wi "Hah! It looks like that camera will be useful after all, lad!"
    if radio_static == "_s":
        voice "n30_GregoryWont_s"
    else:
        voice "n30_GregoryWont_c"
    wt_wi "Gregory won't have a reason to kick you out anymore!"
    play music audio.light
    show ky happy
    show pearl happy
    with dissolve
    "Pearl and Kyle fist pump the air together."
    show ky happy # Trying to essentially put in a pseudo-pause before more Walkie stuff through undetectable sprite dissolve; unclear if it'll work with nvl
    $ chibi_davos = "images/chibi/davos_happy.png"
    if radio_static == "_s":
        voice "n30_GoodFor_s"
    else:
        voice "n30_GoodFor_c"
    wt_da "Good for you Cassie!"
    $ chibi_jax = "images/chibi/jax_happy.png"
    if radio_static == "_s":
        voice "n30_CongratsCassie_s"
    else:
        voice "n30_CongratsCassie_c"
    wt_ja "Congrats, Cassie!"
    $ chibi_eva = "images/chibi/eva_happy.png"
    if radio_static == "_s":
        voice "n30_NotSure_s"
    else:
        voice "n30_NotSure_c"
    wt_ev "Not sure why we're cheering for Cassie, but... Yay Cassie!"
    $ chibi_cassie = "images/chibi/cassie_worried.png"
    if radio_static == "_s":
        voice "n30_IICant_s"
    else:
        voice "n30_IICant_c"
    wt_ca "I-I can't with you all."
    show lorenzo happy with dissolve
    voice "n30_KyleSeems"
    lo "Kyle seems pretty happy about that."
    voice "n30_ShouldveSeen"
    pe "Should've seen him in person, he was cheering!"
    show ast happy
    voice "n30_WerentYou"
    ast "Weren't you also fist pumping the air?"
    voice "n30_WellYeah"
    pe "Well, yeah! I'm excited for him, too!"
    $ chibi_morgan = "images/chibi/morgan_happy.png"
    voice "n30_CassieDid"
    wt_mo "Cassie, did you catch that? Kyle's going to stay for longer."
    $ chibi_ruran = "images/chibi/ruran_happy.png"
    if radio_static == "_s":
        voice "n30_ShesHiding_s"
    else:
        voice "n30_ShesHiding_c"
    wt_ru "She's hiding behind me."
    if radio_static == "_s":
        voice "n30_LooksLike_s"
    else:
        voice "n30_LooksLike_c"
    wt_ru "Looks like the message has been well received."
    $ chibi_cassie = "images/chibi/cassie_worried.png"
    if radio_static == "_s":
        voice "n30_NotYou_s"
    else:
        voice "n30_NotYou_c"
    wt_ca "Not you too, Ruran."
    $ chibi_davos = "images/chibi/davos_neutral.png"
    if radio_static == "_s":
        voice "n30_AwwCassie_s"
    else:
        voice "n30_AwwCassie_c"
    wt_da "Aww, Cassie, don't hide."
    voice "n30_IllDo"
    ky "I'll do my best, guys! {w=1.2}I'm glad that my skills will be of some value now!"
    nvl clear
    "Well, if I do indirectly end up contributing to modern medicine study, that's a win in my book."
    "I wonder if the weather had something to do with the fungi appearing."
    stop music fadeout 3.0
    scene black with longfade
    jump dec_1

label dec_2:
    #INT: Main tent
    scene bg maintent_day with longfade
    $ current_day = _("December 2nd")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    play ambience amb_intcampday fadein 3.0
    #Aston and Lorenzo's POV

    "While the rest were out for the day, Aston and Lorenzo were alone in the main tent."
    show lorenzo sick at centerright with dissolve
    show ast sad at centerleft with dissolve
    "It seems like the bear hasn't stopped its torment on Lorenzo."
    "Waking up in a cold sweat countless times, he developed a fever overnight."

    voice "d2_YourTemperature"
    ast "Your temperature... When did it start? Last night?"
    show lorenzo scared
    voice "d2_HowBad"
    lo "How bad is it?"

    "Aston removes the thermometer from Lorenzo's mouth."

    voice "d2_38Degrees"
    ast "38 degrees, that's a fever."
    voice "d2_DoYouWantMe"
    ast "Do you want me to take you to the hospital?"
    show lorenzo sad
    voice "d2_IDontKnowIf"
    lo "I don't know if that's feasible right now."
    voice "d2_WedNeed"
    lo "We'd need to tell Gregory."
    show ast angry
    voice "d2_NoIm"
    ast "No. I'm not willing to take that risk."
    voice "d2_StillWorried"
    lo "Still worried about what happened to Elliot?"
    voice "d2_TheIssue"
    ast "The issue is that we don't know what happened."
    show ast inthought
    voice "d2_OneDay"
    ast "One day he's at camp, the next day he goes missing."
    voice "d2_CallMe"
    ast "Call me paranoid, but I don't want to find out. Not when Gregory is here."
    show lorenzo sick
    voice "d2_ThatMakes"
    lo "That makes two of us, then."
    stop ambience fadeout 3.0

    show lorenzo sad behind ast
    "Lorenzo fumbles with his sleeve, finding it increasingly difficult to resist the urge to scratch the itch on his arm."
    "His actions draw Aston's attention, who now prompts him for an answer."
    show ast sad
    voice "d2_WhatsWrong"
    ast "What's wrong?"

    play music audio.light
    play sound sleeve
    "Lorenzo rolls up his left sleeve."
    "A rash. Less severe than Kyle's...but the similarities are undeniable."

    show ast with move:
        xpos 650
    show lorenzo with move:
        xpos 800
    "Aston cups Lorenzo's face with one hand and then pulls him into an embrace."

    show lorenzo sad
    show ast sad behind lorenzo
    with dissolve
    voice "d2_IDontKnowWhat"
    lo "I don't know what this means, and truthfully... I am afraid of it."
    show lorenzo sick
    voice "d2_SeeingKyles"
    lo "Seeing Kyle's arm... I wish it was just a coincidence, but it's starting to look the part."

    show ast inthought
    "Aston ponders for a moment."

    show ast inthought #basically cheating a pause via dissolve
    voice "d2_IfIt"
    ast "If it spreads on contact, then it wouldn't make sense."
    voice "d2_ImThe"
    ast "I'm the one changing his bandages every day."
    show ast sad
    voice "d2_AnyIdea"
    ast "Any idea where you could've gotten this?"
    show lorenzo sad
    voice "d2_ImNot"
    lo "I'm not too sure myself."

    show ast with move:
        xpos 500

    "Aston gently releases Lorenzo from the hug, and begins cleaning the affected area."
    voice "d2_PromiseMe"
    ast "Promise me you'll keep this between us for now?"
    voice "d2_AtLeast"
    ast "At least...{w=0.8}not until we figure out what's really happening."
    show lorenzo neutral
    voice "d2_YouHave"
    lo "You have my word, amore."

    "Holding Lorenzo's hands in his, Aston takes a deep breath."
    show ast neutral with dissolve
    with Pause(0.3)
    show ast happy with dissolve
    voice "d2_YoureGoing"
    ast "You're going to be okay, love."
    show lorenzo smile
    voice "d2_WellFigure"
    ast "We'll figure something out."
    stop music fadeout 3.0

label dec_3:
    #INT: Main tent
    scene bg maintent_day with longfade
    $ current_day = _("December 3rd")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    play ambience amb_intcampday fadein 1.0
    show ast neutral
    "Today I was tasked with lunch duties, helping Aston out in the main tent."
    "A certain someone really wanted tomato soup, so I'm on 'can opening' duty."
    play sound radio
    "Suddenly, Aston's Walkie goes off on the table."
    voice "d3_MorganCould"
    ast "Morgan, could you help me with that?"
    voice "d3_SureThing"
    mo "Sure thing, bud."
    $ chibi_wilbur = "images/chibi/wilbur_happy.png"
    if radio_static == "_s":
        voice "d3_AstonMy_s"
    else:
        voice "d3_AstonMy_c"
    wt_wi "Aston, my boy, are you there?"
    $ chibi_morgan = "images/chibi/morgan_neutral.png"
    voice "d3_HisHands"
    wt_mo "His hands are full but he's listening, Wilbur."
    $ chibi_wilbur = "images/chibi/wilbur_neutral.png"
    if radio_static == "_s":
        voice "d3_OkayWonderful_s"
    else:
        voice "d3_OkayWonderful_c"
    wt_wi "Okay, wonderful! We just want to check in on Kyle."
    voice "d3_Yes"
    wt_ast "Yes?"
    $ chibi_ruran = "images/chibi/ruran_worried.png"
    if radio_static == "_s":
        voice "d3_HasKyle_s"
    else:
        voice "d3_HasKyle_c"
    wt_ru "Has Kyle had trouble sleeping recently?"
    show ast inthought
    voice "d3_IDont"
    wt_ast "I don't think so."
    if radio_static == "_s":
        voice "d3_YouWanna_s"
    else:
        voice "d3_YouWanna_c"
    wt_wi "You wanna tell him yourself, lass?"
    $ chibi_cassie = "images/chibi/cassie_neutral.png"
    if radio_static == "_s":
        voice "d3_ItsLike_s"
    else:
        voice "d3_ItsLike_c"
    wt_ca "It's like narcolepsy, but the other way around."
    $ chibi_cassie = "images/chibi/cassie_worried.png"
    if radio_static == "_s":
        voice "d3_BummerI_s"
    else:
        voice "d3_BummerI_c"
    wt_ca "Bummer... I don't remember what the word was..."
    $ chibi_ruran = "images/chibi/ruran_neutral.png"
    if radio_static == "_s":
        voice "d3_ItsInsomnia_s"
    else:
        voice "d3_ItsInsomnia_c"
    wt_ru "It's insomnia, and you've been having that for..."
    $ chibi_ruran = "images/chibi/ruran_worried.png"
    if radio_static == "_s":
        voice "d3_HasIt_s"
    else:
        voice "d3_HasIt_c"
    wt_ru "Has it been a week yet?"
    $ chibi_cassie = "images/chibi/cassie_neutral.png"
    if radio_static == "_s":
        voice "d3_ALittle_s"
    else:
        voice "d3_ALittle_c"
    wt_ca "A little over a week."
    if radio_static == "_s":
        voice "d3_IWish_s"
    else:
        voice "d3_IWish_c"
    wt_ca "I wish this was a problem I could sleep off."
    if radio_static == "_s":
        voice "d3_ButYes_s"
    else:
        voice "d3_ButYes_c"
    wt_wi "But yes, my boy, we were checking in just to see if everything is in order."
    $ chibi_wilbur = "images/chibi/wilbur_happy.png"
    if radio_static == "_s":
        voice "d3_GladTo_s"
    else:
        voice "d3_GladTo_c"
    wt_wi "Glad to hear that Kyle is okay!"
    $ chibi_ruran = "images/chibi/ruran_worried.png"
    if radio_static == "_s":
        voice "d3_AnotherThing_s"
    else:
        voice "d3_AnotherThing_c"
    wt_ru "Another thing, Aston... Have you noticed anyone else with these rashes?"
    if radio_static == "_s":
        voice "d3_IfMore_s"
    else:
        voice "d3_IfMore_c"
    wt_ru "If more of these pop up, we would have to start sending people to a hospital."
    $ chibi_ruran = "images/chibi/ruran_neutral.png"
    if radio_static == "_s":
        voice "d3_ItMay_s"
    else:
        voice "d3_ItMay_c"
    wt_ru "It may be something that we're not equipped to handle out here."
    show ast neutral
    "Aston freezes up."
    "That's... Quite unlike him."
    show ast inthought with dissolve
    $ chibi_morgan = "images/chibi/morgan_worried.png"
    voice "d3_NotThat"
    wt_mo "Not that we've noticed here. You worried that it's contagious?"
    if radio_static == "_s":
        voice "d3_AlwaysA_s"
    else:
        voice "d3_AlwaysA_c"
    wt_ru "Always a possibility. It would be better to cover all our bases."
    $ chibi_morgan = "images/chibi/morgan_neutral.png"
    voice "d3_WellWell"
    wt_mo "Well, we'll let you know if anything new happens, Ruran."
    $ chibi_ruran = "images/chibi/ruran_happy.png"
    if radio_static == "_s":
        voice "d3_ThatWould_s"
    else:
        voice "d3_ThatWould_c"
    wt_ru "That would be ideal. Thank you, Morgan."
    $ chibi_morgan = "images/chibi/morgan_happy.png"
    voice "d3_AndTake"
    wt_mo "And take care, Cassie!"
    $ chibi_cassie = "images/chibi/cassie_happy.png"
    if radio_static == "_s":
        voice "d3_IShall_s"
    else:
        voice "d3_IShall_c"
    wt_ca "I shall."
    nvl clear
    #radio end

    "First Kyle's arm, then Lorenzo's nightmares...and now Cassie's insomnia?"
    show ast sad
    voice "d3_MorganI"
    ast "Morgan, I-"
    voice "d3_ItsOkay"
    mo "It's okay, Aston. I know."
    voice "d3_AndI"
    mo "And I trust that you have your reasons."
    voice "d3_AstonVNVR"
    ast "..."
    show ast happy
    voice "d3_Thanks"
    ast "Thanks."
    hide ast
    "That was the most heartfelt \"thanks\" I've heard from him."
    "I figure Aston has his own reasons, too, but I won't pry for now."
    "It's not hard to imagine Aston covering for Lorenzo, though."
    "I've caught him scratching his arm through his sleeve more times than I can count in the past few days."
    "If it's contagious then... This could get ugly really fast."
    stop ambience fadeout 3.0

    #EXT: Camp 1
    show bg camp1_day with dissolve
    play ambience amb_campday fadein 1.0
    play sound cloth
    with Pause(1.0)
    show ky neutral
    #SFX bump
    "I bump directly into Kyle, who happened to be right outside the tent."
    voice "d3_IsEavesdropping"
    mo "Is eavesdropping your new hobby?"
    show ky confused
    voice "d3_NNoI"
    ky "N-No, I didn't mean to."
    voice "d3_ImJust"
    mo "I'm just kidding. You must be worried about her."
    show ky sad
    voice "d3_ThatObvious"
    ky "That obvious, huh?"
    "Kyle's too easy to read. {w=0.6}It's not hard to guess how he's feeling."
    "He looks down at his forearm worriedly."
    voice "d3_HeyDont"
    mo "Hey, don't you start blaming yourself. We don't even know what's happening to Cassie yet."
    voice "d3_WhatIf"
    ky "What if it was me?"
    voice "d3_ThenI"
    mo "Then I would've gotten it too, but I've been sleeping like a baby every night."
    show ky neutral
    "The tension in his shoulders visibly relaxes."
    voice "d3_WannaHelp"
    mo "Wanna help me out with lunch?"
    show ky smile
    voice "d3_YeahId"
    ky "Yeah! I'd love to, Morgan."
    stop ambience fadeout 3.0

label dec_4:
    scene bg camp1_night with longfade
    $ current_day = _("December 4th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    play music audio.light

    "Night falls in camp."
    "With the info I've gathered over the past few days, I think it's time for another update."
    scene black with fade
    "After being interrupted by Gregory multiple times, I waited for the signal before dialing up Colin."
    "And...{w=0.6}great, it looks like Gregory's snoring."
    "Time to call my 4 year old."

    #INT: Morgan's tent
    show bg morganstent with dissolve

    #TODO PHONE
    "Alrighty, Pancake time."
    show satphone
    #voice "d4_GreatTiming"
    if radio_static == "_s":
        voice "d4_GreatTiming_s"
    else:
        voice "d4_GreatTiming_c"
    co "Great timing, Morg."
    voice "d4_HeyPanc"
    mo "Hey Panc-"
    #voice "d4_AhAh"
    if radio_static == "_s":
        voice "d4_AhAh_s"
    else:
        voice "d4_AhAh_c"
    co "Ah ah! We don't have to do this every time."
    voice "d4_ButWe"
    mo "But we have to."
    #voice "d4_SaysWho"
    if radio_static == "_s":
        voice "d4_SaysWho_s"
    else:
        voice "d4_SaysWho_c"
    co "Says who?"
    voice "d4_YoursTruly"
    mo "Yours truly."
    voice "d4_JokesAside"
    mo "Jokes aside, you sound like you got some info for me."
    #voice "d4_YeahI"
    if radio_static == "_s":
        voice "d4_YeahI_s"
    else:
        voice "d4_YeahI_c"
    co "Yeah, I did find something interesting. It's about Gregory."
    #voice "d4_DidGreg"
    if radio_static == "_s":
        voice "d4_DidGreg_s"
    else:
        voice "d4_DidGreg_c"
    co "Did Greg ever tell you that he has a daughter?"
    voice "d4_VaguelyWhy"
    mo "Vaguely, why?"
    #voice "d4_ShesBedridden"
    if radio_static == "_s":
        voice "d4_ShesBedridden_s"
    else:
        voice "d4_ShesBedridden_c"
    co "She's bedridden, in the hospital, and she's in desperate need of a new liver."
    voice "d4_ThatWas"
    mo "That...was definitely not the news I was expecting to hear tonight."
    voice "d4_ExplainsWhy"
    mo "Explains why he wants to retire so soon."
    #voice "d4_HeTold"
    if radio_static == "_s":
        voice "d4_HeTold_s"
    else:
        voice "d4_HeTold_c"
    co "He told you that?"
    voice "d4_YepIn"
    mo "Yep, in a few months or so."
    voice "d4_SaidThat"
    mo "Said that he'd...finally be able to spend time with her."

    "The both of us fall silent upon this newfound revelation."
    "A heart wrenching one in fact."

    #voice "d4_StillThat"
    if radio_static == "_s":
        voice "d4_StillThat_s"
    else:
        voice "d4_StillThat_c"
    co "Still, that doesn't mean he's off the suspect list."
    voice "d4_YoureRight"
    mo "You're right."
    voice "d4_AnywayMy"
    mo "Anyway...my turn now, Pancake. I've got two for you today."
    #voice "d4_HellYeah"
    if radio_static == "_s":
        voice "d4_HellYeah_s"
    else:
        voice "d4_HellYeah_c"
    co "Hell yeah, what's up?"
    voice "d4_WeMight"
    mo "We might have a third case of the sickness."
    #voice "d4_SoIts"
    if radio_static == "_s":
        voice "d4_SoIts_s"
    else:
        voice "d4_SoIts_c"
    co "So it's rashes, nightmares, and what now?"
    voice "d4_Insomnia"
    mo "Insomnia."
    voice "d4_CassieDoesnt"
    mo "Cassie doesn't seem to have any other physical ailments."
    #voice "d4_WhatDo"
    if radio_static == "_s":
        voice "d4_WhatDo_s"
    else:
        voice "d4_WhatDo_c"
    co "What do the other camp medics say?"
    voice "d4_TheyDont"
    mo "They don't know if it's contagious."
    voice "d4_ButWhat"
    mo "But what I do know is that Aston is hiding something."
    #voice "d4_IsThat"
    if radio_static == "_s":
        voice "d4_IsThat_s"
    else:
        voice "d4_IsThat_c"
    co "Is that so?"
    voice "d4_MyBest"
    mo "My best guess is that he's covering for Lorenzo. He might also have a rash."
    voice "d4_SeenHim"
    mo "Seen him scratching his forearm through his coat way too many times now."
    voice "d4_AsFor"
    mo "As for why he's hiding it... It feels like there's more to this under the surface."
    #voice "d4_MightBe"
    if radio_static == "_s":
        voice "d4_MightBe_s"
    else:
        voice "d4_MightBe_c"
    co "Might be worth prying that out of him or Lorenzo himself."
    #voice "d4_SoWhats"
    if radio_static == "_s":
        voice "d4_SoWhats_s"
    else:
        voice "d4_SoWhats_c"
    co "So, what's the second one?"
    voice "d4_OtherThan"
    mo "Other than the fact that the lake's eroding... Apparently, they found a new fungi-like microorganism present in the water."
    voice "d4_TheBest"
    mo "The best case scenario is that we find a new source of antibiotic medication."
    #voice "d4_SoundsLike"
    if radio_static == "_s":
        voice "d4_SoundsLike_s"
    else:
        voice "d4_SoundsLike_c"
    co "Sounds like Heralign's gonna strike a pot of gold with that."
    #voice "d4_ButThe"
    if radio_static == "_s":
        voice "d4_ButThe_s"
    else:
        voice "d4_ButThe_c"
    co "But the worst case scenario I'm hearing is that it does the opposite?"
    voice "d4_YeahAnd"
    mo "Yeah...and as of now, we can't drink that until they find out what the fungi does."
    #voice "d4_YallGot"
    if radio_static == "_s":
        voice "d4_YallGot_s"
    else:
        voice "d4_YallGot_c"
    co "Y'all got enough supplies up there?"
    voice "d4_IdSay"
    mo "I'd say plenty. Lorenzo's got that covered for us, at least."
    #voice "d4_AightThats"
    if radio_static == "_s":
        voice "d4_AightThats_s"
    else:
        voice "d4_AightThats_c"
    co "Aight, that's good. And good work, Morg, you've been working hard!"
    voice "d4_OfCourse"
    mo "Of course, Pancake. I'm the best."
    #voice "d4_ThinkI"
    if radio_static == "_s":
        voice "d4_ThinkI_s"
    else:
        voice "d4_ThinkI_c"
    co "Think I should stop inflating your ego."

    hide satphone
    "I hung up on Colin."
    "Fungi, rashes... I hate the image that my mind's painting right now."
    "Putting two and two together, it does sound plausible that they're related."
    "I trust that the guys at the RC will find out soon enough."
    scene black with longfade
    stop music fadeout 3.0

label dec_5:
    #INT: Main tent
    scene bg maintent_day with dissolve
    $ current_day = _("December 5th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    play music audio.neutral fadein 3.0
    show ky sad at left
    show lorenzo sick at centerleft
    show pearl sad at right
    show ast neutral at centerright
    with dissolve
    show ky with move:
        xalign -0.5
    hide ky with dissolve
    show lorenzo with move:
        xalign -0.4
    hide lorenzo with sdissolve

    "The next morning, I walk into the main tent just in time to see Aston and Pearl shoo-ing Lorenzo and Kyle back into their tents."
    "Lorenzo looks a lot worse for wear."
    "And Kyle looks like he's sleepier today."

    voice "d5_AreThose"
    mo "Are those two alright?"
    show ast inthought
    voice "d5_ALittle"
    ast "A little worse than yesterday. I'll check in on them in a bit."
    voice "d5_ImWorried"
    pe "I'm worried for them."

    play sound beep
    "Oop, looks like the radio is on again."
    show gr neutral at left
    "And Gregory walks in right on time."
    
    if radio_static == "_s":
        voice "d5_HelloHello_s"
    else:
        voice "d5_HelloHello_c"
    wt_ko "Hello hello! Is everyone here?"
    $ chibi_jax = "images/chibi/jax_happy.png"
    if radio_static == "_s":
        voice "d5_HeyKoda_s"
    else:
        voice "d5_HeyKoda_c"
    wt_ja "Hey Koda, C2's here."
    show pearl smile
    show ast neutral
    voice "d5_KodaCamp"
    wt_pe "Koda! Camp 1's here!"
    voice "d5_AndHello"
    wt_pe "And hello, Jax! Looks like you beat Davos to the radio again."
    if radio_static == "_s":
        voice "d5_DavosJust_s"
    else:
        voice "d5_DavosJust_c"
    wt_ja "Davos just needs to try harder next time."
    $ chibi_davos = "images/chibi/davos_worried.png"
    if radio_static == "_s":
        voice "d5_YouKnow_s"
    else:
        voice "d5_YouKnow_c"
    wt_da "You know I can't reach the radio if you raise it up high like that! That's cheating."
    $ chibi_jax = "images/chibi/jax_neutral.png"
    if radio_static == "_s":
        voice "d5_TheyDont_s"
    else:
        voice "d5_TheyDont_c"
    wt_ja "They don't need to know that."
    $ chibi_koda = "images/chibi/koda_happy.png"
    if radio_static == "_s":
        voice "d5_HahaWonderful_s"
    else:
        voice "d5_HahaWonderful_c"
    wt_ko "Haha! Wonderful that everyone's here. I come bearing a new mission, friends!"
    if radio_static == "_s":
        voice "d5_IsaakAnd_s"
    else:
        voice "d5_IsaakAnd_c"
    wt_ko "Isaak and Eva decided it's time to move camp!"
    $ chibi_koda = "images/chibi/koda_neutral.png"
    if radio_static == "_s":
        voice "d5_SoRemember_s"
    else:
        voice "d5_SoRemember_c"
    wt_ko "So, remember when we said stuff about animals and lake dirt stuff?"
    if radio_static == "_s":
        voice "d5_TheyWant_s"
    else:
        voice "d5_TheyWant_c"
    wt_ko "They want dirt samples from the east side mountain, just so we can be sure that it's definitely coming from the lake."
    $ chibi_koda = "images/chibi/koda_happy.png"
    if radio_static == "_s":
        voice "d5_AndTo_s"
    else:
        voice "d5_AndTo_c"
    wt_ko "And to kill two birds with one stone, moving to higher ground means that you have more vantage over the forest on ground level."
    if radio_static == "_s":
        voice "d5_PerfectFor_s"
    else:
        voice "d5_PerfectFor_c"
    wt_ko "Perfect for scouting animals."
    voice "d5_SoUh"
    wt_gr "So, uh... Are we joining camps again, kid?"
    if radio_static == "_s":
        voice "d5_OnlyIf_s"
    else:
        voice "d5_OnlyIf_c"
    wt_is "Only if you want to."
    if radio_static == "_s":
        voice "d5_ItIs_s"
    else:
        voice "d5_ItIs_c"
    wt_is "It is imperative that you grab samples on the mountains."
    if radio_static == "_s":
        voice "d5_WhicheverIs_s"
    else:
        voice "d5_WhicheverIs_c"
    wt_is "Whichever is efficient, I guess?"

    "I'm secretly hoping that our camps can merge so that I can meet the rest."
    "But on the other hand, calling Colin may prove more difficult with more ears around."
    "I'm not the one making decisions here, so... No point thinking about it until it happens."

    if radio_static == "_s":
        voice "d5_JoiningCamps_s"
    else:
        voice "d5_JoiningCamps_c"
    wt_ja "Joining camps would be really fun."
    if radio_static == "_s":
        voice "d5_WhatSay_s"
    else:
        voice "d5_WhatSay_c"
    wt_ja "What say you, Wilbur and Gregory?"
    show pearl happy
    voice "d5_IHave"
    wt_gr "I have no objections. It is the most efficient way."
    $ chibi_wilbur = "images/chibi/wilbur_happy.png"
    if radio_static == "_s":
        voice "d5_ThatSettles_s"
    else:
        voice "d5_ThatSettles_c"
    wt_wi "That settles it, then!"
    if radio_static == "_s":
        voice "d5_AndIt_s"
    else:
        voice "d5_AndIt_c"
    wt_wi "And it looks like we'll finally see Morgan in the flesh!"
    voice "d5_OhMy"
    wt_pe "Oh my goodness, that means everyone will meet Morgan for the first time!"
    $ chibi_morgan = "images/chibi/morgan_happy.png"
    voice "d5_AboutTime"
    wt_mo "About time for that big reveal, huh?"
    voice "d5_AndHere"
    wt_mo "And here I thought I could stay mysterious forever."
    $ chibi_wilbur = "images/chibi/wilbur_neutral.png"
    if radio_static == "_s":
        voice "d5_ThatIs_s"
    else:
        voice "d5_ThatIs_c"
    wt_wi "That is perhaps the most exciting news, yes!"
    $ chibi_wilbur = "images/chibi/wilbur_happy.png"
    if radio_static == "_s":
        voice "d5_TheMore_s"
    else:
        voice "d5_TheMore_c"
    wt_wi "The more friends to camp with, the merrier!"
    $ chibi_davos = "images/chibi/davos_happy.png"
    if radio_static == "_s":
        voice "d5_WeCan_s"
    else:
        voice "d5_WeCan_c"
    wt_da "We can do campfire story nights again...can't wait!"
    $ chibi_koda = "images/chibi/koda_happy.png"
    if radio_static == "_s":
        voice "d5_IdLove_s"
    else:
        voice "d5_IdLove_c"
    wt_ko "I'd love to join too, Davos."
    if radio_static == "_s":
        voice "d5_HeheWe_s"
    else:
        voice "d5_HeheWe_c"
    wt_da "Hehe, we can bet on how many marshmallows Pearl will burn."
    show ast happy
    show pearl confused
    voice "d5_ICan"
    wt_pe "I can just eat the marshmallows you toast! Problem solved."

    "Alright, so that's plan A...merging of camps."
    "Lots of new faces and hopefully lots of info."

    if radio_static == "_s":
        voice "d5_IllGo_s"
    else:
        voice "d5_IllGo_c"
    wt_ca "I'll go check the coordinates real quick. Let's establish a meet up point for tomorrow!"
    if radio_static == "_s":
        voice "d5_IllWalkie_s"
    else:
        voice "d5_IllWalkie_c"
    wt_ca "I'll Walkie you later, Gregory!"
    show gr happy
    voice "d5_ThatllBe"
    wt_gr "That'll be lovely, Cassie."
    show gr confused
    voice "d5_HowLong"
    wt_gr "How long do you reckon we'll be up there, Isaak?"
    if radio_static == "_s":
        voice "d5_UntilI_s"
    else:
        voice "d5_UntilI_c"
    wt_is "Until I have enough. There's no rough estimate right now."
    $ chibi_koda = "images/chibi/koda_happy.png"
    if radio_static == "_s":
        voice "d5_WellLeave_s"
    else:
        voice "d5_WellLeave_c"
    wt_ko "We'll leave you guys to it for now! Big day tomorrow!"
    nvl clear
    #radio ends

    show ast neutral
    show pearl neutral
    with dissolve
    voice "d5_WellYou"
    gr "{w=0.5}Well, you heard the man. Let's start packing the essentials."
    show gr neutral
    voice "d5_WereMoving"
    gr "We're moving at dawn."
    voice "d5_AyeAye"
    mo "Aye aye, captain."

label dec_6_1:
    scene bg camp1_day with longfade
    $ current_day = _("December 6th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    "Essentials and equipment have all been well packed."

    "Today is moving day."
    "New terrain to conquer, new friends to meet."
    "I'm sure it'll be lovely."
    show gr neutral at left
    voice "d6_GotEverything"
    gr "Got everything ya need, Pearl? Personal belongings, what not?"
    show pearl happy at centerright
    voice "d6_IWould"
    pe "I would hope so!"
    voice "d6_DidYou"
    mo "Did you remember your compass?"
    show pearl sad
    voice "d6_Aww"
    pe "Aww..."
    show lorenzo smile at right
    hide pearl
    with dissolve
    voice "d6_LooksLike"
    lo "Looks like she forgot."
    show ast neutral
    voice "d6_HowIs"
    ast "How is the route up going to be?"
    show gr with move:
        xpos 200
    show lorenzo with move:
        xpos 1600
    voice "d6_AlrightySo"
    gr "Alrighty, so...here's the route that Cassie drew for us."


    "Gregory holds out his map with outstretched hands for us to see."
    show gr happy
    voice "d6_WereGonna"
    gr "We're gonna start climbing the mountain over 'ere. It's less steep of an angle to trek, she said."
    voice "d6_OnceWeve"
    gr "Once we've reached the midpoint, we're gonna pivot to this area here. A nice flat area to set up camp."
    voice "d6_DoYou"
    mo "Do you know how long that might take us?"
    show gr confused
    voice "d6_AFew"
    gr "A few hours at least. We should be able to get there before sundown."
    show lorenzo neutral
    voice "d6_AndWere"
    lo "And we're meeting them at the midpoint, yes?"
    show gr neutral
    voice "d6_ThatIs"
    gr "That is correct."

    show ky smile at left:
        xpos -100
    voice "d6_AreWe"
    ky "Are we going to come back later to retrieve everything?"
    voice "d6_YesThats"
    gr "Yes, that's why the essentials are the only things that we're carrying today. We've gotta make multiple trips over the next few days."
    show ky happy
    voice "d6_CoolCool"
    ky "Cool, cool! I'm happy to help wherever needed!"
    voice "d6_WellDefinitely"
    mo "We'll definitely be needing the extra hands, Kyle."

    show pearl happy at right
    voice "d6_ImBack"
    pe "I'm back and ready to go! Double checked my pockets this time."
    show lorenzo smile
    voice "d6_ShallWe"
    lo "Shall we?"

    scene bg forest2 with dissolve
    #EXT: Forest mountain
    "In a single file, we followed Gregory up the trail."
    "Hiking up the snow doesn't seem too bad now that I've had a whole month of practice."
    #SFX snowfootmulti
    "The snow crunches under our feet in a nice, rhythmic pattern."
    show ky smile at left
    show pearl smile:
        xpos 300
        yalign 1.0
    show gr neutral at center
    show lorenzo smile:
        xpos 1000
        yalign 1.0
    show ast neutral at right


    play sound beep
    "Beep!"
    "It's Gregory's Walkie."
    if radio_static == "_s":
        voice "d6_HelloMy_s"
    else:
        voice "d6_HelloMy_c"
    wt_wi "Hello my friends! Checking in to see if everyone's on their merry way!"
    voice "d6_WeveStarted"
    wt_ky "We've started trekking a while ago, Wilbur! We're on our way!"
    if radio_static == "_s":
        voice "d6_GladTo_s"
    else:
        voice "d6_GladTo_c"
    wt_da "Glad to hear you're excited, Kyle!"
    show ky happy
    voice "d6_IMean"
    wt_ky "I mean, it's photography! Of course I'm excited."
    show ky flustered
    voice "d6_ImAlso"
    wt_ky "I'm also excited to see you guys... Cassie especially."
    show ky smile
    if radio_static == "_s":
        voice "d6_CassieIs_s"
    else:
        voice "d6_CassieIs_c"
    wt_ru "Cassie is once again hiding behind me, but she's got the message."
    $ chibi_cassie = "images/chibi/cassie_worried.png"
    if radio_static == "_s":
        voice "d6_RuranHow_s"
    else:
        voice "d6_RuranHow_c"
    wt_ca "Ruran! How could you?!"
    if radio_static == "_s":
        voice "d6_Haha_s"
    else:
        voice "d6_Haha_c"
    wt_ru "Haha!"
    $ chibi_davos = "images/chibi/davos_neutral.png"
    if radio_static == "_s":
        voice "d6_AlsoI_s"
    else:
        voice "d6_AlsoI_c"
    wt_da "Also, I hope Pearl didn't forget her compass today."
    $ chibi_morgan = "images/chibi/morgan_happy.png"
    voice "d6_SheDid"
    wt_mo "She did."
    show pearl sad
    voice "d6_MorganI"
    pe "Morgan! I am a good camp guide, I swear!"
    voice "d6_WeBelieve"
    lo "We believe in you, Pearl."
    show pearl smile
    voice "d6_ThankYou"
    pe "Thank you."
    if radio_static == "_s":
        voice "d6_OnThe_s"
    else:
        voice "d6_OnThe_c"
    wt_ja "On the topic of photography... What animal do you think we'll see most of, Kyle?"
    show ky neutral
    voice "d6_YouKnow"
    wt_ky "You know, I'm not exactly sure since this is the first time we'll be up here."
    show ky happy
    voice "d6_MyGuess"
    wt_ky "My guess would be wolves or coyotes...any non-friendly but friend-shaped doggos."
    if radio_static == "_s":
        voice "d6_ImHoping_s"
    else:
        voice "d6_ImHoping_c"
    wt_da "I'm hoping we can capture birds. We've never really seen them on lower ground."
    $ chibi_davos = "images/chibi/davos_happy.png"
    if radio_static == "_s":
        voice "d6_BirdwatchingsAbout_s"
    else:
        voice "d6_BirdwatchingsAbout_c"
    wt_da "Birdwatching's about to get interesting!"
    $ chibi_wilbur = "images/chibi/wilbur_neutral.png"
    if radio_static == "_s":
        voice "d6_HowFar_s"
    else:
        voice "d6_HowFar_c"
    wt_wi "How far more till the meet up point, Cassie?"
    $ chibi_cassie = "images/chibi/cassie_neutral.png"
    if radio_static == "_s":
        voice "d6_WellWith_s"
    else:
        voice "d6_WellWith_c"
    wt_ca "Well, with our current pacing, we'll see them in about an hour or less!"
    $ chibi_ruran = "images/chibi/ruran_happy.png"
    if radio_static == "_s":
        voice "d6_ThatSounds_s"
    else:
        voice "d6_ThatSounds_c"
    wt_ru "That sounds great. We'll be just on time for lunch. This time, together."
    voice "d6_IShould"
    wt_mo "I should get Pearl to do a curtain reveal for me."
    voice "d6_WellI"
    wt_pe "Well, I don't have curtains, but you can crouch behind all of us!"
    $ chibi_morgan = "images/chibi/morgan_neutral.png"
    voice "d6_SoundsLike"
    wt_mo "Sounds like a plan."
    voice "d6_MorganCan"
    gr "Morgan, can you hold the map for me? I just need to grab my compass real quick."
    stop music

    if persistent.screenshake:
        with hpunch

    show lorenzo neutral
    show pearl confused
    show ky confused
    show ast confused
    show gr confused
    
    play sound boom
    "{b}{i}{size=+5}*boom*"

    "That sounded like a muffled gun, but louder."

    $ chibi_jax = "images/chibi/jax_worried.png"
    if radio_static == "_s":
        voice "d6_YallHear_s"
    else:
        voice "d6_YallHear_c"
    wt_ja "Y'all hear something?"
    nvl clear
    voice "d6_ItWasnt"
    ast "It wasn't just you."
    voice "d6_WasThat"
    mo "Was that a gun, or-"


    if persistent.screenshake:
        with hpunch
    show ast scared
    show lorenzo scared
    show pearl scared
    show ky shaken
    show gr scared

    play sound rumble
    "{b}{i}{size=+5}*rumble*"

    #TODO start shakingggg
    "The ground beneath us starts shaking."
    "That doesn't feel... {w=1.2}Right?"
    "Instinctively, Gregory and I look towards the top of the mountain."
    voice "d6_WhatThe"
    gr "What the-"

    play audio avalanche
    "Oh no."
    "Actually, that's an understatement. We're fucked."
    "From the peak of the mountains, the snow is gushing down at us at breakneck speed."
    if radio_static == "_s":
        voice "d6_AvalancheTake_s"
    else:
        voice "d6_AvalancheTake_c"
    wi "{size=+5}AVALANCHE!! TAKE COVER!!"

    "Wilbur's voice rings out and brings us back to center."
    "Run, hide and survive, or get swallowed alive."

    show cg avalanche
    $ persistent.gallery_avalanche = True
    play audio avalanche2
    voice "d6_DontJust"
    gr "{size=+5}{i}DON'T JUST STAND THERE, RUN!!"

    "Camp dad's voice is loud and clear."
    hide cg
    scene bg forest2 with sdissolve
    "He's right, I have to survive this."
    "Elly... If we're both still alive, you best bet I'm gonna extort free meals from you every day."
    "The things I do... {w=0.5}Or, rather, the things I have to go through for you."

    "I ran as fast as my legs could take me."
    "The snow below my feet keeps giving way. I'll trip if I'm not careful."
    "I can't outrun the snow...it'll catch up to me soon."
    scene bg forest2 with dissolve
    "There's a rock formation up ahead, tall enough to shelter me from the onslaught."
    "Bingo! That's my ticket out of here."
    "Almost there... {w=0.6}Just a few more steps and I'll-"


    show bg forest2:
        zoom 2
        linear 0.2 blur 20
        parallel:
            linear 0.2 ypos 1080

    play sound stone
    voice "d6_Ugh"
    mo "Ugh..."

    "I felt a strike towards the back of my head."
    show black:
        linear 0.5 alpha 0.5
    with Pause (0.5)
    scene black with fade

    "I can't lose consciousness now. I need to... {w=1.0} No..."
    jump tr_dec_6

#Morgan passes out
#Scene transition: Fade to black
#Arc 1 ends



