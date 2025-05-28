label dec_6_2:
    #Arc 2 start
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    #Scene transition: Fade to black, then fade back in slowly
    scene bg maintent_night with longfade
    play ambience amb_intcampnight fadein 1.0
    "I don't know how long it's been."
    "The pounding pain in the back of my head radiates as I try to take in my surroundings."
    "This is...{w=1.0}the main tent?"
    "There was an avalanche and I... {w=0.8}I was trying to hide from the snow and..."
    show ast happy at centerleft

    show pearl smile at centerright
    voice "d6_Morgan"
    ast "Morgan!"
    voice "d6_HesAwake"
    pe "He's awake!"

    "I'm relieved that Aston and Pearl are here...but where are the rest?"

    show ast neutral
    voice "d6_YouAre"
    ast "You are okay, Morgan. We're in the main tent."
    voice "d6_OrMain"
    pe "Or main tent 2.0."
    voice "d6_YouHave"
    ast "You have a wound at the back of your head, perhaps caused by falling debris. You were an unlucky target."
    show ast inthought
    voice "d6_AndYouve"
    ast "And you've been out for about 5 hours now."
    voice "d6_WheresLorenzo"
    mo "Where's Lorenzo... Kyle...{w=0.5}and Gregory?"

    show pearl sad
    show ast sad

    "Pearl looks down...and Aston, he's looking up?"
    "That was not the reaction I'd hope to see."
    "I never thought I'd see him emotional, but it looks like Aston's on the verge of breaking down."

    show pearl neutral
    voice "d6_GregoryHes"
    pe "Gregory... He's outside the tent. He's fine."
    show pearl sad
    voice "d6_KyleIs"
    pe "Kyle is also fine. He's sorting through our supplies and setting up our sleeping space for tonight."

    show pearl depressed
    voice "d6_LorenzoWe"
    pe "Lorenzo... We haven't found him."
    voice "d6_WeveTried"
    pe "We've tried beeping his Walkie, but we haven't received anything."
    show pearl neutral
    voice "d6_ThatsHow"
    pe "That's how we found you! Yours beeped under the snow and we heard it."

    hide ast with sdissolve
    "Aston turns away from us."

    voice "d6_LetsGo"
    mo "Let's go find him."
    voice "d6_YouShould"
    ast "You should rest Morgan, and...it's too dark outside to see right now."
    voice "d6_WeveAlready"
    ast "We've already searched the area around us before sundown."

    show pearl sad
    "His voice is cracking. Pearl reaches out to hold his hand."

    voice "d6_FirstThing"
    mo "First thing at dawn then, Aston."
    voice "d6_LorenzoIs"
    mo "Lorenzo is strong, and I am positive that he'll be okay."

    show ast neutral at centerleft
    "Aston turns around and gives me a light nod."
    "We fall silent, looking at each other I can sense that we're all determined to find him."
    "The worry lingers, but I know we'll do the best we can."
    "He's a tough cookie. He'll survive this."
    stop ambience fadeout 3.0

label dec_7:
    scene bg forest3 with longfade
    $ current_day = _("December 7th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    play music audio.neutral

    "Waking up the next day was challenging."
    "Muscles are sore, head's taken a beating, but other than that I am fine."
    show ast sad
    "Aston and I are currently out looking for Lorenzo."
    "Gregory and the rest are still trying to salvage the camp and deal with the relocation."
    "Our original campsite has been obliterated, but fortunately not covered in a heap of snow."
    "The site with the heaviest impact just so happens to be right in the middle of both C1 and C2."

    #EXT: Forest 2
    show bg forest1

    "Joining us on our search are Davos and Jax."
    "They're trying to cover the area around C2, south of the impact."
    "We doubt that Lorenzo would be around there, since he was with Aston right before the avalanche."
    "But we don't want to take any chances."
    #(TOGGLE) ja da
    
    if radio_static == "_s":
        voice "d7_HowsThe_s"
    else:
        voice "d7_HowsThe_c"
    wt_ja "How's the status of your camp? Heard you got knocked out, Morgan."
    $ chibi_morgan = "images/chibi/morgan_worried.png"
    voice "d7_YepIt"
    wt_mo "Yep. It still hurts too."
    voice "d7_PearlGregory"
    wt_mo "Pearl, Gregory and Kyle are at base, and Aston is here with us to find Lorenzo."
    $ chibi_davos = "images/chibi/davos_worried.png"
    if radio_static == "_s":
        voice "d7_IPromise_s"
    else:
        voice "d7_IPromise_c"
    wt_da "I promise we'll do our best, Aston. We'll find him."
    $ chibi_jax = "images/chibi/jax_neutral.png"

    if radio_static == "_s":
        voice "d7_OnC2s_s"
    else:
        voice "d7_OnC2s_c"
    wt_ja "On C2's side, Cassie sprained her ankle. Wilbur had a few scrapes."
    $ chibi_jax = "images/chibi/jax_worried.png"
    
    if radio_static == "_s":
        voice "d7_RuranAnd_s"
    else:
        voice "d7_RuranAnd_c"
    wt_ja "Ruran and I got pushed out pretty far from the rest. Took a while for us to locate where we were."
    
    if radio_static == "_s":
        voice "d7_IWas_s"
    else:
        voice "d7_IWas_c"
    wt_da "I was lucky enough to avoid most of the hits."

    "Aston has been trying to reach Lorenzo through his Walkie."

    if radio_static == "_s":
        voice "d7_EvaAnd_s"
    else:
        voice "d7_EvaAnd_c"
    wt_ja "Eva and Koda were pretty worried about us."
    $ chibi_jax = "images/chibi/jax_neutral.png"
    
    if radio_static == "_s":
        voice "d7_EvenIsaak_s"
    else:
        voice "d7_EvenIsaak_c"
    wt_ja "Even Isaak called. That was pretty unlike him."
    voice "d7_AnySign"
    ast "Any sign of him?"
    
    if radio_static == "_s":
        voice "d7_WeHavent_s"
    else:
        voice "d7_WeHavent_c"
    wt_da "We haven't seen anything out of the ordinary, Aston."
    $ chibi_jax = "images/chibi/jax_worried.png"
    
    if radio_static == "_s":
        voice "d7_LetsKeep_s"
    else:
        voice "d7_LetsKeep_c"
    wt_ja "Let's keep calling out."
    voice "d7_Lorenzo"
    mo "Lorenzo!"
    
    
    voice "d7_LorenzoWhere_s" # Davos isn't Walkie-fied but IS further away, hence always static'd
    da "Lorenzo! Where are you!"

    "We called his name. No response."

    voice "d7_WhereAre"
    ast "Where are you, my love...?"

    show black with dissolve
    "The search mission went on for hours, but we were unsuccessful. It had to come to a halt for the day."
    "The sun was setting and we had to head back to camp before it became dark."

    "Lorenzo has been missing for about 24 hours now... It's not a good sign."

    #EXT: Camp 1A
    scene bg camp2_day with fade
    show ky smile at centerright
    show ast neutral at centerleft
    voice "d7_MorganAston"
    ky "Morgan, Aston! You're back!"

    show ast with move:
        xpos 1800
    hide ast
    "Aston doesn't respond and heads straight into the tent."
    show ky sad
    "Kyle sees that Lorenzo still hasn't come home."

    voice "d7_ItsNot"
    mo "It's not a \"you\" problem, Kyle. Don't worry."
    voice "d7_YeahI"
    ky "Yeah... I just wish there was something I could do for him right now."
    voice "d7_YouHavent"
    mo "You haven't fully recovered from whatever you're dealing with, either. You need to rest."
    show ky confused
    voice "d7_IKnow"
    ky "I know, which sucks. The best I can do is just hold the fort until everyone comes home."
    show ky smile
    voice "d7_GregoryAnd"
    ky "Gregory and Pearl are gonna help out tomorrow, I think."

    voice "d7_YepHopefully"
    mo "Yep. Hopefully it'll make the search much easier."
    stop music fadeout 3.0
    #INT: Main tent
    scene bg maintent_night with fade
    play ambience amb_campnight fadein 1.0

    "The sleeping bags have all been moved to the main tent for now."
    "Some of our smaller tents were destroyed, so everyone's gotta share the big tent for the time being."
    "I need to call Colin."
    "Time for the waiting game, I guess."
    "Once everyone's asleep, I'll step outside."

    #EXT: Camp 1A
    #(TOGGLE) co
    show bg camp2_night with fade
    show satphone
    voice "d7_HeyPancake"
    mo "Hey Pancake."
    
    if radio_static == "_s":
        voice "d7_WoahYou_s"
    else:
        voice "d7_WoahYou_c"
    co "Woah, you sound horrible. So my birdie in Heralign HQ was right about the situation?"
    voice "d7_IfThey"
    mo "If they heard \"avalanche,\" then...yes. They're right."
    
    if radio_static == "_s":
        voice "d7_WasAnyone_s"
    else:
        voice "d7_WasAnyone_c"
    co "Was anyone hurt? Are you hurt, Morg?"
    voice "d7_PassedOut"
    mo "Passed out for a few hours after getting hit by a rock or something."
    voice "d7_MyHead"
    mo "My head still hurts, but otherwise I'm fine."
    voice "d7_WeDo"
    mo "We do have someone that went missing, though. That's the worrying part."

    if radio_static == "_s":
        voice "d7_JudgingFrom_s"
    else:
        voice "d7_JudgingFrom_c"
    co "Judging from your tone, time's ticking and you still haven't found them?"
    voice "d7_YepLorenzo"
    mo "Yeah. Lorenzo has been missing for a little over 24 hours at this point."
    
    if radio_static == "_s":
        voice "d7_RoughSpot_s"
    else:
        voice "d7_RoughSpot_c"
    co "Rough spot there, bud. I hope he's okay."
    
    if radio_static == "_s":
        voice "d7_ButStill_s"
    else:
        voice "d7_ButStill_c"
    co "But, still... I'm glad you're in one piece, Morg."
    voice "d7_TheThings"
    mo "The things I do for Elly...and you, too!"
    
    if radio_static == "_s":
        voice "d7_WhatDo_s"
    else:
        voice "d7_WhatDo_c"
    co "What do you want from me this time? The snowmobile again?"
    voice "d7_YoureThe"
    mo "You're the best, thank you."
    
    if radio_static == "_s":
        voice "d7_HowAbout_s"
    else:
        voice "d7_HowAbout_c"
    co "How about the welcome home party that we talked about? I'll even cook for you."
    voice "d7_OkayAlright"
    mo "Okay, alright. I'll take that, but you've gotta give papa a kiss."
    
    if radio_static == "_s":
        voice "d7_No_s"
    else:
        voice "d7_No_c"
    co "No."
    voice "d7_AwwAre"
    mo "Aww, are you shy?"
    
    if radio_static == "_s":
        voice "d7_YouEnjoy_s"
    else:
        voice "d7_YouEnjoy_c"
    co "You enjoy terrorizing me, don't you, Morg?"
    voice "d7_GoodnightPancake"
    mo "Goodnight, Pancake. Sweet dreams!"
    
    if radio_static == "_s":
        voice "d7_DidYou_s"
    else:
        voice "d7_DidYou_c"
    co "Did you just kiss the damn ph-"
    hide satphone with sdissolve
    #phone end

    "I hung up on Colin."
    scene black with dissolve
    "I do enjoy terrorizing him...keeps me sane from the mess I'm dealing with here."
    stop ambience fadeout 3.0

label dec_8:
    #INT: Cabin
    scene cottage with longfade
    $ current_day = _("December 8th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    play ambience amb_cabin fadein 1.0
    #Lorenzo's POV
    
    voice "d8_LetsSee"
    lo "Let's see here... I've got food that will last me for a week."
    voice "d8_TwoTwo"
    lo "Two... Two weeks if I can handle eating just one meal per day."

    show black with dissolve
    "On the day of the avalanche, Lorenzo slipped and tumbled down the hill."
    "He escaped death, but still sustained a few bruises here and there."
    "He ended up further away from the rest... Separated from Aston."
    "To make things worse, his Walkie's receiver snapped off during the fall."
    "With no map on hand, it would be difficult to navigate back to camp."
    "When time is ticking and the sun threatens to set...you don't have a lot of options."
    "Shelter is the first prerequisite for survival in this situation."
    "Fortunately, he found himself close to a tiny, deserted cabin."
    "It's not fancy by any means, but at least there's a roof over his head now."
    hide black

    voice "d8_TheFurniture"
    lo "The furniture in here reminds me a lot of the village up north... Maybe this is one of their hunting huts."

    "Looking around, there's a shelf of perishables, a mini fireplace, and lots of blankets and a sole rifle leaning against the wall."
    "Lorenzo made a makeshift bed with an armchair and its matching ottoman."
    "The silver lining is that it's much more comfortable than a sleeping bag."

    voice "d8_INeed"
    lo "I need to start finding my bearings tomorrow. Cassie's map never had a cabin on it, so this must be an area that we haven't been to yet."
    voice "d8_ImSure"
    lo "I'm sure he's worried sick about me."
    voice "d8_HangTight"
    lo "Hang tight, amore. I'll find you."
    voice "d8_OrYoull"
    lo "Or you'll find me first... I think that's more probable."

    #BG Window
    show bg window
    "The scenery out the window is unhelpful."
    "It's snowing."
    "All around there's just trees and snow."
    "And there's a nice rock formation in the distance, but that's about it."
    "Time passes much slower without the rest of them."

    #BG Window with bear
    #TODO ASK ELINA ABOUT MISSING TREES STUFF
    show cg bearwindow1
    "About this time of day, Aston would've been making dinner."
    stop ambience

    #BG Window
    hide cg
    voice "d8_WaitWhat"
    lo "Wait, what was that?"
    play music audio.anxious
    "Out of the corner of his eye, Lorenzo swears that he saw something huge."
    "Something... {w=1.0}Unpleasantly familiar."
    show cg bearwindow2
    "He pinches himself."

    voice "d8_ImStill"
    lo "I'm still wide awake...so then why?"

    hide cg
    "He looks out the window again."

    #BG Window with bear
    show cg bearwindow3
    play sound lobeargrowl
    if persistent.screenshake:
        with hpunch
    $ persistent.gallery_bearwindow = True
    voice "d8_LorenzoVNVR"
    lo "..."

    show black with pushupquick
    hide cg
    "He crouches under the window to catch his breath."
    voice "d8_TheDoor"
    lo "The door! The door... Locked, yes. The window...that won't do. I need to cover it up."

    hide black
    show bg cottage2
    play sound blanket
    "He runs to the blankets and quickly drapes it over the window."
    "After pacing around the room nervously, he decided that he'll hold the rifle in hand while he sleeps tonight."
    "Not sure if the rifle would do any damage but, it's safer to have it than not."
    stop music fadeout 3.0


label dec_9:
    #start scene black
    scene black with dissolve
    $ current_day = _("December 9th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    "The search today went on longer than the other days."
    "Still no sign of Lorenzo."
    "We've cleared the area around the lake, the surrounding area of the village."
    "Even where I was first dropped off, but still nothing."
    "The site of the avalanche yielded no results either."
    "The guys at Camp 2 have been digging around too."
    "I heard Eva and Koda were there to support the camp as well."
    "We've never found any of Lorenzo's belongings."
    "He must've been pretty far when we separated."
    play sound backpack volume 0.5
    "*rustle*"
    "Sounds like I'm not the only one awake."

    #INT: Main tent
    scene bg maintent_night with dissolve
    play ambience amb_intcampnight fadein 1.0
    "I cracked my eyes open slightly."
    show ast inthought
    "It's Aston."
    "He's standing up and checking his pockets."
    "I checked my clock, it's 11:41pm. That's already pretty late at camp."
    "Is he doing what I think he's doing?"
    stop ambience fadeout 3.0
    play music audio.neutral
    menu:
        "Call him":
            voice "d9_Aston"
            mo "Aston."
            show ast confused
            "I think I startled him."
            voice "d9_GoBack"
            ast "Go back to sleep, Morgan."
            "Aston is doing exactly what I think he's doing."
            "He's going to go out at night, in the pitch dark silence, alone."
            "I stand up next to him."

            menu:
                "Convince him not to go":
                    voice "d9_IDont"
                    mo "I don't think it's a good idea."
                    show ast angry
                    voice "d9_IfYoure"
                    ast "If you're not going to help me, please do not stop me."

                "Join him":
                    voice "d9_IKnow"
                    mo "I know what you're doing, but please let me come along. It's dangerous to go alone."
                    show ast sad
                    "Aston looks worriedly at me."

        #choice branch 2 ends
            show gr neutral at right
            voice "d9_AreYou"
            gr "Are you guys heading out?"
            "Gregory sits up, tiredly."
            show gr angry
            voice "d9_YoureNot"
            gr "You're not supposed to go out after night remember? I'm liable for your safety."
            show ast angry
            voice "d9_LorenzoIs"
            ast "Lorenzo is out there, I can't possibly sleep it off like it's nothing."
            show gr neutral
            voice "d9_LookYou"
            gr "Look, you can try if you want."
            voice "d9_ButIt"
            gr "But it is cold as shit out there, and your flashlight is not gonna be helpful."
            "Aston doesn't say anything else."
            "Determined, he turns to leave."
            hide ast
            voice "d9_HesUsually"
            mo "He's usually not that reckless. Let me go check on him."
            voice "d9_MorganLet"
            gr "Morgan, let him be. He'll come back tomorrow."
            voice "d9_But"
            mo "But-"
            show gr angry
            "Gregory shoots me a glare."
            "I don't think I can catch up to Aston anymore at this point."
            hide gr
            "I'm no longer hearing footsteps outside the tent."
            "If I look for him now, it would not do any good."
            "Damn it."
            "I counted my losses and stayed in the tent all night. I didn't get any sleep."

        "Follow him out":
            "Aston is doing exactly what I think he's doing."
            "He's going to go out at night, in the pitch dark silence, alone."
            "I followed him out the tent."

            show bg camp2_night
            #choice branch 2 starts
            menu follow_aston:
                "Convince him not to go":
                    "I called out to him."
                    voice "d9_IDont"
                    mo "I don't think it's a good idea."
                    show ast angry
                    voice "d9_IfYoure"
                    ast "If you're not going to help me, please do not stop me."
                    voice "d9_DontEven"
                    ast "Don't even bother following me."
                    hide ast with sdissolve
                    "Aston took off from the camp."
                    "I can't gear up quick enough to catch up to him."
                    voice "d9_WaitAston"
                    mo "Wait, Aston!"
                    "Damn it."
                    "I counted my losses and stayed in the tent all night. I didn't get any sleep."

                "Join him":
                    $ aston_safe = True
                    $ joined_aston = True
                    voice "d9_IKnow"
                    mo "I know what you're doing, but please let me come along. It's dangerous to go alone."
                    show ast sad
                    "Aston looks worriedly at me."
                    voice "d9_AlrightGear"
                    ast "Alright, gear up quickly. I'll wait for you."
                    "I gave Aston a quick nod and ran back in to gear up."
                    "The two of us set out on a little adventure to find Lorenzo."
                    "Is it a dumb choice? Probably."
                    "There's lots to fear about the forest at night."
                    "Is it still worth a try? Absolutely."
                    "Lorenzo is a dear friend, and to Aston?"
                    "Lorenzo is his everything."
                    jump find_lorenzo

        #choice branch 2 ends
    #choice branch 1 ends
    stop music fadeout 3.0


label dec_10:
    #This sequence only happens if you fail to join Aston on his adventure, then it just continues downwards
    #(STRIKE 1 added to Gregory sus meter)
    #EXT: Camp 1A
    scene bg camp2_day with longfade
    $ current_day = _("December 10th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    play ambience amb_campday fadein 1.0
    if not joined_aston:
        "The search commences today."
        "Gregory was right about Aston, he made it back before dawn."
        show ast neutral
        "The dark circles under his eyes and his expressions tell me that his search was unsuccessful."

        voice "d10_AstonFromMorgan"
        mo "Aston?"
        voice "d10_GoodMorning"
        ast "Good morning, Morgan."
        show ast sad
        voice "d10_IdLikeToApologise"
        ast "I'd like to apologise for yesterday."
        voice "d10_NoPlease"
        mo "No please don't, you're good."
        voice "d10_JustThat"
        mo "Just that, if you're planning on doing that again tonight, please let me know."
        show ast neutral
        voice "d10_AlrightI"
        ast "Alright, I shall."
        show ast sad
        voice "d10_MySearch"
        ast "My search...was unsuccessful."
        voice "d10_ItsOkay"
        mo "It's okay, we'll keep trying. You have an ally here."
        show ast happy
        "Aston flashes me a weak smile, and nods."
        stop ambience fadeout 3.0

    #Skip to this sequence if you successfully join Aston on his adventure
    label find_lorenzo:
        scene forest3 with fade
    #EXT: Forest
        play ambience amb_campnight fadein 1.0
        "Did I ever mention loving night walks?"
        "Well, I hate this."
        "A night walk in the forest is never fun, unless you live for the thrill."
        "I don't particularly find putting myself at risk of getting mauled by animals 'thrilling' so to speak."
        "I'm just glad that it isn't snowing right now."
        "And the fact that Aston is with me...at least we're not alone in this dreaded cold."
        "We decided to take an entirely different path this time."
        "Gregory did say the east side of the mountains is a big no-no."
        "But that's exactly the direction we are going to go."
        "After walking for a bit, my flashlight reflects off a different surface."
        "Shiny. It's not a tree."
        "Is that a window?"

        show ast neutral
        voice "d10_AstonLook"
        mo "Aston, look."

        "We shined our flashlights towards the same spot."
        "A cabin...it looks kinda small."
        "A hunting cabin, maybe?"
        "We walked up to the door and inspected it up close."

        voice "d10_ISuppose"
        mo "I suppose we should give a polite knock before entering?"
        stop ambience fadeout 5.0
        play sound knock
        "Aston knocks on the door."
        show ast sad
        voice "d10_LorenzoAre"
        ast "Lorenzo, are you in here?"
        voice "d10_AstonFromLorenzo"
        lo "Aston?"

        show cg findinglorenzo
        $ persistent.gallery_findinglorenzo = True
        play music audio.light

        hide ast
        play sound cabinopen
        "Aston barges into the cabin to see a petrified Lorenzo."

        voice "d10_Lorenzo"
        ast "Lorenzo!"
        voice "d10_AAmoreI"
        lo "A-Amore... {w=1.0}I thought I'd never see you again."
        play sound cabinclose

        "I closed the door behind Aston and let them have their moment."
        "The two of them share a long awaited embrace."
        "It fills me with the purest form of emotional warmth to see them like this."

        hide cg
        show bg cottage2
        show ast happy at centerleft
        show lorenzo sad at centerright
        voice "d10_ThankGoodness"
        ast "Thank goodness."
        voice "d10_IKnew"
        lo "I knew you'd find me, amore."
        voice "d10_ImSorry"
        lo "I'm sorry for worrying you, and everyone as well."

        "With tears forming in his eyes, Lorenzo beams at me as well."
        show lorenzo smile
        voice "d10_ItsGood"
        lo "It's good to see you too, Morgan."

        "I gave him a gentle pat on his shoulder."

        voice "d10_AndIm"
        mo "And I'm glad that you're okay."
        show ast sad
        voice "d10_IDont"
        ast "I don't want you to stay here alone, love."
        show lorenzo sad
        voice "d10_ButIm"
        ast "But I'm worried about bringing you back to camp."
        voice "d10_WhatsThat"
        mo "What's that about?"

        "The two look at me, and then at each other."
        "Lorenzo breaks the silence first."
        show lorenzo neutral
        show ast neutral
        voice "d10_ThereWas"
        lo "There was this person at camp before you...his name is Elliot."

        "Elliot!"
        "I have never been this happy to hear a name spoken out loud."

        voice "d10_OneDay"
        lo "One day, he just disappeared without a trace."
        voice "d10_HisBelongings"
        lo "His belongings all have been rummaged through, as if he was rushing to somewhere."
        show ast inthought
        voice "d10_AndThe"
        ast "And the reason why I don't want Lorenzo to go back to camp is because of Gregory."
        voice "d10_ElliotHad"
        ast "Elliot had a descriptively similar rash forming on the back of his right shoulder."
        voice "d10_RuranWas"
        ast "Ruran was treating him back then. I never had a peek at it, so I can't be sure."
        show ast neutral
        voice "d10_OnThe"
        ast "On the night before he disappeared, I overheard Gregory on the phone."
        voice "d10_HisVery"
        ast "His very words were 'I'll take care of him, ma'am.' I didn't pay any mind to that at the time..."

        show ast angry
        voice "d10_ButEver"
        ast "But ever since Elliot disappeared, I didn't like what I was realising when I put two and two together."
        show lorenzo pondering
        voice "d10_WeDidnt"
        lo "We didn't have any evidence, but we have been really cautious about Gregory ever since."
        show lorenzo neutral
        voice "d10_ButI"
        lo "But I still don't want to believe that he'd do something to Elliot."
        voice "d10_ButGregory"
        mo "But Gregory doesn't seem suspicious of Kyle?"
        show lorenzo pondering
        voice "d10_IdLikeToBelieve"
        lo "I'd like to believe that it's because Kyle was bitten by Susie."
        show lorenzo sad
        voice "d10_WhereasElliot"
        lo "Whereas Elliot and I... I don't even know how I got it in the first place."
        voice "d10_DoYouThinkThat"
        mo "Do you...think that it's the same infection, but from multiple sources?"
        show ast inthought
        voice "d10_ThatWould"
        ast "That would be probable, yes."
        voice "d10_SpeakingOf"
        mo "Speaking of infections... How are you doing, Lorenzo?"
        voice "d10_MyArm"
        lo "My arm is still red...but I think something worse has been happening to me."
        show lorenzo sick
        voice "d10_IIDont"
        lo "I-I don't know, I want to believe that I was just seeing things."

        show ast neutral with move:
            xpos 600
        show lorenzo neutral
        "Aston squeezes Lorenzo's hand to help ease his nerves. Lorenzo takes a deep breath before he continues."

        voice "d10_ItsThe"
        lo "It's the bear, but... But I was sure I saw it right outside the window."
        voice "d10_IPinched"
        lo "I pinched myself while looking directly at it, and no, I wasn't dreaming."
        show lorenzo sad
        voice "d10_AstonMorgan"
        lo "Aston, Morgan... I really don't enjoy the uneasiness I feel running down my spine every time I hear something outside these walls."
        show ast sad
        voice "d10_DoYouWantMe"
        ast "Do you want me to stay the night, love?"
        voice "d10_GregoryWould"
        lo "Gregory would be the problem. Both of you can't stay here."
        show ast neutral
        voice "d10_WedNeed"
        mo "We'd need a plan, then."
        voice "d10_TheGame"
        mo "The game ends if Gregory gets suspicious before Lorenzo's arm heals."
        voice "d10_ThisWould"
        mo "This would mean that Aston and I can only visit you during the night."
        voice "d10_AndThis"
        mo "And this would mean that you have to tank through the day without us here."
        show lorenzo neutral
        voice "d10_IThink"
        lo "...I think I can do that."
        show ast sad
        voice "d10_WillYou"
        ast "Will you be okay?"
        show lorenzo smile
        voice "d10_ForYou"
        lo "For you, amore... I will be strong for you."
        voice "d10_HaveI"
        mo "Have I ever told you guys that y'all are awfully cute?"
        hide ast
        voice "d10_AstonVNVR"
        ast "..."
        show lorenzo happy
        voice "d10_HahaAmore"
        lo "Haha! {w=0.6}Amore, why did you turn away?"
        show ast neutral at centerleft
        voice "d10_ItsNothing"
        ast "It's nothing."
        voice "d10_AlrightLet"
        mo "Alright. Let me know when you're ready to go back, Aston."
        voice "d10_WeHave"
        mo "We have about 5 hours till dawn, but ideally we should get some sleep in, too."
        voice "d10_WouldntWant"
        mo "Wouldn't want to look suspiciously groggy the next day."
        show ast sad
        voice "d10_ThatsVery"
        ast "That's very true."
        voice "d10_WellThen"
        mo "Well then, wake me up when it's time."
        hide ast
        hide lorenzo
        "I sat in a corner and grabbed a blanket."
        "I'll let them have some privacy."
        "Aston will wake me up when it's time to head back."

    #To Sharkie, skip this sequence if you fail to join Aston on his adventure
        if joined_aston:
        #INT: Main tent
            scene bg maintent_day with dissolve
            "We made it back before sunrise."
            "Aston fell asleep immediately upon getting back."
            "His face no longer scrunches up while he sleeps."
            "No more tossing and turning, either."
            "All is well now."
    stop music fadeout 3.0

label dec_11:
    #EXT: Camp 1A
    scene bg camp2_day with longfade
    $ current_day = _("December 11th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    play ambience amb_campday fadein 1.0
    show gr neutral at centerleft
    voice "d11_GuysWeve"
    gr "Guys, we've received an extra mission."
    "Gregory interrupts breakfast with urgent news."
    show pearl smile at centerright
    voice "d11_WhatIs"
    pe "What is it, what is it?"
    voice "d11_SomeoneFrom"
    gr "Someone from the village is missing."
    voice "d11_SoWhile"
    gr "So while we look for Lorenzo, we'll also have to keep our eyes peeled for another person."

    "Someone else is missing?"
    "We exchanged quiet glances, letting the weight of the situation sink in."
    "While everyone has been worried about Lorenzo, there's now potentially another victim."
    "Lorenzo was lucky."
    "I hope they survive this as well."
    show pearl confused
    voice "d11_DidSomeone"
    pe "Did someone report it?"
    show gr confused
    voice "d11_YeahIsaak"
    gr "Yeah, Isaak is in contact with the village. There's a hotline for complaining if we ever get too rowdy here."

    "So someone told Isaak this information?"
    "I mean, I already knew that the whole 'the village hates us' facade was probably a lie..."
    "But why would they be anywhere near our camp when the avalanche happened?"
    "Just casually strolling to our camp?"
    "We've been on the search for a few days now. There hasn't been any sign of another survivor."
    "It would seem that Aston also shares the same sentiment."
    "He looks at me, reflecting the same expression that I have."
    "Doubt."
    "The search, now for two, commences."
    stop ambience fadeout 3.0

    scene bg cottage2 with fade
    #Lorenzo's POV
    "Lorenzo is wide awake and feeling restless."

    "The bear's presence has been weighing heavily on his mind."
    "Hearing growling right out the door every once in a while..."
    "The knocking on the window is starting to get annoying, too."
    voice "d11_IdLike"
    lo "I'd like to sleep, if you would be so kind?"
    "No response."
    voice "d11_Grazie"
    lo "Grazie."
    "He pulls the blanket higher up to cover his shoulders."
    play ambience amb_lobear fadein 1.0
    voice "d11_LoLorenzo"
    who "Lo-Lorenzo."
    "The unexpected voice sends a shiver down his spine. That sounded like Aston."
    show lorenzo scared
    "Lorenzo jolts up from his bed."

    voice "d11_AmoreIs"
    lo "Amore? Is that you?"
    voice "d11_LLenzo"
    who "L-Lenzo."
    show lorenzo pondering
    "Nevermind. The fear dissipates and it turns into confusion."

    voice "d11_Lorenzo"
    who "Lorenzo."
    show lorenzo sad
    "Lorenzo's face scrunches up in disappointment."
    "Aston doesn't say his name like that... {w=1.0}This is just insulting."
    "This realization sparked a defiant fire within him."
    show lorenzo neutral
    voice "d11_LorensoIm"
    lo "Lorenso- {w=0.4}I'm hallucinating, aren't I?"


    "For once, instead of fear... Lorenzo is, frankly, really sick of this."
    "The torment needs to stop."

    voice "d11_OkayIll"
    lo "Okay, I'll play your game."
    voice "d11_IfYoure"
    lo "If you're not going to leave me alone, I might as well get to know you."
    "He grabs his journal and turns to a blank page and jots down some notes."
    play sound pen
    "Characteristics:"
    "Black bear, no fur, goop-like."
    "Green stuff looks like a fluid of some sort dripping from its mouth."
    "Doesn't act like a normal bear."

    voice "d11_AndThis"
    lo "And, this... This is a new feature."

    "Mimics speech, but it's not very smart."
    voice "d11_BearGrowl"
    be "*growl*"
    show lorenzo smile
    voice "d11_SalveImitatore"
    lo "Salve, imitatore."
    stop ambience fadeout 1.0


label dec_12:
    #EXT: Camp 1A
    #(TOGGLE) hi
    scene bg camp2_night with longfade
    $ current_day = _("December 12th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    play ambience amb_campnight fadein 1.0
    #Gregory's POV
    "Gregory sits on a rock some distance away from the main tent."
    show gr neutral
    "It's time for his weekly check in."
    if radio_static == "_s":
        voice "d12_YoureA_s"
    else:
        voice "d12_YoureA_c"
    who "You're a day late."
    voice "d12_IKnow"
    gr "I know. Lots of stuff happening at camp at the moment."
    if radio_static == "_s":
        voice "d12_RightFirst_s"
    else:
        voice "d12_RightFirst_c"
    who "Right. First an avalanche, then what?"
    show gr confused
    voice "d12_MissingPeople"
    gr "Missing people. Lorenzo and one of the villagers."
    if radio_static == "_s":
        voice "d12_TheFinancier_s"
    else:
        voice "d12_TheFinancier_c"
    who "The financier? Do you need me to send a replacement?"
    show gr angry
    voice "d12_What"
    gr "What?"
    voice "d12_ListenHere"
    gr "Listen here, lady. I don't care what you rich people think about us."
    voice "d12_ButLorenzo"
    gr "But Lorenzo isn't someone you can just replace like that."
    if radio_static == "_s":
        voice "d12_TheRich_s"
    else:
        voice "d12_TheRich_c"
    who "The 'rich people' like the one you're talking to right now can buy you a liver."
    show gr worried
    voice "d12_GregoryVNVR"
    gr "..."
    if radio_static == "_s":
        voice "d12_ThinkAbout_s"
    else:
        voice "d12_ThinkAbout_c"
    who "Think about it Gregory, once your job here is done, you'll have all the time in the world to be with your little girl."
    if radio_static == "_s":
        voice "d12_ForfeitThe_s"
    else:
        voice "d12_ForfeitThe_c"
    who "Forfeit the rescue mission if it's too time consuming."
    if radio_static == "_s":
        voice "d12_IWant_s"
    else:
        voice "d12_IWant_c"
    who "I want results, not excuses or sob stories."
    show gr neutral
    "Gregory takes a moment to readjust."
    voice "d12_IsThere"
    gr "Is there something you told Isaak but you're not telling me?"
    if radio_static == "_s":
        voice "d12_NoI_s"
    else:
        voice "d12_NoI_c"
    who "No, I haven't spoken to him in weeks."
    if radio_static == "_s":
        voice "d12_ThatBoy_s"
    else:
        voice "d12_ThatBoy_c"
    who "That boy never picks up."
    show gr worried
    voice "d12_ImWorried"
    gr "I'm worried about the mold."
    voice "d12_WhatHappens"
    gr "What happens if the whole camp falls ill?"
    if radio_static == "_s":
        voice "d12_BeA_s"
    else:
        voice "d12_BeA_c"
    who "Be a darling and make the right decisions then. You already know how to prevent it."
    if radio_static == "_s":
        voice "d12_IfIsaak_s"
    else:
        voice "d12_IfIsaak_c"
    who "If Isaak could do it, you can too."
    if radio_static == "_s":
        voice "d12_GoodLuck_s"
    else:
        voice "d12_GoodLuck_c"
    who "Good luck, Gregory. You know what's best for your family."

    "She hangs up on him."
    show gr neutral
    "Gregory takes a look at the tent and sighs."
    "They may not be family, they may not even be friends..."
    "But they are people Gregory spends the most time with."
    "And that doesn't discredit the fact that, deep down, he cares."
    stop ambience fadeout 3.0

label dec_13:
    #EXT: Camp 1A
    #(TOGGLE) co
    scene bg camp2_day with longfade
    $ current_day = _("December 13th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    play ambience amb_campday fadein 1.0
    "Early this morning, Gregory announced that the rescue mission will take a break for now."
    "Even though Aston and I found Lorenzo."
    "This still leaves a bitter taste in our mouths."
    "Aston wears his usual nonchalant expression as Gregory pats him on the shoulder."
    "Kyle and Pearl were obviously saddened by the news..."
    "They weren't in their cheery mood for the rest of the day."
    "Later on, I overheard Gregory on the Walkie with Wilbur."
    "It would seem that C2 isn't taking this decision lightly."
    "On one hand, I understand that there's a quota to meet."
    "On the other... Well, I hate it."
    "That would mean giving up on Lorenzo."
    "With nothing much to do for the rest of the day, I think this would be a good time to drop updates."

    #EXT: Camp 1A
    show bg camp2_night
    stop ambience fadeout 3.0
    "Right. Now that everyone's sleeping, 'tis the time."
    play ambience amb_campnight fadein 1.0

    show satphone
    voice "d13_Pancake"
    mo "Pancake!"
    if radio_static == "_s":
        voice "d13_TheNumber_s"
    else:
        voice "d13_TheNumber_c"
    co "The number you have dialed is unavailable, please tr-"
    voice "d13_OkayPancake"
    mo "Okay, pancake batter, I have something for you."
    if radio_static == "_s":
        voice "d13_ThatsEven_s"
    else:
        voice "d13_ThatsEven_c"
    co "That's even worse."
    voice "d13_DoYou"
    mo "Do you want to be goopy or fluffy? Pick one."
    if radio_static == "_s":
        voice "d13_Fluffy_s"
    else:
        voice "d13_Fluffy_c"
    co "Fluffy..."
    voice "d13_NiceAnyway"
    mo "Nice. Anyway, you need to hear this."
    voice "d13_LorenzosIn"
    mo "Lorenzo's in a cabin in the forest, but his symptoms are getting worse."
    voice "d13_ThenEllys"
    mo "Then Elly's name popped up in conversation."
    voice "d13_GreggysInvolved"
    mo "Greggy's involved in some way, but we don't have evidence."
    voice "d13_AstonOverheard"
    mo "Aston overheard him talking to someone the night before he disappeared."
    voice "d13_AndNow"
    mo "And now Lorenzo is going to camp at the cabin because they don't want to take any chances."
    voice "d13_EllysRash"
    mo "Elly's rash apparently looks exactly like the rashes we're dealing with, and it didn't come from a bite."
    voice "d13_WhichIs"
    mo "Which is why Kyle is safe, he's an outlier."
    if radio_static == "_s":
        voice "d13_NowYoure_s"
    else:
        voice "d13_NowYoure_c"
    co "Now you're talking, Morg! That's a lot that you've gathered here."
    if radio_static == "_s":
        voice "d13_EllyAnd_s"
    else:
        voice "d13_EllyAnd_c"
    co "Elly and Greggy, huh? I'll see if I can dig up more info about that mysterious caller that he reports to."
    voice "d13_AlrightNice"
    mo "Alright, nice! Good talk Pan-"
    hide satphone
    #phone ends

    "He hung up on me."
    "Damn it, he knows my tricks. That ain't fun."
    "I'll need new ways to annoy him."
    stop ambience fadeout 1.0

label dec_14:
    #EXT: Forest
    scene bg forest3 with longfade
    $ current_day = _("December 14th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    play ambience amb_asthalu fadein 1.0

    show ast neutral
    "Aston and I are once again on our way to meet Lorenzo."
    "This time, we brought supplies and some tools to fix his Walkie."
    "I was walking ahead of him with my flashlight illuminating the dense forest."
    "When suddenly, the footsteps behind me stopped abruptly."

    show ast confused
    voice "d14_MorganDid"
    ast "Morgan, did you hear that?"

    "I turn to face Aston."

    voice "d14_WhatDid"
    mo "What did you hear?"

    show ast inthought
    "He shakes his head, signaling me to stay quiet as he focuses on the sound."
    "His gaze glued to a tree to our right."

    show ast sad
    voice "d14_Lorenzo"
    ast "Lorenzo?"
    voice "d14_IDont"
    mo "I don't hear him?"

    show ast confused
    "Aston looks at me dumbfounded."
    "He's clearly hearing something I don't."
    "I should say something."

    #choice branch starts
    menu:
        "Investigate the sound.":
            $ aston_safe = True
            $ aston_follows = True
            voice "d14_br1_AstonI"
            mo "Aston, I don't know what you're hearing."
            voice "d14_ButDo"
            mo "But do you want to investigate the sound?"
            show ast sad
            voice "d14_YesPlease"
            ast "Yes, please."
            "We inch closer to the tree, supposedly that's where the source is coming from."
            "There was no one there."
            show ast inthought
            voice "d14_ISwore"
            ast "I swore I heard him."
            voice "d14_ButYoure"
            ast "But you're right, let's head t-"
            show ast sad
            "Aston freezes up again."
            voice "d14_WhatIs"
            mo "What is it? Talk to me."
            "As I try to get a hold of him, my flashlight dies."
            show black
            play sound flashlight
            "I swapped my batteries out as fast as I could."
            hide black
            show ast scared
            "When the lights turn back on, Aston stands there uneasily."
            voice "d14_MorganCan"
            ast "...Morgan, can you take me to Lorenzo?"
            voice "d14_SayNo"
            mo "Say no more."

        "Continue on without investigating.":
            voice "d14_br2_AstonI"
            mo "Aston, I don't know what you're hearing."
            voice "d14_ButWeve"
            mo "But we've got to get to Lorenzo."
            show ast sad
            "I had to practically drag him along."
            show ast inthought
            voice "d14_ISwore"
            ast "I swore I heard him."
            voice "d14_ButYoure"
            ast "But you're right, let's head t-"
            show ast sad
            "Aston freezes up again."
            voice "d14_WhatIs"
            mo "What is it? Talk to me."
            "As I try to get a hold of him, my flashlight dies."
            show black
            hide ast
            play sound flashlight
            "I swapped my batteries out as fast as I could."
            hide black
            "When the lights turn back on, Aston has gone missing."
            voice "d14_Aston"
            mo "Aston?!"
            "Fuck."
            "He doesn't have a flashlight."
            "I called out to him again."
            "No response."
            "I need to get to Lorenzo, and just pray that Aston shows up at the cabin."
    stop ambience fadeout 1.0


    #choice branch ends
#TODO DOUBLE CHECK THIS WORKS AS PROPERLY
    #If Aston follows you
    if aston_follows:
        scene bg cottage2 with dissolve
        play music audio.light
        #INT: Cabin
        show lorenzo happy at center
        show ast happy at left
        "Upon entering the cabin together, we see Lorenzo waiting patiently for us to arrive."
        "His face lights up at the sight of us."
        voice "d14_br1_ImGlad"
        lo "I'm glad to see you both!"
        show ast with move:
            xpos 400
        play sound hug
        "Aston runs to Lorenzo and gives him a quick hug."
        show ast with move:
            xpos 300
        show lorenzo smile
        "Lorenzo then reaches out to grab his journal."
        voice "d14_HaveA"
        lo "Have a seat, I have some info for you guys."
        play sound page
        "He flips to his recent notes in his journal."
        show ast neutral
        voice "d14_HaveYou"
        mo "Have you been studying it?"
        show lorenzo neutral
        voice "d14_YesThat"
        lo "Yes. That and all my symptoms."
        voice "d14_YouveHad"
        mo "You've had hallucinations that called your name? In Aston's voice?"
        show lorenzo scared
        voice "d14_IDid"
        lo "I did not enjoy that one bit. It was horrifying at first but now I am sick of its games."


        show lorenzo sad
        voice "d14_br1_BecauseI"
        lo "Because I know for a fact that you don't sound like that, amore."
        show ast inthought
        "Aston looks like he's deep in thought."
        voice "d14_AstonAre"
        mo "Aston... Are you alright?"

        show ast neutral
        voice "d14_IWasnt"
        ast "I wasn't, but I am feeling a lot better now."
        show ast inthought
        voice "d14_IfWhat"
        ast "If what you're saying is true, then what I heard outside was...not you."
        voice "d14_br1_IfYou"
        ast "If you weren't there to accompany me Morgan, I think I would've been a goner."

        "I gave Aston a gentle pat."
        show ast sad
        voice "d14_ButWill"
        ast "But will you be okay, love?"
        voice "d14_WhatIf"
        ast "What if the hallucinations get worse?"
        show lorenzo smile
        voice "d14_IllBe"
        lo "I'll be fine amore, no need to worry about me."
        "Lorenzo reaches out to cup Aston's face."
        show lorenzo with move:
            xpos 900
        show ast happy
        voice "d14_AndYou"
        lo "And you... You are much stronger than you think."
        stop music fadeout 3.0

    else:
        #If Aston doesn't follow you, but doesn't die
        if aston_safe == True:
            scene bg cottage2 with dissolve
            #INT: Cabin
            show lorenzo smile
            "Upon entering the cabin, I see Lorenzo waiting patiently for us to arrive."
            show lorenzo sad
            "Seeing me close the door without Aston behind me, Lorenzo begins to worry."
            voice "d14_br2_ImGlad"
            lo "I'm glad to see you Morgan but where's Aston?"
            voice "d14_HeHe"
            mo "He... He ran off. I tried to stop him but he said he kept hearing things."
            voice "d14_WhenI"
            mo "When I finally got my flashlight working again, Aston was gone."
            "Just then the door swings open again, Aston is standing there trying to catch his breath."
            play music audio.light
            show ast neutral at left
            voice "d14_SorryIm"
            ast "Sorry I'm late."
            show lorenzo scared
            voice "d14_AstonDont"
            lo "Aston! Don't scare me like that."
            show lorenzo sad
            show ast sad with move:
                xpos 400
            play sound hug
            "Aston runs to Lorenzo and gives him a quick hug."
            show ast with move:
                xpos 300
            show ast happy with dissolve
            show lorenzo smile
            "Lorenzo then reaches out to grab his journal."
            voice "d14_HaveA"
            lo "Have a seat, I have some info for you guys."
            play sound page
            "He flips to his recent notes in his journal."
            show ast neutral
            voice "d14_HaveYou"
            mo "Have you been studying it?"
            show lorenzo neutral
            voice "d14_YesThat"
            lo "Yes. That and all my symptoms."
            voice "d14_YouveHad"
            mo "You've had hallucinations that called your name? In Aston's voice?"
            show lorenzo scared
            voice "d14_IDid"
            lo "I did not enjoy that one bit. It was horrifying at first but now I am sick of its games."

            show lorenzo sad
            voice ""
            lo "Because I know for a fact that you don't sound like that, amore."
            show ast inthought
            "Aston looks like he's deep in thought."
            voice "d14_AstonAre"
            mo "Aston... Are you alright?"

            show ast neutral
            voice "d14_ImSorry"
            ast "I'm sorry I ran off, but I am feeling a lot better now."
            show ast inthought
            voice "d14_IfWhat"
            ast "If what you're saying is true, then what I heard outside was...not you."
            voice "d14_br2_IfYou"
            ast "If you hadn't reminded me that Lorenzo was safe Morgan, I think I would've been a goner."

            "I gave Aston a gentle pat."
            show ast sad
            voice "d14_ButWill"
            ast "But will you be okay, love?"
            voice "d14_WhatIf"
            ast "What if the hallucinations get worse?"
            show lorenzo smile
            voice "d14_IllBe"
            lo "I'll be fine amore, no need to worry about me."
            "Lorenzo reaches out to cup Aston's face."
            show lorenzo with move:
                xpos 900
            show ast happy
            voice "d14_AndYou"
            lo "And you... You are much stronger than you think."
            stop music fadeout 3.0

        #If Aston is going to die
        else:
            scene bg cottage2 with dissolve
            #INT: Cabin
            play ambience amb_cabin fadein 1.0
            show lorenzo smile
            "Upon entering the cabin, I see Lorenzo waiting patiently for us to arrive."
            show lorenzo sad
            "Seeing me close the door without Aston behind me, Lorenzo begins to worry."
            voice "d14_br2_ImGlad"
            lo "I'm glad to see you Morgan but where's Aston?"
            voice "d14_HeHe"
            mo "He... He ran off. I tried to stop him but he said he kept hearing things."
            voice "d14_WhenI"
            mo "When I finally got my flashlight working again, Aston was gone."
            show lorenzo sick
            #voice "" missing VNVR
            lo "..."
            "Lorenzo then reaches out to grab his journal."
            show lorenzo sad
            voice "d14_WellHave"
            lo "Well have a seat, I have some info for you Morgan."
            play sound page
            "He flips to his recent notes in his journal."
            voice "d14_HaveYou"
            mo "Have you been studying it?"
            show lorenzo neutral
            voice "d14_YesThat"
            lo "Yes. That and all my symptoms."
            voice "d14_YouveHad"
            mo "You've had hallucinations that called your name? In Aston's voice?"
            show lorenzo scared
            voice "d14_IDid"
            lo "I did not enjoy that one bit. It was horrifying at first but now I am sick of its games."
            show lorenzo sad
            voice "d14_br2_BecauseI"
            lo "Because I know for a fact that he doesn't sound like that."
            voice "d14_WhatAston"
            mo "What Aston heard outside was definitely not you then."
            voice "d14_ItWould"
            lo "It would seem that way, yes."
            voice "d14_MorganWill"
            lo "Morgan. Will you help me find him?"
            voice "d14_IWill"
            mo "I will, Lorenzo."
            stop ambience fadeout 3.0

    #If on the 9th, you follow Aston, then it's +1
    #If on the 9th, Aston goes away himself it's +0
    #If on the 14th, you investigate it's +1
    #If on the 14th, you don't investigate it's +0
    #Aston will die if you end up with 0, Aston won't die if you end up with 1 or 2

label dec_15:
    #EXT: Forest
    scene bg forest3 with longfade
    $ current_day = _("December 15th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    #If Aston is safe
    if aston_safe:
        "Today is my turn to accompany Kyle on his photography session."
        "I can't take my mind off what happened last night."
        "Hallucinations and...all of Lorenzo's symptoms?"
        show ky smile
        voice "d15_OhDear"
        ky "Oh dear Morgan! There's lots of deer."
        "That horrible pun snapped me back into reality."
        show ky happy
        "Kyle seems amused with my reaction."
        show ky smile
        voice "d15_WhatsWrong"
        ky "What's wrong, Morgan? Do you want to head back to camp?"
        voice "d15_IllBe"
        mo "I'll be alright Kyle. I've just got lots of things on my mind."

    #If Aston is not safe
    else:
        "Today is my turn to accompany Kyle on his photography session."
        "I can't take my mind off what happened last night."
        "Hallucinations and...all of Lorenzo's symptoms?"
        "And Aston... I haven't seen him since last night."
        show ky smile
        voice "d15_OhDear"
        ky "Oh dear Morgan! There's lots of deer."
        "That horrible pun snapped me back into reality."
        show ky happy
        "Kyle seems amused with my reaction."
        show ky sad
        voice "d15_StillThinking"
        ky "Still thinking about Aston?"
        voice "d15_YeahBut"
        mo "Yeah...but I'll be alright Kyle."

    #continue script from here
    play sound camera2
    "Click click!"
    voice "d15_DoYou"
    ky "Do you want to talk about it or...?"
    show ky confused
    voice "d15_ActuallyHold"
    ky "Actually hold that thought Morgan, are you seeing what I'm seeing over there?"
    hide ky
    show bg forest3_animals
    "Amongst the herd of deer lies a disturbing goop of an animal."
    play music audio.anxious

    "It looks like a dead bird."
    show ky sad
    voice "d15_NoooooWhat"
    ky "Nooooo what happened here?"
    voice "d15_MightBe"
    mo "Might be worth taking pictures of that."

    "Although hesitant at first, Kyle begins snapping a few pictures."
    "Now that I'm actually taking in my surroundings, I realized that there were more of these piles."
    "I gave Kyle a nudge on his shoulder."
    show ky shaken
    voice "d15_KyleVNVR"
    ky "..."

    "Yeah that's a valid reaction."
    "It seems to be mostly birds?"
    "They've definitely been here long enough to start rotting."
    show ky sad
    "\"Do not attempt to handle animal carcasses without protective gear.\""
    "Gotta respect the rules in \"The Camp Guide's Guide.\""
    "It'll definitely be worthwhile to pick some of them up."

    voice "d15_LetsHead"
    mo "Let's head back to camp Kyle, I've got samples to grab."
    show ky shaken
    voice "d15_AAreYou"
    ky "A-Are you gonna pick all of them up?"
    voice "d15_OneShould"
    mo "One should suffice I hope?"
    stop music fadeout 3.0

label dec_16:
    #EXT: Camp 1A
    #If Aston safe
    if aston_safe:
        scene cottage2 with longfade
        $ current_day = _("December 16th")
        $ save_name = current_date(_("Arc 2"), current_day)
        show screen date_label with dissolve
        play music audio.light
        "Day shift with camp duties. Night shift with Lorenzo."
        show lorenzo smile:
            xpos 900
            yalign 1.0
            zoom 1.02
        show ast happy:
            xpos 300
            yalign 1.0
            zoom 1.02
        "Today, Lorenzo greets us at the door as opposed to curling up in the chair."
        voice "d16_InGood"
        mo "In good spirits today?"
        show lorenzo happy
        voice "d16_GettingBetter"
        lo "Getting better day by day. How are you Aston?"
        voice "d16_ItsBothering"
        ast "It's bothering me, but Morgan has been keeping me sane."

        "I kept an eye on him whilst doing our camp duties."
        "Occasionally, he'll pause what he's doing and look towards the forest."
        "Aston doesn't tell me what he hears or when, but he always looks to me for confirmation."
        "If I don't hear anything, then there's no cause for concern."
        "This is a system that we've set up."
        show ast neutral
        show lorenzo pondering
        voice "d16_IveStudied"
        lo "I've studied the thing a bit more."
        show lorenzo neutral
        voice "d16_AnOdd"
        lo "An odd question but, have you seen any animals that look like this?"

        "He points at his journal, to sketches of animals covered with black viscous substance."

        voice "d16_ItsFunny"
        mo "It's funny you say that, but yes I did. Birds, many dead birds."
        show lorenzo scared
        voice "d16_YYouDidnt"
        lo "Y-You didn't use your bare hands right?"
        voice "d16_TheCamp"
        mo "\"The Camp Guide's Guide\" said that I couldn't so I've got gear, don't worry."
        show lorenzo neutral
        voice "d16_OkayGood"
        lo "Okay good for you, amico. I didn't have gear when I saw what was in the icebox in the RC."
        voice "d16_WhatWas"
        ast "What was in it?"
        show lorenzo sick
        voice "d16_UnidentifiableMass"
        lo "Unidentifiable mass, but it looks exactly like the drawing and the bear that I'm dealing with."
        show ast inthought
        show lorenzo sad
        voice "d16_ThatWould"
        ast "That would mean you're patient 0, and that I most likely got it from you."

        show ast neutral:
            subpixel True
            zoom 1.02
            linear 0.20 zoom 1.02
        with Pause(0.30)
        show ast neutral:
            zoom 1.0

        show lorenzo sad:
            subpixel True
            zoom 1.02
            linear 0.20 zoom 1.02
        with Pause(0.30)
        show lorenzo sad:
            zoom 1.0

        "The two of them stared at me, and took a few steps back."
        voice "d16_JustFor"
        ast "Just for precaution, Morgan."

        "Aston and Lorenzo didn't have a bite. Kyle is an outlier."

        voice "d16_DoYou"
        mo "Do you think... Elliot had also been exposed the same way?"
        show ast inthought
        voice "d16_IWouldnt"
        ast "I wouldn't be surprised, he spent a lot of time at the RC. Eva and him were close."

        "Was Elliot trying to dig around at the RC?"
        "Something of importance must be happening there."
        "I wonder how the water-fungi testing is going."
        "Time to make a trip down there, but I can't show up uninvited."
        "I'll have to find a reason to."
        stop music fadeout 3.0


    #If Aston not safe
    else:
        scene bg camp2_day with longfade
        $ current_day = _("December 16th")
        $ save_name = current_date(_("Arc 2"), current_day)
        show screen date_label with dissolve
        play ambience amb_campday fadein 1.0
        "Aston has been missing for two days now."
        "C1 aborted the original dirt and photography mission."
        "Gregory said that we're doing round 2 of search and rescue."
        "Now there's 3 people on the missing persons list."
        "\"What happened to him?\""
        "\"Where is he?\""
        "\"Is he okay?\""
        "\"Was there something I could've done differently that night?\""
        "These are all the questions that circle my mind."
        "This is essentially another Elly situation."
        "But if I spent every waking hour worrying about him, I wouldn't be in the right headspace to deal with the actual threats."
        "To deal with whatever Heralign's can of worms is."
        "I have to put my feelings aside and focus on the mission."
        "Maybe it's a stubborn trait of mine, but I'm going to keep believing that he's okay."
        "Because Elly is well... Elly."
        "But with Aston, it's different."
        "I've seen it happen right in front of me."
        "I've seen him dealing with an infection that could drive him to literal madness."
        "And I've seen it manifest itself to Lorenzo."
        "I can't shake the thoughts I'm having."
        "And we still have not figured out how contagious it is."
        "With so many questions unanswered, the uncertainty kills me."
        show pearl sad
        voice "d16_HeyCan"
        pe "Hey, can you hear me?"
        "Pearl's voice brings me back."
        show pearl smile
        "With a concerned look on her face, she extends her arms out and offers a hug."
        "I accepted the hug and she gave me a few pats on the back."
        play sound hug
        show pearl neutral
        voice "d16_YouLooked"
        pe "You looked like you needed it Morgan."
        voice "d16_AndYoure"
        pe "And you're not alone here, we're all here with you."
        voice "d16_WeAre"
        pe "We are going to find them."
        show pearl smile
        voice "d16_AndThen"
        pe "And then I'm going to force feed Aston some greens for running away from camp like that."
        "The image of Pearl running after him with a can of pea soup is hilarious."
        show pearl happy
        "Seeing that her comment elicited a chuckle out of me, she nodded, satisfied with her work."
        stop ambience fadeout 3.0

label dec_17:
    scene bg forest3 with longfade
    $ current_day = _("December 17th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    play ambience amb_campday fadein 1.0

    #Kyle's POV
    show ky smile at centerleft
    show pearl smile at centerright
    "Kyle and Pearl paired up today to grab some pictures."
    play sound camera3
    "Click click click!"
    voice "d17_LetsSee"
    pe "Let's see squirrels, squirrels, squirrels...and one napping wolf!"
    show ky happy
    show pearl happy
    voice "d17_GoodEye"
    ky "Good eye, Pearl!"
    show pearl smile
    play sound camera3
    "Click click click!"
    show ky neutral
    "He looks down at his camera, proud of his shots."

    show ky happy
    voice "d17_LooksLike"
    ky "Looks like our harvest today is bountiful!"
    show pearl happy
    voice "d17_AwwYeah"
    pe "Aww yeah!"

    "All of a sudden, something caught Kyle's attention."
    show ky confused
    "An animal moving in his peripheral vision?"
    voice "d17_PearlIm"
    ky "Pearl, I'm gonna check out that tree."
    show pearl neutral
    voice "d17_OkayIll"
    pe "Okay! I'll be here."
    hide pearl

    "Kyle positions himself behind a large tree, peeking to observe the animal at a safe distance."
    "A large chunk of fur phases through the trees."
    "He approaches the animal with caution."

    show ky shaken
    voice "d17_OhShit"
    ky "Oh shit that's a bear."
    stop ambience fadeout 1.0
    play music audio.anxious fadein 3.0

    "The bear doesn't notice Kyle's presence."
    play sound camera1
    "Click!"
    show cg glitchedphoto
    "He checks his camera."
    "It's a tad blurry."
    hide cg

    show ky neutral
    voice "d17_LetMe"
    ky "Let me try that again."
    play sound camera1
    "Click!"
    "He checks his camera once again."
    "The bear isn't in the picture."
    show ky confused
    voice "d17_What"
    ky "What."

    "Seems like the bear was moving about and now it's clawing a tree."
    show ky neutral
    voice "d17_OkayThird"
    ky "Okay, third time's the charm!"
    play sound flash
    "Click!"

    show ky shaken
    voice "d17_Shit"
    ky "Shit."

    "The flash turned on."

    voice "d17_PleaseDont"
    ky "Please don't see me, please don't see me..."

    "Kyle breaks vision from the bear, hiding behind a large tree."
    play sound beargrowl
    "*growl*"
    voice "d17_KyleVNVR"
    ky "..."
    show pearl smile at centerright
    voice "d17_HeyaKyle"
    pe "Heya Kyle! How's the photo taking going?"
    voice "d17_PearlKeep"
    ky "Pearl! Keep it down. There's a bear behind this tree."
    voice "d17_ItWas"
    ky "It was growling."
    show pearl confused
    voice "d17_GGrowlingDont"
    pe "G-Growling? Don't pull my leg Kyle, why would a bear be out and about this time of the year?"
    voice "d17_ArentThey"
    pe "Aren't they hibernating?"
    show ky sad
    voice "d17_IHave"
    ky "I have pictures. Let's go back to camp and I'll show you."
    show pearl neutral
    voice "d17_IfYou"
    pe "If you saw a bear, I'll believe you! But you need to take a deep breath now, your breathing is ragged."

    "Pearl is right."
    "Kyle takes a few deep breaths and the two head back to camp."

    #EXT: Camp 1A
    show bg maintent_night
    show ky confused
    "Kyle flips through the camera's gallery once more."
    "There's a blurry shot."
    "One out of frame."
    "And the last one...distorted."
    show pearl smile
    voice "d17_OohWhat"
    pe "Ooh! What's this glitchy effect on this blob?"
    play sound camera1
    "Kyle takes another picture on the spot."
    "There's no distortion."
    show pearl confused
    voice "d17_IsIt"
    pe "Is it broken?"
    voice "d17_MyCameras"
    ky "My camera's fine, but my pictures are not."
    show ky neutral
    voice "d17_CouldYou"
    ky "Could you grab my laptop Pearl? I need backups of these before I lose 'em."
    show pearl smile
    voice "d17_OnIt"
    pe "On it!"
    stop music fadeout 3.0

label dec_18:
    #INT: Main tent
    #(TOGGLE) isa ev ko
    scene bg maintent_day with longfade
    $ current_day = _("December 18th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    play ambience amb_intcampday fadein 1.0
        #Kyle's POV
    show ky smile
    play sound beep
    "Kyle's Walkie starts beeping."
    "It's from Koda."
    #radio starts
    $ chibi_koda = "images/chibi/koda_happy.png"
    if radio_static == "_s":
        voice "d18_HiKyle_s"
    else:
        voice "d18_HiKyle_c"
    wt_ko "Hi Kyle! Is now a good time?"
    $ chibi_kyle = "images/chibi/kyle_happy.png"
    voice "d18_ImAll"
    wt_ky "I'm all ears!"
    $ chibi_eva = "images/chibi/eva_neutral.png"
    if radio_static == "_s":
        voice "d18_ItWould_s"
    else:
        voice "d18_ItWould_c"
    wt_ev "It would seem that most of the animals are okay."
    $ chibi_eva = "images/chibi/eva_worried.png"
    if radio_static == "_s":
        voice "d18_ButThere_s"
    else:
        voice "d18_ButThere_c"
    wt_ev "But there were two strange things you've encountered?"
    $ chibi_kyle = "images/chibi/kyle_worried.png"
    voice "d18_YeahThe"
    wt_ky "Yeah, the bird stuff and a bear."
    $ chibi_eva = "images/chibi/eva_neutral.png"
    if radio_static == "_s":
        voice "d18_YouSaw_s"
    else:
        voice "d18_YouSaw_c"
    wt_ev "You saw a bear? Sure it wasn't something else?"
    $ chibi_koda = "images/chibi/koda_worried.png"
    if radio_static == "_s":
        voice "d18_WouldntThey_s"
    else:
        voice "d18_WouldntThey_c"
    wt_ko "Wouldn't they be hibernating?"
    voice "d18_ThatsWhat"
    wt_ky "That's what Pearl has been saying... But I am convinced that I saw one."
    $ chibi_kyle = "images/chibi/kyle_neutral.png"
    voice "d18_IfThere"
    wt_ky "If there really was one, I'll try snagging pictures again."
    if radio_static == "_s":
        voice "d18_SafetysFirst_s"
    else:
        voice "d18_SafetysFirst_c"
    wt_ko "Safety's first, Kyle! Don't end up on the headlines."
    $ chibi_kyle = "images/chibi/kyle_happy.png"
    voice "d18_IAm"
    wt_ky "I am a professional, don't you worry, Koda!"
    if radio_static == "_s":
        voice "d18_AndThe_s"
    else:
        voice "d18_AndThe_c"
    wt_is "And the bird pictures... Those were the same ones like the one that Morgan picked up, yes?"
    $ chibi_kyle = "images/chibi/kyle_neutral.png"
    voice "d18_OhHey"
    wt_ky "Oh hey, Isaak! And yes."
    if radio_static == "_s":
        voice "d18_HowMany_s"
    else:
        voice "d18_HowMany_c"
    wt_is "How many birds were there?"
    $ chibi_kyle = "images/chibi/kyle_worried.png"
    voice "d18_About8"
    wt_ky "About 8 to 10? Have you guys found out why this is happening?"
    if radio_static == "_s":
        voice "d18_NoWe_s"
    else:
        voice "d18_NoWe_c"
    wt_is "No. We haven't got an inkling."
    voice "d18_AndIts"
    wt_ky "And its appearance? The globby slimy icky stuff?"
    if radio_static == "_s":
        voice "d18_SameAnswer_s"
    else:
        voice "d18_SameAnswer_c"
    wt_is "Same answer."
    voice "d18_DoYou"
    wt_ky "Do you think it has something to do with the water?"
    if radio_static == "_s":
        voice "d18_IsaakVNVR_s"
    else:
        voice "d18_IsaakVNVR_c"
    wt_is "..."
    if radio_static == "_s":
        voice "d18_UUhWe_s"
    else:
        voice "d18_UUhWe_c"
    wt_ko "U-Uh, we don't know just yet, but we'll let you know when we do!"
    voice "d18_SorrySorry"
    wt_ky "Sorry, sorry. Just want to make sure that we're all safe while we're out there."
    $ chibi_eva = "images/chibi/eva_happy.png"
    if radio_static == "_s":
        voice "d18_AnywayThanks_s"
    else:
        voice "d18_AnywayThanks_c"
    wt_ev "Anyway, thanks Kyle. Really great shots by the way, stunning photos."
    $ chibi_kyle = "images/chibi/kyle_happy.png"
    voice "d18_ITake"
    wt_ky "I take pride in that! Thank you!"
    stop ambience fadeout 3.0
    stop music fadeout 3.0
    #radio ends
    nvl clear
    scene black with longfade
    jump dec_19

label dec_20:
#20th Aston safe

    play music audio.light
    scene bg camp2_day with longfade
    $ current_day = _("December 20th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    if aston_safe:
        "While enjoying a cup of cocoa by myself, I received a Walkie beep from Wilbur."
        play sound beep
        #radio start
        #(TOGGLE) wi ru

        if radio_static == "_s":
            voice "d20_br1_HelloMorgan_s"
        else:
            voice "d20_br1_HelloMorgan_c"
        wt_wi "Hello, Morgan! Are you there?"
        $ chibi_morgan = "images/chibi/morgan_neutral.png"
        voice "d20_WhatsUp"
        wt_mo "What's up?"
        $ chibi_ruran = "images/chibi/ruran_worried.png"
        if radio_static == "_s":
            voice "d20_HowIs_s"
        else:
            voice "d20_HowIs_c"
        wt_ru "How is Aston?"
        $ chibi_morgan = "images/chibi/morgan_worried.png"
        voice "d20_HesHanging"
        wt_mo "He's hanging in there, I think. I'm looking out for him, don't worry."
        if radio_static == "_s":
            voice "d20_AstonIs_s"
        else:
            voice "d20_AstonIs_c"
        wt_ru "Aston is strong... Perhaps too strong. He takes on everything and bottles up his own emotions."
        if radio_static == "_s":
            voice "d20_LorenzoIs_s"
        else:
            voice "d20_LorenzoIs_c"
        wt_ru "Lorenzo is the only person who he confides with, and with him missing..."
        $ chibi_wilbur = "images/chibi/wilbur_worried.png"
        if radio_static == "_s":
            voice "d20_KeepAn_s"
        else:
            voice "d20_KeepAn_c"
        wt_wi "Keep an eye on him will you, son? He needs all the support he can get."
        $ chibi_morgan = "images/chibi/morgan_neutral.png"
        voice "d20_OfCourse"
        wt_mo "Of course."
        #radio ends
        nvl clear
        "I look towards Aston who's taking a quick nap in the corner of the tent."
        "He'll be okay under my watch."

    #20th Aston not safe
    #EXT: Camp 1A
    else:
        "While enjoying a cup of cocoa by myself, I received a quick Walkie beep from Wilbur."
        play sound beep
        #radio start
        $ chibi_wilbur = "images/chibi/wilbur_worried.png"
        if radio_static == "_s":
            voice "d20_br2_HelloMorgan_s"
        else:
            voice "d20_br2_HelloMorgan_c"
        wt_wi "Hello, Morgan! Are you there?"
        $ chibi_morgan = "images/chibi/morgan_neutral.png"
        voice "d20_WhatsUp"
        wt_mo "What's up?"
        $ chibi_ruran = "images/chibi/ruran_worried.png"
        if radio_static == "_s":
            voice "d20_AnyUpdates_s"
        else:
            voice "d20_AnyUpdates_c"
        wt_ru "Any updates on Aston?"
        $ chibi_morgan = "images/chibi/morgan_worried.png"
        voice "d20_AstonHasnt"
        wt_mo "Aston... Hasn't come back."
        if radio_static == "_s":
            voice "d20_SoTheres_s"
        else:
            voice "d20_SoTheres_c"
        wt_ru "So there's no sign of both of them yet..."
        $ chibi_wilbur = "images/chibi/wilbur_worried.png"
        if radio_static == "_s":
            voice "d20_KeepUs_s"
        else:
            voice "d20_KeepUs_c"
        wt_wi "Keep us updated will you, son? Let us know if you've seen them."
        $ chibi_morgan = "images/chibi/morgan_neutral.png"
        voice "d20_OfCourse"
        wt_mo "Of course."
        #radio ends
        nvl clear
        "I look towards the empty corner of the tent."
        "I'm sorry, Lorenzo."

label dec_21:
    scene bg maintent_day with longfade
    $ current_day = _("December 21st")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    #INT: Main tent
    show ky confused
    "Kyle is looking through his camera gallery."
    show ky smile
    voice "d21_HmmmOh"
    ky "Hmmm... Oh, Morgan! Hello!"
    "He notices me walking into the tent."
    voice "d21_CanI"
    ky "Can I get your opinion on something?"
    "He tilts the camera towards me."
    show cg glitchedphoto

    "I don't...like what I am seeing here."
    voice "d21_WeirdHuh"
    ky "Weird, huh? My camera glitched out on this photo."
    voice "d21_ThatLooks"
    mo "That looks like a bear, no?"
    voice "d21_IMean"
    ky "I mean, yeah, I saw it with my eyeballs."
    show ky sad
    voice "d21_ButIt"
    ky "But it looked nothing like the picture here."
    hide cg
    "I touched Kyle's forehead to feel his temperature."
    show ky happy
    voice "d21_NoFever"
    ky "No fever!"
    "I'm not sure if Kyle is infected."
    show ky neutral
    "But I can't cross out the chance that he might be hallucinating as well."
    "Another bear of all things."
    "Hibernation doesn't seem like a popular activity here."
    voice "d21_CouldI"
    mo "Could I get a copy of that?"
    show ky smile
    voice "d21_AbsolutelyGive"
    ky "Absolutely, give me just a moment!"
    "Great, another delivery for Colin."

label dec_22:
    #EXT: Camp 1A
    scene bg maintent_day with longfade
    $ current_day = _("December 22nd")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    show pearl confused
    "Pearl seems frantic today."
    "Searching high and low for something... Her compass, maybe?"

    voice "d22_SearchingFor"
    mo "Searching for your compass again, Pearl?"
    show pearl sad
    voice "d22_Yep"
    pe "Yep."

    "I'll help her look around then."
    hide pearl
    show bg camp2_day
    "I circled around the campsite."
    "Looks like it isn't behind our tents."
    "I circled around our campfire."
    "There's just our crock pot."
    "..."
    "You know what, I should just have a look anyway."
    "What?"
    "Did she actually put her compass in here?"
    show pearl neutral
    voice "d22_PearlI"
    mo "Pearl? I found it, but...why was it in the crock pot?"
    show pearl confused
    voice "d22_WhatReally"
    pe "What, really? That's pretty odd, but thanks Morgan!"
    hide pearl
    "She took her compass from my hands and ran off into the main tent."
    "Is it just me, or does Pearl seem off today?"

label dec_23:
    #(TOGGLE) ko da
    scene bg maintent_day with longfade
    $ current_day = _("December 23rd")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    #INT: Main tent
    show pearl smile
    voice "d23_PearlAre"
    da "Pearl? Are you okay?"
    show pearl neutral
    voice "d23_ImGood"
    pe "I'm good! Think I've been feeling a lot more tired these days."
    if radio_static == "_s":
        voice "d23_DavosHike2Hours_s"
    else:
        voice "d23_DavosHike2Hours_c"
    da "Don't make me hike 2 hours to get to you. You know that I will!"
    if radio_static == "_s":
        voice "d23_KodaHike4Hours_s"
    else:
        voice "d23_KodaHike4Hours_c"
    ko "Don't make me hike 4 hours to get to you... You know I'm not fit to do that."
    show pearl smile
    voice "d23_ISwear"
    pe "I swear that I'm fine, guys!"

    "I walked into a conversation that the trio were having."
    "She says that she's fine. I genuinely hope so."

label dec_24:
    $ current_day = _("December 24th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    #24th Aston safe
    if aston_safe:
        scene cottage2 with longfade
        "Aston heads over to the cottage again, this time without Morgan."
        "Lorenzo and Aston spend their evening chatting away over a packet of instant meat and potatoes."
        "And when it was almost time to sleep, Aston routinely brought the blankets over to the armchair."
        #CG: Aston and Lorenzo cuddling
        show cg christmas
        $ persistent.gallery_christmas = True
        play sound snuggle
        "The two cuddle up together on the armchair."
        "It just barely fits the two of them."
        "As the clock struck midnight, it was finally time."

        voice "d24_HappyChristmas"
        ast "Happy Christmas, love."
        voice "d24_br1_BuonNatale"
        lo "Buon Natale, amore."

        "If one goes down, the other shall follow. This has always been the case for them."
        "They'll stick together through thick and thin."
        "And there's nothing in the world that will stop them from celebrating their favorite time of the year, together."

    #24th Aston not safe
    else:
        scene bg cottage2 with longfade
        show lorenzo sad
        "Lorenzo stares longingly out the window."
        "Gentle specks of white falling to the ground."
        "But there was still no sign of Aston."
        show lorenzo sick
        play sound cloth
        "He hugs his legs close to his chest."
        show black
        show ast happy:
            zoom 2.0
            xalign 0.5
        "Eyes closed, Aston's face flashes by."
        voice "d24_br2_BuonNatale"
        lo "Buon Natale, amore."
        voice "d24_IMiss"
        lo "I miss you."

        hide black
        hide lorenzo
        hide ast

        "If one goes down, the other shall follow. This has always been the case for them."
        "But it would seem that for the first time, Lorenzo was truly alone."
        "Christmas just isn't the same without your beloved."
    stop music fadeout 1.0

label dec_25:
    scene bg camp2_day with longfade
    $ current_day = _("December 25th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    play music audio.xmas
    "Christmas."
    "This year, everything's different."
    "An unfamiliar place, with unfamiliar faces."
    "The comfort of my home seems like a distant memory now."
    "Last year, Elly and I attempted to make a rotisserie chicken in his oven."
    "Didn't go well."
    "We drank a bit too much too early and passed out in the living room while it was cooking."
    "We woke up two hours after it was supposed to be done."
    "The smell was foul."
    "Not only did we not have dinner, we had a busted oven with a depressing-looking chicken."
    "Perhaps we should do it again next Christmas for old time's sake."
    "If only this dumbass would show up soon."
    "Oh well, I shall try to make the most of it right now."
    "I should beep everyone today."
    #(TOGGLE) yes
    menu christmas:
        "Beep Wilbur":
            if not christmas_wi:
                $ christmas_wi = True
                $ chibi_morgan = "images/chibi/morgan_happy.png"
                voice "d25_MerryChristmasWilbur"
                wt_mo "Merry Christmas, Wilbur!"
                $ chibi_wilbur = "images/chibi/wilbur_happy.png"
                if radio_static == "_s":
                    voice "d25_MorganThank_s"
                else:
                    voice "d25_MorganThank_c"
                wt_wi "Morgan! Thank you and Merry Christmas to you too!"
                $ chibi_wilbur = "images/chibi/wilbur_neutral.png"
                if radio_static == "_s":
                    voice "d25_MakeSure_s"
                else:
                    voice "d25_MakeSure_c"
                wt_wi "Make sure to have a great feast today and call your family, yes?"
                $ chibi_morgan = "images/chibi/morgan_neutral.png"
                voice "d25_YouBet"
                wt_mo "You bet I will."
                nvl clear
            else:
                "I've already talked to him."

        "Beep Ruran":
            if not christmas_ru:
                $ christmas_ru = True
                $ chibi_morgan = "images/chibi/morgan_happy.png"
                voice "d25_MerryChristmasRuran"
                wt_mo "Merry Christmas, Ruran!"
                $ chibi_ruran = "images/chibi/ruran_happy.png"
                if radio_static == "_s":
                    voice "d25_MerryChristmasFromRuran_s"
                else:
                    voice "d25_MerryChristmasFromRuran_c"
                wt_ru "Merry Christmas to you too, Morgan!"
                if radio_static == "_s":
                    voice "d25_IHopeThatYour_s"
                else:
                    voice "d25_IHopeThatYour_c"
                wt_ru "I hope that your wishes come true."
                $ chibi_morgan = "images/chibi/morgan_neutral.png"
                voice "d25_LikewiseTo"
                wt_mo "Likewise to you, Ruran."
                nvl clear
            else:
                "I've already talked to her."

        "Beep Davos":
            if not christmas_da:
                $ christmas_da = True
                $ chibi_morgan = "images/chibi/morgan_happy.png"
                voice "d25_DavosMerry"
                wt_mo "Davos! Merry Christmas!"
                $ chibi_davos = "images/chibi/davos_neutral.png"
                if radio_static == "_s":
                    voice "d25_MerryChristmasFromDavos_s"
                else:
                    voice "d25_MerryChristmasFromDavos_c"
                wt_da "Merry Christmas Morgan! I heard the moon's going to be bright tonight!"
                $ chibi_davos = "images/chibi/davos_happy.png"
                if radio_static == "_s":
                    voice "d25_YouWouldnt_s"
                else:
                    voice "d25_YouWouldnt_c"
                wt_da "You wouldn't want to miss out on that!"
                $ chibi_morgan = "images/chibi/morgan_neutral.png"
                voice "d25_ThatSounds"
                wt_mo "That sounds lovely, I'll be sure to look up tonight."
                nvl clear
            else:
                "I've already talked to him."

        "Beep Cassie":
            if not christmas_ca:
                $ christmas_ca = True
                $ chibi_morgan = "images/chibi/morgan_happy.png"
                voice "d25_MerryChristmasCassie"
                wt_mo "Merry Christmas, Cassie!"
                $ chibi_cassie = "images/chibi/cassie_happy.png"
                if radio_static == "_s":
                    voice "d25_AwwThank_s"
                else:
                    voice "d25_AwwThank_c"
                wt_ca "Aww, thank you, Morgan! Merry Christmas to you too!"
                $ chibi_morgan = "images/chibi/morgan_neutral.png"
                voice "d25_IHopeYourAnkle"
                wt_mo "I hope your ankle has been healing well."
                $ chibi_cassie = "images/chibi/cassie_neutral.png"
                if radio_static == "_s":
                    voice "d25_ThankfullyIt_s"
                else:
                    voice "d25_ThankfullyIt_c"
                wt_ca "Thankfully it has! Give it another week or two, and I'll be up and running!"
                $ chibi_morgan = "images/chibi/morgan_happy.png"
                voice "d25_ItsA"
                wt_mo "It's a Christmas miracle!"
                $ chibi_cassie = "images/chibi/cassie_happy.png"
                if radio_static == "_s":
                    voice "d25_YoureSo_s"
                else:
                    voice "d25_YoureSo_c"
                wt_ca "You're so right."
                nvl clear
            else:
                "I've already talked to her."

        "Beep Jax":
            if not christmas_ja:
                $ christmas_ja = True
                $ chibi_morgan = "images/chibi/morgan_happy.png"
                voice "d25_MerryChristmas"
                wt_mo "Merry Christmas!"
                $ chibi_jax = "images/chibi/jax_neutral.png"
                if radio_static == "_s":
                    voice "d25_AndMerry_s"
                else:
                    voice "d25_AndMerry_c"
                wt_ja "And Merry Christmas to you!"
                $ chibi_morgan = "images/chibi/morgan_neutral.png"
                voice "d25_HowsChristmas"
                wt_mo "How's Christmas for you so far?"
                $ chibi_jax = "images/chibi/jax_happy.png"
                if radio_static == "_s":
                    voice "d25_ISlept_s"
                else:
                    voice "d25_ISlept_c"
                wt_ja "I slept in today, so now I'm all refreshed."
                $ chibi_morgan = "images/chibi/morgan_happy.png"
                voice "d25_NothingBeats"
                wt_mo "Nothing beats those extra hours of sleep."
                "Nice, Jax and I are like-minded in that regard."
                nvl clear
            else:
                "I've already talked to him."

        "Beep Koda":
            if not christmas_ko:
                $ christmas_ko = True
                $ chibi_morgan = "images/chibi/morgan_happy.png"
                voice "d25_HeyKoda"
                wt_mo "Hey Koda! Merry Christmas!"
                $ chibi_koda = "images/chibi/koda_happy.png"
                if radio_static == "_s":
                    voice "d25_MorganMerry_s"
                else:
                    voice "d25_MorganMerry_c"
                wt_ko "Morgan! Merry Christmas! I hope your day has been great!"
                $ chibi_morgan = "images/chibi/morgan_neutral.png"
                voice "d25_ItHas"
                wt_mo "It has been, yes. Hope you're taking time off to actually relax!"
                $ chibi_koda = "images/chibi/koda_neutral.png"
                if radio_static == "_s":
                    voice "d25_EvaKicked_s"
                else:
                    voice "d25_EvaKicked_c"
                wt_ko "Eva kicked me out of the lab today just for that reason!"
                $ chibi_koda = "images/chibi/koda_happy.png"
                if radio_static == "_s":
                    voice "d25_TimeFor_s"
                else:
                    voice "d25_TimeFor_c"
                wt_ko "Time for some well earned rest!"
                nvl clear
            else:
                "I've already talked to them."

        "Beep Eva":
            if not christmas_ev:
                $ christmas_ev = True
                $ chibi_morgan = "images/chibi/morgan_happy.png"
                voice "d25_MerryChristmasEva"
                wt_mo "Merry Christmas, Eva!"
                $ chibi_eva = "images/chibi/eva_happy.png"
                if radio_static == "_s":
                    voice "d25_ThanksMerry_s"
                else:
                    voice "d25_ThanksMerry_c"
                wt_ev "Thanks! Merry Christmas to you too, Morgan."
                $ chibi_eva = "images/chibi/eva_neutral.png"
                if radio_static == "_s":
                    voice "d25_IHopeYouPrepared_s"
                else:
                    voice "d25_IHopeYouPrepared_c"
                wt_ev "I hope you prepared presents."
                $ chibi_morgan = "images/chibi/morgan_worried.png"
                voice "d25_OhI"
                wt_mo "Oh, I didn't."
                $ chibi_eva = "images/chibi/eva_happy.png"
                if radio_static == "_s":
                    voice "d25_ReallyThats_s"
                else:
                    voice "d25_ReallyThats_c"
                wt_ev "Really? That's a shame."
                voice "d25_WellWheres"
                wt_mo "Well where's mine, then?"
                "Eva just doesn't respond after that."
                "No presents then, I guess."
                nvl clear
            else:
                "I've already talked to her."

        "Beep Isaak":
            if not christmas_is:
                $ christmas_is = True
                if radio_static == "_s":
                    voice "d25_Hello_s"
                else:
                    voice "d25_Hello_c"
                wt_is "Hello?!"
                $ chibi_morgan = "images/chibi/morgan_worried.png"
                voice "d25_MerryChristmasIsaak"
                wt_mo "Merry Christmas... Isaak?"
                if radio_static == "_s":
                    voice "d25_OhIts_s"
                else:
                    voice "d25_OhIts_c"
                wt_is "Oh, it's you."
                if radio_static == "_s":
                    voice "d25_MerryChristmasFromIsaak_s"
                else:
                    voice "d25_MerryChristmasFromIsaak_c"
                wt_is "Merry Christmas to you too, Morgan."
                "I think he might've been expecting someone else."
                nvl clear
            else:
                "I've already talked to him."

        "Beep Lorenzo":
            if not christmas_lo:
                $ christmas_lo = True
                if aston_safe:
                    $ chibi_morgan = "images/chibi/morgan_neutral.png"
                    voice "d25_MerryChristmasLorenzo"
                    wt_mo "Merry Christmas, Lorenzo."
                    "He won't respond because it's daytime, but I know that he can hear me, and that's all that matters."
                else:
                    $ chibi_morgan = "images/chibi/morgan_worried.png"
                    voice "d25_MerryChristmasLorenzo"
                    wt_mo "Merry Christmas, Lorenzo."
                    "I'll bring Aston back to you."
                nvl clear
            else:
                "I've already talked to him."

        #Everyone has to be beeped once, and if you're done
    if christmas_wi and christmas_ca and christmas_da and christmas_ev and christmas_is and christmas_ja and christmas_ko and christmas_lo and christmas_ru:
        "Looks like that's everyone. Might as well call Colin, too!"
    else:
        jump christmas

    #radio ends
    #TODO phone starts
    show satphone
    voice "d25_MerryChristmasToMy"
    mo "Merry Christmas to my lovely Pancake!"
    if radio_static == "_s":
        voice "d25_MerryChristmasMorg_s"
    else:
        voice "d25_MerryChristmasMorg_c"
    co "Merry Christmas Morg!"
    voice "d25_SoAbout"
    mo "So about the snowmobi-"
    if radio_static == "_s":
        voice "d25_No_s"
    else:
        voice "d25_No_c"
    co "No."
    if radio_static == "_s":
        voice "d25_IllGet_s"
    else:
        voice "d25_IllGet_c"
    co "I'll get you something else when you're back."
    voice "d25_OohA"
    mo "Ooh, a surprise gift from Pancake? I'll take that."
    hide satphone
    #phone ends
    "I wonder what he meant by that, now he's got me curious."
    "Oh well, time for my fellow camp mates."

    #INT: Main tent
    scene bg maintent_day with dissolve
    voice "d25_MerryChristmasEveryone"
    mo "Merry Christmas everyone!"
    show gr neutral at left
    voice "d25_MerryChristmasYoureDone"
    gr "Merry Christmas. You're done with the calls?"

    "I gave a light nod to Gregory."

    show ky happy at right
    show pearl happy at centerright
    voice "d25_MerryChristmasFromKyle"
    ky "Merry Christmas Morgan!"
    voice "d25_MerryChristmasFromPearl"
    pe "Merry Christmas Morgan!"

    "These two, I swear. They really do share the same brain cells."

    #IF Aston not safe skip the lines below
    if aston_safe:
        show ast happy at centerleft
        voice "d25_HappyChristmas"
        ast "Happy Christmas Morgan."
        "And Aston here balances out the energies."

    hide gr
    hide ast
    hide ky
    hide pearl
    "They resumed their preparations for lunch."
    "Looks like we're having two different soup flavors today."
    "Heh... Like a Christmas tree, red and green."
    "Alright, now there's just one final person."
    "I take a deep breath."
    voice "d25_MerryChristmasElly"
    mo "Merry Christmas, Elly."
    stop music fadeout 3.0

label dec_26:
    scene bg camp2_day with longfade
    $ current_day = _("December 26th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    play music audio.neutral

    "Ah yes, it's time for my favorite hobby."
    "Tormenting my beloved 37 year old child."
    "But first, I should send him some pictures."
    "And... Sent!"
    play sound ding
    #TODO phone start
    #(TOGGLE) co
    show satphone
    if radio_static == "_s":
        voice "d26_HeyaMorg_s"
    else:
        voice "d26_HeyaMorg_c"
    co "Heya Morg, calling again so soon?"
    voice "d26_PancakeIve"
    mo "Pancake! I've missed you, and I feel like I haven't gotten you up to speed yet."
    if radio_static == "_s":
        voice "d26_WowThats_s"
    else:
        voice "d26_WowThats_c"
    co "Wow, that's sweet. So what's good, Morg?"
    voice "d26_BigThings"
    mo "Big things happened, lots of new discoveries over the past week. Did you see the goods?"
    if radio_static == "_s":
        voice "d26_ImLooking_s"
    else:
        voice "d26_ImLooking_c"
    co "I'm looking at a handwritten list and a glitched out picture, what's the deal with 'em?"
    voice "d26_ListContains"
    mo "List contains Lorenzo's observations. The bear he's hallucinating about."
    voice "d26_WereDealing"
    mo "We're dealing with more than just physical symptoms now."
    if radio_static == "_s":
        voice "d26_YoureSaying_s"
    else:
        voice "d26_YoureSaying_c"
    co "You're saying that it's both visual and auditory shit?"
    voice "d26_YeahAnd"
    mo "Yeah, and I have a feeling that Kyle almost caught it on camera."
    voice "d26_IDoubt"
    mo "I doubt he'd lie about seeing a bear, but it is weird that that's the only thing that's distorted in the photo."
    if radio_static == "_s":
        voice "d26_HmmmThink_s"
    else:
        voice "d26_HmmmThink_c"
    co "Hmmm... Think I'll have to consult my doctors to see if there's a possibility."
    voice "d26_IDo"
    mo "I do have some bad news though. Aston is also infected."
    voice "d26_AndIm"
    mo "And I'm pretty sure that he hears things that I don't."

    if not aston_safe:
        voice "d26_HeWent"
        mo "He went missing a day after our last update and hasn't come back since..."
        voice "d26_IIWas"
        mo "I... I was there and I should've stopped him from running off, but my flashlight died and-"
        if radio_static == "_s":
            voice "d26_Morgan_s"
        else:
            voice "d26_Morgan_c"
        co "Morgan."
        #TODO voice "" missing VNVR
        mo "..."
        if radio_static == "_s":
            voice "d26_ChinUp_s"
        else:
            voice "d26_ChinUp_c"
        co "Chin up, Morg. If he's missing, you do whatever you can to find them."
        voice "d26_Mmhmm"
        mo "Mmhmm."
    if radio_static == "_s":
        voice "d26_OkayAnd_s"
    else:
        voice "d26_OkayAnd_c"
    co "Okay, and what about Elly? Do you think it's also related?"
    voice "d26_ItMay"
    mo "It may very well be the same thing, yes."
    if radio_static == "_s":
        voice "d26_SorryMorg_s"
    else:
        voice "d26_SorryMorg_c"
    co "Sorry Morg, you're cutting off."
    voice "d26_HelloCan"
    mo "Hello? Can you- Can you hear me?"
    if radio_static == "_s":
        voice "d26_TheresSomething_s"
    else:
        voice "d26_TheresSomething_c"
    co "There's something wrong with your line."
    voice "d26_Pancake"
    mo "Pancake?"
    hide satphone
    #phone ends
    "The phone call disconnects."
    "Weak signal? Never had this issue before."
    "I called him once more."
    "Looks like it's not going through. Guess I'll try again another time."
    stop music fadeout 3.0

label dec_27:
    scene bg maintent_night with longfade
    $ current_day = _("December 27th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    play ambience amb_intcampnight fadein 1.0
    play sound backpack
    "In the dead of the night, I heard someone rummaging through their backpacks."

    if aston_safe:
        "That's not Aston I'm hearing. He's usually very quiet about it."

    show pearl neutral
    "I sat up to see Pearl frantically packing her gear."
    voice "d27_PearlWhat"
    mo "Pearl, what are you doing?"
    show pearl smile
    voice "d27_MorganI"
    pe "Morgan! I, uh...couldn't sleep at all."
    voice "d27_AndThe"
    mo "...and the gear?"
    show pearl sad
    voice "d27_FineYou"
    pe "...Fine, you caught me...but don't tell the others."
    show pearl neutral

    if aston_safe:
        voice "d27_ImGoingToFindLorenzo"
        pe "I'm going to find Lorenzo."
    else:
        voice "d27_ImGoingToFindThem"
        pe "I'm going to find them."

    #choice branch
    if aston_safe:
        menu:
            "Let's think about it for a second":
                $ pearl_safe = True
                #aka the treat her like a sensible adult route, tell her that's not possible
                voice "d27_PearlNoThinkAbout"
                mo "Pearl, no. Think about it for a second."
                show pearl sad
                voice "d27_ItsCold"
                mo "It's cold, dark and you could get mauled by an animal. I can't let that happen to you."

            "It's dangerous, you won't survive the cold":
                $ pearl_safe = True
                #aka the treat her like a child route, tell her that it won't work and that you don't want her walking out by herself
                voice "d27_PearlNoYouWont"
                mo "Pearl, no. You won't survive out there."
                show pearl sad
                voice "d27_br1_HowAre"
                mo "How are you going to find Lorenzo if you don't even know where to begin searching? It's reckless."
        #choice branch ends
        voice "d27_br1_ImNotGonnaJust"
        pe "I'm not gonna just stay here, I need to do something."
        voice "d27_br1_OneDay"
        pe "One day the search for Lorenzo happens, then it ends abruptly."
        show pearl depressed
        voice "d27_br1_ImNotGoingTo"
        pe "I'm not going to wait till more of us go missing. I can't take it."

        show ast neutral at right
        "Aston wakes up and tries to get a hold of the situation."
        "He gives her a quick pat on the head."
        show ast sad
        show pearl sad
        voice "d27_PearlIts"
        ast "Pearl, it's gonna be okay. You just have to trust us."
        voice "d27_br1_PearlYou"
        mo "Pearl, you are brave and kind, and I know you want to help."
        show pearl depressed
        #voice "" missing VNVR
        pe "..."
        "Tears welled up in her eyes."
        voice "d27_IWish"
        pe "I wish I could do more."
        show ast neutral
        voice "d27_br1_YoureDoing"
        ast "You're doing enough Pearl. Let's go back to sleep okay?"
        stop ambience fadeout 1.0

    #If Aston not safe
    else:
        menu:
            "Let's think about it for a second":
                $ pearl_safe = True
                voice "d27_PearlNoThinkAbout"
                mo "Pearl, no. Think about it for a second."
                show pearl sad
                voice "d27_ItsCold"
                mo "It's cold, dark and you could get mauled by an animal. I can't let that happen to you."
                voice "d27_br2_ImNotGonnaJust"
                pe "I'm not gonna just stay here, I need to do something."
                show pearl depressed
                voice "d27_br2_OneDay"
                pe "One day the search for Lorenzo happens, then it ends abruptly."
                voice "d27_AndNow"
                pe "And now it's happening to Aston."
                voice "d27_br2_ImNotGoingTo"
                pe "I'm not going to wait till more of us go missing. I can't take it."

            "It's dangerous, you won't survive the cold":
            #aka the treat her like a child route, tell her that it won't work and that you don't want her walking out by herself
                voice "d27_PearlNoYouWont"
                mo "Pearl, no. You won't survive out there."
                show pearl sad
                voice "d27_br2_HowAre"
                mo "How are you going to find them if you don't even know where to begin searching? It's reckless."
                
                #straight to pearldeath
        #choice branch ends

    #Pearl survives (BRANCH FLAGGED) is this pearl safe aston safe chunk redundant or am I crazy?
        if pearl_safe:
            #If Aston is safe
            if aston_safe:
                voice "d27_br1_PearlYou"
                mo "Pearl, you are brave and kind, and I know you want to help."
                show pearl sad
                #voice "" missing VNVR
                pe "..."
                "Tears welled up in her eyes."
                voice "d27_IWish"
                pe "I wish I could do more."
                voice "d27_br1_YoureDoing"
                ast "You're doing enough Pearl. Let's go back to sleep okay?"
                stop ambience fadeout 1.0


        #If Aston is not safe
            else:
                show pearl sad
                voice "d27_br2_PearlYou"
                mo "Pearl, you are brave and kind, and I know you want to help."
                show pearl depressed
                #voice "" missing VNVR
                pe "..."
                "Tears welled up in her eyes."
                voice "d27_IWish"
                pe "I wish I could do more."
                voice "d27_br2_YoureDoing"
                mo "You're doing enough, but right now you need to get some sleep."
                stop ambience fadeout 1.0


        #Pearl's dead end
        else:
            show pearl confused
            voice "d27_BeingCalculative"
            pe "Being calculative hasn't brought anywhere has it now, Morgan?"
            show pearl depressed
            voice "d27_EveryoneThinks"
            pe "Everyone thinks I'm reckless when I'm just trying to help..."
            voice "d27_ThatsNot"
            mo "That's not what I me-"
            show gr confused at right
            voice "d27_WheresThis"
            gr "Where's this attitude coming from?"
            show ky confused at left
            voice "d27_PearlWhats"
            ky "Pearl? What's happening?"

            "Gregory and Kyle have been awoken by the sound."

            show pearl sad with move:
                subpixel True
                zoom 0.99
                parallel:
                    xpos 900
            voice "d27_NoYou"
            pe "No you stay away. I'll prove you wrong."

            "Shit, not again."
            show pearl neutral with move:
                xpos -300
            with Pause(0.1)
            hide pearl with sdissolve
            show ky shaken
            play sound toolrack
            "With a swift movement, she knocks over the tool rack blocking the flap of the tent."

            show gr angry with move:
                linear 0.3 xpos 1700
            voice "d27_PearlGet"
            gr "Pearl! Get back here this instant!"

            "Crap, she forgot her compass."
            "Kyle rushes to move the rack out the way while we quickly gear up."
            stop ambience fadeout 3.0

            #EXT: Camp 1
            scene bg camp2_night with dissolve
            play ambience amb_campnight fadein 1.0
            show ky shaken at centerleft
            voice "d27_PearlWhere"
            ky "Pearl! Where are you?"
            show gr angry at centerright
            voice "d27_ThisIs"
            gr "This is not a fucking game Pearl, come back now!"
            "This is all my fault."
            "If anything happens to her, I-"
            "...I won't be able to forgive myself."


            #Scene transition: Fade to black > Fade in forest BG
            scene bg forest3 with longfade

            #Pearl's POV
            show pearl neutral
            play sound wind2
            "The wind picks up tremendously as Pearl trudges through the snow."

            show pearl sad
            voice "d27_UghI"
            pe "Ugh... I knew I should've checked my pockets. Now I'm out here lost and without my compass."
            voice "d27_AndHere"
            pe "And here I thought circling the base of the mountain was a great idea."
            #I can ANIMATE THIS (RUMI)
            voice "d27_ILook"
            pe "I look left? Trees and snow. Look right? Trees and snow. Look straight ahead and oh wow! Trees and snow."
            show pearl depressed
            voice "d27_TheSnow"
            pe "The snow is...unrelenting too. It's cold."
            show pearl neutral
            voice "d27_ComeOn"
            pe "Come on Pearl! Focus focus!"
            stop ambience fadeout 1.0
            play ambience amb_icebody fadein 5.0

            show cg pearldeath
            $ persistent.gallery_pearldeath = True
            "Pearl finds herself in front of a large forest clearing. Oddly shaped stones stick out from the ground in a disorderly manner."
            "She walks up to one and inspects it up close."

            voice "d27_OhYeah"
            pe "Oh yeah that's stone alrig-"
            voice "d27_PearlVNVR2"
            pe "..."

            "It was in fact not stone."
            "Or at least to Pearl."
            "Disfigured and grotesque looking...humans."
            "Frozen in time, freezing the frame of their unfortunate fate."
            play sound snowground
            "Pearl collapses onto the ground, unable to make sense of what she just saw."

            voice "d27_NopeNope"
            pe "Nope! Nope nope nope-"

            "After successfully scrambling to her feet, she takes off in another direction."
            "The snow fall gets heavier by the second, and snow blindness makes it worse to navigate the path."
            "But fortunately she was lucky. She squints her eyes to see a large rock wall ahead."

            voice "d27_TheMountain"
            pe "The mountain! Now I just have to make it back."
            play sound snowrun

            "Pearl starts sprinting towards it, but unbeknownst to her, the terrain ahead was a rather dangerous one."
            play sound slip

            voice "d27_Shi"
            pe "Shi-"
            show black with pushupquick
            hide cg
            play sound fall
            show cg pearldeath2
            "Pearl loses her footing and slips down a ravine."
            stop ambience fadeout 1.0

        #If is Aston is present and safe, then Pearl will be safe
        #If Aston is not safe, choosing Let's think about it, Pearl will be safe
        #If Aston is not safe, choosing You won't survive the cold, Pearl skips to death scene

label dec_28:
    scene bg camp2_day with longfade
    $ current_day = _("December 28th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    play music audio.neutral

    #Gregory's POV
    show gr neutral
    "Gregory is alone at the campsite."
    "Morgan and the rest are out on a search mission again."

    show gr angry
    play sound dial
    voice "d28_ComeOn"
    gr "Come on... Pick up damn it."

    "Gregory tries reaching HQ on his phone but the calls keep disconnecting."
    "It is frustrating."
    "Even more so when it's an urgent matter."

    #If Pearl is okay
    if pearl_safe:
        "People around him are falling ill at an overwhelming rate and there's nothing he can do."
        "There aren't enough tents after the avalanche hit."

    #If Pearl is not okay
    else:
        "People have been disappearing from camp and there's not enough manpower to do another search and rescue mission."
        "But the quota unfortunately doesn't stop for anyone."

    show gr neutral
    voice "d28_PlanB"
    gr "Plan B it is."
    #(TOGGLE) ma
    "Gregory gives up and decides to call the supply crew."
    "They're more likely to pick up."
    if radio_static == "_s":
        voice "d28_NowThats_s"
    else:
        voice "d28_NowThats_c"
    ma "Now that's a name I haven't seen in months. What do you need?"
    voice "d28_INeed"
    gr "I need you to get our CEO lady on the phone."
    if radio_static == "_s":
        voice "d28_HeyIf_s"
    else:
        voice "d28_HeyIf_c"
    ma "Hey if you forgot, I'm just the supply guy."
    if radio_static == "_s":
        voice "d28_IfYoure_s"
    else:
        voice "d28_IfYoure_c"
    ma "If you're not here to get stuff like Lorenzo usually does, then I'm gonna hang up."
    #(BRANCH FLAGGED) was not branched before, need test
    if pearl_safe: 
        show gr angry
        voice "d28_br1_DidShe"
        gr "Did she not tell you anything?"

    else:
        show gr angry
        voice "d28_br2_DidShe"
        gr "Did she not tell you about Lorenzo?"

    if radio_static == "_s":
        voice "d28_IsThere_s"
    else:
        voice "d28_IsThere_c"
    ma "Is there something I should know?"
    voice "d28_ThatDamn"
    gr "That damn b-"
    #(BRANCH FLAGGED) was not branched before, need test
    if pearl_safe:
        voice "d28_br1_AndYouve"
        gr "And you've never realized that Lorenzo's missing?"

    else:
        voice "d28_br2_AndYouve"
        gr "And you've never realized that he's missing?"

    if radio_static == "_s":
        voice "d28_WoahThere_s"
    else:
        voice "d28_WoahThere_c"
    ma "Woah there. I'm just doing my job. Lorenzo ain't the only person I deal with."
    show gr neutral
    if radio_static == "_s":
        voice "d28_IfTheres_s"
    else:
        voice "d28_IfTheres_c"
    ma "If there's an order, I will complete it. Simple as that."
    if radio_static == "_s":
        voice "d28_ButNo_s"
    else:
        voice "d28_ButNo_c"
    ma "But no, she never mentioned anything about Lorenzo or whatever."
    voice "d28_WellLet"
    gr "Well, let her know that Gregory's calling."
    if radio_static == "_s":
        voice "d28_IllDo_s"
    else:
        voice "d28_IllDo_c"
    ma "I'll do my best, but no promises."

    show gr worried
    "Gregory exhales deeply."
    "Stuck in this predicament that nobody wants to be in."
    "Knowing the true nature of this operation, and then deceiving the ones that he's working closely with."
    "The choice that he made now affects everyone around him."
    "But to Gregory, it's a necessary burden to bear."
    stop music fadeout 3.0
    jump dec_29

label dec_30:
    $ current_day = _("December 30th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    scene bg maintent_night with dissolve
    with vpunch
    play sound radiotower
    "*CRASH*"
    "I was rudely woken up by a horrendous noise."
    "What the hell was that?"

    #show ky confused with sdissolve
    voice "d30_WuhHuh"
    ky "Wuh huh?"

    "Seems like Kyle was also abruptly pulled out of dream land."
    show gr neutral at centerleft with dissolve
    #with Pause(1.0)
    show gr neutral with move:
        xpos -100
    hide gr neutral
    "I see Gregory running out the tent to go have a look."
    "At least it doesn't sound like an avalanche this time."

    #EXT: Camp 1A
    scene bg camp2_night with sdissolve
    play ambience amb_campnight fadein 1.0
    play sound radio
    "Gregory's Walkie starts beeping the moment I step foot outside."
    #(TOGGLE) ca
    show gr neutral at centerleft
    if radio_static == "_s":
        voice "d30_HeyaGregory_s"
    else:
        voice "d30_HeyaGregory_c"
    ca "Heya Gregory, I was gonna say that we got the new maps but it seems like we have a new problem."
    if radio_static == "_s":
        voice "d30_AnyIdea_s"
    else:
        voice "d30_AnyIdea_c"
    ca "Any idea where that was coming from?"
    show gr worried
    voice "d30_MyGuess"
    gr "My guess is that the radio tower's down."
    if radio_static == "_s":
        voice "d30_OhThats_s"
    else:
        voice "d30_OhThats_c"
    ca "Oh, that's bad news alright. I'll relay the message to Wilbur and the rest."
    show gr neutral
    voice "d30_YeahThanks"
    gr "Yeah. Thanks."

    "Is that why the signal has been trash lately?"
    "Gregory turns to see the confusion on my face."
    voice "d30_SoWhat"
    mo "So what I'm getting is that the radio tower crashed?"
    voice "d30_WedNeed"
    gr "We'd need to check it out tomorrow. Best case scenario is that we can fix it ourselves."
    show gr confused
    voice "d30_WorstCase"
    gr "Worst case scenario is that we have to wait for backup."
    voice "d30_HowLong"
    mo "How long does that usually take?"
    voice "d30_TwoWeeks"
    gr "Two weeks."
    voice "d30_AreWe"
    mo "Are we basically stranded here?"
    show gr neutral
    voice "d30_YeahWeve"
    gr "Yeah. We've lost contact with HQ."
    show ky sad at centerright
    voice "d30_WhatIf"
    ky "What if HQ forgets about us?"

    #If Pearl is safe
    if pearl_safe:
        voice "d30_WeCould"
        show pearl sad at right
        pe "We could leave camp by ourselves if they don't reach us, right?"
    voice "d30_WellThink"
    gr "We'll think about it when it happens."

    scene bg maintent_night with sdissolve
    stop ambience fadeout 3.0
    play ambience amb_intcampnight fadein 1.0
    "I ran back into the main tent to grab my satellite phone."
    "Yep. Signal's completely dead."
    "The gravity of the situation finally sinks in. Which means Colin...he can't reach me."
    "But I'm not too worried, since Colin does have my location."
    "It's just that, well... It'll probably jeopardize the mission."
    "Whoever Gregory is calling at HQ... Guess he won't be able to reach them anytime soon."


    #If Aston is safe
    if aston_safe:
        show ast neutral
        voice "d30_WellHave"
        ast "We'll have to check on Lorenzo tonight."
        "Aston, who's also now awake, checks his phone."
        "I should also go to the cabin tonight."
        stop ambience fadeout 1.0


        scene bg cottage2 with fade
        show lorenzo sad
        play music audio.light
        "We're paying Lorenzo a visit."
        show ast neutral at centerleft
        voice "d30_br1_SoThe"
        lo "So the loud crash I heard was real, then?"
        voice "d30_YesWe"
        ast "Yes, we took a look at the radio tower on our way here. There's a piece missing from it."
        show ast inthought
        voice "d30_MightveBeen"
        ast "Might've been the receiver."
        voice "d30_HasThis"
        mo "Has this ever happened before?"
        show lorenzo pondering
        voice "d30_br1_IDont"
        lo "I don't think so, amico. The maintenance crew usually comes in every three months."
        show ast neutral
        voice "d30_WeveNever"
        ast "We've never had issues prior, so I'm hoping it'll be resolved quickly."
        show ast sad
        voice "d30_HowHave"
        ast "How have you been feeling?"
        show lorenzo smile
        voice "d30_TheBear"
        lo "The bear is still around, but that's about it. Hasn't been speaking to me anymore."
        "Lorenzo's state seems to be improving."
        "Aston touches his forehead."
        show ast inthought
        voice "d30_IThinkYourTemperature"
        ast "I think your temperature seems fine now too."
        show ast happy
        voice "d30_WereGoing"
        ast "We're going back to camp together, Lorenzo."
        show lorenzo happy
        "He tousles Lorenzo's hair gently."
        "I'm glad things are starting to change for the better."
        stop music fadeout 3.0

    #If Aston is not safe
    else:
        "I should also go to the cabin tonight."
        stop ambience fadeout 1.0
        scene bg cottage2 with fade
        play ambience amb_lobear fadein 1.0

        show lorenzo scared
        "I'm paying Lorenzo a visit."
        voice "d30_br2_SoThe"
        lo "So the loud crash I heard was real, then?"
        show lorenzo neutral
        voice "d30_TheRadio"
        mo "The radio tower is broken, yeah."
        voice "d30_HasThis"
        mo "Has this ever happened before?"
        show lorenzo sad
        voice "d30_br2_IDont"
        lo "I don't think so, amico. The maintenance crew usually comes in every three months."
        voice "d30_HowAre"
        mo "How are you feeling Lorenzo?"
        show lorenzo sick
        voice "d30_IThinkItsGetting"
        lo "I... I think it's getting worse."
        hide lorenzo
        "Lorenzo's state is becoming significantly unstable."
        voice "d30_LLaren"
        ha "L-Laren... Lorezo... "
        "He seems like he's shaking under the covers."
        "I wish I could do something for him, maybe get Ruran here to check on him while I'm away."
        "I know Aston would've done the same."
        stop ambience fadeout 1.0
        stop music fadeout 1.0
    
    scene black with longfade

label dec_31:
    $ current_day = _("December 31st")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    scene bg forest2 with dissolve
    play music audio.neutral
    "The next morning comes."
    show gr neutral
    "Gregory and I are checking up on the radio tower today."
    #SFX snowfoot
    "Hiking up this mountain gives me déjà vu."
    "Just earlier this month, we had plans to merge camps."
    "But then an avalanche happened."
    "Camp merging didn't happen."
    "Lorenzo's hiding in the cabin, and then hallucinating a bear."
    # TODO DOUBLE CHECK THE LOGIC
    #If Aston is safe
    if aston_safe:
        "Aston is now ill with his auditory hallucinations."
    #If Aston is not safe
    else:
        "Aston is now ill with his auditory hallucinations and... we don't know where he is now."
    #If Pearl is safe
    if pearl_safe:
        "Pearl also fell sick and hasn't been acting like herself."
    #If Pearl is dead
    else:
        "Pearl also fell sick, but then left camp one night and didn't come back..."
    "So many things happened in the span of a month."
    "Gosh... Did Elly have to go through this many things?"
    "At least Gregory and I are meeting up with Davos and Jax today."
    "The two representatives from C2."
    #If Aston is not safe AND if Pearl is dead
    if not aston_safe and not pearl_safe:
        "I wonder how they feel about the news, knowing that your friends are still missing."
    #If Aston OR Pearl are not safe
    if aston_safe or pearl_safe:
        "I wonder how they feel about the news, knowing that your friend is still missing."
    show gr confused
    voice "d31_MorganIm"
    gr "Morgan, I'm going to take a look at the fuse. Mind bringing Davos and Jax over here when they're up?"
    hide gr
    voice "d31_ToThe"
    mo "To the midpoint then. I'll meet them there."
    "I beep Jax on the Walkie."

    #If everyone safe
    if aston_safe and pearl_safe:
        #TODO radio start
        #(TOGGLE) ja da
        
        if radio_static == "_s":
            voice "d31_br1_GoodMorning_s"
        else:
            voice "d31_br1_GoodMorning_c"
        $ chibi_jax = "images/chibi/jax_neutral.png"
        wt_ja "Good morning. We're on our way."
        if radio_static == "_s":
            voice "d31_br1_Just5_s"
        else:
            voice "d31_br1_Just5_c"
        $ chibi_davos = "images/chibi/davos_happy.png"
        wt_da "Just 5 minutes or so left! We'll be there soon."
        voice "d31_br1_TheViews"
        $ chibi_morgan = "images/chibi/morgan_happy.png"
        wt_mo "The view's great up here, guys."
        $ chibi_jax = "images/chibi/jax_happy.png"
        if radio_static == "_s":
            voice "d31_br1_HellYeah_s"
        else:
            voice "d31_br1_HellYeah_c"
        wt_ja "Hell yeah. Nice to finally watch you in action, Mr. Rusty with rifles."
        voice "d31_br1_IsThat"
        $ chibi_morgan = "images/chibi/morgan_neutral.png"
        wt_mo "Is that going to be my new nickname?"
        $ chibi_jax = "images/chibi/jax_happy.png"
        if radio_static == "_s":
            voice "d31_br1_Yeah_s"
        else:
            voice "d31_br1_Yeah_c"
        wt_ja "Yeah."
        $ chibi_morgan = "images/chibi/morgan_happy.png"
        voice "d31_br1_ImReady"
        wt_mo "I'm ready to be humbled then, Mr. Great with guns."
        $ chibi_davos = "images/chibi/davos_neutral.png"
        if radio_static == "_s":
            voice "d31_br1_WhatsWith_s"
        else:
            voice "d31_br1_WhatsWith_c"
        wt_da "What's with the rifle thing? Are you getting private lessons from Jax?"
        voice "d31_br1_IWish"
        wt_mo "I wish."
        $ chibi_davos = "images/chibi/davos_happy.png"
        if radio_static == "_s":
            voice "d31_br1_OhMorgan_c"
        else:
            voice "d31_br1_OhMorgan_c"
        wt_da "Oh, Morgan! I think I see you up there!"
        $ chibi_morgan = "images/chibi/morgan_neutral.png"
        voice "d31_br1_NiceLets"
        wt_mo "Nice! Let's meet up at the midpoint in 5."
        #radio ends
        "I look away from my Walkie to see someone waving."
        "It's Davos, I think, since he's the shorter one."
        "They still have a ways to get here."
        nvl clear

    #If Pearl is missing
    else:
    #radio start
        voice "d31_br2_GoodMorning_c"
        $ chibi_jax = "images/chibi/jax_neutral.png"
        wt_ja "Good morning. We're on our way."
        voice "d31_br2_Just5_c"
        $ chibi_davos = "images/chibi/davos_neutral.png"
        wt_da "Just 5 minutes left. We'll be there soon."
        voice "d31_br2_TheViews"
        $ chibi_morgan = "images/chibi/morgan_neutral.png"
        wt_mo "The view's great up here guys."
        voice "d31_br2_HellYeah_c"
        $ chibi_jax = "images/chibi/jax_neutral.png"
        wt_ja "Hell yeah, nice to finally watch you in action, Mr. Rusty with rifles."
        voice "d31_br2_IsThat"
        wt_mo "Is that going to be my new nickname?"
        $ chibi_jax = "images/chibi/jax_happy.png"
        voice "d31_br2_Yeah_c"
        wt_ja "Yeah."
        voice "d31_br2_ImReady"
        $ chibi_morgan = "images/chibi/morgan_happy.png"
        wt_mo "I'm ready to be humbled then, Mr. Great with guns."
        voice "d31_br2_IThink_c"
        $ chibi_davos = "images/chibi/davos_happy.png"
        wt_da "I think I see you Morgan!"
        voice "d31_br2_NiceLets"
        $ chibi_morgan = "images/chibi/morgan_neutral.png"
        wt_mo "Nice! Let's meet up at the midpoint in 5."
        nvl clear
    #radio ends
        "Davos seems like he's trying to hold it together today, I'm worried for him."


    #continue here
    stop music
    "I should have a look around. I wonder if you can see Lorenzo's cabin from up here."
    "But then again, the cabin is to the north, and so is the radio tower."
    "Cassie would've spotted it if there weren't so many trees."
    "I'll take a peek at the east."
    "There's nothing on the east side other than a few natural rock formations."
    "Looks like there's also a ravine."
    "And south is where C2 and RC can be seen."
    "It'll be the first time I lay my eyes on-"
    play sound kick
    "..."
    play music audio.anxious
    "I kicked something."
    "Something under the snow, maybe?"
    voice "d31_MorganWere"
    da "Morgan, we're here!"
    "I heard Davos calling out from behind me."
    "But I'm far too concerned about what I see on the ground in front of me to respond."
    voice "d31_HeyMorg"
    ja "Hey Morg- Oh what the fuck."
    show cg frozenbody:
        zoom 2.0
        xpos -1300
        ypos -700
        blur 5
    $ persistent.gallery_frozenbody = True
#TODO talk to elina
    "A body."
    "A dead body."
    "With lesions and gaping wounds, possibly by wolves."
    "And... weird mushrooms growing out of it?"
    "Mauled to an unidentifiable state."
    show cg frozenbody with fade:
        zoom 1.0
        blur 0
        xalign 0.5
        yalign 1.0
    "The only telltale sign that it was a human was the arm protruding out from the snow."


    #If Pearl and Aston is safe
    if aston_safe and pearl_safe:
        "Davos turns away from the sight."
        voice "d31_TheDay"
        ja "The day always turns into an eventful one when I least expect it."
        voice "d31_br1_ThisLooks"
        da "This...looks like a horrible way to die."
        voice "d31_br1_IImGonna"
        da "I-I'm gonna go call my pops."
        voice "d31_WellThen"
        mo "Well then... We're stranded and now there's a dead body."
        voice "d31_WhatElse"
        mo "What else could possibly go wrong?"

    #If either Pearl or Aston is missing
    else:
        "I'm not ready to identify who it is."
        "Davos turns away from the sight."
        voice "d31_TheDay"
        ja "The day always turns into an eventful one when I least expect it."
        voice "d31_br2_ThisLooks"
        da "This...looks like a horrible way to die."
        voice "d31_br2_IImGonna"
        da "I-I'm gonna go call my pops."
        voice "d31_WellThen"
        mo "Well then... We're stranded and now there's a dead body."
        voice "d31_WhatElse"
        mo "What else could possibly go wrong?"

    scene black with longfade
    with Pause(2.0)
    jump dec_31_2
###----------This was the end of the first demo :)----------###

label dec_31_2:
    stop music fadeout 12.0
    "What a turn of events."
    "Upon closer inspection, there seems to be some leftover fabric of what they were wearing."
    "Linen texture... It's not a material that any of us wear out here."

    if not aston_safe: # Will be true if Pearl's dead
        "I'm...glad it's not someone we know."

    "Davos went away to get Wilbur, and Jax is crouching down with me."
    "He doesn't seem all that phased by the corpse."
    scene bg forest2 with dissolve
    show ja serious at centerleft
    voice "d31_YoureOddly"
    ja "You're oddly calm about this."
    voice "d31_ICould"
    mo "I could say the same to you."
    show ja inthought
    voice "d31_NotThe"
    ja "Not the first time I've seen one, but it still gets me every time."
    voice "d31_YouMe"
    mo "You, me...the same, then."
    "Body structure-wise, or at least what we could gather from what's left of them, suggests that they were an adult male."
    "Several gaping wounds left all over by bites from a large animal."
    "His torso has practically been ripped wide open, the same spot where the disc-like mushrooms have been growing."
    "The smell... I can't even begin to describe it."
    "This has to be some sort of sick joke."

    voice "d31_SoMr"
    mo "So... Mr. Great with Guns... Sample collection time?"
    show ja neutral
    voice "d31_HahaI"
    ja "Haha... I guess we'd better be the ones to do it. I'm not traumatizing the poor boy."
    voice "d31_YouThink"
    mo "You think he's the villager we're looking for?"
    voice "d31_ItsA"
    ja "It's a reasonable guess. We won't know until we bring the body down."
    show ja inthought
    voice "d31_ISure"
    ja "I sure as hell didn't sign up to do arm and back day today."
    voice "d31_MorganJax"
    gr "Morgan? Jax?"
    show ja neutral
    "Gregory calls us from somewhere to our left."
    voice "d31_DavosHe"
    gr "Davos, he... He filled me in. Stay put. I'm going to get extra help."
    voice "d31_GotIt"
    mo "Got it!"
    "Focusing back on the task at hand, Jax and I geared up for sample collection."
    scene black with dissolve
    "This time...on something that was once human and alive."
    "I'm sorry."
    play sound scoop2
    "I'll be taking your harvest."
    "These disc-like mushrooms aren't the edible kind."
    "Not that I would want to take a bite."
    scene black
    hide ja with dissolve


    voice "d31_MorganAny"
    ja "Morgan. Any idea what this is?"
    scene forest2 with dissolve
    show ja neutral at center
    play music audio.neutral fadein 1.0
    "Jax carefully holds up a piece of an unusually shaped paper fragment in the palm of his hand."
    "It crumbles into dust as he tries to pick it up once more."
    "Taking another look around at our surroundings, there seem to be more of these tiny specks of dusty paper fragments."

    voice "d31_DoYou"
    mo "Do you remember the sound we heard right before the avalanche? I think I may have an idea of what this could be."
    show ja serious
    voice "d31_Dynamite"
    ja "Dynamite?" 
    voice "d31_Bingo"
    mo "Bingo."
    "I feel a sense of dread forming in the pit of my stomach."
    "Dynamite. For what purpose?"
    "Was this the real cause of the avalanche?"
    "Who is this person?"
    "If they're a villager... How did they even get dynamite?"
    "..."
    "Was there another party involved?"

    show ja inthought
    voice "d31_WhatDo"
    ja "What do you think we should do? With dynamite potentially in the picture, I mean."
    voice "d31_WeDont"
    ja "We don't know their motive, and we lost Lorenzo in the process."

    if not aston_safe:
        if not pearl_safe:
            voice "d31_AndBoth"
            ja "And... Both Aston and Pearl, too."
        else:
            voice "d31_AndAston"
            ja "And... Aston, too."

    "Right. He doesn't know that Lorenzo's still alive."
    "But, for the body and traces of dynamite... There's no clear motive."
    "We should tell the rest...but what are the chances of the culprit hiding in plain sight?"
    "Nah... I think it's worth a try if it could scare them out of hiding."

    voice "d31_WeShould"
    mo "We should let the others know that we may have found the cause for our failed camp merge."
    show ja neutral
    voice "d31_GladTo"
    ja "Glad to know we're on the same page, then."

    scene black with longfade
    "Wilbur, Gregory and Davos appeared shortly after." 
    "They brought a stretcher to move the body down the mountain."
    "Later that afternoon, we contacted the village."
    "They recognized him."
    "It was him. The missing villager."
    "And...he was my ride up into the mountains. I couldn't even recognize him in the state he was in."
    "And to think, he was up there all alone under a pile of snow."
    "For 3 weeks...at least."
    "We still haven't got the exact cause of death."
    "The only thing we could rule out is that he threw the explosives far enough away from him."
    "There were only minimal signs of blast injuries, but a whole lot of other wounds that I no longer want to think about."
    stop music fadeout 3.0
    stop ambience fadeout 3.0

label jan_1:
    $ current_day = _("January 1st")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    scene black
    with Pause(2.5)
    play ambience amb_village fadein 1.0
    "After the shock of yesterday's events, we greeted the New Year with a funeral." 
    "Today is the villager's burial day."
    play music audio.sad
    scene village2 with dissolve # will need other BG with no Susie, kids, etc
    "A few of us were at the village to pay our respects."
    show wi neutral at left
    show ky neutral at centerleft
    show isa serious at right
    show ja neutral at centerright
    "Kyle and I from C1, Jax and Wilbur from C2, and, surprisingly, Isaak from the RC."
    "A large crowd gathered around the deceased's grave."
    show ky sad
    voice "j1_HeWas"
    ky "He was such a great guy... He was the one that introed me to the farm animals...{w=0.5}to Susie."
    show ky shaken
    voice "j1_IllMiss"
    ky "I'll miss you."
    voice "j1_ImSure"
    wi "I'm sure he'd be happy to know that, Kyle."
    show ky sad
    "There was a lady dressed differently from the rest, standing to the side with two children...presumably his family."
    "The younger child sobs uncontrollably."
    "He does not understand why their father will be laid in the deep, freezing soil for eternity."
    "An older man takes the center. The crowd starts to quiet down upon his arrival."

    voice "j1_ThatsThe"
    wi "That's the village elder."
    "He begins to speak, starting off the funeral with a few words."
    "The family, too, take turns to say their eulogies."
    "Tears were spilled and many stories were shared."
    scene black with fade
    stop ambience fadeout 2.0
    stop music fadeout 3.0

    "I'm no stranger to funerals."
    "I had to witness both my parents' on the same day many years ago."
    "It hurts occasionally, but I'm glad I had my people."
    "My support network. I took comfort in their presence."
    play music audio.light
    "Elly was there, too."
    "Through every bottle I drank on my worst days."
    "Through every piled up laundry basket I never bothered to touch."
    "Through every meal that I didn't want to eat."
    "He checked in on me, made sure I drank enough water, made sure I had food in my system."
    "It's still funny to me how he thought he could masterchef his way into my kitchen." 
    stop music fadeout 1.5
    "For the record, I never forget to season my food...so clearly, I'm the better cook."
    
    
    scene village2 # same bg as earlier; no Susie, Kyle, kids
    show wi neutral at left
    show ky sad at centerleft
    show isa serious at right
    show ja neutral at centerright
    with dissolve
    "I snapped out of my thoughts for a second as I realized the speeches had concluded."
    "Looks like it's time for the next task on the agenda - the burial."
    play music audio.neutral
    "The village elder takes out a flask filled with a clear liquid from his belt."
    "He uncorks it, and out comes a pungent stench."
    "It smells like... Vinegar?"
    voice "j1_WhatAre"
    mo "What are they doing with that?"
    "My question was immediately answered as the elder dumps all of its contents into the grave."
    show ja confused
    show wi worried
    "I glance at my friends, who look just as perplexed as I do."
    show ky confused
    voice "j1_DidDid"
    ky "Did... Did they just pour it onto the body?"
    voice "j1_IveNever"
    ky "I've never been to a funeral, so, like...is this normal?"
    voice "j1_IDont"
    mo "I don't think so?"
    voice "j1_VinegarTo"
    isa "Vinegar, to kill off any leftover spores."
    show isa inthought
    voice "j1_YouDid"
    isa "You did harvest fungi from his body. Surely you remember?"
    show wi happy
    voice "j1_AlwaysA"
    wi "Always a smart one, Isaak! I wouldn't have guessed."
    show ja happy
    voice "j1_ItsSuper"
    ja "It's super convenient that they had vinegar ready, then."
    "Once the container was emptied, the villagers began shovelling, burying him."
    stop music fadeout 2.0
    stop ambience fadeout 2.0
    scene black with longfade
    "I hope he rests in peace."

label jan_2:
    $ current_day = _("January 2nd")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    scene maintentday with dissolve
    play ambience amb_intcampday fadein 2.0

    if not aston_safe:
        "I am on stay-at-camp duty today while the others are out collecting samples."
        "The camp's a lot quieter and there wasn't much to do, other than a little housekeeping in the main tent."
        "We still have about a month's worth of food left in the stash."
        "I don't think we need to worry for now...unless the radio tower isn't gonna be fixed within the next two weeks."
        "Radio tower is still down, comms are still off."
        "Well, organizing my notes wouldn't be a bad use of time."
        "Yeah. I think I'll do just that."
        stop ambience fadeout 2.0

        #INT: Morgan's tent
        scene morganstent with longfade
        play music audio.neutral
        "Alrighty, writing time."
        "A body found in a...strange state, with large, gaping wounds."
        "A type of fungus growing in winter, on said body."
        "An avalanche that was most likely set off by explosives."
        "And why were there even explosives in the first place?"
        "My campmates are getting sick, and hallucinating things that aren't there."
        "My campmates... That's right. I never had the chance to find those documents that Gregory had on hand."

        #If Pearl okay
        if pearl_safe:
            "Gregory is away with Pearl and Kyle...they won't be back for another hour or so."
        else:
            "Gregory is away with Kyle...they won't be back for another hour or so."

        "Do I want to push my luck?"
        "I can't call myself an investigator if I don't."
        "I won't feel worthy to own a snowmobile either."
        "Time for some good ol' detective work."

        #EXT: Camp 1
        scene camp1day with longfade
        "Not wanting to waste the perfect opportunity, I beeline straight to Gregory's tent."
        "I place my hands on the tent zipper and take a deep breath."
        voice "j2_AlrightHere"
        mo "Alright, here goes nothing." 
        
        scene gregtent with longfade
        "Gregory's tent doesn't have much in it..."
        "He doesn't sleep in here, but his belongings are all in here."
        "But there is one picture frame atop his storage box that stands out."
        "It's younger Gregory with a child. It must be her."
        "I've...never seen him smile like that."
        "I go to take a look at his backpack."
        "It's not the usual ones we use when we're out in the field - it's a smaller one. For personal use, I'm guessing."
        play sound zipopen
        scene black with fade
        "Annnnnd nothing... Just information I already knew about Heralign."
        "We've got a permit letter here, listing Gregory's qualifications and such."
        "Oh, he's been working at Heralign for about 4 years."
        "Okay, enough about him. I think I'll try the storage boxes next."
        scene gregtent with dissolve
        with Pause(1.0)
        "And...sure enough, I did indeed find a folder containing the papers with the special status labels."
        "Good job, Morgan."
        "There were the same profiles, some now with multiple '???' markings in their status."
        "The redacted profiles were also in the same folder."
        "And, lo and behold... It looks like Kyle and I have our very own, too."
        "These are definitely new."
        "I flipped through them some more."
        "There's Pearl's, Aston's, and Lorenzo's."
        if pearl_safe:
            "Aston's and Lorenzo's status now has 'Missing' written there."
            "And Pearl's has a '???' penned down."
            "Looks like Gregory isn't sure how she's doing."
        else:
            "All three of them now have 'Missing' written in their status."
            "Reading these felt like a jab in my heart."
        
        scene black with longfade
        stop music fadeout 2.0
        stop ambience fadeout 0.5
        "I reverted the tent back to its original, untouched state."
        "...or as close as I could manage."
        "I do need to tell the others at some point."
        "They all deserve to know."

    else: # Aston's OK
        "Aston and I are on stay-at-camp duty today, while the rest are out sample collecting."
        "The camp's a lot quieter and there wasn't much to do, other than a little housekeeping in the main tent."
        "We still have about a month's worth of food left in the stash."
        "I don't think we need to worry for now...unless the radio tower isn't gonna be fixed within the next two weeks."
        "Radio tower is still down, comms are still off."
        "Well, organizing my notes wouldn't be a bad use of time."
        "Yeah. I think I'll do just that."
        voice "j2_AstonIll"
        mo "Aston, I'll be in my tent for a bit. Call me if you need anything."
        show ast neutral at left
        "Aston looks up from the storage box and gives me a nod."
        stop ambience fadeout 2.0

        scene morganstent with longfade
        play music audio.neutral
        #INT: Morgan's tent
        "Alrighty, writing time."
        "A body found in a...strange state, with large, gaping wounds."
        "A type of fungus growing in winter, on said body."
        "An avalanche that was most likely set off by explosives."
        "And why were there even explosives in the first place?"
        "My campmates are getting sick, and hallucinating things that aren't there."
        "My campmates... That's right. I never had the chance to find those documents that Gregory had on hand."
        "Aston's probably still in the main tent."
        "Gregory is away with Pearl and Kyle...they won't be back for another hour or so."
        "Do I want to push my luck?"
        "I can't call myself an investigator if I don't."
        "I won't feel worthy to own a snowmobile either."
        "Time for some good ol' detective work."
        scene black with longfade

        #EXT: Camp 1
        scene camp1day with dissolve
        "Not wanting to waste the perfect opportunity, I beeline straight to Gregory's tent."
        "And then as I had my hands on the tent zipper, I was interrupted by Aston sneaking up behind me."
        show ast neutral with sdissolve
        voice "j2_Morgan"
        ast "Morgan?"
        "I jump in surprise...again."
        "It's getting kind of embarrassing."
        voice "j2_DoYouEverGet"
        mo "Do you ever get that feeling of déjà vu? 'Cause I'm pretty sure we've had this conversation."
        show ast happy
        voice "j2_YesWhat"
        ast "Yes. What were you looking at?"
        voice "j2_YoureGonna"
        mo "You're gonna follow the same script?"
        voice "j2_IKnow"
        ast "I know when to be a little humorous."
        show ast inthought
        voice "j2_ThoughSkulking"
        ast "Though...skulking about in his tent seems like a bad idea. Are you sure you want to do this?"
        voice "j2_INeed"
        mo "I need to satisfy my curiosity...and I need some answers."
        show ast neutral
        voice "j2_DoYouWantAny"
        ast "Do you want any help?"

        menu j2Papers:
            "Be truthful about the papers":
                $ j2_astonPapers = True
                voice "j2_ItsAbout"
                mo "It's about the papers, if you remember the morning of our first storm together."
                show ast inthought
                voice "j2_INever"
                ast "I never wanted to pry, but I'm assuming that...if you're willing to take this kind of risk, they must be important."
                voice "j2_ImHoping"
                mo "I'm hoping I'd find them here."

                scene gregtent with longfade
                "Gregory's tent doesn't have much in it..."
                "He doesn't sleep in here, but his belongings are all in here."
                "But there is one picture frame atop his storage box that stands out."
                "It's younger Gregory with a child. It must be her."
                "I've...never seen him smile like that."
                "Aston carefully sorts through Gregory's storage while I take a look at his backpack."
                "It's not the usual ones we use when we're out in the field - it's a smaller one. For personal use, I'm guessing."
                play sound zipopen
                scene black with fade
                "Annnnnd nothing... Just information I already knew about Heralign." 
                "We've got a permit letter here, listing Gregory's qualifications and such."
                "Oh, he's been working at Heralign for about 4 years."
                voice "j2_MorganAre"
                ast "Morgan, are these the papers you're looking for?"

                # Deliberately staggered, operating under thought that gregtent will be a typical BG/not super up-close like morganstent
                scene gregtent with dissolve
                show ast sad at left with dissolve

                "I turn to see Aston holding a large folder, an alarmed look on his face."
                "Sure enough, he did indeed find the papers with the special status labels."
                voice "j2_YeahThose"
                mo "Yeah, those are the ones... May I?"
                "He handed over the folder and I quickly grabbed a few packets from within." 
                "There were the same profiles, some now with multiple '???' markings in their status." 
                "The redacted profiles were also in the same folder."
                "And, lo and behold... It looks like Kyle and I have our very own, too."
                show ast confused
                voice "j2_AreThese"
                ast "Are these new?"
                voice "j2_LooksLike"
                mo "Looks like it. I never noticed I had one that day." 
                "I flipped through them some more."
                "There's Pearl's, Aston's and Lorenzo's."
                "Lorenzo's status now has 'Missing' written there..."
                "And both Pearl and Aston's have a '???' penned down."
                "Looks like Gregory isn't sure how they're doing."
                voice "j2_YoureConfusing"
                mo "You're confusing the guy."
                "I turn Aston's profile toward him and point to his status."
                show ast happy
                voice "j2_ISuppose"
                ast "I suppose that's a good thing? I'm glad I'm hiding it well, then."
                voice "j2_StillHearing"
                mo "Still hearing stuff?"
                show ast inthought
                voice "j2_OccasionallyIt"
                ast "Occasionally. It doesn't really phase me anymore, though."
                voice "j2_LorenzoIs"
                ast "Lorenzo is fine, and so am I. There would be no reason for him to scream."
                voice "j2_YouSay"
                mo "You say the latter half with such...calm."
                show ast happy
                voice "j2_ICant"
                ast "I can't just run off in panic every time now, can I?"
                voice "j2_MmhmmI"
                mo "Mmhmm... I think we've got what we came for. Let's get outta here."

                scene black with longfade
                stop music fadeout 2.0
                stop ambience fadeout 0.5
                "We reverted the tent back to its original, untouched state."
                "...or as close as we could manage."
                "Aston and I agreed to keep it between us for now. We plan to discuss it while Lorenzo is present."
           
            "Leave Aston out of this":
                voice "j2_YeahWould"
                mo "Yeah. Would you be kind enough to alert me if he's back early?"
                voice "j2_AndWell"
                mo "And, well... Don't tell him I'm snooping."
                show ast happy
                voice "j2_ConsiderIt"
                ast "Consider it done."
                "Aston leaves me be and sits out at the campfire."
                voice "j2_ThanksAston"
                mo "Thanks, Aston."
                voice "j2_AlrightHere"
                mo "Alright, here goes nothing."
                
                scene gregtent with longfade
                "Gregory's tent doesn't have much in it..."
                "He doesn't sleep in here, but his belongings are all in here."
                "But there is one picture frame atop his storage box that stands out."
                "It's younger Gregory with a child. It must be her."
                "I've...never seen him smile like that."
                "I go to take a look at his backpack."
                "It's not the usual ones we use when we're out in the field - it's a smaller one. For personal use, I'm guessing."
                play sound zipopen
                scene black with fade
                "Annnnnd nothing... Just information I already knew about Heralign."
                "We've got a permit letter here, listing Gregory's qualifications and such."
                "Oh, he's been working at Heralign for about 4 years."
                "Okay, enough about him. I think I'll try the storage boxes next."
                scene gregtent with dissolve
                with Pause(1.0)
                "And...sure enough, I did indeed find a folder containing the papers with the special status labels."
                "Good job, Morgan."
                "There were the same profiles, some now with multiple '???' markings in their status." 
                "The redacted profiles were also in the same folder."
                "And, lo and behold... It looks like Kyle and I have our very own, too."
                "These are definitely new."
                "I flipped through them some more."
                "There's Pearl's, Aston's, and Lorenzo's."
                "Lorenzo's status now has 'Missing' written there..."
                "And both Pearl and Aston's have a '???' penned down."
                "Looks like Gregory isn't sure how they're doing."

                scene black with longfade
                stop music fadeout 2.0
                stop ambience fadeout 0.5
                "I reverted the tent back to its original, untouched state."
                "...or as close as I could manage."
                "I left his tent to find Aston still looking in the direction the others went."
                "I do need to tell him and the others at some point."
                "They all deserve to know."


label jan_3:
    scene black
    $ current_day = _("January 3rd")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    scene forest3night with dissolve
    if not aston_safe: 
        if not pearl_safe: # Both gone
            "Back out in the cold again."
            "I'm making my way toward Lorenzo's cabin."
            "I haven't seen him in a few days." 
            "Kyle's arm has been healing up well."
            "I learned a bit of first aid from Ruran over the Walkie to treat his rashes..."
            "So I'm betting that Lorenzo's arm will heal up just as well, eventually."

            scene cottage2 with longfade
            play music audio.sad fadein 3.0
            show lo scared at centerright
            voice "j3_br1_AndYou"
            lo "And you said...what was growing out of him?"
            voice "j3_br2_MushroomsTons"
            mo "Mushrooms. Tons of them, stacked atop one another."
            voice "j3_br2_TheBody"
            mo "The body also looks like it had been brutally attacked."
            voice "j3_br2_WeStill"
            mo "We still don't know what kind of animal or...thing...did that."
            voice "j3_br1_AndWhere"
            lo "And where did the dynamite come from?"
            voice "j3_br1_CantSay"
            mo "Can't say. We've only found fragments so far."
            voice "j3_br1_IfThere"
            mo "If there really was dynamite involved...that sound we heard right before the avalanche could very well have been the same explosion."
            "I fill him in on the situation that happened over the past few days."

            show lo sick
            voice "j3_br2_WowThis"
            lo "Wow, this is a lot to take in..."
            voice "j3_br2_LorenzoVNVR"
            lo "..."
            show lo sad
            voice "j3_br2_IIm"
            lo "I...I'm just glad that it wasn't...Aston."
            voice "j3_br2_HeStill"
            mo "He still hasn't come by?"
            voice "j3_br2_NoAnd"
            lo "No... And if he's not with you, then I assume he hasn't come back to camp either."
            stop music fadeout 1.0

            with Pause(0.7)
            play sound knock
            "*knock knock*"
            "Someone knocks loudly on the cabin's door."
            "The two of us turn to each other, then look back cautiously at the door."
            voice "j3_HelloAnyone"
            wi "Hello? Anyone in here?"
            show lo scared
            voice "j3_br2_IsIs"
            lo "Is... Is that Wilbur?"
            voice "j3_Wilbur"
            mo "Wilbur!"
            play music audio.light
            show lo sad
            show ja happy at centerleft
            show wi happy at left
            with dissolve
            "A wave of relief washes over us as two familiar faces greet us."
            "It's Wilbur and Jax."
            voice "j3_br3_LorenzoMy"
            wi "Lorenzo, my friend! Glad to see you're okay."
            voice "j3_br3_AndHello"
            ja "And hello, Morgan. You seem to be everywhere."
            voice "j3_br3_ICant"
            mo "I can't deny that."
            show lo smile
            voice "j3_br2_ItsLovely"
            lo "It's lovely seeing you all."
            voice "j3_br2_ISee"
            wi "I see that you have a setup here... How long have you been camping out?"
            show lo neutral
            voice "j3_br2_TheAvalanche"
            lo "The avalanche was...surprisingly kind to me."
            voice "j3_br2_ISuffered"
            lo "I suffered a few bruises here and there, but I was otherwise okay. This cabin wasn't too far from where I ended up..."
            voice "j3_br2_AndIve"
            lo "And I've been here ever since."
            voice "j3_br2_ThenMorgan"
            lo "Then...Aston and Morgan found me a few days later, cowering under a blanket."
            show ja inthought
            voice "j3_br3_C2Never"
            ja "C2 never gave up the search, Lorenzo."
            voice "j3_br3_WeTook"
            ja "We took turns every night, slowly expanding our search radius into the northern forest."
            voice "j3_br3_WereHoping"
            ja "We're hoping to find Aston and Pearl this way too."
            play music audio.sad
            show ja serious
            show lo scared
            with dissolve
            voice "j3_br3_WWhatDo"
            lo "W-What do you mean by 'find Aston and Pearl?' What happened to Pearl?"
            "Right... I never told him."
            voice "j3_br3_PearlShe"
            mo "Pearl, she... She also ran away from camp."
            voice "j3_br3_SheWasnt"
            lo "She wasn't looking for us...right?"
            "I avoided his gaze."
            "That night still haunts me."
            show lo sick
            voice "j3_br3_AndYou"
            lo "And you... Didn't tell me...{w=1.0}"

            voice "j3_br3_ButWhy"
            ja "But...why not go back to camp when they first found you?"
            "Jax attempts to change the subject for a while."
            voice "j3_br2_ItsA"
            mo "It's...a long story."
            voice "j3_br2_IDont"
            mo "I don't think we can finish it in one sitting."
            voice "j3_br2_WellI"
            wi "Well, I think we can leave storytime for later. What matters is that you're safe, my friend."
            voice "j3_br2_LetsHelp"
            wi "Let's help you pack, then we'll walk you home."
            "Lorenzo doesn't look too keen on the idea."
            show lo neutral
            voice "j3_br3_ActuallyI"
            lo "Actually, I think I'd much rather stay here."
            voice "j3_br3_IfAston"
            lo "If Aston shows up, or Pearl... I want to be here."
            voice "j3_br3_WeCould"
            ja "We could always leave a spare Walkie for them to use. You should head back to camp."
            show lo sad
            voice "j3_br3_IJust"
            lo "I just... I can't leave. I'm sorry."
            "I can see that Lorenzo is also worried about his symptoms."
            "And I don't think he wants to bring those up now, either."
            voice "j3_br2_WellIf"
            wi "Well, if you insist. I trust your judgment, Lorenzo."
            voice "j3_br2_IllKeep"
            mo "I'll keep an eye on him, Wilbur."
            voice "j3_br2_ThankYouMyBoy"
            wi "Thank you, my boy."
            scene black with longfade
            stop ambience fadeout 4.0
            stop music fadeout 3.0
            "Wilbur and Jax left for C2, and I decided to stay with Lorenzo for a bit longer."


        else: # Pearl OK, Aston gone
            "Back out in the cold again."
            "I'm making my way toward Lorenzo's cabin."
            "I haven't seen him in a few days." 
            "Kyle's arm has been healing up well."
            "I learned a bit of first aid from Ruran over the Walkie to treat his rashes..."
            "So I'm betting that Lorenzo's arm will heal up just as well, eventually."

            scene cottage2 with longfade
            play music audio.sad fadein 3.0
            show lo scared at centerright
            voice "j3_br1_AndYou"
            lo "And you said...what was growing out of him?"
            voice "j3_br2_MushroomsTons"
            mo "Mushrooms. Tons of them, stacked atop one another."
            voice "j3_br2_TheBody"
            mo "The body also looks like it had been brutally attacked."
            voice "j3_br2_WeStill"
            mo "We still don't know what kind of animal or...thing...did that."
            voice "j3_br1_AndWhere"
            lo "And where did the dynamite come from?"
            voice "j3_br1_CantSay"
            mo "Can't say. We've only found fragments so far."
            voice "j3_br1_IfThere"
            mo "If there really was dynamite involved...that sound we heard right before the avalanche could very well have been the same explosion."
            "I fill him in on the situation that happened over the past few days."
            voice "j3_br2_WowThis"
            lo "Wow, this is a lot to take in..."
            voice "j3_br2_LorenzoVNVR"
            lo "..."
            voice "j3_br2_IIm"
            lo "I...I'm just glad that it wasn't...Aston."
            voice "j3_br2_HeStill"
            mo "He still hasn't come by?"
            voice "j3_br2_NoAnd"
            lo "No... And if he's not with you, then I assume he hasn't come back to camp either."
            stop music fadeout 1.0

            with Pause(0.7)
            play sound knock
            "*knock knock*"
            "Someone knocks loudly on the cabin's door."
            "The two of us turn to each other, then look back cautiously at the door."
            voice "j3_HelloAnyone"
            wi "Hello? Anyone in here?"
            show lo scared
            voice "j3_br2_IsIs"
            lo "Is... Is that Wilbur?"
            voice "j3_Wilbur"
            mo "Wilbur!"
            play music audio.light
            show lo sad with move:
                xpos 1600
                yalign 1.0
            show ja happy at centerleft
            show wi happy at left
            show pe smile:
                xpos 180
                yalign 1.0
            with dissolve
            hide lo with None
            show lo sad with None:
                xpos 1288
                yalign 1.0
            "A wave of relief washes over us as three familiar faces greet us."
            "Wilbur, Jax and...Pearl?"
            show pe happy
            voice "j3_LorenzoOh" # Can remove branch tag if duped
            pe "Lorenzo! Oh boy, I've missed you so much!"
            show pe with move:
                xpos 1200
                yalign 1.0
            play sound jacket
            "Pearl runs towards him and gives him the biggest hug."
            show lo smile
            voice "j3_br2_HelloPearl"
            lo "Hello, Pearl."
            voice "j3_br2_LassHere"
            wi "Lass here told us she followed you all the way out from camp."
            show pe sad with move:
                xpos 950
                yalign 1.0
            voice "j3_br2_IWas"
            pe "I was having nightmares about the shrooms and couldn't go back to sleep."
            show pe smile
            voice "j3_br2_ThenI"
            pe "Then I heard Morgan gearing up, so I wanted to come along!"
            voice "j3_br2_ItsLovely"
            lo "It's lovely seeing you all."
            voice "j3_br2_ISee"
            wi "I see that you have a setup here... How long have you been camping out?"
            show lo neutral
            voice "j3_br2_TheAvalanche"
            lo "The avalanche was...surprisingly kind to me."
            voice "j3_br2_ISuffered"
            lo "I suffered a few bruises here and there, but I was otherwise okay. This cabin wasn't too far from where I ended up..."
            voice "j3_br2_AndIve"
            lo "And I've been here ever since."
            show lo sad
            voice "j3_br2_ThenMorgan"
            lo "Then...Aston and Morgan found me a few days later, cowering under a blanket."
            show ja inthought
            voice "j3_br2_C2Never"
            ja "C2 never gave up the search, Lorenzo."
            voice "j3_br2_WeTook"
            ja "We took turns every night, slowly expanding our search radius into the northern forest."
            voice "j3_br2_AndWere"
            ja "And...we're hoping to find Aston this way, too."
            show lo sad
            voice "j3_br2_ThankYouJaxIt"
            lo "Thank you, Jax. It means a lot to me."
            voice "j3_br2_OfCourse"
            ja "Of course. But...why hide from everyone? Why not go back to camp when they first found you?"
            voice "j3_br2_ItsA"
            mo "It's...a long story."
            voice "j3_br2_IDont"
            mo "I don't think we can finish it in one sitting."
            voice "j3_br2_WellI"
            wi "Well, I think we can leave storytime for later. What matters is that you're safe, my friend."
            voice "j3_br2_LetsHelp"
            wi "Let's help you pack, then we'll walk you home."
            stop music fadeout 3.0
            "Lorenzo doesn't look too keen on the idea."
            play music audio.sad
            show lo neutral
            voice "j3_br2_ActuallyI"
            lo "Actually, I think I'd much rather stay here."
            voice "j3_br2_IfAston"
            lo "If Aston shows up... I want to be here when he does."
            show pe sad
            voice "j3_br2_LorenzoWe"
            pe "Lorenzo... We can't leave you out here all alone."
            show ja neutral
            voice "j3_br2_PearlsRight"
            ja "Pearl's right, Lorenzo. And if you're worried, we could always leave a spare Walkie for him to use here."
            show lo sad
            voice "j3_br2_IJust"
            lo "I just... I can't leave. I'm sorry."
            "I can see that Lorenzo is also worried about his symptoms."
            "And I don't think he wants to bring those up now, either."
            voice "j3_br2_WellIf"
            wi "Well, if you insist. I trust your judgment, Lorenzo."
            voice "j3_br2_IllKeep"
            mo "I'll keep an eye on him, Wilbur."
            voice "j3_br2_ThankYouMyBoy"
            wi "Thank you, my boy."
            scene black with longfade
            stop ambience fadeout 4.0
            stop music fadeout 3.0
            "Wilbur and Jax walked Pearl back to C1 while I decided to stay with Lorenzo for a bit longer."
    
    else: # Both OK!
        "Back out in the cold again."
        "Aston and I are making our way towards Lorenzo's cabin."
        "Lorenzo's physical state has been rapidly improving over the last week."
        "His rashes have been healing nicely."
        "Aston says that Kyle's arm has been doing well, too, so it sounds like there are some comparable characteristics in the symptoms."
        "If there are no other complications, we can discharge him from the cabin tonight."
        show ast happy at left with dissolve
        with Pause(0.2)
        show ast with move:
            xpos 350
            yalign 1.0
        voice "j3_ExcitedTo"
        mo "Excited to see him? You're walking way faster than normal today."
        voice "j3_br1_YoudBetter"
        ast "You'd better catch up then."
        "Aston doesn't directly answer the question, but the smile on his face makes how he's feeling evident."
        scene cottage with longfade
        play music audio.light fadein 3.0
        show ast neutral at right
        show lo scared at centerright
        voice "j3_br1_AndYou"
        lo "And you said...what was growing out of him?"
        voice "j3_br1_MushroomsTons"
        mo "Mushrooms. Tons of them, stacked atop one another."
        voice "j3_br1_TheBody"
        ast "The body had also sustained several attacks on the torso region..."
        show ast inthought
        voice "j3_br1_WeStill"
        ast "We still aren't sure what kind of animal would leave it in such a state."
        voice "j3_br1_AndWhere"
        lo "And where did the dynamite come from?"
        voice "j3_br1_CantSay"
        mo "Can't say. We've only found fragments so far."
        show ast neutral
        voice "j3_br1_IfThere"
        mo "If there really was dynamite involved...that sound we heard right before the avalanche could very well have been the same explosion."
        "We fill him in on the situation that happened over the past few days."
        show lo sad
        voice "j3_br1_WowThis"
        lo "Wow, this is a lot to take in..."
        show ast happy
        voice "j3_br1_ButFor"
        ast "But, for a bit of good news... I think you're all set to come back to camp with us."
        show lo happy
        voice "j3_br1_YouThink"
        lo "You think so? Is it finally time, amore?"
        voice "j3_br1_WelcomeHome"
        mo "Welcome home, Lorenzo."

        with Pause(0.7)
        play sound knock
        show lo sad with None
        show ast neutral with None
        "*knock knock*"
        "Someone knocks loudly on the cabin's door."
        "The three of us turn to each other, then look back cautiously at the door."
        voice "j3_HelloAnyone"
        wi "Hello? Anyone in here?"
        show lo scared
        voice "j3_br1_IsIs"
        lo "Is... Is that Wilbur?"
        voice "j3_Wilbur"
        mo "Wilbur!"
        play music audio.light
        show lo smile with move:
            xpos 1300
            yalign 1.0
        show ast happy with move:
            xpos 1700
            yalign 1.0
        show ja happy at centerleft
        show wi happy at left
        show pe smile:
            xpos 180
            yalign 1.0
        with dissolve
        hide lo with None
        show lo smile with None:
            xpos 1300
            yalign 1.0
        "A wave of relief washes over us as three familiar faces greet us."
        "Wilbur, Jax and...Pearl?"
        show pe happy
        voice "j3_LorenzoOh" # Can remove branch tag if duped
        pe "Lorenzo! Oh boy, I've missed you so much!"
        show pe with move:
            xpos 1200
            yalign 1.0
        play sound jacket
        "Pearl runs towards him and gives him the biggest hug."
        show lo smile
        voice "j3_br1_HelloPearl"
        lo "Hello, Pearl."
        #show wi happy #If Wilbur has an alt bigger smile, maybe?
        voice "j3_br1_LassHere"
        wi "Lass here told us she followed you boys all the way out from camp."
        show pe sad with move:
            xpos 850
            yalign 1.0
        voice "j3_br1_IWas"
        pe "I was having nightmares about the shrooms and couldn't go back to sleep."
        show pe smile
        voice "j3_br1_ThenI"
        pe "Then I heard you guys gearing up, so I wanted to come along!"
        voice "j3_br1_ItsLovely"
        lo "It's lovely seeing you all."
        voice "j3_br1_IAlways"
        wi "I always had a feeling you'd made it out in one piece!"
        voice "j3_br1_WeNeed"
        ja "We need to have a reunion party at some point."
        voice "j3_br1_ImJust"
        pe "I'm just...so happy to see both of you here together. You know...in the same room, side by side?"
        show pe happy
        voice "j3_br1_IHavent"
        pe "I haven't seen Aston smile this much in, like, forever."
        "Aston's face flushes a little."
        voice "j3_br1_ISee"
        wi "I see that you have a setup here... How long have you been camping out?"
        show lo pondering
        show pe smile
        with dissolve
        voice "j3_br1_TheAvalanche"
        lo "The avalanche was...surprisingly kind to me."
        voice "j3_br1_ISuffered"
        lo "I suffered a few bruises here and there, but I was otherwise okay. This cabin wasn't too far from where I ended up..."
        voice "j3_br1_AndIve"
        lo "And I've been here ever since."
        show lo smile
        voice "j3_br1_ThenMorgan"
        lo "Then...Aston and Morgan found me a few days later, cowering under a blanket."
        show ja inthought
        voice "j3_br1_C2Never"
        ja "C2 never gave up the search, Lorenzo."
        show ja happy
        voice "j3_br1_WeTook"
        ja "We took turns every night, slowly expanding our search radius into the northern forest."
        voice "j3_br1_ButIt"
        ja "But it looks like we didn't need to do that after all. You guys had it covered."
        show ast sad
        voice "j3_br1_ImTruly"
        ast "I'm truly sorry, Jax. We didn't mean to mislead you, let alone keep you up at night."
        voice "j3_br1_NahIm"
        ja "Nah, I'm just glad you're alright! But...why hide from everyone? Why not go back to camp when they first found you?"
        show ast neutral
        voice "j3_br1_ItsA"
        mo "It's...a long story."
        voice "j3_br1_IDont"
        mo "I don't think we can finish it in one sitting."
        show wi neutral
        voice "j3_br1_WellI"
        wi "Well, I think we can leave storytime for later. What matters is that you're safe, my friend."
        voice "j3_br1_LetsHelp"
        wi "Let's help you pack, then we'll walk you home."
        voice "j3_br1_IdLove"
        lo "I'd love that."
        scene black with longfade
        stop music fadeout 2.0
        stop ambience fadeout 2.0

        scene forest2night with dissolve
        "The walk back to camp felt a lot lighter than usual."
        "Not only did we get the perfect conclusion to our search and rescue mission..."
        "We officially reunited the lovebirds."
        play music audio.light
        show pe confused at left
        voice "j3_br1_LorenzoAre"
        pe "Lorenzooooo, are you okay?"
        "Pearl turns around to check on him every once in a while."

        play sound rustle1
        show lo scared at right
        play sound snuggle
        show lo smile
        voice "j3_br1_IThink"
        lo "I think I haven't been using my legs in awhile."
        hide pe
        hide lo
        "Despite taking it in good stride, Lorenzo does seem to be struggling to keep up."
        
        show ast inthought at centerleft
        with dissolve
        
        voice "j3_br1_MorganCould"
        ast "Morgan, could you help me with this?"
        voice "j3_br1_SureGive"
        mo "Sure. Give it here."
        play sound backpacktoss
        scene black with dissolve
        "Aston chucks me his backpack and bends forward in front of Lorenzo, prompting him to hop on."
        voice "j3_br1_ICan"
        lo "I can walk fine, amore! I'll just-"
        voice "j3_br1_GetOn"
        ast "Get on. I'll carry you."
        voice "j3_br1_IfYou"
        lo "If you insist!"
        "The other four of us moved to the side so as to not get in the way."

        show cg lorenzobackpack
        voice "j3_br1_AwwwLook"
        pe "Awww, look at them!"
        voice "j3_br1_TheyLook"
        wi "They look good together, don't they, lass?"
        voice "j3_br1_PersonallyIm"
        ja "Personally, I'm a little jealous."
        voice "j3_br1_TakingOne"
        mo "Taking one for the team, Jax? I'd let you carry me back to camp."
        voice "j3_br1_IdMuch"
        ja "I'd much rather carry Pearl...she's lighter."
        # Some kind of zoom?

        show cg lorenzobackpack with Dissolve(1.6):
            zoom 1.7
            blur 0
            xalign 0.5
            yalign 0.2
        voice "j3_br1_GrazieAmore"
        lo "Grazie, amore."
        voice "j3_br1_AnythingFor"
        ast "Anything for you." 
        voice "j3_br1_WhatWas"
        lo "What was that?"
        voice "j3_br1_YouHeard"
        ast "You heard me."

        stop music fadeout 3.0
        stop ambience fadeout 2.0
        scene black with dissolve
        hide cg lorenzobackpack

label jan_4:
    scene camp1day with longfade
    $ current_day = _("January 4th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    if not aston_safe:
        if not pearl_safe:
            "I reached C1 at the crack of dawn."
            "I wasn't looking at the time. I hope I'm not too late to sneak back into camp."
            "I spent the last few hours trying to convince Lorenzo, but he never budged..."
            "Determined as ever to stay in the cabin."
            "I don't think he wants to talk to me anymore, after learning that Pearl's also missing."
            scene maintentday with fade
            play music audio.sad
            "As I entered the main tent, everyone's gaze was on me."
            "I guess I'm too late."
            show ky sad at left
            show gr angry at centerleft
            with dissolve
            voice "j4_br3_MorganWhere"
            gr "Morgan. Where were you?"

            menu j4GregConvo3:
                "Lie":
                    $ greg_sus += 1
                    voice "j4_br2_IUh"
                    mo "I, uh... I was out for a little walk."
                    voice "j4_br3_WilburWalkied"
                    gr "Wilbur Walkie-d me this morning. You can stop with the bullshit."
                "Tell the truth":
                    voice "j4_br2_WeFound"
                    mo "We found Lorenzo."
                    show ky happy
                    voice "j4_br2_YesNow"
                    ky "Yes! Now we can bring him home!"

            # Happens in either case

            voice "j4_br2_HeDoesnt"
            mo "He doesn't want to leave the cabin, though."
            show ky confused
            show gr confused
            with dissolve
            voice "j4_br2_ITried"
            mo "I tried, all night, to convince him to come back to us."
            show ky sad
            voice "j4_br3_PoorLorenzo"
            ky "Poor Lorenzo... I don't think he's taking it well."
            show gr neutral
            voice "j4_br3_WellWere"
            gr "Well, we're gonna have to bring him back today no matter what. How he feels about it is irrelevant."

            #EXT: whichever forest is en route (check earlier in Arc 2)
            scene forest2 with longfade 

            "Well, here goes another round of walking back to the cabin."
            "This time, with the rest of C1...or, at least, what's left of them."


            play sound kick # Some kind of snow walk cronch 
            scene black with fade

            "Lorenzo, although surprised, said nothing when he first saw us."
            "He and Gregory exchanged a few words while we stood outside."
            "We overheard them getting into a heated conversation, but hesitated to interfere."
            "In the end, an exhausted Lorenzo reluctantly agreed to follow us back to camp."
            "Gregory wasn't about to leave a sick campmate out in the cold, alone."
            scene black with dissolve
            "Still, Lorenzo left his Walkie on the shelf."
            "Holding onto hope that they're still out there."

        else: # Pearl OK, Aston gone
            "I reached C1 at the crack of dawn."
            "I wasn't looking at the time. I hope I'm not too late to sneak back into camp."
            "I spent the last few hours trying to convince Lorenzo, but he never budged..."
            "Determined as ever to stay in the cabin."
            scene maintentday with fade
            play music audio.sad
            "As I entered the main tent, everyone's gaze was on me."
            "I guess I'm too late."
            show pe sad at centerright
            show ky neutral at left
            show gr angry at centerleft
            with dissolve
            voice "j4_br2_MorganWhere"
            gr "Morgan. Where were you?"

            #CHOICE BRANCH

            menu j4GregConvo2:
                "Lie":
                    $ greg_sus += 1
                    voice "j4_br2_IUh"
                    mo "I, uh... I was out for a little walk."
                    "Pearl shifts around nervously."
                    show ky sad
                    voice "j4_br2_GregoryKnows"
                    pe "Gregory knows, Morgan... Wilbur gave him a call."
                "Tell the truth":
                    voice "j4_br2_WeFound"
                    mo "We found Lorenzo."
                    show ky happy
                    voice "j4_br2_YesNow"
                    ky "Yes! Now we can bring him home!"

            # Happens in either case
            show gr confused
            with dissolve
            voice "j4_br2_HeDoesnt"
            mo "He doesn't want to leave the cabin, though."
            voice "j4_br2_ITried"
            mo "I tried, all night, to convince him to come back to us."
            show pe depressed
            voice "j4_br2_HeStill"
            pe "He still wants to wait for Aston..."
            show gr neutral
            voice "j4_br2_WellWere"
            gr "Well, we're gonna have to bring him back today no matter what. How he feels about it is irrelevant."

            #EXT: whichever forest is en route (check earlier in Arc 2)
            scene forest2 with longfade 
            
            "Well, here goes another round of walking back to the cabin."
            "This time, with the rest of C1."

            play sound kick # Some kind of snow walk cronch 
            scene black with fade

            "Lorenzo, although surprised, said nothing when he first saw us."
            "He and Gregory exchanged a few words while we stood outside."
            "In the end, he reluctantly agreed to follow us back to camp." 
            "Gregory wasn't about to leave a sick campmate out in the cold, alone."
            "Still, Lorenzo left his Walkie on the shelf."
            "Holding onto hope that Aston is still out there."

    else: # Both OK
        "We neared C1 at the crack of dawn."
        "From afar, we could see Gregory and Kyle running in and out of the main tent."
        "They must be alarmed to see everyone else missing."
        "Kyle reaches for his Walkie and tries beeping somebody."
        "Oh, it's me."

        # Only Walkie thing in any of these branches
        if radio_static == "_s":
            voice "j4_MorganWhereIsEveryone_s"
        else:
            voice "j4_MorganWhereIsEveryone_c"
        # voice "j4_br1_MorganWhereIsEveryone[radio_static]"

        nvl clear
        wt_ky "Morgan? Where is everyone?"
        voice "j4_br1_JustTurn"
        wt_mo "Just turn around, Kyle."
        nvl clear

        play music audio.light fadein 1.0
        show ky sad at left
        "He looks up from his Walkie to see all of us walking back to the main tent."
        show ky neutral
        voice "j4_br1_LorenzoIs"
        ky "Lorenzo...? Is that you?"
        show lo smile at centerright
        voice "j4_br1_BuongiornoKyle"
        lo "Buongiorno, Kyle."
        show ky happy
        voice "j4_br1_OhMy"
        ky "Oh my goodness, Gregory! They're back and they have Lorenzo!"

        show gr worried at centerleft
        "Gregory looks tired, surprised and relieved as he walks out of the tent towards us."
        show lo sad
        voice "j4_br1_Gregory"
        lo "Gregory..."
        "Gregory reaches out to pat Lorenzo on the shoulder."
        show gr happy
        voice "j4_br1_GladTo"
        gr "Glad to have you back."
        show gr neutral
        show lo smile
        with dissolve

        "He notices that Wilbur and Jax are also here."
        show wi neutral at centerright behind lo
        show ja happy at right
        voice "j4_br1_HeyaGregory"
        ja "Heya, Gregory."
        voice "j4_br1_YouLook"
        wi "You look worse for wear my friend!"

        show gr angry
        voice "j4_br1_YouThink"
        gr "You think? Imagine waking up to your camp deserted."
        show ky smile
        voice "j4_br1_ButIm"
        ky "But I'm still here!"
        show gr neutral
        voice "j4_br1_ImagineWaking"
        gr "...imagine waking up to only see one other person when there should be three others."
        voice "j4_br1_SoWhat"
        gr "So, what is this? Aston, Morgan, Pearl - I think y'all have some explaining to do."
        "There it is. Okay...think, Morgan, think."
        hide wi
        hide ja
        hide ky
        with Dissolve(1.0)
        voice "j4_br1_AstonAnd"
        mo "Aston and I wanted to go on a night walk, but we took a different route and stumbled across a cabin."
        show ast neutral at right behind lo
        voice "j4_br1_LorenzoWas"
        mo "Lorenzo was sheltering inside."
        voice "j4_br1_AndWhy"
        gr "And why couldn't have you come back earlier?"
        show ast inthought
        voice "j4_br1_HisBelongings"
        ast "His belongings were lost in the avalanche."
        voice "j4_br1_WithNo"
        ast "With no map on hand and a broken Walkie, there's no way he could've made it back safely."
        voice "j4_br1_AndHow"
        gr "And...how did you last as long as you did without any food?"
        show lo pondering
        voice "j4_br1_TheCabin"
        lo "The cabin had enough supplies to last me for a month if I was frugal with it, so I was really fortunate."
        "Gregory eyes us suspiciously. I don't think he buys our story."
        show pe depressed at center behind gr 
        voice "j4_br1_TheRest"
        pe "The rest didn't know I tagged along... I'm sorry for wandering off without telling you."
        voice "j4_br1_IHeard"
        pe "I heard people gearing up, and I was so caught up in the moment that I didn't think."
        hide ast
        hide pe
        with dissolve
        show wi neutral at right
        voice "j4_br1_BlameIt"
        wi "Blame it on me, Gregory. I was the one that asked the rest to join me."
        show lo smile
        show wi happy
        voice "j4_br1_LooksLike"
        wi "Looks like it all worked out in the end!"
        "Wilbur plays along with our story."

        show gr confused
        voice "j4_br1_GregoryVNVR"
        gr "..."
        voice "j4_br1_ComeOn"
        wi "Come on, Greggy. Aren't you at least a little happy?"
        show gr angry
        voice "j4_br1_YeahSure"
        gr "Yeah, sure. But I need them to stop running away like that."
        voice "j4_br1_LightenUp"
        wi "Lighten up a little and maybe they'd be happier to stay."
        show gr scared with None
        "Oh damn, Wilbur."

        # ideally Gregory expression change that waits for completion before this next bit
        show gr neutral with Dissolve(1.0)
        voice "j4_br1_PointTaken"
        gr "...point taken."

        hide wi
        with dissolve
        show ast happy at right behind lo
        voice "j4_br1_AnywaySeeing"
        ast "Anyway, seeing as everyone's already up...shall we make breakfast?"
        show pe smile behind lo
        voice "j4_br1_IThought"
        pe "I thought you'd never ask! I'm starving."
        show ky happy at left
        voice "j4_br1_JoinUs"
        ky "Join us, guys!"
        hide ast
        hide gr
        with dissolve
        with Pause(0.5)
        show ky smile
        show ja happy at right
        with dissolve
        voice "j4_br1_IWant"
        ja "I want anything but tomato soup. I know you guys have loads of that."
        voice "j4_br1_ThatsGood"
        mo "That's good news for Pearl."
        show lo neutral
        show pe confused with move:
            xpos 700
        voice "j4_br1_DontYuck"
        pe "Don't yuck my yum, thank you."
        show wi happy at center
        with dissolve
        voice "j4_br1_AtLeast"
        wi "At least I know what to get for your birthday, Pearl."
        show pe happy
        voice "j4_br1_MoreSoup"
        pe "More soup?"
        "Wilbur just shrugs at Pearl."
        show ky happy
        voice "j4_br1_IThink"
        ky "I think we'd end up giving Pearl a garage full of tomatoes."
        hide pe
        hide wi
        hide ky
        hide ja
        with dissolve
        show ast smile behind lo
        "Aston turns to Lorenzo, who hasn't said anything in awhile."
        show ast inthought
        voice "j4_br1_AreYou"
        ast "Are you alright?"
        show lo smile
        voice "j4_br1_ItsJust"
        lo "It's just... It's great to be back."
        show ast happy

    stop music fadeout 3.0
    stop ambience fadeout 2.0
    scene black with longfade

label jan_5:
    $ current_day = _("January 5th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    scene black
    scene isaaklab2 with dissolve
    play music audio.neutral
    "Back at the RC, Isaak and Eva are just about to crack open the fungi samples that were collected the other day."
    "Other than the bits contaminated by dried blood, the samples are surprisingly clean."
    show isa neutral at centerleft
    voice "j5_IsThis"
    isa "Is this what was harvested from the body?"
    show ev inthought at centerright
    voice "j5_ApparentlySo"
    ev "Apparently so. Have you seen anything like this before, Isaak?"
    voice "j5_CantSay"
    isa "Can't say I have."
    show isa serious
    voice "j5_ThoughI"
    isa "Though I knew it could technically happen... Mold and fungi can grow almost anywhere."
    show ev worried
    voice "j5_StillThe"
    ev "Still, they way they described it..."
    voice "j5_ItsHard"
    ev "It's hard to imagine that all this would be growing out of a barely-decomposed body."
    show isa inthought
    "Isaak squints inquisitively at Koda's absence."
    voice "j5_IsThat"
    isa "Is that why it's just us today?"
    show ev happy
    voice "j5_IDontThinkKoda"
    ev "I don't think Koda can stomach that imagery, so I asked them to do lab clean-up and supply checks for my station."
    show isa serious with None
    voice "j5_TheyllNeed"
    isa "They'll need firmer resolve if they want to survive in this field."
    voice "j5_ImSure"
    ev "I'm sure it'll get better over time. I have full trust in them."
    show ev inthought
    voice "j5_AndIm"
    ev "And...{w=0.4}I'm pretty sure this is an uncommon situation that we're dealing with."
    show isa inthought
    "Isaak pauses for a moment and thinks."
    voice "j5_ComeTo"
    isa "Come to think of it, you two seemed like you knew each other before your assignment here."
    voice "j5_ImPretty"
    ev "I'm pretty sure we've mentioned that before, Isaak."
    show isa neutral
    voice "j5_IDontUsuallyPay"
    isa "I don't usually pay attention to anything outside of what's in front of me."

    voice "j5_KodasMy"
    ev "Koda's my junior. They were just a first-year student when I graduated."
    show ev neutral
    voice "j5_WhydYou"
    ev "Why'd you ask?"
    voice "j5_ImJust"
    isa "I'm just curious. You're always looking out for them."
    voice "j5_YeahBecause"
    ev "Yeah, because you're generally unapproachable."
    show isa inthought
    voice "j5_GregoryOnce"
    isa "...Gregory once said the same thing."
    show ev happy
    voice "j5_PerhapsIts"
    ev "Perhaps it's time to change?"
    show isa neutral
    voice "j5_IDontGetPaid"
    isa "I don't get paid to make friends...and, frankly, I don't have that kind of leisure time."
    voice "j5_WeHave"
    isa "We have limited mold samples to care for right now. Let's focus on the task at hand."
    show ev inthought
    voice "j5_YeahLets"
    ev "Yeah, let's. I wouldn't want you to turn it into mushroom stew when I'm not looking."
    show isa serious
    voice "j5_WereYou"
    isa "Were you always this irritating?"
    show ev happy
    voice "j5_LetsFocus"
    ev "Let's focus on the task at hand, Isaak."
    voice "j5_IsaakVNVR"
    isa "..."

    scene black with fade
    stop music fadeout 2.0
    with Pause(1.5)

label jan_6:
    $ current_day = _("January 6th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    play ambience amb_campnightwfire fadein 1.0
    if aston_safe:
        "It's the dead of night, but the campfire is still burning brightly."
        "Is someone else also having trouble sleeping?"

        scene camp1night with dissolve
        "I walk out to see the Aston and Lorenzo sitting side by side at the fire."
        "They're having a great time, from what I can tell. I don't think I've ever seen Aston laugh like this before."
        "I'm sure they feel a huge weight lifted off their shoulders keeping that secret."
        "And for my part, I don't have to do night shifts with Aston anymore."
        "Goodbye to my irregular sleeping schedule..."
        scene black with fade
        "And welcome back to my decent amount of sleep."
        stop ambience fadeout 1.0
        stop music fadeout 2.0
        scene black
        with Pause(1.2)

    else: # No Aston
        "It's the dead of night, but the campfire is still burning brightly."
        "Is someone else also having trouble sleeping?"

        scene camp1night with dissolve
        "I walk out to see Lorenzo sitting outside by himself next to the fire."
        if pearl_safe:
            "I should check up on him."
            show lo sad at centerright
            voice "j6_HowAre"
            mo "How are you doing?"
            voice "j6_IFeel"
            lo "I feel safer here with everyone but... I don't feel great."
            voice "j6_ICan"
            mo "I can imagine... I'm sorry, Lorenzo."
            voice "j6_ButHey"
            mo "But, hey - Wilbur's overruled Gregory's no-search-mission orders."
            voice "j6_AndYoure"
            mo "And you're not going to be alone in this anymore."

        else: # No Pearl, no Aston
            "I should check up on him...and also try to make up for not telling him sooner."
            show lo sad at centerright
            voice "j6_LorenzoId"
            mo "Lorenzo... I'd like to apologize."
            voice "j6_YouDont"
            lo "You don't have to, Morgan."
            voice "j6_IWish"
            lo "I wish you'd told me earlier...about Pearl."
            voice "j6_ButI"
            lo "But I know you were just looking out for me."
            voice "j6_IDidnt"
            mo "I didn't want to make things feel any worse for you. That's all."
            voice "j6_EspeciallyNot"
            mo "Especially not when you were out there alone."

        # Happens either branch where Aston gone

        show lo neutral
        voice "j6_IWas"
        lo "I was never really alone to begin with."
        voice "j6_Bear"
        mo "Bear?"
        show lo sick
        voice "j6_BearStill"
        lo "Bear. Still stalking, still talking."
        voice "j6_StillHim"
        lo "Still...{w=1.25}him."

        # Unsprite the Lorenzo
        hide lo
        "Lorenzo buries his face in his hands."
        "He doesn't say anything after that."
        stop ambience fadeout 1.0
        stop music fadeout 2.0
        scene black
        with Pause(1.8)

label jan_7:
    $ current_day = _("January 7th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    scene maintentday with dissolve
    play music audio.neutral
    "As I was cleaning up after breakfast, I heard voices coming from outside the main tent."

    scene camp1day with fade
    if pearl_safe:
        show pe happy at centerright
        show ky smile at centerleft
        with dissolve
        voice "j7_OkayOkay"
        pe "Okay, okay, I'm sat! I've got snacks and I'm ready for the lore drop!"
        "It seems like Pearl and Kyle have a 3-way Walkie setup going."
        "Kyle notices me approaching."
        voice "j7_MorganCome"
        ky "Morgan! Come sit with us!"

    else: #Pearl nuh uh
        show ky confused at centerleft
        voice "j7_OkayI"
        ky "Okay... I think it's working now, Koda!"
        "A 3-way Walkie... I've seen this before."
        "Kyle notices me approaching."
        show ky smile
        voice "j7_HeyMorgan"
        ky "Hey, Morgan! Wanna join me?"

    voice "j7_DavosWas"
    ky "Davos was just about to drop some village lore!"
    voice "j7_VillageLore"
    mo "Village lore? I'm listening."

    # Walkie call
    
    # VERY scuffed way of doing it, but it works

    if radio_static == "_s":
        voice "j7_OkaySoLikeMy_s"
    else:
        voice "j7_OkaySoLikeMy_c"
    $ chibi_davos = "images/chibi/davos_happy.png"
    wt_da "Okay so, like, my pops was telling me about the village the other day."
    
    if radio_static == "_s":
        voice "j7_ApparentlyThe_s"
    else:
        voice "j7_ApparentlyThe_c"
    $ chibi_davos = "images/chibi/davos_neutral.png"
    wt_da "Apparently, the villagers don't like going to the river that much."
    
    if radio_static == "_s":
        voice "j7_AndIts_s"
    else:
        voice "j7_AndIts_c"
    wt_da "And it's because many years ago a woman drowned in it, so BAM- It's haunted!"

    if pearl_safe:
        voice "j7_YouKinda"
        wt_pe "You kinda suck at telling stories, Davos. There's literally no build-up."
        
        if radio_static == "_s":
            voice "j7_ImWaiting_s"
        else:
            voice "j7_ImWaiting_c"
        wt_da "I'm waiting for what's called audience participation. Quick, ask me questions!"
        
        voice "j7_OkaySoWhatsHaunting"
        wt_pe "Okay... So what's haunting the river? The same woman?"
    
    else: # Pearl nuh uh
        if radio_static == "_s":
            voice "j7_WhatDo_s"
        else:
            voice "j7_WhatDo_c"
        $ chibi_koda = "images/chibi/koda_worried.png"
        wt_ko "What do you mean by 'haunted,' Davos? You can't just end the story there."

    if radio_static == "_s":
        voice "j7_TheyveNever_s"
    else:
        voice "j7_TheyveNever_c"
    wt_da "They've never found her body, but they've seen her spirit!"

    $ chibi_kyle = "images/chibi/kyle_worried.png"
    voice "j7_SoTheres"
    wt_ky "So there's still a human body in the body of water?"
    $ chibi_morgan = "images/chibi/morgan_neutral.png"
    voice "j7_AndBy"
    wt_mo "And by spirit...you mean the villagers spotted a floating entity?"

    if radio_static == "_s":
        voice "j7_YeahAnd_s"
    else:
        voice "j7_YeahAnd_c"
    $ chibi_davos = "images/chibi/davos_happy.png"
    wt_da "Yeah, and her head isn't where her head's supposed to be."

    if radio_static == "_s":
        voice "j7_WWhatIs_s"
    else:
        voice "j7_WWhatIs_c"
    $ chibi_koda = "images/chibi/koda_worried.png"
    wt_ko "W-What is that supposed to mean?"

    if radio_static == "_s":
        voice "j7_IveNever_s"
    else:
        voice "j7_IveNever_c"
    $ chibi_davos = "images/chibi/davos_worried.png"
    wt_da "I've never actually asked the details... It's just not there, I suppose?"
    
    voice "j7_SureWilburs"
    wt_mo "Sure Wilbur's not messing with you, Davos?"
    $ chibi_morgan = "images/chibi/morgan_happy.png"
    voice "j7_SoundsLike"
    wt_mo "Sounds like one of those stories designed to warn kids about the dangers of drowning by scaring them."

    if radio_static == "_s":
        voice "j7_MyPops_s"
    else:
        voice "j7_MyPops_c"
    wt_da "My pops? Nah, he never lies to me."

    if radio_static == "_s":
        voice "j7_BesidesThe_s"
    else:
        voice "j7_BesidesThe_c"
    $ chibi_davos = "images/chibi/davos_happy.png"
    wt_da "Besides, the only person this story is scaring is Koda."

    if radio_static == "_s":
        voice "j7_ShutUp_s"
    else:
        voice "j7_ShutUp_c"
    $ chibi_koda = "images/chibi/koda_neutral.png"
    wt_ko "Shut up, Davos."

    if radio_static == "_s":
        voice "j7_MaybeYoull_s"
    else:
        voice "j7_MaybeYoull_c"
    $ chibi_davos = "images/chibi/davos_happy.png"
    wt_da "Maybe you'll find her hiding under your bed tonight. Ooh, or floating through the walls!"

    if radio_static == "_s":
        voice "j7_HowAm_s"
    else:
        voice "j7_HowAm_c"
    $ chibi_koda = "images/chibi/koda_worried.png"
    wt_ko "How am I supposed to sleep tonight, Davos?"

    if radio_static == "_s":
        voice "j7_AfraidMaybe_s"
    else:
        voice "j7_AfraidMaybe_c"
    $ chibi_davos = "images/chibi/davos_neutral.png"
    wt_da "Afraid. Maybe with one eye open, too."

    if pearl_safe:
        voice "j7_YouCan"
        wt_pe "You can always come join us at camp if you're too scared to sleep alone!"
    else:
        voice "j7_IfYoure"
        $ chibi_kyle = "images/chibi/kyle_neutral.png"
        wt_ky "If you're worried about ghosts, you could always come stay with us!"

    if radio_static == "_s":
        voice "j7_C1And_s"
    else:
        voice "j7_C1And_c"
    $ chibi_koda = "images/chibi/koda_neutral.png"
    wt_ko "C1 and C2 are much closer in proximity to the village, so I'll pass, thank you."
    
    $ chibi_kyle = "images/chibi/kyle_happy.png"
    voice "j7_WeCan"
    wt_ky "We can go to you, then!"

    if radio_static == "_s":
        voice "j7_IsaakWould_s"
    else:
        voice "j7_IsaakWould_c"
    $ chibi_koda = "images/chibi/koda_worried.png"
    wt_ko "Isaak would skin me alive if I invited anyone over without permission."

    voice "j7_SoBetween"
    $ chibi_morgan = "images/chibi/morgan_neutral.png"
    wt_mo "So...between the ghost lady and Isaak, who do you think is scarier?"

    if radio_static == "_s":
        voice "j7_IsaakFor_s"
    else:
        voice "j7_IsaakFor_c"
    $ chibi_koda = "images/chibi/koda_neutral.png"
    wt_ko "Isaak. For sure. Just, uh...don't tell him I said that, please..."

    scene black with fade
    nvl clear
    stop music fadeout 2.0
    stop ambience fadeout 1.0
    scene black

label jan_8:
    $ current_day = _("January 8th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    scene waterbody with dissolve
    "Today marks the second week of the new year, and we're starting off with week two with some classic sample collection."
    "Collecting samples is something I look forward to now."
    "As mundane as it is, the predictability is honestly relaxing. "
    "Every day, you see dirt and snow, and you dig 'em up."
    "Every day, you see some nasty lake water, and you take some."
    "And every day, you...take a look at the trees..."

    voice "j8_WaitWhat" 
    mo "Wait...what is this?"

    scene forest2 with dissolve
    play music audio.anxious fadein 3.0
    "I take it back."
    "I remember seeing claw marks on trees and assumed that it was a natural scratching post for the wildlife."
    "This is very different."
    "I move closer to it to examine the size of the markings."
    "Whatever left these here...had claws half the width of my forearm."
    "And that's to say nothing of the greenish substance left in a thin film over the bark."
    "I'm glad this tree is still standing, but I feel like if I gave it a kick with enough force, it'd snap and fall over."
    "But I'm not about to coat my boots in this green goo, so..."
    scene black with dissolve
    "Oh, well."
    "So much for predictability..."
    stop music fadeout 5.0
    "I'd be a talented psychic if I could predict discovering shit like this."

    scene black
    stop ambience fadeout 1.0
    with Pause(2.5)

label jan_9:
    $ current_day = _("January 9th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    scene maintentday with dissolve
    play music audio.light

    # WALKIE

    # Realistically, you should be able to do this just through stuff like "voice 'j9_br2_HeyaC1[radio_static],'" but something about appending the variable at the end
    # is giving Ren'Py a bit of trouble in parsing the filename. So, how I've presently done it is scuffed beyond belief, but the key thing's that it works. -Jett
    if not aston_safe:
        if radio_static == "_s":
            voice "j9_br2_HeyaC1_s"
        else:
            voice "j9_br2_HeyaC1_c"
        $ chibi_cassie = "images/chibi/cassie_neutral.png"
        wt_ca "Heya, C1! How's everyone doing?"

        "Cassie's voice comes through the radio in the main tent."
        voice "j9_br2_ImGood"
        $ chibi_morgan = "images/chibi/morgan_neutral.png"
        wt_mo "I'm good, Cassie. Lorenzo's here with me."
        
        if radio_static == "_s":
            voice "j9_br2_AwesomeAnd_s"
        else:
            voice "j9_br2_AwesomeAnd_c"
        $ chibi_cassie = "images/chibi/cassie_happy.png"
        wt_ca "Awesome...and welcome back, Lorenzo! How does the sleeping bag feel?"

        voice "j9_br2_IKind"
        # $ chibi_lorenzo = "images/chibi/lorenzo_worried.png"
        wt_lo "I...kind of miss the armchair I had in the cabin. The sleeping bag's a little less comfortable, but it's good to be closer to everyone."
        
        if radio_static == "_s":
            voice "j9_ThatsSweet_s"
        else:
            voice "j9_ThatsSweet_c"
        $ chibi_ruran = "images/chibi/ruran_happy.png"
        wt_ru "That's sweet, Lorenzo."

        if radio_static == "_s":
            voice "j9_AnywayWere_s"
        else:
            voice "j9_AnywayWere_c"
        $ chibi_ruran = "images/chibi/ruran_neutral.png"
        wt_ru "Anyway, we're here to talk about our long-awaited camp merging. For a different reason this time."

        if radio_static == "_s":
            voice "j9_DavosAnd_s"
        else:
            voice "j9_DavosAnd_c"
        wt_ru "Davos and Jax began showing symptoms of a common cold this morning, and I think it's far too much of a coincidence for us to keep falling sick like this."
        
        if radio_static == "_s":
            voice "j9_HenceWere_s"
        else:
            voice "j9_HenceWere_c"
        $ chibi_morgan = "images/chibi/morgan_neutral.png"
        wt_ca "Hence, we're calling for a quarantine camp!"

        voice "j9_AQuarantine"
        wt_mo "A quarantine camp?"

        if radio_static == "_s":
            voice "j9_br2_SoFar_s"
        else:
            voice "j9_br2_SoFar_c"
        $ chibi_ruran = "images/chibi/ruran_worried.png"
        wt_ru "So far we've had Kyle's rashes, Cassie and her insomnia, and now cold symptoms..."

        if radio_static == "_s":
            voice "j9_br2_WilburAnd_s"
        else:
            voice "j9_br2_WilburAnd_c"
        $ chibi_ruran = "images/chibi/ruran_neutral.png"
        wt_ru "Wilbur and I figured it'll be much easier to manage everyone's symptoms and the spread of illness with a quarantine camp...since it's just me right now."
        
        voice "j9_br2_GotIt"
        wt_mo "Got it. That sounds good, Ruran. We'll be sure to bring this up to Gregory."

    else: # Aston OK!
        if radio_static == "_s":
            voice "j9_br1_HeyaC1_s"
        else:
            voice "j9_br1_HeyaC1_c"
        $ chibi_cassie = "images/chibi/cassie_neutral.png"
        wt_ca "Heya, C1 campers! How's everyone doing?"

        "Cassie's voice comes through the radio in the main tent."
        voice "j9_br1_WereGood"
        $ chibi_morgan = "images/chibi/morgan_neutral.png"
        wt_mo "We're good, Cassie. Lorenzo and Aston are here with me."

        if radio_static == "_s":
            voice "j9_br1_AwesomeAnd_s"
        else:
            voice "j9_br1_AwesomeAnd_c"
        $ chibi_cassie = "images/chibi/cassie_happy.png"
        wt_ca "Awesome...and, hi, Lorenzo! How does the sleeping bag feel?"
        
        voice "j9_br1_IDidnt"
        # $ chibi_lorenzo = "images/chibi/lorenzo_happy.png"
        wt_lo "I didn't miss sleeping on packed snow, but at least now it's warmer with company."
        
        if radio_static == "_s":
            voice "j9_ThatsSweet_s"
        else:
            voice "j9_ThatsSweet_c"
        $ chibi_ruran = "images/chibi/ruran_happy.png"
        wt_ru "That's sweet, Lorenzo."

        if radio_static == "_s":
            voice "j9_AnywayWere_s"
        else:
            voice "j9_AnywayWere_c"
        $ chibi_ruran = "images/chibi/ruran_neutral.png"
        wt_ru "Anyway, we're here to talk about our long-awaited camp merging. For a different reason this time."

        if radio_static == "_s":
            voice "j9_DavosAnd_s"
        else:
            voice "j9_DavosAnd_c"
        wt_ru "Davos and Jax began showing symptoms of a common cold this morning, and I think it's far too much of a coincidence for us to keep falling sick like this."
        
        if radio_static == "_s":
            voice "j9_HenceWere_s"
        else:
            voice "j9_HenceWere_c"
        $ chibi_cassie = "images/chibi/cassie_neutral.png"
        wt_ca "Hence, we're calling for a quarantine camp!"

        voice "j9_AQuarantine"
        wt_mo "A quarantine camp?"

        voice "j9_br1_SoFar"
        # $ chibi_aston = "images/chibi/aston_worried.png"
        wt_ast "So far we've had rashes, unexplainable insomnia and now cold symptoms..."
        voice "j9_br1_ItllBe"
        # $ chibi_aston = "images/chibi/aston_neutral.png"
        wt_ast "It'll be much easier for us to keep an eye on symptoms and control the spread of illness with everyone together."
        voice "j9_br1_WeCan"
        wt_ast "We can keep everyone accounted for and anticipate more people falling sick."

        if radio_static == "_s":
            voice "j9_ThatsRight_s"
        else:
            voice "j9_ThatsRight_c"
        wt_ru "That's right."

        voice "j9_br1_WellBring"
        wt_ast "We'll bring this up to Gregory, then. Thank you, Ruran."
    nvl clear
    stop music fadeout 2.0
    scene black with longfade
    with Pause(1.5)

label jan_10:
    $ current_day = _("January 10th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    scene black
    scene forest2 with dissolve
    show gr neutral
    show ky smile at centerright
    with dissolve

    play music audio.neutral fadein 1.5
    "Gregory received a beep while we were out in the field."

    # WALKIE
    
    if radio_static == "_s":
        voice "j10_GregoryAre_s"
    else:
        voice "j10_GregoryAre_c"
    $ chibi_isaak = "images/chibi/isaak_neutral.png"
    wt_is "Gregory, are you away from camp?"
    # $ chibi_gregory = "images/chibi/gregory_neutral.png"
    voice "j10_YesIsaak"
    wt_gr "Yes, Isaak."

    if radio_static == "_s":
        voice "j10_GoodWe_s"
    else:
        voice "j10_GoodWe_c"
    wt_is "Good. We have an update for you."
    

    if radio_static == "_s":
        voice "j10_WeveWell_s"
    else:
        voice "j10_WeveWell_c"
    $ chibi_eva = "images/chibi/eva_neutral.png"
    wt_ev "We've...well, for better or for worse, found that there's a correlation between the bird carcasses and the new fungus samples that we've found."
    
    $ chibi_morgan = "images/chibi/morgan_neutral.png"
    voice "j10_DidntYou"
    wt_mo "Didn't you guys also find traces of fungi in the lake?"
    
    if radio_static == "_s":
        voice "j10_YesThats_s"
    else:
        voice "j10_YesThats_c"
    wt_ev "Yes, that's correct. All are similar strands of fungi, though we still don't have a firm explanation as to why this is happening."
    
    voice "j10_ItsLike"
    $ chibi_kyle = "images/chibi/kyle_worried.png"
    wt_ky "It's like everything is melting into a pot of goo!"

    if radio_static == "_s":
        voice "j10_HelloKyle_s"
    else:
        voice "j10_HelloKyle_c"
    $ chibi_eva = "images/chibi/eva_happy.png"
    wt_ev "Hello, Kyle! And, yes it does seem that way, doesn't it?"

    voice "j10_SoWhatDoYall"
    wt_gr "So, what do y'all need? More of everything?"

    if radio_static == "_s":
        voice "j10_TheUsual_s"
    else:
        voice "j10_TheUsual_c"
    wt_is "The usual, yes. Until I have enough."
    voice "j10_ThatDoesnt"
    wt_gr "That doesn't help gauge how much we actually need to grab, but...sure."

    voice "j10_WhereDo"
    wt_gr  "Where do you even plan on storing these samples, anyway? It's like you never run out of space."

    if radio_static == "_s":
        voice "j10_ThatsA_s"
    else:
        voice "j10_ThatsA_c"
    wt_is "That's a problem for the supply team, not me."
    
    if radio_static == "_s":
        voice "j10_YouAlso_s"
    else:
        voice "j10_YouAlso_c"
    $ chibi_eva = "images/chibi/eva_neutral.png"
    wt_ev "You also make it Koda's problem."
    
    if radio_static == "_s":
        voice "j10_IsaakVNVR_s"
    else:
        voice "j10_IsaakVNVR_c"
    wt_is "..."
    "Sheesh, Eva... But, good of her to stand up for Koda."
    
    $ chibi_kyle = "images/chibi/kyle_neutral.png"
    voice "j10_SoWhatYoureSaying"
    wt_ky "So... What you're saying is you want animals, you want shrooms, and you want shrooms from animals?"

    if radio_static == "_s":
        voice "j10_IfThat_s"
    else:
        voice "j10_IfThat_c"
    wt_is "If that helps with your understanding, Kyle... Yes."
    
    voice "j10_OkayGot"
    wt_ky "Okay, got it!"

    $ chibi_kyle = "images/chibi/kyle_worried.png"
    voice "j10_ThoughI"
    wt_ky "Though I really hope we find more animals alive than dead..."
    
    if radio_static == "_s":
        voice "j10_IfTheyre_s"
    else:
        voice "j10_IfTheyre_c"
    wt_is "If they're dead, they can't bite you."

    voice "j10_KyleVNVR"
    wt_ky "..."

    voice "j10_YouveJust"
    wt_mo "You've just got to stop reaching your hand out to every fluffy creature you see, Kyle."
    voice "j10_ButTheyre"
    wt_ky "But they're so friend-shaped..."
    nvl clear

    hide ky
    hide gr
    with dissolve
    scene forest2
    with Pause(0.2)
    "What happened to the main goal of finding penicillin?"
    "Will collecting more of these really help with the operation?"
    "If anything, I wouldn't want to consume medicine sourced and freshly harvested from the dead."
    "That sounds kinda messed up."
    "With the profiles that I found in Gregory's storage box, I can't help but think that they're trying to find something entirely different."
    
    stop music fadeout 2.0
    scene black with longfade
    with Pause(2.0)
    # Transition into Arc 3; yeehaw!
    jump tr_jan_11










