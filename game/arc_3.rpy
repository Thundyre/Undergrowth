label jan_11:
    #Arc 3 start
    $ current_day = _("January 11th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    #Scene transition: Fade to black, then fade back in slowly
    scene bg snowyplain with dissolve
    play ambience amb_icebody fadein 1.0
    "Out in the snow once more." 
    "What were we collecting today…?"
    "Oh, right… I needed to grab something out here…I think."
    "Roughly where Gregory marked on my map this morning."

    voice "j11_NowWhere"
    mo "Now… Where am I?"

    "I gaze up and back down to my map."
    "The terrain doesn't feel familiar in the slightest, but I couldn't have gone that far from camp."
    "I'm sure I'll recognize the side of the mountain, at least."
    "Can't get too lost with a waypoint I can see from afar."

    #CHOICE BRANCH START
    #Choices here don't actually matter but there will be three instances of: Left Right choices 

    "Anyway, which direction was I going…?"
    #Jumps may not be necessary, so feel free to change
    menu dir1:
        "Left":
            "I don't recognize this place on my map."
            "There's no trail here."
            jump dir2
        "Right":
            "I don't recognize this place on my map."
            "There's no trail here."
            jump dir2
    menu dir2:
        "Left":
            "How far did I wander off…?"
            "Or did my compass suddenly decide to stop working today?"
            voice "j11_YoMorgan"
            el "Yo, Morgan! Can you hear me?"
            "Elliot?"
            voice "j11_MorganThis"
            el "Morgan, this way!" 
            jump dir3
        "Right":
            "How far did I wander off…?"
            "Or did my compass suddenly decide to stop working today?"
            voice "j11_YoMorgan"
            el "Yo, Morgan! Can you hear me?"
            "Elliot?"
            voice "j11_MorganThis"
            el "Morgan, this way!" 
            jump dir3
    menu dir3:
        "Left":
            voice "j11_NoThats"
            el "No…that's your left, dummy."
        "Right":
            voice "j11_YoureAlmost"
            el "You're almost there!"
    "Elly's voice guides me to the edge of the lake."
    voice "j11_Elly"
    mo "Elly…?"
    voice "j11_YouKnow"
    el "You know…you look really different."
    voice "j11_WhatDo"
    mo "What do you mean?"
    "I peer into the lake, my own face reflecting off the water's surface."
    voice "j11_WellFor"
    el "Well, for starters…your hair's a lot longer. I dig it!"
    voice "j11_ButYou"
    el "But, hmmm... You also feel different. Something's wrong."
    voice "j11_WellYeah"
    mo "Well, yeah - I don't see you anywhere. Where are you?"
    "Elly never answers my question."
    if not aston_safe:
        #If Aston nuh uh
        voice "j11_NoI"
        el "No, I meant more along the lines of…I don't know…how did you even lose him in the forest?"
        voice "j11_TheMorgan"
        el "The Morgan I knew would've paid more attention. If he were here, perhaps things would be different for Aston now."
        voice "j11_PoorLorenzo"
        el "Poor Lorenzo…"
        if not pearl_safe:
            voice "j11_AndPearl"
            el "And Pearl… She didn't deserve that, did she?"
            voice "j11_WhereDo"
            el "Where do you think she ended up?"
            voice "j11_ComeOn"
            el "Come on, guess!"
        voice "j11_CutItOutElly"
        mo "Cut it out, Elly."
        voice "j11_IDontKnow"
        mo "I don't know what kind of sick joke you're playing, but this is not how I imagined our reunion going."

    else:
        voice "j11_ButIt"
        el "But it could just be just my imagination."
        voice "j11_YoureDoing"
        el "You're doing…as well as you possibly could be. {w=0.8}For now."
        voice "j11_CutItOutEllyThatsNot"
        mo "Cut it out, Elly. That's not funny."

    voice "j11_ItsBeen"
    el "It's been two months, Morgan. You better hurry it up before I have to tag you out!"
    voice "j11_WhatThe"
    mo "...what the fuck does that even mean?"
    voice "j11_TagMe"
    mo "Tag me out from what?"
    voice "j11_IllSee"
    el "I'll see you later, Morgan!"
    voice "j11_Wait"
    mo "Wait-"

    stop ambience fadeout 0.5
    scene black with longfade
    with Pause(0.4)
    scene bg maintent_night with dissolve

    if not aston_safe:
        if not pearl_safe:
            "I was suddenly jolted awake from my sleep."
            show ky shaken
            voice "j11_OhMorgan"
            ky "Oh, Morgan… I was so worried."
            "Kyle helped me sit upright."
            show ky smile
            voice "j11_HereI"
            ky "Here… I got you something to drink."
            "I nodded at Kyle as thanks."

        else:
            voice "j11_Morgan"
            pe "... Morgan!"
            show pe sad
            "Pearl shakes my shoulders."
            voice "j11_YouLook"
            pe "You look like you were having a bad dream…"
            voice "j11_IThink"
            mo "I-I think I need some water."
            show pe neutral
            voice "j11_IllBe"
            pe "I'll be right back!"
            "She leaves my side to grab a bottle for me."

    else:
        show ast sad
        show pe sad at centerleft
        with dissolve
        voice "j11_MorganYou"
        ast "Morgan? You were talking in your sleep."
        "Aston nudges me awake."
        voice "j11_YoureShaking"
        pe "You're shaking, Morgan…"
        "I look down at my hands. Sure enough… I was trembling."
        voice "j11_IThink"
        mo "I-I think I need some water."
        hide ast
        "Aston nods and gets up to grab me a bottle."
        "And Pearl takes both my hands in hers."
        "It was only then I noticed how cold my own fingers were in comparison to hers, even through the gloves."

    scene maintentnight
    "…"
    "What the hell was that dream…?"
    "Was that…really Elly?"
    stop ambience fadeout 3.0

label jan_12:
    scene black with longfade
    $ current_day = _("January 12th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    with Pause(0.3)
    if not aston_safe:
        if not pearl_safe:
            "After our call with Ruran the other day, we brought up the idea of merging camps to Gregory."
            "He agreed more easily than I expected."
            "So today…is our long-awaited camp merging day."
            play music audio.light
            scene bg walkpath with fade
            "This time, we approached it in a different way."
            "Gregory and Wilbur went straight ahead to our new camp's destination without carrying any of our heavier gear up the mountain."
            "A lookout, scouting type of role."
            "If and when they notice anything amiss… We'll be the first to know."
            "Real-time updates through the Walkie should prevent a repeat of last month's events."

            #Beep walkie time, Aston and Pearl dead

            #voice "j12_OkayWilbur[radio_static]"
            if radio_static == "_s":
                voice "j12_OkayWilbur_s"
            else:
                voice "j12_OkayWilbur_c"
            # $ chibi_gregory = "images/chibi/gregory_neutral.png"
            wt_gr "Okay, Wilbur and I are at the summit. We've cleared the area, and y'all should be safe to leave camp."
            
            if radio_static == "_s":
                voice "j12_ThoughBe_s"
            else:
                voice "j12_ThoughBe_c"
            wt_gr "Though…be careful on the way up. There's lots of fallen tree branches up the trail."

            if radio_static == "_s":
                voice "j12_br2_BetterLate_s"
            else:
                voice "j12_br2_BetterLate_c"
            $ chibi_wilbur = "images/chibi/wilbur_neutral.png"
            wt_wi "Better late than never! So, please, take whatever time you need."

            voice "j12_br2_WellBeThereIn"
            $ chibi_morgan = "images/chibi/morgan_worried.png"
            wt_mo "We'll be there in about another hour, I think."

            if radio_static == "_s":
                voice "j12_LooksLike_s"
            else:
                voice "j12_LooksLike_c"
            $ chibi_cassie = "images/chibi/cassie_neutral.png"
            wt_ca "Looks like it's…roughly two hours on our end."
        else:
            "After our call with Ruran the other day, we brought up the idea of merging camps to Gregory."
            "He agreed more easily than I expected."
            "So today…is our long-awaited camp merging day."
            "Or, as Pearl said earlier, 'camp merging 2.0.'"
            play music audio.light
            scene bg walkpath with fade
            "This time, we approached it in a different way."
            "Gregory and Wilbur went straight ahead to our new camp's destination without carrying any of our heavier gear up the mountain."
            "A lookout, scouting type of role."
            "If and when they notice anything amiss… We'll be the first to know."
            "Real-time updates through the Walkie should prevent a repeat of last month's events."
            
            #Beep boop walkie start (but Aston's dead)
            if radio_static == "_s":
                voice "j12_OkayWilbur_s"
            else:
                voice "j12_OkayWilbur_c"
            # $ chibi_gregory = "images/chibi/gregory_neutral.png"
            wt_gr "Okay, Wilbur and I are at the summit. We've cleared the area, and y'all should be safe to leave camp."
            
            if radio_static == "_s":
                voice "j12_ThoughBe_s"
            else:
                voice "j12_ThoughBe_c"
            wt_gr "Though…be careful on the way up. There's lots of fallen tree branches up the trail."

            if radio_static == "_s":
                voice "j12_br2_BetterLate_s"
            else:
                voice "j12_br2_BetterLate_c"
            $ chibi_wilbur = "images/chibi/wilbur_neutral.png"
            wt_wi "Better late than never! So, please, take whatever time you need."

            voice "j12_br2_WellBeThereIn"
            $ chibi_morgan = "images/chibi/morgan_worried.png"
            wt_mo "We'll be there in about another hour, I think."

            if radio_static == "_s":
                voice "j12_LooksLike_s"
            else:
                voice "j12_LooksLike_c"
            $ chibi_cassie = "images/chibi/cassie_neutral.png"
            wt_ca "Looks like it's…roughly two hours on our end."


            if radio_static == "_s":
                voice "j12_ObligatoryQuestion_s"
            else:
                voice "j12_ObligatoryQuestion_c"
            wt_da "Obligatory question, Pearl - did you remember your-"

            voice "j12_CompassYes"
            # $ chibi_pearl = "images/chibi/pearl_happy.png"
            wt_pe "Compass? Yes, I did this time!"
            voice "j12_ICan"
            # $ chibi_lorenzo = "images/chibi/lorenzo_neutral.png"
            wt_lo "I can attest to that…though she did grab mine by mistake first."
            voice "j12_br2_HushLorenzo"
            # $ chibi_pearl = "images/chibi/pearl_worried.png"
            wt_pe "Hush, Lorenzo!"

            if radio_static == "_s":
                voice "j12_OhYeah_s"
            else:
                voice "j12_OhYeah_c"
            $ chibi_davos = "images/chibi/davos_happy.png"
            wt_da "Oh, yeah! I forgot to mention this earlier, but Koda's on the Walkie with us, too!"

            if radio_static == "_s":
                voice "j12_ThisMorning_s"
            else:
                voice "j12_ThisMorning_c"
            $ chibi_davos = "images/chibi/davos_neutral.png"
            wt_da "This morning, they were all like, 'Have you left yet? Is everyone okay? Did you bring enough supplies? Please don't explode on the way up-'"
            
            if radio_static == "_s":
                voice "j12_YeahYeah_s"
            else:
                voice "j12_YeahYeah_c"
            $ chibi_koda = "images/chibi/koda_worried.png"
            wt_ko "Yeah, yeah. I'm paranoid, I know."

            if radio_static == "_s":
                voice "j12_IJust_s"
            else:
                voice "j12_IJust_c"
            $ chibi_koda = "images/chibi/koda_neutral.png"
            wt_ko "I just want to make sure you guys all get there in one piece."
            
            voice "j12_WorriedFor"
            $ chibi_kyle = "images/chibi/kyle_neutral.png"
            wt_ky "Worried for us, Koda? That's so sweet!"
            
            if radio_static == "_s":
                voice "j12_WellBeOkayKoda_s"
            else:
                voice "j12_WellBeOkayKoda_c"
            $ chibi_ruran = "images/chibi/ruran_happy.png"
            wt_ru "We'll be okay, Koda. Thank you for checking in!"

            voice "j12_ComeTo"
            wt_pe "Come to think of it, Morgan… We never actually did the whole curtain reveal, huh?"
            voice "j12_AtThisPointIve"
            $ chibi_morgan = "images/chibi/morgan_neutral.png"
            wt_mo "At this point I've only yet to meet Ruran, Cassie…and the rest at the RC."

            if radio_static == "_s":
                voice "j12_ICould_s"
            else:
                voice "j12_ICould_c"
            $ chibi_jax = "images/chibi/jax_happy.png"
            wt_ja "I could act a little surprised if you want to do another official reveal."

            voice "j12_DontEmbarrass"
            $ chibi_morgan = "images/chibi/morgan_worried.png"
            wt_mo "Don't embarrass yourself, Jax."

            if radio_static == "_s":
                voice "j12_YouCould_s"
            else:
                voice "j12_YouCould_c"
            $ chibi_cassie = "images/chibi/cassie_happy.png"
            wt_ca "You could still do it for Ruran and me, at least!"

            if radio_static == "_s":
                voice "j12_YesId_s"
            else:
                voice "j12_YesId_c"
            wt_ru "Yes, I'd love to see what Pearl comes up with!"

            voice "j12_OohWhat"
            $ chibi_kyle = "images/chibi/kyle_neutral.png"
            wt_ky "Ooh! What about the blankets I got from…"
            "Kyle pauses for a moment, but quickly shakes off whatever pang of sadness had hit him."
            voice "j12_WWeCould"
            $ chibi_kyle = "images/chibi/kyle_worried.png"
            wt_ky "W-We could use the blankets as a makeshift curtain!"

            # $ chibi_pearl = "images/chibi/pearl_happy.png"
            voice "j12_TotallyThats"
            wt_pe "Totally. That's a great call, Kyle!"
            voice "j12_AtThisPointI"
            $ chibi_morgan = "images/chibi/morgan_neutral.png"
            wt_mo "At this point I feel like one of those magician's pet animals."

            if radio_static == "_s":
                voice "j12_WouldYou_s"
            else:
                voice "j12_WouldYou_c"
            wt_ko "Would you be doing one at the RC as well?"

            if radio_static == "_s":
                voice "j12_OnSecond_s"
            else:
                voice "j12_OnSecond_c"
            $ chibi_koda = "images/chibi/koda_neutral.png"
            wt_ko "On second thought… Don't."
    else:
        "After our call with Ruran the other day, we brought up the idea of merging camps to Gregory."
        "He agreed more easily than I expected."
        "So today…is our long-awaited camp merging day."
        "Or, as Pearl said earlier, 'camp merging 2.0.'"
        play music audio.light
        scene bg walkpath with fade

        "This time, we approached it in a different way."
        "Gregory and Wilbur went straight ahead to our new camp's destination without carrying any of our heavier gear up the mountain."
        "A lookout, scouting type of role."
        "If and when they notice anything amiss… We'll be the first to know."
        "Real-time updates through the Walkie should prevent a repeat of last month's events."
        #beep Walkie start

        if radio_static == "_s":
            voice "j12_OkayWilbur_s"
        else:
            voice "j12_OkayWilbur_c"
        # $ chibi_gregory = "images/chibi/gregory_neutral.png"
        wt_gr "Okay, Wilbur and I are at the summit. We've cleared the area, and y'all should be safe to leave camp."
    
        if radio_static == "_s":
            voice "j12_ThoughBe_s"
        else:
            voice "j12_ThoughBe_c"
        wt_gr "Though…be careful on the way up. There's lots of fallen tree branches up the trail."

        if radio_static == "_s":
            voice "j12_br1_BetterLate_s"
        else:
            voice "j12_br1_BetterLate_c"
        $ chibi_wilbur = "images/chibi/wilbur_neutral.png"
        wt_wi "Better late than never, my friends! So take your time."
        
        voice "j12_br1_WellBeThereIn"
        # $ chibi_aston = "images/chibi/aston_neutral.png"
        wt_ast "We'll be there in an hour."

        if radio_static == "_s":
            voice "j12_RoughlyTwo_s"
        else:
            voice "j12_RoughlyTwo_c"
        
        wt_ca "Roughly…two hours on our end!"

        if radio_static == "_s":
            voice "j12_ObligatoryQuestion_s"
        else:
            voice "j12_ObligatoryQuestion_c"
        wt_da "Obligatory question, Pearl - did you remember your-"

        voice "j12_CompassYes"
        # $ chibi_pearl = "images/chibi/pearl_happy.png"
        wt_pe "Compass? Yes, I did this time!"
        voice "j12_ICan"
        # $ chibi_lorenzo = "images/chibi/lorenzo_neutral.png"
        wt_lo "I can attest to that…though she did grab mine by mistake first."

        voice "j12_br1_HushLorenzo"
        # $ chibi_pearl = "images/chibi/pearl_worried.png"
        wt_pe "Hush, Lorenzo!"
        voice "j12_NeverChange"
        # $ chibi_aston = "images/chibi/aston_happy.png"
        wt_ast "Never change, Pearl."

        if radio_static == "_s":
            voice "j12_OhYeah_s"
        else:
            voice "j12_OhYeah_c"
        $ chibi_davos = "images/chibi/davos_happy.png"
        wt_da "Oh, yeah! Koda's on the Walkie with us, too!"

        if radio_static == "_s":
            voice "j12_ThisMorning_s"
        else:
            voice "j12_ThisMorning_c"
        $ chibi_davos = "images/chibi/davos_neutral.png"
        wt_da "This morning, they were all like, 'Have you left yet? Is everyone okay? Did you bring enough supplies? Please don't explode on the way up-'"
        
        if radio_static == "_s":
            voice "j12_YeahYeah_s"
        else:
            voice "j12_YeahYeah_c"
        $ chibi_koda = "images/chibi/koda_worried.png"
        wt_ko "Yeah, yeah. I'm paranoid, I know."

        if radio_static == "_s":
            voice "j12_IJust_s"
        else:
            voice "j12_IJust_c"
        $ chibi_koda = "images/chibi/koda_neutral.png"
        wt_ko "I just want to make sure you guys all get there in one piece."
        
        voice "j12_WorriedFor"
        $ chibi_kyle = "images/chibi/kyle_neutral.png"
        wt_ky "Worried for us, Koda? That's so sweet!"
        
        if radio_static == "_s":
            voice "j12_WellBeOkayKoda_s"
        else:
            voice "j12_WellBeOkayKoda_c"
        $ chibi_ruran = "images/chibi/ruran_happy.png"
        wt_ru "We'll be okay, Koda. Thank you for checking in!"

        voice "j12_ComeTo"
        wt_pe "Come to think of it, Morgan… We never actually did the whole curtain reveal, huh?"
        voice "j12_AtThisPointIve"
        $ chibi_morgan = "images/chibi/morgan_neutral.png"
        wt_mo "At this point I've only yet to meet Ruran, Cassie…and the rest at the RC."

        if radio_static == "_s":
            voice "j12_ICould_s"
        else:
            voice "j12_ICould_c"
        $ chibi_jax = "images/chibi/jax_happy.png"
        wt_ja "I could act a little surprised if you want to do another official reveal."

        voice "j12_DontEmbarrass"
        $ chibi_morgan = "images/chibi/morgan_worried.png"
        wt_mo "Don't embarrass yourself, Jax."

        if radio_static == "_s":
            voice "j12_YouCould_s"
        else:
            voice "j12_YouCould_c"
        $ chibi_cassie = "images/chibi/cassie_happy.png"
        wt_ca "You could still do it for Ruran and me, at least!"

        if radio_static == "_s":
            voice "j12_YesId_s"
        else:
            voice "j12_YesId_c"
        wt_ru "Yes, I'd love to see what Pearl comes up with!"

        voice "j12_OohWhat"
        $ chibi_kyle = "images/chibi/kyle_neutral.png"
        wt_ky "Ooh! What about the blankets I got from…"
        "Kyle pauses for a moment, but quickly shakes off whatever pang of sadness had hit him."
        nvl clear

        voice "j12_WWeCould"
        $ chibi_kyle = "images/chibi/kyle_worried.png"
        wt_ky "W-We could use the blankets as a makeshift curtain!"

        # $ chibi_pearl = "images/chibi/pearl_happy.png"
        voice "j12_TotallyThats"
        wt_pe "Totally. That's a great call, Kyle!"

        voice "j12_AtThisPointI"
        $ chibi_morgan = "images/chibi/morgan_neutral.png"
        wt_mo "At this point I feel like one of those magician's pet animals."

        if radio_static == "_s":
            voice "j12_WouldYou_s"
        else:
            voice "j12_WouldYou_c"
        $ chibi_koda = "images/chibi/koda_happy.png"
        wt_ko "Would you be doing one at the RC as well?"

        if radio_static == "_s":
            voice "j12_OnSecond_s"
        else:
            voice "j12_OnSecond_c"
        $ chibi_koda = "images/chibi/koda_neutral.png"
        wt_ko "On second thought… Don't."

    
    nvl clear
    stop music fadeout 3.0
    scene black with longfade
    "And so the long trek upwards begins."
    "By sundown, we had the majority of our fixtures set up."
    "Tents assembled."
    "Campfire up and running for the night."
    "All that's left is a good night's sleep."
    scene black
    with Pause(1.3)

label jan_13:
    $ current_day = _("January 13th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    "It's the night of the 13th."
    play ambience amb_campnightwfire fadein 1.0
    "Everyone has pretty much settled into the new camp."
    "And tonight is going to be a special one - it's marshmallow night, but with C1 and C2 together."
    scene camp3night with fade
    "Everyone's just mingling around camp until it's time."
    "Time to see what they're up to."

    if not aston_safe:
        #BRANCH 3: Both Aston and Pearl are dead
        if not pearl_safe:
            play music audio.sad
            menu jan13Convos3:
                "Ruran, Wilbur, Lorenzo & Gregory":
                    if not jan13_wilGregRuLo:
                        show cg j13campcrew with dissolve
                        $ jan13_wilGregRuLo = True
                        voice "j13_HelloMorgan"
                        wi "Hello, Morgan!"
                        voice "j13_WhatAre"
                        mo "What are we up to?"
                        voice "j13_ReminiscingAbout"
                        wi "Reminiscing about our years together… Greggy here wants to retire soon."
                        voice "j13_YoureMaking"
                        gr "Hey! You're making us sound older than we are."
                        voice "j13_ButIt"
                        ru "But it has been a long while, hasn't it?"
                        scene camp3night with dissolve
                        with Pause(0.5)
                        show lo sad at centerright with dissolve
                        "Lorenzo doesn't seem very chatty today, zoning out whilst staring at the campfire."
                        voice "j13_DoYouWantSomething"
                        mo "Do you…want something to drink, Lorenzo?"
                        show lo pondering
                        voice "j13_HuhOh"
                        lo "Huh? Oh, no thank you, amico. Thanks for asking."
                        show gr neutral at left
                        voice "j13_MindGrabbing"
                        gr "Mind grabbing me a can, Morg?"
                        "I gave Gregory a little nod before leaving."
                    else:
                        "I've already talked to them."

                "Davos, Jax & Koda":
                    if not jan13_davJaxKo:
                        $ jan13_davJaxKo = True
                        "Jax accompanies the lone Davos, sitting next to the campfire."
                        "Koda's voice is coming through the Walkie, but I can't parse what they're saying."
                        "And Davos…"
                        "I look towards the small pile of marshmallows, burnt to smithereens."
                        "Jax leans over to say something to Davos, squeezes his shoulder, and then gently grabs the stick to take over roasting duty."
                        "If Pearl were here, she'd get a kick out of Davos' marshmallow troubles…"
                        "Though I think her presence might've prevented them entirely."
                    else:
                        "They seem busy right now."

                "Cassie & Kyle":
                    if not jan13_cassieKyle:
                        $ jan13_cassieKyle = True
                        "Kyle and Cassie, they're huddled together tonight."
                        "..."
                        "Is she… Is she crying?"
                        "I should leave them be for now."
                        "I don't think Cassie is up for a conversation right now…and Kyle looks much the same."
                    else:
                        "I don't think either of them are up for chatting right now."
            
            if jan13_wilGregRuLo and jan13_davJaxKo and jan13_cassieKyle:
                scene camp3night with dissolve
                "And I think…that's it."
                "People are together in their own little groups."
                "Supporting each other in another's absence."
                "..."
                "The same smell of burnt marshmallows lingers… It tickles my nose."
                "The same sound of light chatter around the campfire continues into the night."
                "But tonight's marshmallow felt...{w=0.5}different."
                "'The Camp Guide's to Camp Guiding' could never have prepared me for this."
                "Pearl once said that marshmallow nights could sometimes mean campfire story nights, if Wilbur's here."
                "But I don't think he's in the mood to share any tales."
                "We don't have a full audience, he said."
                stop ambience fadeout 1.0
                stop music fadeout 3.0
            else:
                scene camp3night with dissolve
                jump jan13Convos3
        
        #BRANCH 2: Pearl safe, Aston dead
        else:
            play music audio.light
            menu jan13Convos2:
                "Lorenzo & Ruran":
                    if not jan13_lorenzoRuran:
                        $ jan13_lorenzoRuran = True
                        show lo sad at left
                        show ru happy at right
                        with dissolve
                        voice "j13_HeyaGuysHopeIm"
                        mo "Heya, guys. Hope I'm not interrupting."
                        voice "j13_WelcomeMorgan"
                        ru "Welcome, Morgan. We were…just talking about Aston."
                        voice "j13_IRememberTheFirst"
                        ru "I remember the first time we ever worked together was during a night shift."
                        voice "j13_HeWas"
                        ru "He was exhausted…but still kept it together. He never shows the slightest hint of that in front of others, especially our patients."
                        show lo smile
                        voice "j13_ThatSounds"
                        lo "That sounds like Aston alright. Pragmatic and considerate."
                        show lo sad
                        voice "j13_AndThats"
                        lo "And that's what I love about him…"
                        "I gently pat Lorenzo's back."

                    else:
                        "I've already talked to them."

                "Wilbur & Gregory":
                    if not jan13_wilGreg:
                        $ jan13_wilGreg = True
                        show gr confused at centerleft
                        show wi neutral at centerright
                        voice "j13_HelloMorgan"
                        wi "Hello, Morgan!"
                        voice "j13_WhatAre"
                        mo "What are we up to?"
                        voice "j13_ReminiscingAbout"
                        wi "Reminiscing about our years together… Greggy here wants to retire soon."
                        show gr happy
                        voice "j13_YoureMaking"
                        gr "Hey! You're making us sound older than we are."
                        voice "j13_PeopleUsually"
                        wi "People usually retire in their 60's, but look at you."
                        show gr neutral
                        voice "j13_ItsOkay"
                        mo "It's okay, Greggy. People have free will."
                        voice "j13_GregoryVNVR"
                        gr "..."
                        show wi happy
                        voice "j13_AhMorgan"
                        wi "Ah, Morgan, you're a fun one."

                    else:
                        "I've already talked to them."

                "Pearl, Davos & Koda":
                    if not jan13_pearlDavKo:
                        $ jan13_pearlDavKo = True
                        show pe sad at left
                        show da sad at center
                        with dissolve
                        voice "j13_SoPearl"
                        ko "So Pearl, what's the burnt marshmallow counter?"
                        show pe depressed
                        voice "j13_16You"
                        pe "16… You know what, I should stop wasting food. Aston wouldn't-"
                        "Pearl…"
                        show da neutral
                        voice "j13_GiveIt"
                        da "Give it here, Pearl. I'll roast them for you."
                        "Davos takes over marshmallow roasting duty."
                    else:
                        "I've already talked to them."

                "Cassie & Kyle":
                    if not jan13_cassieKyle:
                        $ jan13_cassieKyle = True
                        "Kyle and Cassie, they're huddled together tonight."
                        "..."
                        "Is she… Is she crying?"
                        "I should leave them be for now."
                        "I don't think Cassie is up for a conversation right now…and Kyle looks much the same."
                    else:
                        "I don't think either of them are up for chatting right now."

                "Jax":
                    if not jan13_jax:
                        $ jan13_jax = True
                        show ja neutral with dissolve
                        "Jax has a can of beer in his hand."
                        voice "j13_MindIf"
                        mo "Mind if I join ya?"
                        voice "j13_WhatIf"
                        ja "What if I did? Still gonna invade my personal space?"
                        voice "j13_YouWont"
                        mo "You won't shoo me away."

                        #Special for this branch
                        voice "j13_HowAre"
                        mo "How are you holding up?"
                        show ja inthought
                        voice "j13_CouldBe"
                        ja "Could be better… What about you?"
                        
                        voice "j13_IMean"
                        ja "I mean, you do seem to have a lot of unusual life experiences under your belt but…seriously, are you good?"
                        voice "j13_YeahIm"
                        mo "Yeah. I'm good, but, uh… I don't really like to talk about it."
                        show ja happy
                        voice "j13_AlrightI"
                        ja "Alright, I won't pry."
                        voice "j13_AndYou"
                        mo "And, you?"
                        voice "j13_MilitaryVet"
                        ja "Military vet…well, until I lost my vision over here."
                        "He taps gently on the right side of his face. Yeah…the lens of his eye does look a little cloudy."
                        "The more you know."
                        "Jax shakes his beer can and peers into the opening."
                        show ja inthought
                        voice "j13_OohIm"
                        ja "Ooh, I'm out. I think I'll go grab another one. See you in a bit, Morgo."

                    else:
                        "I've already talked to him."

            if jan13_lorenzoRuran and jan13_wilGreg and jan13_pearlDavKo and jan13_cassieKyle and jan13_jax:
                scene camp3night with dissolve
                "And I think…that's it."
                "People are together in their own little groups."
                "Supporting each other in another's absence."
                "..."
                "The same smell of burnt marshmallows lingers… It tickles my nose."
                "The same sound of light chatter around the campfire continues into the night."
                "But tonight's marshmallow felt...{w=0.5}different."
                "'The Camp Guide's to Camp Guiding' could never have prepared me for this."
                "Pearl once said that marshmallow nights could sometimes mean campfire story nights, if Wilbur's here."
                "But I don't think he's in the mood to share any tales."
                "We don't have a full audience, he said."

                stop ambience fadeout 1.0
                stop music fadeout 3.0
            else:
                scene camp3night with dissolve
                jump jan13Convos2
    #BRANCH 1: Everyone OK
    else: 
        play music audio.light
        menu jan13Convos1:
            "Aston & Lorenzo":
                if not jan13_astonLorenzo:
                    $ jan13_astonLorenzo = True
                    show lo smile at centerleft
                    show ast happy at centerright
                    with dissolve
                    voice "j13_HeyaGuysHopeIm"
                    mo "Heya, guys. Hope I'm not interrupting."
                    show lo happy
                    voice "j13_NotAt"
                    lo "Not at all, Morgan! Come sit."
                    voice "j13_WeWere"
                    ast "We were just talking about you, actually."
                    voice "j13_OhDo"
                    mo "Oh? Do tell."
                    voice "j13_HowYou"
                    lo "How you covered for us…in front of Gregory."
                    show lo neutral
                    voice "j13_AndThen"
                    lo "And then we were comparing notes on what we've been experiencing on our end. In terms of the bear…and things like it."
                    voice "j13_DoYouGuysPlan"
                    mo "Do you guys plan on telling the others?"
                    show ast inthought
                    voice "j13_IHaveMyReservations"
                    ast "I have my reservations about Gregory, as you well know - but I think we might stand a chance convincing Wilbur to help."
                    voice "j13_IKnow"
                    ast "I know he has questions for us, at least."
                    voice "j13_IHaveAQuestion"
                    mo "I have a question for both of y'all right now…"
                    show ast neutral
                    voice "j13_LorenzoI"
                    mo "Lorenzo, I know it started as nightmares for you, but Aston…how did yours start?"
                    show ast sad
                    voice "j13_IDidnt"
                    ast "I didn't keep track, sorry… But mine didn't start with nightmares."
                    show ast neutral with None
                    voice "j13_AreYouAlsoStarting"
                    ast "Are you also starting to have auditory hallucinations?"
                    voice "j13_ImNot"
                    mo "I'm not entirely sure. I'll bring it up again if it gets worse."
                    voice "j13_YesPlease"
                    ast "Yes, please. It'll keep you sane."
                    voice "j13_AndWilbur"
                    mo "And Wilbur… I'll check in with him when I have the chance."
                    show ast happy
                    show lo smile
                    with dissolve
                    voice "j13_ThankYou"
                    ast "Thank you, Morgan."
                    voice "j13_GrazieAmico"
                    lo "Grazie, amico."

                else:
                    "I've already talked to them."

            "Wilbur, Gregory & Ruran":
                if not jan13_wilGregRu:
                    $ jan13_wilGregRu = True
                    show cg j13campcrew with dissolve
                    "Gregory, Wilbur and Ruran are sitting together."
                    voice "j13_MorganMy"
                    wi "Morgan, my boy!"
                    voice "j13_HeyaGuysWhatAre"
                    mo "Heya, guys! What are we up to?"
                    voice "j13_ReminiscingAbout"
                    wi "Reminiscing about our years together… Greggy here wants to retire soon."
                    voice "j13_YoureMaking"
                    gr "Hey! You're making us sound older than we are."
                    voice "j13_ButIt"
                    ru "But it has been a long while, hasn't it?"
                    voice "j13_IRememberMeetingWilbur"
                    ru "I remember meeting Wilbur during my first time being out in the field. That was about…a decade ago."
                    voice "j13_YouDont"
                    mo "You don't look that much older than me, Ruran."
                    voice "j13_AwwThank"
                    ru "Aww, thank you, Morgan. You're very kind."
                    voice "j13_AnywayIts"
                    wi "Anyway, it's almost time for campfire story time! They've been looking forward to this for months."
                    voice "j13_OohCant"
                    mo "Ooh, can't wait for that!"

                else:
                    "I've already talked to them."

            "Pearl, Davos & Koda":
                if not jan13_pearlDavKo:
                    $ jan13_pearlDavKo = True
                    show pe smile at left
                    show da neutral at center
                    with dissolve
                    voice "j13_WhatsThe"
                    ko "What's the burnt marshmallow counter?"
                    show pe neutral
                    voice "j13_Zero"
                    pe "Zero."
                    voice "j13_NahAdd"
                    da "Nah. Add 16 to that number."
                    voice "j13_WowPearl"
                    ko "Wow, Pearl, that's kinda impressive."
                    "She burns another one."

                    show da happy
                    voice "j13_MakeIt"
                    da "Make it 17 now."
                    show pe confused
                    voice "j13_ICantWorkWell"
                    pe "I can't work well under pressure!"
                    "Wow. The others weren't kidding when they said Pearl was exceptional at burning all her marshmallows."
                else:
                    "They all seem busy with the marshmallows."

            "Cassie & Kyle":
                if not jan13_cassieKyle:
                    $ jan13_cassieKyle = True
                    
                    show ca happy at centerleft
                    voice "j13_MorganCome"
                    ca "Morgan! Come be a tiebreaker for us!"
                    "Cassie calls out to me."
                    show ky confused at right
                    voice "j13_OkayLike"
                    ky "Okay, like…do you do the dishes after you eat, or do you wash as you cook?"
                    voice "j13_TheLatter"
                    ca "The latter is obviously better. It's efficient!"
                    show ky neutral
                    voice "j13_ILike"
                    ky "I like to enjoy my meals first before I clean up."
                    voice "j13_AreYouGuysAlready"
                    mo "Are you guys already discussing the fun little problems you'd face if you lived together?"
                    show ky flustered
                    voice "j13_KyleVNVR"
                    ky "..."
                    voice "j13_HaveYou"
                    mo "Have you guys even decided who's gonna be the main cook yet?"
                    show ca flustered
                    voice "j13_CassieVNVR"
                    ca "..."
                    voice "j13_CompromiseIs"
                    mo "Compromise is key, guys!"
                    show ca sad
                    voice "j13_ICantWithYou"
                    ca "I can't with you, Morgan."
                else:
                    "I've already talked to them."

            "Jax":
                if not jan13_jax:
                    $ jan13_jax = True
                    show ja neutral with dissolve
                    "Jax has a can of beer in his hand."
                    voice "j13_MindIf"
                    mo "Mind if I join ya?"
                    voice "j13_WhatIf"
                    ja "What if I did? Still gonna invade my personal space?"
                    voice "j13_YouWont"
                    mo "You won't shoo me away."
                    voice "j13_AnEventful"
                    ja "An eventful two months, huh? I almost feel bad for you."
                    voice "j13_ImAdaptable"
                    mo "I'm adaptable, and I love a good challenge."
                    show ja inthought
                    voice "j13_IMean"
                    ja "I mean, you do seem to have a lot of unusual life experiences under your belt but…seriously, are you good?"
                    voice "j13_YeahIm"
                    mo "Yeah. I'm good, but, uh… I don't really like to talk about it."
                    voice "j13_AlrightI"
                    show ja happy
                    ja "Alright, I won't pry."
                    voice "j13_AndYou"
                    mo "And, you?"
                    voice "j13_MilitaryVet"
                    ja "Military vet…well, until I lost my vision over here."
                    "He taps gently on the right side of his face. Yeah…the lens of his eye does look a little cloudy."
                    "The more you know."
                    "Jax shakes his beer can and peers into the opening."
                    show ja inthought
                    voice "j13_OohIm"
                    ja "Ooh, I'm out. I think I'll go grab another one. See you in a bit, Morgo."
                    "I wave him a quick goodbye."

                else:
                    "I've already talked to him."

        if jan13_astonLorenzo and jan13_wilGregRu and jan13_pearlDavKo and jan13_cassieKyle and jan13_jax:
            scene camp3night with dissolve
            "I'm glad everyone seems to be in good spirits."
            "And it looks like campfire story time is about to start!"
            "Today on the story menu is…"
            menu j13Storytime:
                "Listen to the story in full":
                    "Wilbur tells us a tale about a brave fisherman and a red kraken."
                    "'One, the fish it feeds.'"
                    "'The fisherman met a lost child out at sea.'"
                    "'It cries out in hunger, he hears its plea.'"
                    "'An arm broken, it swims meekly.'"
                    "'A fish a day, turned into weekly.'"
                    "'An uncanny friendship, blossoming, it began.'"
                    "'A hand reaching in, from the pier he stands.'"
                    "'Two, the waves they crash.'"
                    "'Grow and grow, its feelers shine.'"
                    "'Massive, towering, a sight to see.'"
                    "'But little does he know that feeding a plenty.'"
                    "'The adoration for the beast, in turn fueled its crave.'"
                    "'Alas, true colors show the monster it became.'"
                    "'Splashing, thrashing, seething with anger.'"
                    "'Its hunger never satiated, its demands never-ending.'"
                    "'The beast was no longer the friend he once made.'"
                    "'The beast perhaps never saw him as a friend.'"
                    "'The beast was never to be tamed.'"
                    "'The brave fisherman had a choice to make.'"
                    "'Subdue the beast, or dangers his family may face.'"
                    "'Three, the heart resents.'"
                    "'A spear through its heart or a town without a pier.'"
                    "'And swoop!'"
                    "'A jab to its pulse, red hues circulate.'"
                    "'Lingering in the sea bed, awaiting its wake.'"
                    "'People 'round cheer, the fisherman peers.'"
                    "'Down into the seabed, down into the abyss.'"
                    "'His friend now lost, its cries unfound.'"
                    "'Laid to rest, the dear Kraken's wrath.'"
                    "..."
                    "So what I got from that is to not feed the wildlife…got it."
                    "'The Camp Guide's Guide to Camp Guiding' already had a whole page on that."
                    "Though… If Wilbur wasn't a camp guide, I think he'd do well as a storyteller."
                    "Davos, on the other hand, doesn't seem to have the same affinity with it."
                    "Maybe it comes with age."

                "Half-listen to the story":
                    "Wilbur tells us a tale about a brave fisherman and a red kraken."
                    "..."
                    "So what I got from that is to not feed the wildlife…got it."
                    "'The Camp Guide's Guide to Camp Guiding' already had a whole page on that."
                    "Though… If Wilbur wasn't a camp guide, I think he'd do well as a storyteller."
                    "Davos, on the other hand, doesn't seem to have the same affinity with it."
                    "Maybe it comes with age."
            stop ambience fadeout 1.0
            stop music fadeout 3.0
        else:
            scene camp3night with dissolve
            jump jan13Convos1

label jan_14:
    scene camp3day with longfade
    $ current_day = _("January 14th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    play music audio.neutral
    show gr neutral at left
    if not aston_safe: #Aston nuh uh
        if not pearl_safe: #Pearl nuh uh
            voice "j14_AlrightIsaak"
            gr "Alright. Isaak called this morning… Unsurprisingly, the man wants more shrooms."
            voice "j14_WhosOn"
            gr "Who's on deck for a sample collection day?"
            show wi neutral at right
            voice "j14_ThisIs"
            wi "This is…one of my scheduled days, I think."
            voice "j14_ImIn"
            mo "I'm in."
            show da happy at centerright
            voice "j14_IllGo"
            da "I'll go, too!"
            voice "j14_FourPeople"
            gr "... Four people will be more than enough."
            voice "j14_LetsGo"
            gr "Let's go."

            scene black with dissolve
            "Mushrooms in winter… What are the odds of actually finding them out in the wild?"
            "And in this weather, without special conditions?"
            "Is he stockpiling them for something?"
            "Honestly… {w=0.7}It would really suck to find some just like the last time we encountered them."
            "I'd like to see normal shroom behavior for once, please."


            scene forest3 with longfade
            "Today is different, though. We've got extra company from C2."
            "Ever since we merged camps, we've had our schedules rearranged."
            "One group of sample collectors, and the other…on search and rescue."
            "Just the four of us today…wait, where's Davos?"
            "I turn to see him trudging forward a ways behind us with uneven steps."


            voice "j14_DavosYoureLookingA"
            mo "Davos? You're…looking a little pale, bud. Are you feeling alright?"
            voice "j14_YeahImImFine"
            da "Yeah, I'm… I'm fine. Just…a little…"
            #SFX: snow thud (snow body, body in the snow)
            with Pause (1.2)
            play sound snowground
            stop music fadeout 1.0
            with Pause (0.8)
            voice "j14_DavosShout"
            wi "{size=+5}Davos?!"
            scene black with fade
        
        else: #Pearl fine, Aston nuh uh
            jump j14_pearlOK
    else: #Everyone okay
        label j14_pearlOK:
            voice "j14_AlrightIsaak"
            gr "Alright. Isaak called this morning… Unsurprisingly, the man wants more shrooms."
            voice "j14_WhosOn"
            gr "Who's on deck for a sample collection day?"
            show pe happy at center
            voice "j14_Pearl"
            pe "Pearl!"
            show da happy at centerright
            voice "j14_Davos"
            da "Davos!"
            voice "j14_Morgan"
            mo "Morgan…?"
            show wi happy at right
            voice "j14_Wilbur"
            wi "Wilbur!"
            show gr confused
            voice "j14_FineFive"
            gr "... Fine. Five people will be more than enough."
            voice "j14_IThink"
            mo "I think you're forgetting something, Greggy."
            show gr neutral with None
            voice "j14_ImNot"
            gr "I'm not even gonna dignify that with a response."

            scene black with dissolve

            "Haha…nice response, Gregory."
            "Though, mushrooms in winter… What are the odds of actually finding them out in the wild?"
            "And in this weather, without special conditions?"
            "Is he stockpiling them for something?"
            "Honestly… {w=0.7}It would really suck to find some just like the last time we encountered them."
            "I'd like to see normal shroom behavior for once, please."

            scene forest3 with longfade
            "Today is different, though. We've got extra company from C2."
            "Ever since we merged camps, we've had our schedules rearranged."
            "More hands on deck, more samples to collect."
            "Just the five of us today…wait, where's Davos?"


            voice "j14_DavosYoureSoSlow"
            pe "Davos, you're so slow today, are you…okay?"
            voice "j14_YeahImJustA"
            da "Yeah! I'm just a...little dizzy. I'll...catch up...soon."
            #SFX: snow thud (snow body, body in the snow)
            with Pause (1.2)
            play sound snowground
            stop music fadeout 1.0
            with Pause (0.8)
            voice "j14_DavosShout"
            wi "{size=+5}Davos?!"
            scene black with fade

label jan_15:
    scene black
    $ current_day = _("January 15th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    with Pause(1.0)
    scene medtent with dissolve
    show da neutral at centerleft
    show wi worried at centerright
    show ru neutral at center
    with dissolve
    if not pearl_safe: # Pearl nuh uh
        voice "j15_HowAre"
        wi "How are you doing, my boy?"
        voice "j15_ImFine"
        da "I'm fine. I promise. I think it's just…something I ate."
        "Davos is lying on a bed in the quarantine tent."
        "He collapsed in the snow yesterday while we were out… Gave Wilbur a huge fright."
        voice "j15_DoesAnything"
        ru "Does anything come to mind?"
        voice "j15_IMeanIDid"
        da "I mean, I did have some marshmallows the other night, but…"
        show da sad
        voice "j15_ThatShouldnt"
        da "That shouldn't matter…right?"
    else: # Everyone OK
        voice "j15_HowAre"
        wi "How are you doing, my boy?"
        voice "j15_ImFine"
        da "I'm fine. I promise. I think it's just…something I ate."
        "Davos is lying on a bed in the quarantine tent."
        "He collapsed in the snow yesterday while we were out… Gave Wilbur a huge fright."
        voice "j15_DoesAnything"
        ru "Does anything come to mind?"
        show pe confused at right with dissolve
        voice "j15_IMeanYouDid"
        pe "I mean, you did eat a lot of marshmallows the other night…"
        show da happy
        voice "j15_YouMean"
        da "You mean the ones you didn't burn?"
        show pe happy
        voice "j15_WellYeah"
        pe "Well, yeah!"

    if pearl_safe:
        hide pe with dissolve
    #Regardless of branch
    show wi serious with dissolve
    voice "j15_HowLong"
    wi "How long do you think he'll need to stay here, Ruran?"
    show ru worried
    voice "j15_CantSay"
    ru "Can't say for sure yet…we'll need to observe his symptoms for a little longer before making any estimates."
    show da confused
    voice "j15_SymptomsI"
    da "Symptoms? I just got a little dizzy. I hardly think it's-"
    show da depressed with None
    "Davos lets out a sudden, unusually harsh sneeze."
    voice "j15_YouWere"
    mo "…you were saying?"
    voice "j15_UhOh"
    da "Uh oh. I-I think I sneezed too hard."
    "His nose is bleeding."
    voice "j15_ListenTo"
    wi "Listen to Ruran, Davos. Stay here and let her monitor your symptoms."
    "Wilbur grabs a small packet of tissues and passes it to Davos."
    show da neutral
    voice "j15_OkayI"
    da "Okay… I will, but I'm sure I'll be fine tomorrow!"
    scene black with fade
    "Little did we know that Davos' symptoms would worsen overnight."
    show cg davosburrito
    "He developed a fever, and kept drifting in and out of sleep."

    if aston_safe:
        "Aston and Ruran said that they'll keep an eye on him."
    else:
        "Ruran said that she'll keep an eye on him."

    "Right now, there isn't too much cause for concern. He may just be fighting off a common cold."
    "But if it persists…we might need to provide some further intervention."
    scene black with longfade


label jan_16:
    # Darkness with snowmobile ambient
    $ current_day = _("January 16th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    "Gregory and I are heading towards the RC today, which means…"
    "I finally have an excuse to get acquainted with Gregory's snowmobile."
    "I knew he couldn't keep us apart forever."
    "I'll also finally be able to put faces to the three remaining people I haven't met, but that's secondary."
    "It's time to find out what piqued Elly's interest."

    # RC interior
    scene rclobby with fade
    play music audio.neutral
    show ko happy at centerleft
    show gr neutral at right
    with dissolve
    voice "j16_MorganHey"
    ko "Morgan? Hey! It's Koda…though, I guess you could have figured that out from our calls. Anyway, welcome to the RC!"
    voice "j16_AndLet"
    ko "And - let me help you with that, Gregory."
    show gr happy
    voice "j16_ThanksKid"
    gr "Thanks, kid. Is he around?"
    voice "j16_YoullFind"
    ko "You'll find Isaak at his usual station."
    show gr neutral
    voice "j16_IllBe"
    gr "I'll be across the way, then. See you later, Morg."
    hide gr
    voice "j16_104Do"
    mo "10-4. Do you want these over here, Koda?"
    voice "j16_YesThankYouThank"
    ko "Yes! Thank you, thank you."
    "As I place the final boxes down, I take in my surroundings."
    "Mentally mapping the area down."

    voice "j16_SoHow"
    ko "So…how are the others, Morgan?"
    voice "j16_TheyreNot"
    mo "They're not doing too hot… Ruran's idea to merge the camps was honestly a great call."
    show ko sad
    voice "j16_MaybeIts"
    ko "Maybe it's time to work these legs and pay everyone a visit…"
    voice "j16_YouMust"
    ev "You must be Morgan!"
    hide ko
    "As I turned towards Eva's voice, I had to do a double take."
    show ev happy
    voice "j16_WhatSomething"
    ev "What? Something on my face?"
    "She looks like an exact copy of Elly…"
    voice "j16_OhUh"
    mo "Oh, uh…nah. You just really look like someone I know."
    show ev inthought
    voice "j16_HmReally"
    ev "Hm. Really? She must be pretty, then."
    voice "j16_YeahI"
    mo "Yeah? I…guess he is?"
    show ev happy
    voice "j16_OhRight"
    ev "Oh, right. You haven't met Mr. Grumpy, have you?"
    voice "j16_IHavent"
    mo "I haven't even seen Mr. Grumpy yet. I just got here."
    voice "j16_LetsGo"
    ev "Let's go say hi, shall we?"
    scene black with dissolve
    "Eva leads the way to Isaak's lab."

    # Isaak lab
    scene bg isaaklab2 with longfade
    show isa inthought at centerleft
    show gr neutral at centerright
    with dissolve
    voice "j16_IsaakMorgan"
    ev "Isaak? Morgan's here!"
    "Eva opens the lab door to reveal a tall blonde man standing next to Gregory."
    "The lab is just as you'd imagine it to be…"
    "Spotless, organized, and a little too tidy for my liking."
    "I'm sure Koda spends a lot of time and effort keeping it in this state."
    voice "j16_OhHello"
    isa "Oh. Hello."
    "He barely looks up from the checklist he's holding."
    voice "j16_HeyIsaak"
    mo "Hey, Isaak. Nice to finally meet you in person."
    show isa neutral
    "I extend a hand for him to shake, though he only takes it after a long hesitation."

    # mini-desvcrojog to explain the chronology oopsie
    "This handshake feels... {w=1.5}Ah, shit. Right. We did meet before - at that villager's funeral."

    voice "j16_MorgansHelping"
    gr "Morgan's helping me with the delivery today. Thought it'd be worthwhile to have him meet the rest of the RC crew."
    show isa serious
    voice "j16_AlrightJust"
    isa "Alright. Just keep your hands to yourself and leave the samples where they need to be."
    "Chilly...as usual."
    "I expected no less from Isaak."
    "I don't think he even noticed my slip-up."

    show ev inthought at right
    voice "j16_BeNice"
    ev "Be nice."
    show isa inthought
    voice "j16_IsaakVNVR"
    isa "..."
    "He wipes the hand he used to shake mine on the back of his coat."
    "Right in front of me, Isaak? That's just plain rude."
    show gr confused
    voice "j16_SoThats"
    gr "So that's…24 bags all accounted for?"
    voice "j16_YesThank"
    isa "Yes. Thank you."
    "Taking in my surroundings, I noticed he has a large icebox sitting against the corner."
    voice "j16_ItsThat"
    el "It's that one."
    voice "j16_ThatOne"
    mo "...that one?"
    show isa serious
    voice "j16_ThatsAn"
    isa "That's an icebox… Large enough for you to fit inside."
    voice "j16_HaveYou"
    mo "Have you tried sitting in it yourself to come to that conclusion?"

    show gr happy with None
    play sound GregoryLaugh
    "Gregory tries to stifle his laugh."
    voice "j16_NoId"
    isa "No. I'd need to clear it out first. Rest assured that, by volume, it could easily accommodate a human volume of components."
    "I don't think he's making a threat, but I still don't like the implication there."
    stop music fadeout 2.0
    scene black with longfade

label jan_17:
    play ambience amb_snowmobilewind fadein 1.0
    $ current_day = _("January 17th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    voice "j17_HoldTight"
    gr "Hold tight, Morg. The wind's starting to pick up."
    "On the snowmobile, Gregory and I are on the way back to camp from the RC."
    voice "j17_WeStill"
    mo "We still have snowstorms at this time of year? Thought that was a November thing."
    voice "j17_IDont"
    gr "I don't think it's a storm we're having, just strong winds."
    voice "j17_ThenAgain"
    gr "Then again, there's no way for us to get confirmation with the busted radio tower, so it's not as though we have the particulars."
    scene black
    with Pause (2.0)
    "After about 25 minutes, we've almost reached the camp…but we have a problem."
    voice "j17_ArghI"
    gr "Argh… I don't think the snowmobile can fit through… We need to take a detour."
    "Lots of snow piled up on a fallen tree, blocking our usual route back to camp."
    voice "j17_OrActually"
    gr "Or, actually, why don't I drop you off here?"
    voice "j17_ItsA"
    gr "It's a short walk. I'll need help assessing the damage around the camp - this'd give both of us a head start. The wind isn't as strong now, anyway."
    voice "j17_SureThing"
    mo "Sure thing. I'll see you at camp."
    scene black
    with Pause(0.3)
    "Goodbye, snowmobile. I'll miss you."
    scene black
    with Pause(0.5)
    stop ambience fadeout 0.5
    # Forest

    with Pause (1.5)
    scene forest4 with dissolve
    play music audio.sad
    play ambience amb_stronkwind fadein 0.2
    "I regret agreeing to this. The wind might have died down a little, but it's still really strong."
    "Oh well… At least I'm almost there."
    "I've seen two fallen trees on the way here."
    "In the distance, near camp…is that one more?"
    "I continue my walk at a slightly brisker pace."

    voice "j17_OhLook"
    el "Oh, look! It's red!"
    "What's…red?"
    play music audio.anxious
    "Shit… There's a person under that tree."
    "Long dark hair…"
    voice "j17_Ruran"
    mo "Ruran?!"
    play sound snowrun
    show cg rurantree
    stop ambience fadeout 5.0
    "There she was, lying on the ground…with a tree branch puncturing the right side of her body."
    "The blood seeps through the snow, dyeing it a deep red."

    voice "j17_FuckThats"
    mo "Fuck…that's a lot of blood."
    "I need to act quickly."

    if not aston_safe:
        menu treeChoice2:
            "Push the tree out of the way":
                "Maybe if I could just move the tree out of the way…"
                "And then I'll be able to snap the branch off and carry her back to camp."
                "I'm sorry, this might hurt."
                play sound treemove
                "..."
                "The tree's out of the way. I'm gonna drag her out from underneath it, but first…the branch."
                menu treeSubChoice1:
                    "Remove the branch and apply pressure":
                        "Okay. Here goes."
                        "..."
                        "I underestimate how much blood…can just…"
                        "Okay, no. Don't look at it. We need to put pressure on it, Morgan."
                        "With one hand on her wound, and my other arm supporting her weight… I do my best to carry her back to camp."
                        "Hang tight, Ruran."
                        scene black with fade
                        "Upon reaching camp, I'm met by Jax and Wilbur frantically searching for Ruran."
                        "She was then immediately transferred into the tent for emergency care."
                        $ ruran_safe = False
                        $ ru_branch_yoinked = True
                        jump afterTree2
                    "Leave the branch":
                        "On second thought... Let's not do that."
                        "..."
                        "Think Morgan, think. What do I do in this situation?"
                        voice "j17_MorganIs"
                        ja "Morgan? Is that Ruran?!"
                        "Jax calls out to me from a distance."
                        voice "j17_YeahI"
                        mo "Yeah! I need help over here!"
                        voice "j17_br2_RuransUnconscious"
                        mo "Ruran's unconscious, losing a lot of blood."
                        voice "j17_br2_PunctureWound"
                        mo "Puncture wound to the right side of her stomach… There's a branch sticking out of her."
                        voice "j17_GotIt"
                        ja "Got it! Just don't touch anything, we're coming over!"
                        scene black with fade
                        $ ruran_safe = True
                        jump afterTree2

            "Don't try to move the tree":
                "No, I can't possibly push the tree out the way alone… Not without hurting her in the process."
                "I need to get help."
                "There's a chance that no one picks up their Walkie…but I could also just run back to camp. It's not that far."

                menu treeSubChoice2:
                    "Run back to camp":
                        "I'll be right back, Ruran… I promise."
                        scene black with fade
                        "I took off quickly toward our camp to get everyone's help."
                        "Upon reaching camp, I was met with Jax and Wilbur frantically searching for Ruran."
                        "They quickly followed me out to the field and the three of us transported her body back to camp for emergency care."
                        $ ruran_safe = False
                        $ ru_abandoned = True
                        jump afterTree2

                    #Try Walkie
                    "Try calling on the Walkie":
                        "Jax was with Ruran when I left, right? They were taking shifts to care for Davos."
                        "No one's beeping back."
                        "..."
                        "Think Morgan, think. What do I do in this situation?"
                        voice "j17_MorganIs"
                        ja "Morgan? Is that Ruran?!"
                        "Jax calls out to me from a distance."
                        voice "j17_YeahI"
                        mo "Yeah! I need help over here!"
                        voice "j17_br2_RuransUnconscious"
                        mo "Ruran's unconscious, losing a lot of blood."
                        voice "j17_br2_PunctureWound"
                        mo "Puncture wound to the right side of her stomach… There's a branch sticking out of her."
                        voice "j17_GotIt"
                        ja "Got it! Just don't touch anything, we're coming over!"
                        $ ruran_safe = True
                        jump afterTree2

            # afterward
        label afterTree2:
            stop music fadeout 1.0
            stop ambience fadeout 2.0
            scene black with longfade
            hide cg rurantree

            play ambience amb_campnightwfire fadein 0.5
            "A few hours had passed."
            "Cassie and Lorenzo are in the tent treating Ruran's wounds."
            "They aren't medical professionals, but they've been around enough to be able to grasp very basic concepts of emergency care."
            "Jax is off to the side, offering help to them wherever needed."
            "The camp has never been this quiet…"
            scene camp3night with dissolve
            "Everyone sits around anxiously, waiting for news."
            show wi sad at right
            "Wilbur paces restlessly…"
            "The two people whom he's closest with now are both in that tent."

            show ky smile at left
            voice "j17_WilburTheyre"
            ky "Wilbur… They're going to be okay."
            "And for a moment, Wilbur's face softens and gives him a nod of acknowledgement."
            voice "j17_HowAbout"
            ky "How about I go prep breakfast?"
            voice "j17_LetsBe"
            ky "Let's be in our best, most energized state for when they wake up!"
            #If Pearl okay (otherwise skip)
            
            if pearl_safe:
                show pe happy at centerright
                voice "j17_LetMe"
                pe "Let me help you out, Kyle!"
                hide ky
                hide pe
                with dissolve
            else:
                hide ky
            "Meanwhile, we could hear Gregory off to the side, cursing at his satellite phone."
            "I wish I could call Colin, too."

            #SFX
            scene camp3night with dissolve
            play sound cloth
            show lo sad
            show ca sad at centerleft
            with dissolve
            "The tent flap swings quickly open, and out comes Lorenzo."
            voice "j17_WeveStopped"
            lo "We've stopped the blood, but that's…as much as we could do."
            voice "j17_ShesAlive"
            lo "She's alive…just not in the best state. Davos is still asleep in his bed."
            show wi sad at centerright
            voice "j17_br2_CanI"
            wi "Can I… Can I see them?"
            voice "j17_br2_ComeOn"
            ca "Come on in, Wilbur."
            scene black with dissolve
            "I let out a sigh of relief."
            "Thank goodness she's alive."
            voice "j17_IdHardly"
            el "I'd hardly call that alive."
            voice "j17_LorenzoDid"
            el "Lorenzo did the best he could… But did you?"
            "..."
            voice "j17_Well"
            el "Well?"
            "The last thing I need now is to have the voice in my head questioning my every decision…so I desperately try my best to pay it no mind."
            stop ambience fadeout 3.0
            stop music fadeout 3.0

    else: # Aston fine, Pearl fine
        menu treeChoice1:
            "Push the tree out of the way":
                "Maybe if I could just move the tree out of the way…"
                "And then I'll be able to snap the branch off and carry her back to camp."
                voice "j17_MorganWait"
                ast "Morgan, wait! Don't move anything yet! We're on our way!"
                jump afterTree1
            "Don't try to move the tree":
                "No, I can't possibly push the tree out the way alone… Not without hurting her in the process."
                "I need to get help."
                voice "j17_MorganDont"
                ast "Morgan! Don't touch anything, we're coming over!"
                jump afterTree1

        # Stuff afterward
        label afterTree1:
            "I hear Aston's voice in the distance."
            voice "j17_WhatsHer"
            ast "What's her status?"
            voice "j17_br1_RuransUnconscious"
            mo "Ruran's unconscious, losing a lot of blood."
            voice "j17_br1_PunctureWound"
            mo "Puncture wound to the right side of her stomach… There's a branch sticking out of her."
            voice "j17_WhatShould"
            mo "What should I do now?"
            voice "j17_KeepHer"
            ast "Keep her warm! I…see the others grabbing the last of our gear. We'll be there soon!"
            "I don't have anything on me other than my jacket, but…"
            "If Wilbur can stand the cold with just a sweater on, so can I."
            "Surely it won't be that bad."
            voice "j17_YoullBe"
            mo "You'll be okay, Ruran… I've got you."
            $ ruran_safe = True

            stop music fadeout 1.0
            stop ambience fadeout 2.0
            scene black with longfade
            hide cg rurantree

            play ambience amb_campnightwfire fadein 0.5
            "We've passed the 4 hour mark."
            "Aston, with the help of Cassie and Lorenzo, are in the tent treating Ruran's wounds."
            "The camp has never been this quiet…"
            scene camp3night with dissolve
            "Everyone sits around anxiously, waiting for news."
            show wi sad at right
            "Wilbur paces restlessly…"
            "The two people whom he's closest with now are both in that tent."
            show ky smile at left
            voice "j17_WilburTheyre"
            ky "Wilbur… They're going to be okay."
            "And for a moment, Wilbur's face softens and gives him a nod of acknowledgement."
            voice "j17_HowAbout"
            ky "How about I go prep breakfast?"
            show ky happy
            voice "j17_LetsBe"
            ky "Let's be in our best, most energized state for when they wake up!"
            show pe happy at centerright
            voice "j17_LetMe"
            pe "Let me help you out, Kyle!"
            hide ky
            hide pe
            hide wi
            with dissolve
            "Meanwhile, we could hear Gregory off to the side, cursing at his satellite phone."
            show ja pissed
            voice "j17_MaintenanceCrew"
            ja "Maintenance crew is taking their sweet time… We can't even call for a fucking ambulance."
            voice "j17_AndEven"
            mo "And even if we did, the hospital's 4 hours away…"
            "I wish I could call Colin, too."
            #SFX
            scene camp3night with dissolve
            play sound cloth
            show ast sad
            show ca neutral at centerleft
            with dissolve
            "The tent flap swings quickly open, and out comes Aston."
            voice "j17_TheBranch"
            ast "The branch missed all her important organs."
            show ast inthought
            voice "j17_ButThere"
            ast "But there was a lot of blood loss, so…she's still unconscious right now."
            show ast sad with None
            voice "j17_ShellBe"
            ast "She'll be okay as long as we keep her temperature stable."
            voice "j17_AndDavos"
            ast "And… Davos is just sleeping."
            show wi sad at centerright
            voice "j17_br1_CanI"
            wi "Can I… Can I see them?"
            show ca happy
            voice "j17_br1_ComeOn"
            ca "Come on in, Wilbur."
            scene black with dissolve
            "I let out a sigh of relief."
            "Thank goodness…"
            stop ambience fadeout 3.0
            stop music fadeout 3.0
            # End of best branch

label jan_18:
    scene camp3day with longfade
    $ current_day = _("January 18th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    play music audio.neutral
    if not aston_safe:
        "It's the day after Ruran's rescue and surgery."
        "Both beds in the quarantine camp are occupied."
        "Jax, Lorenzo, and Cassie have been taking supervisory shifts to monitor their conditions."
        "And Wilbur…he hasn't slept a wink since."
        "I should pay them a visit."
        scene bg medtent with fade
        
        "It's Cassie's shift right now."
        show ca sad
        voice "j18_br2_MorningMorgan"
        ca "Morning, Morgan."
        show ca with move:
            xpos 600
        "She drapes a blanket over a sleeping Wilbur, sitting next to Davos' bed."
        voice "j18_br2_JustFell"
        mo "Just fell asleep?"
        voice "j18_br2_YeahAbout"
        ca "Yeah…about time he did."
        "I look over to Ruran. She's also sleeping… But she looks like she's in pain."
        "Cassie doesn't comment on Ruran's state."
        show ca inthought
        voice "j18_br2_HeyMorgan"
        ca "Hey, Morgan? My shift ends in an hour…mind calling Jax in once he's up?"
        voice "j18_YepCan"
        mo "Yep, can do."

        scene bg maintentday with longfade
        "I make my way back into the main tent to look for Jax." 
        show ja inthought at centerright
        "Oh, looks like I won't have to wake him up."
        "I see Jax sitting upright in his sleeping bag. He notices me walking in."
        show ja neutral
        voice "j18_MyTurn"
        ja "My turn already?"
        voice "j18_NotQuite"
        mo "Not quite. You've still got an hour to spare."
        "He takes a moment to stretch."
        show ja serious
        voice "j18_ToThink"
        ja "To think that the quarantine camp idea would turn into a literal infirmary tent situation… That kinda sucks."
        voice "j18_ItReally"
        mo "It really does."
        voice "j18_WilburHe"
        ja "Wilbur…he probably feels horrible right now… Having both his kid and best friend in there."
        show ja inthought
        voice "j18_AndWithout"
        ja "And… Without Aston, we're down to zero medics."
        voice "j18_NoneOf"
        ja "None of us are trained to take up that role… So if anything happens, it's just…us."
        voice "j18_WellJust"
        mo "We'll just have to make do until help arrives, then. That's our best option."
        show ja serious
        voice "j18_TheLack"
        ja "The lack of any news from the maintenance crew is baffling, really…"
        voice "j18_AlmostThree"
        mo "Almost…three weeks now, right?"
        voice "j18_CantWait"
        mo "Can't wait to see what Greggy will do when they arrive."
        voice "j18_DidYou"
        show ja happy
        ja "Did you just call him Greggy? That's crazy."
        voice "j18_IveKnown"
        ja "I've known him for a while and he never lets anyone call him that. Other than Wilbur, I think… It would be kinda hilarious to see how he'd react if I did."
        voice "j18_IMean"
        mo "I mean… He hasn't seemed to mind that much. Mileage may vary."
        show ja neutral
        voice "j18_LovePlaying"
        ja "Love playing with fire, don't you?"
        voice "j18_AlwaysFun"
        mo "Always fun to spice things up once in a while."
        show ja happy
        voice "j18_ButAnyway"
        ja "But, anyway, now that I'm awake enough… I think I'll go tag Cassie out. See ya in a bit, Morgo!"
        "With that, Jax leaves the tent."
        stop music fadeout 2.0

    else:
        "It's the day after Ruran's rescue and surgery."
        "Both beds in the quarantine camp are occupied."
        "Aston, Lorenzo, and Cassie have been taking supervisory shifts to monitor their conditions."
        "And Wilbur…he hasn't slept a wink since."
        "I should pay them a visit."
        scene bg medtent with fade

        "It's Cassie's shift right now."
        show ca neutral
        voice "j18_br1_MorningMorgan"
        ca "Morning, Morgan."
        show ca with move:
            xpos 600
        "She drapes a blanket over a sleeping Wilbur, sitting next to Davos' bed."
        voice "j18_br1_JustFell"
        mo "Just fell asleep?"
        voice "j18_br1_YeahAbout"
        ca "Yeah…about time he did."
        "I look over to Ruran. She's also sleeping, but it doesn't look like she's in pain."
        voice "j18_br1_IThink"
        ca "I think she'll be waking up soon."
        voice "j18_br1_ThatsGreat"
        mo "That's great news, Cassie."
        voice "j18_br1_HowAreYouBy"
        mo "How are you, by the way?"
        voice "j18_br1_YouMean"
        ca "You mean with the whole insomnia thing? It's happening every other day now, so it's…getting better?"
        show ca happy
        voice "j18_br1_ImDoing"
        ca "I'm doing okay, though! Don't worry!"
        voice "j18_br1_ButI"
        ca "...but I should try to get some sleep later. My shift ends in an hour."
        voice "j18_br1_MindWaking"
        ca "Mind waking Aston up for me if he's not already awake by then?"
        voice "j18_YepCan"
        mo "Yep, can do."

        scene maintentday with longfade
        "I make my way back into the main tent to look for Aston."
        "Oh, looks like I won't have to wake him up."
        show ast neutral at centerright
        voice "j18_HowAreYouFaring"
        ast "How are you faring?"
        voice "j18_WhatDo"
        mo "What do you mean?"
        show ast inthought
        voice "j18_ForMe"
        ast "For me, it's Lorenzo's voice. And for you…?"
        voice "j18_AhThat"
        mo "Ah, that. Yeah. It's oddly…conversational."
        show ast happy
        voice "j18_ICant"
        ast "I can't tell if that's better or worse for you."
        voice "j18_ItsProbably"
        el "It's probably worse. Right, Morgan?"
        voice "j18_ItsAnnoying"
        mo "It's annoying, I'll say that."
        voice "j18_ElliotVNVR"
        el "..."
        "Aston finds that amusing, too."
        voice "j18_AndHow"
        mo "And how are you faring, Aston?"
        show ast sad
        "He sighs."
        voice "j18_IHonestly"
        ast "I honestly wish I could've done better…"
        voice "j18_IDont"
        ast "I don't know if the decision to operate in the tent was a good one."
        voice "j18_IveGotta"
        mo "I've gotta say, Aston… You were amazing yesterday."
        voice "j18_AndIm"
        mo "And I'm sure you would've done the same thing regardless given the circumstance."
        show ast inthought
        voice "j18_ImJust"
        ast "I'm just doing my job."
        voice "j18_TakeThe"
        mo "Take the compliment for once, will you? You're the reason why she's still alive."
        show ast sad
        voice "j18_ThankYou"
        ast "Thank you."
        voice "j18_IKnow"
        mo "I know Lorenzo is proud of you, and Ruran will be, too. And…come on. You know the rest of the camp appreciates you."
        voice "j18_SoI"
        mo "So, I think you're good to release all that 'gotta-do-everything-myself' tension in your shoulders now."
        show ast smile with None
        voice "j18_IfYoure"
        ast "...if you're teasing me, I hardly think this is the time."
        "He says that, but shakes his arms out a little anyway."
        show ast neutral
        voice "j18_CassiesShift"
        ast "Cassie's shift will be over in…an hour, yes? Maybe I should take the next round. I'm already up - I could even head over now."
        voice "j18_YeahWilburs"
        mo "Yeah. Wilbur's finally getting some sleep, as well."
        show ast smile
        voice "j18_GoodIll"
        ast "Good. I'll see you later, then."
        hide ast
        "With that, Aston closed his personal supply kit, opened the door to the main tent, and departed for his upcoming shift."
        stop music fadeout 2.0
    scene black with fade

label jan_19:
    with Pause(3.0)
    $ current_day = _("January 19th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    scene bg maintent_night with dissolve
    if not aston_safe: # Aston not OK
        if not ruran_safe: # BRANCH 3: Ruran not OK, Aston not OK
            #If Pearl okay, different scene start
            if not pearl_safe:
                show ja neutral
                voice "j19_br2_ShesUp"
                ja "She's up, guys!"
                "Jax calls out to us and gathers everyone into the infirmary tent."
            else:
                show pe smile
                voice "j19_br3_ShesAwake"
                pe "She's awake! Ruran's awake!"
                "Pearl runs into the tent almost tripping over herself."
                "She gathers everyone into the infirmary tent."
            scene bg medtentnight with longfade
            play music audio.light
            show ja neutral at centerright
            show wi smile behind ja
            show ru worried at left
            with dissolve
            voice "j19_RuranCan"
            ja "Ruran, can you hear us?"
            show ru neutral
            voice "j19_YesYes"
            ru "...yes…yes I can."
            "Ruran holds her hands to her head."
            voice "j19_Ruran"
            wi "Ruran…"
            voice "j19_YouWere"
            mo "You were hit by a fallen tree, with a branch sticking into the right side of your stomach."
            voice "j19_LostA"
            mo "Lost a lot of blood and then… Lost consciousness for 2 days."
            show ru confused
            voice "j19_ISeeAndWho"
            ru "I see…and who…?"
            hide ky
            hide wi
            hide ja
            with dissolve
            #show ca happy at right
            with dissolve
            "Cassie gives Ruran a small wave, pointing to herself and Lorenzo."
            show ru happy
            voice "j19_NotBad"
            ru "Not bad, you two."
            show lo sick at center
            voice "j19_ThatsBeing"
            lo "That's being…overly generous."
            show ru angry
            voice "j19_IveSpent"
            ru "I've spent years trying to teach Aston to recognize his worth… Don't make me start with you, too."
            "She pauses for a moment before sighing."
            show ru worried
            voice "j19_HeLoves"
            ru "He loves you, you know. More than I could ever express."
            show lo sad with None
            voice "j19_IKnow"
            lo "I know…"
            voice "j19_AndOh"
            ru "And, oh… {w=1.0}Before you go…"
            show ru neutral
            voice "j19_AstonHas"
            ru "Aston has a collection of medical notes in his belongings. Please, be sure you get them."
            stop music fadeout 15.0
            show lo scared
            voice "j19_WhatDo"
            lo "W-What do you mean?"
            voice "j19_JustDo"
            ru "Just do as I say, Lorenzo…{w=2.0}for me. {w=1.5}For Aston."
            show ru happy with dissolve
            hide lo with dissolve
            voice "j19_NowI"
            ru "Now, I… I think I should sleep for a little longer."
            show wi worried at center behind ru
            voice "j19_RuranI"
            wi "Ruran… I-I don't think now is the time. Why-?"
            show ja shaken at centerleft behind ru
            voice "j19_RuranRuran"
            ja "Ruran? Ruran, don't-"

            "She smiles and holds a finger to her lips."
            scene black with fade
            play music audio.sad
            "The next few moments are a blur."
            "Jax trying to rush to her side, Lorenzo stepping backward to try and shake his sense of bewilderment, Cassie and me attempting to monitor Ruran's vital signs…"
            "To no avail."
            "Of all the ways for a life to end…"
            "A wakeless sleep surrounded by those who love you... \n{w=1.5}Doesn't seem so bad."
            scene black

            #Lorenzo solo scene but it's BAD bad
            #POV swap (please do not sprite the Lorenzo)
            with Pause(3.0)
            scene bg maintent_night with dissolve
            "Thirty minutes later, a shell-shocked Lorenzo sits amongst Aston's things, slowly sifting through the contents of his personal storage box."
            "Just as Ruran said…medical notes, both typed and written in Aston's clean, small print."
            "Lorenzo gently places a hand on either side of the notes binder and gently lifts it out of the box."
            "In the midst of placing them atop Aston's sleeping bag, a brief glint catches Lorenzo's eye."
            "It's a tiny, metal hinge on what looks like a tiny jewelry box."
            "No.{w=1.0} No…"
            play sound tinybox
            "Lorenzo picks up the small box and opens it."
            "Inside is a simple engagement ring - dark-anodized titanium with light-colored edges."
            voice "j19_DannazioneAmore"
            lo "Dannazione, amore-"
            scene maintentnight with dissolve
            
            play sound LorenzoLaugh # For Kylie ref: laugh right before the "Dannazione," just split off as SFX
            "Lorenzo laughs sadly to himself as he unzips his coat and reaches toward one of its inner pouches."
            "From within, he also procures a ring."
            "A simple engagement band - polished titanium left otherwise untouched."
            "Dark-anodized edges meant to match his hair."
            play sound grab
            "He encloses them both in one hand."
            stop music fadeout 3.0
            scene black with longfade


        else: # BRANCH 2: Ruran OK, no Aston
            #If Pearl okay, different scene start
            if not pearl_safe:
                voice "j19_br2_ShesUp"
                ja "She's up, guys!"
                "Jax calls out to us and gathers everyone into the infirmary tent."
            else:
                voice "j19_br1_ShesAwake"
                pe "She's awake! Ruran's awake!"
                "Pearl runs into the tent almost tripping over herself."
                "She gathers everyone into the infirmary tent."
            scene bg medtentnight with longfade
            play music audio.light
            show ky smile at right
            show ja neutral at centerright
            show wi smile behind ja
            show ru worried at left
            with dissolve
            voice "j19_OhIm"
            ky "Oh, I'm so glad you're okay…"
            voice "j19_RuranCan"
            ja "Ruran, can you hear us?"
            show ru neutral
            voice "j19_YesYes"
            ru "...yes…yes I can."
            voice "j19_HowsDavos"
            ru "How's…Davos?"
            "Ruran holds her hands to her head."
            voice "j19_MyBoys"
            wi "My boy's fine, Ruran. Please worry about yourself for now…"
            voice "j19_OkaySo"
            ru "Okay, so…what's our current situation?"
            voice "j19_YouWere"
            mo "You were hit by a fallen tree, with a branch sticking into the right side of your stomach."
            voice "j19_LostA"
            mo "Lost a lot of blood and then… Lost consciousness for 2 days."
            show ru confused
            voice "j19_ThatExplains"
            ru "That explains the localized pain."
            voice "j19_WhatExactly"
            gr "What exactly happened that night, Ruran?"
            voice "j19_IHeard"
            ru "I…heard something prowling outside the tent."
            voice "j19_IDecided"
            ru "I decided to take a quick look outside, then… I heard wood snap behind me."
            voice "j19_ThatsThe"
            ru "...that's the last thing I remember."
            show ja serious
            voice "j19_br2_WhenI"
            ja "When I realized you weren't in the tent and never picked up your Walkie… I went out looking for you."
            voice "j19_GregoryAnd"
            mo "Gregory and I happened to be on the way back to camp, and he dropped me off just a little ways off."
            voice "j19_LotsOf"
            gr "Lots of fallen trees. I couldn't get the snowmobile back to camp the usual way, so I had to take a detour."
            voice "j19_ThenYeah"
            mo "Then…yeah, I found you under a tree."
            voice "j19_ISeeAndWho"
            ru "I see…and who…?"
            hide ky
            hide wi
            hide ja
            with dissolve
            #show ca happy at right
            with dissolve
            "Cassie gives Ruran a small wave, pointing to herself and Lorenzo."
            show ru happy
            voice "j19_NotBad"
            ru "Not bad, you two."
            show lo sick at center
            voice "j19_ThatsBeing"
            lo "That's being…overly generous."
            show ru angry
            voice "j19_IveSpent"
            ru "I've spent years trying to teach Aston to recognize his worth… Don't make me start with you, too."
            "She pauses for a moment before sighing."
            show ru worried
            voice "j19_HeLoves"
            ru "He loves you, you know. More than I could ever express."
            voice "j19_IKnow"
            lo "I know…"
            voice "j19_SoPlease"
            ru "So, please don't think for even a moment that he would…"
            show lo sad
            voice "j19_IITryNot"
            lo "I-I try not to."
            show ru happy
            voice "j19_HeWanted"
            ru "He wanted… He wants to spend the rest of his life by your side."
            stop music fadeout 4.0
            show lo smile
            voice "j19_ThatsAll"
            lo "… That's all I ever wanted."

            #Lorenzo solo scene 
            scene black with dissolve
            play ambience amb_campnightwfire fadein 0.5

            "Lorenzo sits by the campfire."
            "He is holding what appears to be a tiny jewelry box, opened to reveal a simple titanium ring."
            "The metal is smooth but otherwise untouched, though its edges appear to be anodized to a darker color."
            "Come to think of it… This looks like the type of ring Aston would wear, but probably not buy for himself."
            "I wouldn't think of Aston as the type to wear jewelry, anyway, unless…"
            "...oh."
            stop ambience fadeout 2.0
            scene black with longfade

    else: # BRANCH 1: Aston OK, hence Ruran OK!
        voice "j19_br1_ShesAwake"
        pe "She's awake! Ruran's awake!"
        "Pearl runs into the tent almost tripping over herself."
        "She gathers everyone into the infirmary tent."
        scene bg medtentnight with longfade
        play music audio.light
        show ky smile at right
        show ast neutral at centerleft
        show ja neutral at centerright
        show wi smile behind ja
        show ru worried at left
        with dissolve
        voice "j19_OhIm"
        ky "Oh, I'm so glad you're okay…"
        voice "j19_RuranCan"
        ja "Ruran, can you hear us?"
        show ru neutral
        voice "j19_YesYes"
        ru "...yes…yes I can."
        voice "j19_HowsDavos"
        ru "How's…Davos?"
        "Ruran holds her hands to her head."
        voice "j19_MyBoys"
        wi "My boy's fine, Ruran. Please worry about yourself for now…"
        voice "j19_OkaySo"
        ru "Okay, so…what's our current situation?"
        "She looked towards Aston for answers."
        voice "j19_YoureRight"
        ast "You're right here at camp, in our tent."
        show ast inthought
        voice "j19_MorganFound"
        ast "Morgan found you under a tree. Your right side suffered a puncture wound from a tree branch."
        show ast neutral
        voice "j19_ThatExplains"
        ru "That explains the localized pain."
        voice "j19_YesYou"
        ast "Yes. You were lucky… The branch missed all your vital organs, so we were able to remove it with minimal resistance."
        show ast sad
        voice "j19_CassieLorenzo"
        ast "Cassie, Lorenzo and I… We did the best we could with what we have here."
        voice "j19_HadWe"
        ast "Had we found you later…"
        voice "j19_Hypothermia"
        ru "Hypothermia?"
        voice "j19_Yes"
        ast "Yes."
        "Ruran tries to sit up, which sends a sharp pain to her side."
        show ru scared
        voice "j19_OkayAck"
        ru "Okay…ack- No, I should stay still…"
        voice "j19_WhatExactly"
        gr "What exactly happened that night, Ruran?"
        voice "j19_IHeard"
        ru "I…heard something prowling outside the tent."
        show ru neutral
        voice "j19_ToldAston"
        ru "Told Aston that I was going to have a look, then… I heard wood snap behind me."
        voice "j19_ThatsThe"
        ru "...that's the last thing I remember."
        show ast neutral
        voice "j19_br1_WhenI"
        ast "When I realised you hadn't come back and never picked up your Walkie… I went out looking for you."
        voice "j19_GregoryAnd"
        mo "Gregory and I happened to be on the way back to camp, and he dropped me off just a little ways off."
        voice "j19_LotsOf"
        gr "Lots of fallen trees. I couldn't get the snowmobile back to camp the usual way, so I had to take a detour."
        voice "j19_ThenYeah"
        mo "Then…yeah, I found you under a tree."
        voice "j19_ISee"
        ru "I see…"
        "She looks at us one by one, taking in her surroundings once more."
        show ru happy
        voice "j19_SorryFor"
        ru "Sorry for worrying you all…but thank you. Truly."
        show wi happy
        voice "j19_NeverDo"
        wi "Never do this again, my friend. My heart can't take anymore of these scares."
        voice "j19_IllDo"
        ru "I'll do my best, Wilbur."
        show ja happy
        voice "j19_WellIf"
        ja "Well… If Ruran's okay, I think we should let her rest."
        voice "j19_ShouldAvoid"
        ja "Should avoid waking Davos up, too."
        voice "j19_AlrightOut"
        gr "Alright. Out we go, everyone."

        hide ky
        hide wi
        hide ast
        hide ja
        with dissolve

        voice "j19_CallUs"
        ca "Call us if you need anything, Ruran!"
        "Just as I was about to follow the others, Ruran called out to me."
        show ru neutral with None
        voice "j19_Morgan"
        ru "Morgan."
        voice "j19_YesRuranMorgan"
        mo "Yes, Ruran."
        show ru worried
        voice "j19_ThankYouForFinding"
        ru "Thank you for finding me. It must've been really cold."
        voice "j19_ItWas"
        mo "It was freezing, but I'd do it again for you, Ruran."
        voice "j19_Aston"
        ru "Aston…"

        #CG LETS GOOO IF WE GET ONE 
        show cg rurantentnice
        "She reaches out to hold Aston's hand lightly and looks directly at him."
        voice "j19_ThankYou"
        ru "...thank you."
        "He returns her hold with both of his hands."
        voice "j19_YoureWelcome"
        ast "You're welcome, Ruran."
        "Such simple words, but I know so much has been conveyed…"
        "…even I can feel myself tearing up a little."
        voice "j19_LorenzoCome"
        ru "Lorenzo…come here."
        voice "j19_YesRuranLorenzo"
        lo "Yes, Ruran?"
        "She brings Lorenzo's hand together with her other hand and stacks his hand on top of Aston's."
        voice "j19_LifeCan"
        ru "Life can be so fragile, but I'm so happy that you two are always together."
        voice "j19_CherishOne"
        ru "Cherish one another, okay?"
        voice "j19_WeWill"
        lo "We will."
        voice "j19_YouDont"
        ast "You don't have to tell me twice…but please don't say it like-"
        voice "j19_LikeIts"
        ru "Like it's my last wish? I don't plan to leave any time soon."
        voice "j19_IThink"
        ru "I think my head is just…not fully here. I was pulled from the brink of death."
        voice "j19_ButI"
        ru "But I think you know what I mean, yes?"
        voice "j19_IGot"
        ast "I got the message."
        voice "j19_WhatMessage"
        lo "What message, amore?"
        "Is this…a proposal in preparation?"
        "That's hella cute."
        voice "j19_NothingLorenzo"
        ru "Nothing, Lorenzo. Anyway, I think I want to take this opportunity to get a bit more sleep."
        voice "j19_IExpect"
        ru "I expect a fancy dinner for when I wake up later."
        voice "j19_ThatI"
        lo "That I can do for you, Ruran."
        stop music fadeout 3.0
        scene black with longfade
        hide cg rurantentnice

label jan_20:
    scene bg maintent_day with dissolve
    $ current_day = _("January 20th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    play ambience amb_intcampday
    play music audio.neutral
    if not ruran_safe:
        #pain
        "The next morning, a team of 4 people arrived at camp."
        "Heralign logos… They're the maintenance crew, aren't they?"
        voice "j20_br2_WhereThe"
        gr "Where the hell have you been? Three weeks of radio silence and you think you can just waltz in here like nothing ever happened?"
        "Gregory and Wilbur start grilling an older guy in a different uniform. He looks like the leader of the team…I think?"
        voice "j20_br2_WellExplain"
        wi "Well? Explain yourselves."
        voice "j20_br2_HQHas"
        st "HQ has been busy this month. We have orders to follow."
        voice "j20_br2_YouAnd"
        wi "You and I both know that's unacceptable."
        voice "j20_br2_ThreeWeeks"
        gr "Three weeks. Twenty-one days of no contact, and no one in HQ gives a shit that a bunch of us out here are fending for ourselves."
        voice "j20_br2_WereChanging"
        wi "We're changing that two-week rule to one next time. Frankly… I think even 3 days of no contact is enough to be a cause for concern."
        voice "j20_br2_CanWe"
        gr "Can we get an ambulance going?"
        voice "j20_br2_YouThink"
        st "You think we'd have cell service when the tower's down?"
        voice "j20_br2_ListenHere"
        gr "Listen here, our camp medic bled out and died last night. Wilbur's kid is still unconscious with god-knows-what kind of illness."
        voice "j20_br2_InWhat"
        gr "In what way do you not fucking understand the situation we're in?"
        voice "j20_br2_YoureNot"
        st "You're…not the only stop we have to make after we're done here."
        voice "j20_br2_DoYou"
        wi "Do you even hear yourself, Stephen?"
        voice "j20_br2_StephenVNVR"
        st "..."
        voice "j20_br2_IBet"
        gr "I bet you'd never think to bring any supplies, either."
        voice "j20_br2_GregoryI"
        st "Gregory…{w=0.7}I get that you're upset, but supply delivery's not our job."
        voice "j20_br2_AndLet"
        wi "And let me remind you that your crew, unlike ours, is at HQ. Relaying messages to the supply team isn't going to cost you anything."
        voice "j20_br2_ForgetIt"
        gr "Forget it, Wilbur. They already have trouble communicating amongst themselves to begin with."
        voice "j20_br2_JustTell"
        st "Just…tell me where the tower is. The earlier we're done, the quicker y'all can call for support."

    else: #Hooray! Life!
        "The night after Ruran woke up, a team of 4 people arrived at camp."
        "Heralign logos… They're the maintenance crew, aren't they?"
        voice "j20_br1_WhereThe"
        gr "Where the hell have you been? Three weeks of radio silence and you think you can just waltz in here like nothing ever happened?"
        "Gregory and Wilbur start grilling an older guy in a different uniform. He looks like the leader of the team…I think?"
        voice "j20_br1_GregoryLet"
        wi "Gregory, let them explain themselves."
        voice "j20_br1_HQHas"
        st "HQ has been busy this month. We have orders to follow."
        voice "j20_br1_IThink"
        wi "I think you and I both know that's unacceptable, yes?"
        voice "j20_br1_ThreeWeeks"
        gr "Three weeks. Twenty-one days of no contact, and no one in HQ gives a shit that a bunch of us out here are fending for ourselves."
        voice "j20_br1_WereChanging"
        wi "We're changing that two-week rule to one next time. Frankly… I think even 3 days of no contact is enough to be a cause for concern."
        voice "j20_br1_CanWeAtLeast"
        gr "Can we at least get an ambulance going?"
        voice "j20_br1_YouThink"
        st "You think we'd have cell service when the tower's down?"
        voice "j20_br1_GregoryVNVR"
        gr "..."
        voice "j20_br1_HowLong"
        wi "How long do you think you need, then?"
        voice "j20_br1_WeLiterally"
        st "We literally just got here. Just...{w=0.8} Ask me again when we've seen the damage." 
        voice "j20_br1_CanWeUseYour"
        gr "Can we use your truck, then?"
        voice "j20_br1_YoureNot"
        st "You're not the only stop we have to make after we're done here."
        voice "j20_br1_DoYou"
        wi "Do you hear yourself, Stephen?"
        voice "j20_br1_ThenWhat"
        gr "Then…what about camp supplies? Did you guys even think to bring any?"
        voice "j20_br1_RemindMe"
        st "Remind me again how long you've been working here, Gregory? You don't look like you're closing in on retirement age, so…provided you're still 'with it,' you ought to remember that supply delivery's not our job."
        voice "j20_br1_AndLet"
        wi "And let me remind you that your crew, unlike ours, is at HQ. Relaying messages to the supply team isn't going to cost you anything."
        voice "j20_br1_ForgetIt"
        gr "Forget it, Wilbur. They already have trouble communicating amongst themselves to begin with."
        voice "j20_br1_CutThe"
        st "Cut the crap and tell me where the tower is. The earlier we're done, the quicker I can leave."
    
    stop music fadeout 2.0
    "That's what you call camp dad supremacy."
    "Huddled in the main tent, the rest of us sit quietly, digesting what we just heard."
    "Honestly, Wilbur and Gregory had already taken the words out of our mouths."
    "There was nothing else to add."
    if not ruran_safe:
        "They're clearly still grieving…but I appreciate them for setting the record straight."
        "Heralign can't keep getting away with this…"
    else: #Ruran OK
        "And…damn, did they roast him good."
        "But Heralign can't keep getting away with this."

    "When the radio tower's up, Colin needs to hear about this."
    play music audio.neutral
    scene maintentday with dissolve
    voice "j20_HeyMorgan"
    el "Hey, Morgan?"
    "Here we go again… I should head out from the tent before I accidentally respond to him."
    stop ambience fadeout 0.5
    scene black with fade
    
    #Mini-scene with "Elliot"
    play ambience amb_campday
    with Pause(1.2)
    scene forest3 with dissolve
    voice "j20_DoYouLikeDogs"
    el "Do you like dogs, Morgan?"
    "That was a weird conversation starter."

    voice "j20_WhatDo"
    mo "What do you want?"
    voice "j20_ToTalk"
    el "To talk to you, like the good ol' times."
    voice "j20_YoureNot"
    mo "You're not him. Quit talking like that."

    if not ruran_safe: #Ruran not OK
        voice "j20_FineThen"
        el "Fine, then."
        play music audio.anxious
        voice "j20_DoYouWantTo"
        el "Do you want to know what I saw, Morgan?"

        if ru_branch_yoinked:
            voice "j20_BeforeYouSoRecklessly"
            el "Before you so recklessly killed me?"
        if ru_abandoned:
            voice "j20_BeforeYouSoHeartlessly"
            el "Before you so heartlessly left me out there to die?"

        voice "j20_MorganVNVR"
        mo "..."
        voice "j20_IKnow"
        el "I know. You didn't mean to, did you?"
        voice "j20_AfterAll"
        el "After all…{w=0.6}Aston wouldn't have wanted our reunion to be this way."
        voice "j20_ButWhen"
        el "But when it comes to the people we love… {w=0.8}We can't always get what we want."
        voice "j20_TakeA"
        el "Take a moment to reflect, Morgan."
        scene forest3
        
        voice "j20_ButAnyway"
        el "But anyway, I think you need to watch out for your surroundings more often now. Don't say I didn't warn ya!"

    else: #Ruran OK
        voice "j20_AwwwDont"
        el "Awww, don't close the door in my face."
        voice "j20_IShould"
        mo "I should be slamming it into your face."
        voice "j20_HahaThats"
        el "Haha! That's not nice!"
        voice "j20_ButArent"
        el "But aren't you a little curious to know what exactly Ruran saw? I think you'd enjoy it."
        voice "j20_EitherYou"
        mo "Either you tell me or you don't."
        voice "j20_AllIm"
        el "All I'm saying is that you need to watch out for your surroundings more often now, Morgan. Don't say I didn't warn ya!"
    "Watch out for…what?"
    "I have no idea what that means, but thank you, I guess?"
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    scene black with longfade

label jan_21:
    with Pause(1.2)
    $ current_day = _("January 21st")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    scene maintentday with dissolve
    play music audio.light
    show ja happy
    voice "j21_DoYouCarryYour"
    mo "Do you carry your rifle everywhere, Jax?"
    voice "j21_ILike"
    ja "I like to be prepared."
    voice "j21_SoWhats"
    ja "So? What's your pick?"
    "Jax hands me two options, a rifle and a pistol."

    menu jan21Weapons:
        "Take the rifle":
            $ j21_rifle = True
            "Might be a little overkill, but I do want to get some practice in."
            voice "j21_FeelingA"
            mo "Feeling a bit adventurous today, so I'll be taking this."
        "Stick with a pistol":
            $ j21_pistol = True
            "Choosing a weapon that I'm comfortable with will always be a good choice."
            voice "j21_IllBe"
            mo "I'll be sticking with my old reliable, small but mighty." 
    stop music fadeout 2.0
    show ja neutral
    voice "j21_AlrightyThen"
    ja "Alrighty then, let's go hang out with the maintenance crew."
    
    play music audio.neutral
    scene radiotowerday with longfade
    show ja neutral at centerleft
    show ky smile at centerright
    voice "j21_DidThey"
    st "Did they really need to send three of you to supervise us?"
    show ky happy
    voice "j21_JustTwo"
    ky "Just two, actually! I'm just tagging along!"
    "Jax and I were tasked to watch the maintenance crew at work today."
    "Our camp dads want to make sure that the crew doesn't slack off."
    "One day of slacking, one extra day of waiting on camp supplies."
    scene radiotowerday with dissolve
    
    if not ruran_safe:
        "And sometimes, one day wasted…costs us lives."

    "Kyle's here with us just to sightsee."
    "He's never been to the summit before. I'm sure pictures from a bird's eye view will be beautiful."
    "Okay, Morgan. Let's sit back and relax for a bit."
    scene black with fade
    with Pause(1.0)
    "..."
    "Hm. Never mind. I can't sit here for hours on end doing nothing."
    scene radiotowerday with dissolve
    show ja inthought at center

    if not ruran_safe:
        "Jax seems out of it today…even though I know he's trying to hide it."
        "He notices me staring."
        show ja serious
        voice "j21_br2_YesDo"
        ja "Yes? Do you have a question?"
        voice "j21_br2_WereYou"
        mo "Were you and Ruran close?"
        show ja inthought
        voice "j21_br2_YeahShe"
        ja "Yeah… She saved my arm from a nasty bear attack many years ago."
        voice "j21_br2_IWish"
        ja "I wish I could've returned the favor."
    
    else:
        "Jax looks deep in thought."
        "He notices me staring."
        show ja confused
        voice "j21_br1_YesMorgan"
        ja "Yes, Morgan, do you have a question?"
        voice "j21_br1_YouAnd"
        mo "You and Ruran seem to go way back."
        show ja inthought
        voice "j21_br1_YeahShe"
        ja "Yeah… She saved my arm from a nasty bear attack many years ago."
        show ja neutral
        voice "j21_br1_PeopleTalk"
        ja "People talk about risking life and limb for others, but not what it takes to keep 'em intact."
    
    with Pause(0.7)
    voice "j21_GuysI"
    ky "Guys? I don't wanna be rude, but I see a thing."
    "Our conversation was interrupted by a distressed Kyle."
    voice "j21_ThatsNot"
    mo "That's not very descriptive, Kyle. Are we talking about animals, or…?"
    voice "j21_IThink"
    stop music fadeout 2.0
    ky "I think you should come have a look yourselves…especially in case it's not…"
    scene baddawgfar with dissolve
    play music audio.anxious
    "Further in the distance, I see a weird moving mass."
    voice "j21_ISee"
    ja "I see it, Kyle. That's one ugly-looking bastard."

    voice "j21_Dawg1"
    do "Hrrr...{w=1.0}nghuuh..."
    "Could this be what Ruran heard…?"
    voice "j21_OhGreat"
    ja "Oh, great. They talk too."
    voice "j21_ThoseAre"
    ky "Those are actually…so non-friend-shaped."
    voice "j21_DontWanna"
    mo "Don't wanna pet them now, do you?"
    voice "j21_NopeNo"
    ky "Nope. No thank you."
    scene baddawgmid with dissolve
    voice "j21_Dawg2"
    do "Hhhhnheuh...{w=1.0}hnrgh-{w=0.2}gh-{w=0.4}rgh..." 
    "It's very vocal."
    voice "j21_DoYouHaveYour"
    mo "Do you…have your camera with you?"
    voice "j21_YeahLet"
    ky "Y-Yeah! Let me have a go at it."
    play sound camera2
    "*click click*"
    "Kyle quickly checks his camera."
    "These ones do show up in photos."
    voice "j21_IllGo"
    ky "I'll go grab a few more pics up cl-"
    play sound clang
    "*CLANG*"
    "A sound like falling metal rings out behind us."
    scene radiotowerday with dissolve
    voice "j21_ImSorry"
    st "I-I'm sorry, but what the hell is that?!"
    voice "j21_YouHad"
    mo "You had one job. One!"
    scene baddawggone with dissolve
    "When we turned our gaze back to the dog, it was gone."
    "Jax and I turn towards each other. Judging by his expression…{w=0.7}him, me, same page."
    "We ready our weapons and take aim, gesturing to Kyle to stand behind us."
    "..."
    "......"
    voice "j21_ToYour"
    ja "To your right, Morgan!"

    show cg baddawgclose with hpunch:
        zoom 2.8
        blur 0
        xalign 0.1
        yalign 0.7

    voice "j21_Dawg3"
    do "Hrrghau...{w=1.6}huyhr-aaaaun!"
    "Ah, shit. It looks uglier up close."
    stop music fadeout 1.0
    voice "j21_NotToday"
    mo "Not today."

    if j21_rifle:
        scene black with Dissolve(0.35)
        voice "j21_DawgDownRifle"
        do "Hrrrn...{w=1.5} Aoou-raaaur!"
        "Oh, I'm so not used to this recoil, but the dog's down."
        hide cg baddawgclose
        voice "j21_YoureNot"
        ja "You're not rusty at all!"

    if j21_pistol:
        scene black with Dissolve(0.35)
        voice "j21_DawgDownPistol"
        do "Hrrrn...{w=1.5} Aoou-raaaur!"
        "I expected no less of me. Bullseye."
        hide cg baddawgclose
        voice "j21_OhWow"
        ja "Oh, wow, that's a great shot."
    
    scene baddawggone with dissolve
    with Pause(0.2)
    voice "j21_ThankYou"
    mo "Thank you, Jax. Anyway, let's see what we have here."
    "A disfigured, mangled mess of a wolf-sized thing. Love that."
    "Goopy texture. Gross."
    "Front legs with those giant claws. Interesting…"
    "Reminds me of those markings I found the other day."
    "Hind legs that don't even look like legs…but it sure could run fast."
    "Its joints, folding in all the wrong ways."
    "And its best feature?"
    "It has a whole mushroom farm growing on its body, coming through all the fleshy bits."
    show ja confused at centerleft
    voice "j21_DidSomeone"
    ja "Did someone tear you apart and put you back together the wrong way, bud?"
    "Jax prods at the carcass with a stick from the ground."
    show ky shaken at centerright
    voice "j21_ItsLike"
    ky "It's like something made out of playdough."
    show ky sad
    voice "j21_DoWe"
    ky "D-Do we have to carry this back to Isaak?"
    voice "j21_MaybeIll"
    mo "Maybe. I'll beep him just to be sure."
    show ja inthought
    voice "j21_ItllMost"
    ja "It'll most likely be a yes."
    stop ambience fadeout 2.0
    scene black with longfade

label jan_22:
    $ current_day = _("January 22nd")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    scene maintentday with dissolve
    play music audio.neutral

    #Matt(erial) and Lorenzo beat

    "With the radio tower finally up and running again, Lorenzo was able to resume his job as a financier." 
    "He calls Matt, the main guy he liaises with about anything and everything regarding supplies."
    "Lorenzo was kind enough to show me his checklist. It was eight pages long…that's a lot."
    "It doesn't usually go up to more than five, he said."
    "Matt's in for a treat today."
    "Okay, I think he's gonna ring him up now."
    scene maintentday with dissolve
    show lo neutral
    voice "j22_IHeard"
    ma "I heard you gave the maintenance crew shit. So, what do you want, a-?"
    if aston_safe:
        show lo happy
        voice "j22_br1_HelloMatt"
        lo "Hello, Matt! How have you been?"
        voice "j22_WhatIs"
        ma "What? I-Is that you, Lorenzo?"
        show lo pondering with None
        voice "j22_br1_OhYou"
        lo "Oh? You sound like you missed me a lot!"
    else: # Aston and/or Ruran nope
        show lo sad
        voice "j22_br2_HelloMatt"
        lo "Hello, Matt... It's been awhile."
        voice "j22_WhatIs"
        ma "What? I-Is that you, Lorenzo?"

    voice "j22_NothingFeels"
    ma "Nothing feels better than talking to my favorite financier!"
    voice "j22_WhatHappened"
    ma "What happened to you, man? Getting stuck with just Gregory was…unpleasant."
    show lo smile
    voice "j22_IllTell"
    lo "I'll tell you about it the next time I'm back at HQ. For now, though, we need supplies."
    voice "j22_RightReady"
    ma "Right. Ready for your order."
    voice "j22_ThisTime"
    lo "This time, it looks like we need…"
    "Lorenzo begins listing a lengthy checklist, being sure to include ID codes on particularly uncommon requests."
    voice "j22_AhOkay"
    ma "Ah. Okay, that's a lot. General camp supplies, lab restocks and…specialized medical equipment."
    voice "j22_IHate"
    ma "{w=0.5}I hate to ask, but… Did something happen at camp…?"

    #everything is okay 
    if aston_safe:
        show lo neutral
        voice "j22_WeveHad"
        lo "We've had a few medical scares…but fortunately nothing too serious."
        voice "j22_ThankGoodness"
        ma "Thank goodness for Aston and Ruran, then. I'm glad to hear that."
        show lo smile
        voice "j22_YeahIm"
        lo "Yeah, I'm super proud of them."
    #nuh uh route
    else:
        show lo sad
        voice "j22_TheresBeen"
        lo "There's been…{w=0.3}a lot, Matt. I'm not sure where to start."
        voice "j22_ImAll"
        ma "I'm all ears if you want to unload."
        voice "j22_IllTake"
        lo "I'll take you up on that offer…but let's do it another time. I'm still processing everything that's happened."

    hide lo with dissolve
    "They're still on the phone, but I think I've heard enough."
    "Let me head outside to catch some fresh air."
    scene camp3day with dissolve
    with Pause(0.8)
    "Oh. Guess who else's on the phone?"
    "And…{w=0.4}is that Wilbur hiding behind a large tree?"

    #Hilda and Gweggy beat
    show gr angry at centerright
    voice "j22_WellHello"
    hi "Well…hello, Gregory. How-"
    voice "j22_CutThe"
    gr "Cut the pleasantries, Hilda."
    "Confirmation for Colin! It is indeed Hilda."
    voice "j22_ThatAttitude"
    hi "That attitude of yours needs to st-"
    show gr neutral with None
    voice "j22_RadioTower"
    gr "Radio tower down, comms down…and three weeks of absolute silence."

    if aston_safe:
        voice "j22_br1_DoYou"
        gr "Do you expect me to be cheery and happy right now?"
        show gr angry
        voice "j22_br1_TellMe"
        gr "Tell me. How am I supposed to stay calm when the rest of us out here are falling ill, one by one?"
        voice "j22_br1_EvenIf"
        gr "Even if you don't care about us at all… Isn't the research important to you?"
        voice "j22_br1_WhyDid"
        gr "Why did it take you three whole weeks to reach us?"
        voice "j22_br1_HildaVNVR"
        hi "..."
        voice "j22_br1_TheShort"
        hi "The short answer is that I had the coppers pay me a visit…" 
        voice "j22_br1_BargingInto"
        hi "Barging into my office waving their stupid papers at me… That took way too much of my time."
        voice "j22_br1_AsFor"
        hi "As for the state of the camp... I hear you. But the research needs to carry on."

    else:
        voice "j22_br2_AndWere"
        gr "And we're still missing people from our camp…"
        if not ruran_safe: #Additional line if Ruran's also dead
            show gr confused
            voice "j22_br2_WeveLost"
            gr "We've lost both, Hilda. Both our medics."
        show gr angry
        voice "j22_br2_TheRest"
        gr "The rest of us were out here all on our own, Hilda. Wilbur's son might be dying. You want me to stay calm in a time like this?"
        voice "j22_br2_IDont"
        gr "I don't expect you to think of us, at all… Your cold dead heart could never do that."
        voice "j22_br2_IJust"
        gr "I just want to know why… Why three whole weeks?"
        voice "j22_br2_HildaVNVR"
        hi "..."
        voice "j22_br2_TheShort"
        hi "The short answer is that I had the coppers pay me a visit…" 
        voice "j22_br2_SearchWarrant"
        hi "Search warrant whatnot, I don't really care… But that took way too much of my time."
        voice "j22_br2_AsFor"
        hi "As for the state of the camp... I hear you. I'll send you however many replacements you need, but the research needs to carry on."

    #Historically, Hilda hanging up on Gregory hasn't made a sound? "play sound beep" if that's different this time, for whatever reason
    "*beep*"
    "It would seem that Hilda hung up on him."
    show gr angry
    voice "j22_GregoryVNVR"
    gr "..."
    hide gr
    play sound kick
    stop music fadeout 10.0
    "He throws his satellite phone into the snow…then sits down on the cold ground a few moments after."
    scene camp3day with dissolve
    
    play ambience amb_campday fadein(1.0)
    show wi worried at centerleft
    voice "j22_WilburVNVR"
    wi "..."
    "Wilbur is really concerned and disturbed…"
    "I think it's fair to guess that hearing this info is a first for him."
    play sound cloth # or whatever else makes sense
    "He gets up from his hiding spot, and-"
    "Oh, whoops, he noticed me."
    "He turns his head to look at Gregory, and then back at me. A signal for me to follow him."

    #Morgan and Wilbur beat

    scene forest3 with longfade
    play music audio.sad
    show wi serious
    voice "j22_IsThis"
    wi "Is this why Lorenzo didn't want to go back to camp?"
    "Wilbur goes straight to the questions."
    voice "j22_YesWe"
    mo "Yes. We were worried about Gregory… How he'd react to Lorenzo, or any one of us being sick."
    show wi worried
    voice "j22_WhatDo"
    wi "What do you mean?"

    menu jan22WilburConvo:
        "Mention the papers":
            $ greg_sus += 1
            $ jan22_wilburPapers = True
            voice "j22_WeveFound"
            mo "We've found profiles of everyone at camp, and… You know what, let me just show them to you."
            "Wilbur skims through the copies that I have on my phone."
            voice "j22_YourePositive"
            wi "You're positive these are his, lad?"
            "I gave Wilbur an affirmative nod."

        "Don't mention the papers":
            voice "j22_IMean"
            mo "I mean, it's not the first time I've heard him on the phone with Hilda, I think."
            voice "j22_TheyveBeen"
            mo "They've been bringing up the idea of people getting sick… I don't want to imagine what that entails."

    "Wilbur takes a moment to think."
    show wi serious
    voice "j22_ThankYou"
    wi "Thank you for your honesty, Morgan. I... {w=0.6}I need some time to think about this."
    "With that, Wilbur walks off toward the main tent."
    stop ambience fadeout 2.0
    stop music fadeout 2.0


    #Morgo Corgo beat
    scene morganstent with longfade
    play music audio.light
    show satphone

    voice "j22_Pancake"
    mo "Pancake!"
    #voice "j22_Morgan"
    if radio_static == "_s":
        voice "j22_Morgan_s"
    else:
        voice "j22_Morgan_c"
    co "Morgan!"
    voice "j22_ItsMe"
    mo "It's me!"
    #voice "j22_ItsYou"
    if radio_static == "_s":
        voice "j22_ItsYou_s"
    else:
        voice "j22_ItsYou_c"
    co "It's you!"
    voice "j22_ThatsRight"
    mo "That's right! Your one and only, the best of the best, charming and-"
    #voice "j22_OkayThats"
    if radio_static == "_s":
        voice "j22_OkayThats_s"
    else:
        voice "j22_OkayThats_c"
    co "Okay, that's enough."
    voice "j22_IveJust"
    mo "I've just… I've missed you so much, Pancake."
    #voice "j22_AwwI"
    if radio_static == "_s":
        voice "j22_AwwI_s"
    else:
        voice "j22_AwwI_c"
    co "Aww. I could shed a tear, Morg."
    "Colin sounds very happy to hear me."
    #voice "j22_IdLove"
    if radio_static == "_s":
        voice "j22_IdLove_s"
    else:
        voice "j22_IdLove_c"
    co "I'd love to hear updates on the camp, but first… How are you, Morg?"
    voice "j22_OohHoo"
    el "Ooh-hoo-hoo. You wanna tell Pancake that you found me?" 
    voice "j22_MorganVNVR"
    mo "..."
    "Shut up, Elly."
    voice "j22_GoOn"
    el "Go on, bud."
    voice "j22_GimmeA"
    mo "Gimme a moment."
    stop music fadeout 3.0
    #voice "j22_YouDont"
    if radio_static == "_s":
        voice "j22_YouDont_s"
    else:
        voice "j22_YouDont_c"
    co "You don't sound good. What's wrong?"
    voice "j22_ComeOn"
    el "Come on, he's waiting."

    if not aston_safe:
        if not pearl_safe:
            if not ruran_safe: # All 3 gone
                voice "j22_WereWaiting_AstRuPearl"
                el "We're waiting on you, too."
                jump postHal
            else: # Ruran safe, Aston and Pearl dead
                voice "j22_WereWaiting_AstPearl"
                el "We're waiting on you, too."
                jump postHal
        if not ruran_safe:
            if not pearl_safe: # All 3 gone
                voice "j22_WereWaiting_AstRuPearl"
                el "We're waiting on you, too."
                jump postHal
            else: # Pearl safe, Aston and Ruran dead
                voice "j22_WereWaiting_AstRu"
                el "We're waiting on you, too."
                jump postHal
        else: # just Aston gone
            voice "j22_WereWaiting_Ast"
            el "We're waiting on you, too."
            jump postHal
    # Implied "else" at the end of this is that Aston's OK, in which case the line won't play at all
    
    label postHal:
        with Pause(1.2)
        play music audio.neutral
        voice "j22_IThink"
        mo "I think… I've been hearing Elly in my head. It hasn't been fun."
        #voice "j22_HasIt"
        if radio_static == "_s":
            voice "j22_HasIt_s"
        else:
            voice "j22_HasIt_c"
        co "Has it gotten to you?"
        voice "j22_YeahSorry"
        mo "Yeah… {w=0.4}Sorry."
        #voice "j22_WeDont"
        if radio_static == "_s":
            voice "j22_WeDont_s"
        else:
            voice "j22_WeDont_c"
        co "We don't have to do this today, Morg. I'm just glad to know that you're safe and alive."
        #voice "j22_UpdatesFor"
        if radio_static == "_s":
            voice "j22_UpdatesFor_s"
        else:
            voice "j22_UpdatesFor_c"
        co "Updates for another time."
        stop music fadeout 8.0
        # call end SFX? 
        hide satphone
        "With that, we end the call."
        "Colin's right… Better to wait until tomorrow."
        scene black with longfade

label jan_23:
    play music audio.neutral
    $ current_day = _("January 23rd")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    scene morganstent with dissolve
    "I relayed most of the details to Colin through text last night."
    "All three weeks' worth of events…"
    "I promised I'd call him today."
    # play sound whatever normal for Colin
    show satphone
    "*beep*"
    #voice "j23_ColinVNVR"
    if radio_static == "_s":
        voice "j23_ColinVNVR_s"
    else:
        voice "j23_ColinVNVR_c"
    co "..."
    voice "j23_PancakeHow"
    mo "Pancake! How are you?"
    #voice "j23_YeahThere"
    if radio_static == "_s":
        voice "j23_YeahThere_s"
    else:
        voice "j23_YeahThere_c"
    co "Yeah, there it is. I'm alright, Morg. Is today going well for you?"
    voice "j23_NotReally"
    mo "Not really… Greggy's having a fun time calling for emergency services. They haven't been picking up."

    if not ruran_safe:
        voice "j23_BuryingA"
        mo "Burying a body with no assistance or extra supplies is…not something I'm looking forward to."
        #voice "j23_MyCondolences"
        if radio_static == "_s":
            voice "j23_MyCondolences_s"
        else:
            voice "j23_MyCondolences_c"
        co "My condolences, Morg…but I'm sure Ruran wouldn't blame y'all for this."
        voice "j23_YeahI"
        mo "Yeah. I know I can handle it. But, my campmates…"
        "An image of January 19th flashes through my mind…"
    
    #voice "j23_IHear"
    if radio_static == "_s":
        voice "j23_IHear_s"
    else:
        voice "j23_IHear_c"
    co "I hear you. But, if emergency services can't be reached…is there still an issue with the tower?"
    voice "j23_SeeingAs"
    mo "Seeing as we're talking right now, I doubt it. Lorenzo was able to contact the supply crew, and Gregory…absolutely blew up on Hilda yesterday."
    #voice "j23_ThatsAn"
    if radio_static == "_s":
        voice "j23_ThatsAn_s"
    else:
        voice "j23_ThatsAn_c"
    co "That's an interesting turn of events…but not an unexpected one."
    #voice "j23_ButThe"
    if radio_static == "_s":
        voice "j23_ButThe_s"
    else:
        voice "j23_ButThe_c"
    co "But the biggest surprise…are those wolves. In your notes, you called them 'photographable, goopy, and shroom-y?'"
    voice "j23_YupThey"
    mo "Yup. They can talk, too, but seem relatively easy to kill."
    voice "j23_WishYou"
    mo "Wish you saw me in action. I was pretty cool."
    #voice "j23_IveAlready"
    if radio_static == "_s":
        voice "j23_IveAlready_s"
    else:
        voice "j23_IveAlready_c"
    co "I've already seen you in action, Morg. Brag all you like."
    "A thought suddenly crossed my mind."
    voice "j23_RandomQuestion"
    mo "Random question, Pancake. Has… Elly ever told you he had a sister?"
    #voice "j23_YeahWhat"
    if radio_static == "_s":
        voice "j23_YeahWhat_s"
    else:
        voice "j23_YeahWhat_c"
    co "Yeah. What about her?"
    voice "j23_DoYou"
    mo "Do you know…if her name is Eva?"
    #voice "j23_EvaElly"
    if radio_static == "_s":
        voice "j23_EvaElly_s"
    else:
        voice "j23_EvaElly_c"
    co "Eva? Elly didn't really… {w=0.8}Wait, Morg, do you mean Eva from the RC team?"
    voice "j23_SheLooks"
    mo "She looks like a copy of Elly, but…we haven't spoken about him. At least, not yet."
    #voice "j23_AreYou"
    if radio_static == "_s":
        voice "j23_AreYou_s"
    else:
        voice "j23_AreYou_c"
    co "Are you worried that your cover's been compromised?"
    voice "j23_IFeel"
    mo "I feel like if that were the case, I would've been offed already."
    #voice "j23_StaySafe"
    if radio_static == "_s":
        voice "j23_StaySafe_s"
    else:
        voice "j23_StaySafe_c"
    co "Stay safe, please. Doing reckless shit this far into the op won't help anyone."
    voice "j23_IKnow"
    mo "I know, and I'll be careful…but I'm also not backing out after getting so close to real answers. Your papa ain't a quitter."
    #voice "j23_MyPapa"
    if radio_static == "_s":
        voice "j23_MyPapa_s"
    else:
        voice "j23_MyPapa_c"
    co "My papa? What do you me- {w=0.3}Oh. I forgot about being your pseudo-5-year-old."
    voice "j23_NoYoure"
    mo "No, you're 4 years old, sweetie."
    #voice "j23_DoesIt"
    if radio_static == "_s":
        voice "j23_DoesIt_s"
    else:
        voice "j23_DoesIt_c"
    co "Does…it make any difference?"

    if aston_safe and ruran_safe and pearl_safe:
        voice "j23_YeahOf"
        mo "Yeah, of course it does! But…thanks for this, Pancake. I've missed our chats."
    else: #Someone's dead
        voice "j23_YeahBut"
        mo "Yeah. But…thanks for this, Pancake. You really do keep me sane."
    
    #voice "j23_FeelingsMutual"
    if radio_static == "_s":
        voice "j23_FeelingsMutual_s"
    else:
        voice "j23_FeelingsMutual_c"
    co "Feeling's mutual, Morg. Now, go do your thing. You have a case to solve."
    voice "j23_AlrightBye"
    mo "Alright. Bye-bye, Pancake!"
    #voice "j23_YeahOkay"
    if radio_static == "_s":
        voice "j23_YeahOkay_s"
    else:
        voice "j23_YeahOkay_c"
    co "Yeah, okay - bye."
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    scene black with longfade

label jan_24:
    $ current_day = _("January 24th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    if aston_safe or ruran_safe:
        $ davos_safe = True
    else:
        $ davos_safe = False
    with Pause(2.0)
    scene medtent with dissolve
    play ambience amb_intcampday
    if not davos_safe: # Wilbur version
        show wi sad
        "I walked into the quarantine tent today to find Wilbur next to Davos' bed, flipping through a small scrapbook."
        voice "j24_HesA"
        wi "He's a sweet boy, you know."
        voice "j24_MyWife"
        wi "My wife was…very much the same."
        play music audio.oof
        "The book is open to a page filled with pressed flowers."
        "Wilbur gently places his hand next to a pressed Edelweiss at its center."
        show wi neutral
        voice "j24_TheseWere"
        wi "These were her favorites. Flowers were…a passion of hers. And Davos…"
        play sound bookclose
        "He gently closes the book, his eyes fixed on his son."
        show wi worried
        voice "j24_HeMeans"
        wi "He means more to me than I could ever express. My final gift to her is…ensuring that he's safe."
        voice "j24_WhateverMust"
        wi "Whatever must be done for him to…"
        "Wilbur stops and shakes his head, laughing softly to himself."
        show wi happy
        voice "j24_HellBe"
        wi "He'll be alright, Morgan. I have to believe that."
    else:
        with Pause(1.5)
        show da neutral
        voice "j24_Morgan"
        da "Morgan!"
        voice "j24_OhNice"
        mo "Oh, nice! You're up."
        voice "j24_WhatAre"
        mo "What are you looking at?"
        show da happy
        voice "j24_HereCome"
        da "Here, come sit with me. I'll show you."
        "I sit down on the edge of Davos' bed. He has a small scrapbook placed in his lap, open to a page full of pressed flowers."
        play music audio.oof
        "Around each one is a brief anecdote, seemingly focused around the journey to harvest each one."
        voice "j24_MyMom"
        da "My mom really loved these when she was alive."
        "He points toward a pressed Edelweiss at the center of the page."
        show da neutral 
        voice "j24_WhenI"
        da "When I was younger, pops would bring home a bunch of 'em for her."
        show da happy
        voice "j24_TheWay"
        da "The way her face would light up every time…"
        "Davos pauses for a moment."
        voice "j24_CollectingFlowers"
        da "Collecting flowers was one of her favorite things. As a kid, I always said that we'd travel the world gathering new varieties. So, now that it's just pops and me…"
        show da neutral
        voice "j24_ItMight"
        da "It might be a little silly, but I'd love to collect flowers from every single continent. For her. …except Antarctica."
        voice "j24_YeahThatd"
        mo "Yeah. That'd be a little difficult."
        play sound DavosLaugh
        play sound bookclose
        "Davos laughs and closes the scrapbook." 
        voice "j24_AlrightBedtime"
        mo "Alright. Bedtime for you, toasty."
        show da happy
        voice "j24_Toasty"
        da "Toasty?"
        voice "j24_YeahUnless"
        mo "Yeah. Unless you'd prefer…'petal?'"
        show da neutral
        voice "j24_ToastyIs"
        da "Toasty is fine."
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    scene black with longfade

label jan_25:
    $ current_day = _("January 25th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    scene maintentday with dissolve
    play music audio.neutral
    if aston_safe:
        show ast neutral at left
        show lo neutral at right
        "Lorenzo has his journal open to his illustration of the bear."
        "He has a picture of the ugly dog that Kyle took the other day, drawing its features next to the bear."
        voice "j25_BearsBirds"
        mo "Bears, birds, and wolves… What's next? A cow?"
        show ast happy
        voice "j25_CarefulWhat"
        ast "Careful what you wish for, Morgan."
        show lo pondering
        voice "j25_SusieBiting"
        lo "Susie biting Kyle might not mean anything, but still..."
        show lo smile
        "Lorenzo puts his pen down and looks at his finished piece."
        show ja happy behind ast
        voice "j25_HeyWhat"
        ja "Hey, what are y'all up to?"
        voice "j25_LorenzosHere"
        mo "Lorenzo's here drawing the animals we've encountered."
        show ja confused
        voice "j25_WhatsWith"
        ja "What's…with the bear?"
        "Aston and Lorenzo looked at each other for a moment. Debating whether to tell him, maybe?"
        show ast sad
        voice "j25_br1_BeforeThe"
        ast "Before the avalanche, Lorenzo had been having nightmares about a monstrous bear. Well…calling it a bear is a bit generous, seeing as it doesn't look or act like a normal bear."
        show lo neutral
        voice "j25_br1_ThenIt"
        lo "Then it started appearing during my waking hours, calling out to me…"
        voice "j25_br1_TheWorst"
        lo "The worst part was that it sounded like Aston."
        voice "j25_br1_AstonAnd"
        mo "Aston and I were never able to see it, but Lorenzo could… Think hallucinations, Jax."
        show ja shaken
        voice "j25_WaitThis"
        ja "Wait, this is news to me."
        show ja serious
        voice "j25_YoureSaying"
        ja "You're saying that the whole time you were in the cabin, you had an eldritch bear lurking outside…that sounded like a human being?"
        show lo pondering
        voice "j25_YesBut"
        lo "Yes, but I've never been able to actually…touch it? I don't want to attempt that."
        voice "j25_KyleCaught"
        mo "Kyle caught a glitched out photo of a bear once…but you and I both know that it ain't bear season yet."
        show lo neutral
        show ast inthought
        with dissolve
        voice "j25_IAlso"
        ast "I also experienced something similar to Lorenzo's bear…albeit mostly in the form of auditory hallucinations."
        voice "j25_TheyWere"
        ast "They were…screams in the distance, sounding like a highly distressed Lorenzo."
        "Jax looks visibly disturbed by this information."
        show ja inthought
        voice "j25_DontTell"
        ja "Don't tell me you're having these hallucinations too, Morgan."
        voice "j25_IWish"
        mo "I wish I didn't...mine currently comes in the flavor of 'voices in my head.' Nothing visual."
        show ja serious
        voice "j25_IGuess"
        ja "I guess that would explain why you guys seem out of it sometimes…"
        show ast happy
        voice "j25_IDidnt"
        ast "I didn't realise it would be that obvious."
        
        # Next line is a "Maybe" inclusion depending on if it feels OK tonally! If not, should go right from "I didn't realise..." to "Nah, I'm just observant."
        #voice "j25_YouPay"
        #mo "You pay that much attention to me? I'm flattered, Jax."
        show ja happy
        voice "j25_NahIm"
        ja "Nah, I'm just observant."
        show lo smile
        voice "j25_WellIm"
        lo "Well, I'm glad that you're watching over us, Jax."

    else:
        show lo pondering at right
        "Lorenzo has his journal open to his illustration of the bear."
        "He has a picture of the ugly dog that Kyle took the other day, drawing its features next to the bear."
        voice "j25_BearsBirds"
        mo "Bears, birds and wolves… What's next? A cow?"
        show lo neutral
        voice "j25_WeDid"
        lo "We did have Susie."
        "Lorenzo puts his pen down and looks at his finished piece."
        show ja happy behind lo
        voice "j25_HeyWhat"
        ja "Hey, what are y'all up to?"
        voice "j25_LorenzosHere"
        mo "Lorenzo's here drawing the animals we've encountered."
        show ja confused
        voice "j25_WhatsWith"
        ja "What's…with the bear?"
        "Lorenzo looked at me for a moment before continuing."
        show lo sad
        voice "j25_br2_BeforeThe"
        lo "Before the avalanche, I had been having nightmares about a… Well, calling it a bear is a bit generous, since it doesn't look or act like a normal bear."
        voice "j25_br2_ThenIt"
        lo "Then it started appearing during my waking hours, calling out to me…"
        show lo sick
        voice "j25_br2_TheWorst"
        lo "The worst part was that it sounded like Aston."
        voice "j25_br2_AstonAnd"
        mo "Aston and I were never able to see it, but Lorenzo could… Think hallucinations, Jax."
        show lo sad
        show ja shaken
        with dissolve
        voice "j25_WaitThis"
        ja "Wait, this is news to me."
        show ja serious
        voice "j25_YoureSaying"
        ja "You're saying that the whole time you were in the cabin, you had an eldritch bear lurking outside…that sounded like a human being?"
        show lo pondering
        voice "j25_YesBut"
        lo "Yes, but I've never been able to actually…touch it? I don't want to attempt that."
        voice "j25_KyleCaught"
        mo "Kyle caught a glitched out photo of a bear once…but you and I both know that it ain't bear season yet."
        show lo neutral
        voice "j25_BeforeAston"
        mo "Before Aston disappeared, he told me that something similar was happening to him."
        voice "j25_AuditoryHallucinations"
        mo "Auditory hallucinations, sounding like Lorenzo screaming in distress."
        "Jax looks visibly disturbed by this information."
        show ja inthought
        voice "j25_DontTell"
        ja "Don't tell me you're having these hallucinations too, Morgan."
        voice "j25_IWish"
        mo "I wish I didn't...mine currently comes in the flavor of 'voices in my head.' Nothing visual."
        show ja serious
        voice "j25_IGuess"
        ja "I guess that would explain why you guys seem out of it sometimes…"
        voice "j25_YouPay"
        mo "You pay that much attention to me? I'm flattered, Jax."
        show ja happy
        voice "j25_NahIm"
        ja "Nah, I'm just observant."
        show lo smile
        voice "j25_WellIm"
        lo "Well, I'm glad that you're watching over us, Jax."
    stop music fadeout 3.0
    scene black with longfade


label jan_26:
    $ current_day = _("January 26th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    scene camp3day with dissolve
    play music audio.neutral 
    show ca sad at centerleft
    show ky neutral at centerright
    with dissolve

    # BRANCH ONE: People OK
    if aston_safe and pearl_safe and ruran_safe:
        voice "j26_br1_EveryonesFalling"
        ca "Everyone's falling sick, we're dealing with ugly dogs..."
        voice "j26_br1_WhatAre"
        ca "What are we not seeing?"
        "I overheard Cassie and Kyle having a conversation outside the tent."
        show cg j26kylecassie
        voice "j26_br1_TheresA"
        ky "There's a lot that we don't know…but we'll figure it out somehow, Cassie. I'm sure of it."
        voice "j26_br1_HowKyle"
        ca "How, Kyle? What do you think we should do?"
        voice "j26_br1_WeJust"
        ky "We just need to concentrate our efforts into one giant bubble."
        voice "j26_br1_YouBetter"
        ca "You better not do anything stupid."
        "I agree."
        voice "j26_br1_IWont"
        ky "I won't."
        $ j26_fight = False

    # BRANCH TWO: At least one person gone
    else:
        voice "j26_br2_EveryonesFalling"
        ca "Everyone's falling sick, we're dealing with ugly dogs…"

        if not aston_safe or not pearl_safe:
            voice "j26_br2_AndWe"
            ca "And we still have missing people."
        if not ruran_safe:
            voice "j26_br2_AndNow"
            ca "And now… Ruran's dead, Kyle."

        "It looks like both of them are having a bit of a moment."
        "Cassie's really upset. Honestly, who wouldn't be?"
        voice "j26_br2_IWantToDo"
        ca "I want to do something - anything. I want to help, but I don't know what to do."
        voice "j26_br2_IWantPeopleTo"
        ca "I want…people to stop leaving."
        voice "j26_br2_MeToo"
        ky "Me too, Cassie. I'll do something about it."
        show cg j26kylecassie
        voice "j26_br2_HowKyle"
        ca "How, Kyle? What exactly can we do?"
        voice "j26_br2_BabySteps"
        ky "Baby steps, okay? We just need to concentrate our efforts into one giant bubble."
        voice "j26_br2_YouBetter"
        ca "You better not do anything stupid."
        "Yeah. Please don't, Kyle."
        voice "j26_br2_IWont"
        ky "I won't."
        $ j26_fight = True

        stop music fadeout 3.0
        scene black with longfade

label jan_27:
    $ current_day = _("January 27th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    scene medtentnight with dissolve
    play ambience amb_intcampnight
    show isa neutral at left
    show ca inthought at center
    with dissolve
    "What's with the crowd…?"
    voice "j27_DavosIs"
    ca "Davos is still asleep."
    voice "j27_HesIn"
    isa "He's in bad shape."
    "Oh, it's everyone from the RC…including Isaak."
    show ca sad
    voice "j27_YeahHe"
    ca "Yeah, he started breaking out into a cold sweat a few days ago."
    voice "j27_NowHes"
    ca "Now he's just drifting in and out of consciousness."
    show isa inthought
    voice "j27_Fever"
    isa "Fever?"
    voice "j27_HighFever"
    ca "High fever, common cold symptoms… He threw up once, too."
    hide ca
    hide isa
    with dissolve
    "Cassie continues talking about Davos' condition in detail with Isaak."
    "Meanwhile, Eva and Koda are sitting next to Davos."
    show ko sad at centerleft
    show ev worried at centerright
    with dissolve
    voice "j27_AreYou"
    ev "Are you going to stay the night, Koda?"
    voice "j27_YeahI"
    ko "Yeah… I think I should."
    #If Pearl okay
    if pearl_safe:
        show pe depressed at right
        voice "j27_IfThe"
        pe "If the RC needs you, Eva, you can go. I'll stay here with Koda."
        voice "j27_AlrightThanks"
        ev "Alright… Thanks, Pearl."
    else: #If Pearl nuh uh
        voice "j27_IllBe"
        ev "I'll be outside, then. Isaak needs at least one other person with him at the RC."
    
    scene medtentnight with dissolve
    "Eva looks at Davos for a few moments and then takes her leave."
    "Isaak follows soon after."
    "Best I leave them be for now."

    scene black with fade
    stop ambience fadeout 3.0
    with Pause(2.0)

label jan_28:
    play ambience amb_rc
    $ current_day = _("January 28th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    scene black
    voice "j28_Screech1"
    bi "*screech*"
    play music audio.anxious
    # It's honestly eerier without seeing Eva's lab at all, so keeping it in DARKNESS
    voice "j28_WasThat"
    ev "Was…that indoors?"
    "Eva was alone at her station when all of a sudden she heard a call of a distressed animal."
    "The source of the sound… It's coming from Isaak's station."
    "The lab door was ajar, prompting Eva to take a look inside."
    voice "j28_WhatIs"
    ev "What is he handling in there…?"
    # Eventual CG bird-stab, black scene for now to ensure the timing isn't wonky
    scene black with dissolve
    voice "j28_Screech2"
    bi "*screech*"
    voice "j28_OhThis"
    isa "Oh, this one is still alive."
    voice "j28_ThatllDo"
    isa "...that'll do it."
    scene isaaklab2 with dissolve
    show isa inthought at right
    voice "j28_WhatThe"
    ev "What the hell are you doing?"
    "Isaak doesn't turn to face her."

    voice "j28_ExactlyWhat"
    isa "Exactly what you think I'm doing."
    "Isaak pries open the now-unconscious bird's beak slightly."
    play sound birdyeet
    "He pops a tiny pill in its mouth, and chucks it back into a small cage beside him before moving on to the next bird."
    show isa serious
    voice "j28_IdAdvise"
    isa "I'd advise against stepping in here without protective gear."
    voice "j28_ImNot"
    ev "I'm not inviting myself in there after what I just saw."
    "She takes a moment to collect herself."
    voice "j28_WhereDid"
    ev "Where did you get these…{w=0.4}birds?"
    voice "j28_FromThe"
    isa "From the ground. They're the same ones that Morgan found last month."
    stop music fadeout 10.0
    voice "j28_IFind"
    ev "I find that hard to believe…"
    voice "j28_SoWhats"
    ev "So, what's the pill for, then? Did you make those?"
    show isa inthought
    voice "j28_ExperimentationFor"
    isa "Experimentation for a cure. I want to see how it reacts to the mold."
    voice "j28_SoWeve"
    ev "So we've decided that it's just called - 'The Mold.' Not the most creative name…"
    show isa serious with None
    voice "j28_IfThis"
    isa "If this so-called source of medicine that Heralign wants us to find is causing more harm than good… Shouldn't we figure out a cure, Eva?"
    voice "j28_YouMake"
    ev "You make it sound so easy."
    voice "j28_IdNeed"
    isa "I'd need to collect samples from Davos, too. Just to be sure."
    voice "j28_AreYou"
    ev "Are you out of your damn mind?"
    show isa happy
    voice "j28_NotQuite"
    isa "Not quite…? I don't plan to cut him up like this little birdie here."
    "Eva isn't entirely sure if he's joking."
    "...especially not after what she just witnessed."
    scene black with longfade
    stop ambience fadeout 2.0

label jan_29:
    play ambience amb_village
    $ current_day = _("January 29th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    scene village2 with dissolve #TODO: Village 1 with just Kyle + Susie no kids
    with Pause(2.5)
    
    voice "j29_HiSusie"
    ky "Hi, Susie! It's me, Kyle! You gave me a nasty bite last time, remember?"
    voice "j29_SusieVNVR"
    vs "..."
    voice "j29_DontLook"
    ky "Don't look sad, Susie. I forgive you."
    "Kyle's hanging around Susie, taking pictures of her once more."
    scene black with dissolve
    #Janky fix for now
    "He left camp this morning, worried about the farm animals and the people at the village."
    "Those…wolves. They pose a huge threat."
    "If they haven't been informed, they need to be as soon as possible."
    #Either BG transition to version that includes Ethan or flip to version w/o Kyle by Susie + include Ethan sprite
    play music audio.light
    show village2 with dissolve
    voice "j29_HelloWelcome"
    et "Hello! Welcome to the village!"
    show ky happy with dissolve
    voice "j29_OhHello"
    ky "Oh, hello! I'm Kyle!"
    voice "j29_WaitI"
    et "Wait… I know you! Welcome back, I'm Ethan!"
    voice "j29_IveSeen"
    et "I've seen you hanging around Uncle Ferdinand's house…and at his burial."
    show ky sad
    voice "j29_AhYeah"
    ky "Ah, yeah… My condolences, Ethan. He was such a great guy…"
    "Ethan pats Kyle on the back."
    voice "j29_IKnowIMiss"
    et "I know… I miss him too."

    voice "j29_HowsThe"
    ky "How's the family doing, by the way?"
    voice "j29_TheyHad"
    et "They had a rough few weeks…but I'm glad that Aunt Sonya is taking good care of herself."
    voice "j29_ShesBeing"
    et "She's being really strong for the sake of the kids…"
    show ky confused
    voice "j29_AndSusie"
    ky "And Susie? She hasn't mooed at me yet."
    hide ky
    "Kyle reaches out at Susie…again."
    stop music
    voice "j29_KyleDont"
    et "Kyle! Don't!"
    "He yanks Kyle's arm away from Susie."
    voice "j29_SusieShes"
    et "Susie, she's… She's not Susie right now."
    voice "j29_Moo"
    vs "Mooooo…"
    voice "j29_What"
    ky "W-What…"
    voice "j29_MooMoo"
    vs "Moo-moooooooo… moo…"
    "Susie's voice…sounds like garbled nonsense."
    play music audio.light
    voice "j29_ItHappens"
    et "It happens every year when the lake unfreezes. Our friends…get sick. They don't act like themselves."
    voice "j29_MyCousin"
    et "My cousin is doing his best to find a cure for them… For us."
    voice "j29_CousinThats"
    ky "Cousin? That's so cool of him!"
    voice "j29_OhUh"
    et "O-Oh, uh, well… I don't know if he'd associate himself with 'cool?' But I think he is."
    voice "j29_ButPoor"
    ky "But poor Susie… She sounds like she's in pain."

    if ruran_safe and pearl_safe:
        voice "j29_br1_OhIm"
        ky "Oh! I'm here today because I needed to tell someone about the wolves."
    else:
        voice "j29_br2_OhIm"
        ky "Oh! I'm here today because I needed to tell someone about the wolves."

    voice "j29_WolvesThe"
    et "Wolves? The non-friend-shaped doggos that look…interesting?"
    voice "j29_YouCall"
    ky "You call them that, too? I love that! {w=0.5}But, um…yes."

    show cg ethankyle with dissolve

    if ruran_safe:
        voice "j29_WeveSeen"
        ky "We've seen a few in the woods around our camp, so please tell everyone to watch out for them."
    else: # Ruran dead
        voice "j29_AndWell"
        ky "And, well…they… They're just really bad news, so please, tell everyone to be careful?"
    voice "j29_IWill"
    et "I will."

    if ruran_safe and pearl_safe:
        voice "j29_br1_OkayGood"
        ky "Okay, good. I'll head back to camp now before it gets dark."
        voice "j29_br1_MyJob"
        ky "My job here is done!"
    else:
        voice "j29_br2_OkayGood"
        ky "Okay, good. I'll head back to camp now before it gets dark."
        voice "j29_br2_MyJob"
        ky "My job here is done!"

    voice "j29_ComeBack"
    et "Come back soon? We rarely get visitors, and it's always nice to meet new friendly faces!"

    if ruran_safe and pearl_safe:
        voice "j29_br1_IllEven"
        ky "I'll even bring my friends over next time!"
    else:
        voice "j29_br2_IllEven"
        ky "I'll even bring my friends over next time!"

    voice "j29_ItsA"
    et "It's a promise, then!"
    stop ambience fadeout 1.0
    stop music fadeout 2.0
    scene black with longfade
    "Kyle makes his way back to camp."

    scene maintentday with dissolve
    
    show ky happy at centerright
    voice "j29_HiCassie"
    ky "Hi Cassie! I have so much to tell y-"
    show ca angry 
    voice "j29_WhereHave"
    ca "Where have you been all day?"
    "Walking into the main tent, he was welcomed by a very angry Cassie."
    play music audio.sad
    show ky shaken with dissolve
    voice "j29_AreYou"
    ca "Are you for real? Did you forget how dangerous it is to leave camp right now?"
    show ca sad
    voice "j29_TheresNon"
    ca "There's non-shaped-friend…no. I mean, the non-dog-friend-"
    show ky smile
    voice "j29_TheNon"
    ky "The non-friendly, non-friend-shaped doggos?"
    show ca angry with None
    voice "j29_YeahThose"
    ca "Yeah, those! Did you wake up today and forget that they exist and would not-so-lovingly tear you to shreds?"
    show ky sad
    voice "j29_IKnowImSorry"
    ky "I know, I'm sorry…"
    stop music fadeout 4.0
    show ca sad with dissolve

    if not j26_fight:
        voice "j29_ImJust"
        ca "I'm just… I'm glad that you're back. But please never do that again."
    else:
        voice "j29_ItsMy"
        ca "It's my fault, too. I did ask you to do something. It was foolish of me to think that you wouldn't…actually do something."

    voice "j29_IIWas"
    ca "I-I was so, so worried that something had happened to you."
    show ky confused with dissolve
    voice "j29_KylieVNVR"
    ky "..."
    play music audio.light fadein 2.5
    show cg kylssie
    voice "j29_IDidnt"
    ky "I didn't know you cared so much about me."
    voice "j29_WhatDo"
    ca "What do you think?"
    voice "j29_IThink"
    ky "I think you're cute."
    voice "j29_ImIm"
    ca "I'm…{w=0.4}I'm gonna help you charge your Walkie. It must be dead, since you never picked up."
    voice "j29_ThankYou"
    ky "Thank you, Cassie!"
    voice "j29_YoureSo"
    ca "You're so silly, you know that?"
    voice "j29_IfThat"
    ky "If that means that I can put a smile on your face…"
    voice "j29_YeahYou"
    ca "Yeah…{w=1.0}you do, Kyle."
    scene black with dissolve
    "Cassie flees the scene with flushed cheeks."
    hide cg kylssie
    scene black with dissolve
    voice "j29_AwwYes"
    ky "...awww yes! Good job, me!"
    stop music fadeout 3.0
    stop ambience fadeout 2.0

label jan_30:
    scene black
    play ambience amb_campday
    $ current_day = _("January 30th")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    scene camp3day with longfade
    if davos_safe:
        "Today was a day off for me." 
        "I wish something exciting would happen."
        "Huh...? The flap to the quarantine tent's opening up-"
        play music audio.light
        "I see Davos is awake."

        if pearl_safe:
            show ky smile at left
            show pe smile at right
            with dissolve
            "Davos is…sneaking up behind the unsuspecting Kyle and Pearl."
            "He notices me and puts a finger to his lips." 
            "Oh, that'll be funny."
            show da neutral behind ky
            voice "j30_TalkingBehind"
            da "Talking behind my back?"
            show ky shaken with None
            show pe scared with None
            "Both of his targets jolt in response."
            voice "j30_AckWhat"
            pe "Ack! What-"
            show ky happy with dissolve
            voice "j30_DavosYourePearl"
            ky "Davos! You're awake!"
            show da happy behind pe
            voice "j30_CampMustve"
            da "Camp must've been super boring without me, huh, Pearl?"
            show pe confused
            voice "j30_NuhUh"
            pe "Nuh-uh. I kept busy and…didn't even check on you."
            voice "j30_WellI"
            da "Well, I might've been half asleep, but I could've sworn I heard someone - 'Please wake up, I can't roast marshmallows on my own without burning them.'"
            show pe neutral
            voice "j30_ThatsNot"
            pe "That's not what I said!"
            show ky smile
            show pe smile
            with dissolve
            voice "j30_OhPearl"
            ky "Oh, Pearl was definitely worried."
        else:
            show da happy at centerleft
            voice "j30_HeySleepyhead"
            mo "Hey, sleepyhead. Nice to see you up and about."
            voice "j30_ThanksMor"
            da "Thanks, Mor-"
            "Davos is interrupted by Kyle sprinting towards him."
            # IDEALLY, have Kyle enter from right; Jett's not doing the move right now to save time
            show ky happy at centerright
            voice "j30_DavosIm"
            ky "Davos! I'm so glad you're okay! Everyone was so worried about you… Even Gregory seemed really out of it."
            voice "j30_WellGood"
            da "Well, good to know I'm appreciated. Where's my pops?"
        #After Pearl conditionals, follow Aston

        #If Aston okay
        if aston_safe:
            hide ky
            hide pe
            with dissolve
            show ast at left with dissolve
            "Aston joins him outside the tent and squints slightly toward the forest."
            voice "j30_ItLooks"
            ast "It looks like the person who worried the most about you is about to be home."
            "He points over to Wilbur traveling alongside Gregory a little distance away from camp, walking back after a long day of sample collecting."
        else:
            hide pe with dissolve
            show ky smile
            voice "j30_OhYeah"
            ky "Oh, yeah! I think it's almost time for them to- Oh, they're here!"
            scene forest3 with fade
            show gr neutral at centerleft
            show wi neutral at centerright
            with dissolve
            "He points over to Wilbur and Gregory a little ways off from camp, walking back after a long day of sample collecting."

        voice "j30_Pops"
        da "Pops!"
        show cg davoshug #moved up here for MAXIMUM DAMAGE
        "Wilbur's eyes widen at the sight of his beloved son."
        "He drops his bags and runs straight towards Davos, arms outstretched inviting a hug."
        voice "j30_DavosYoureWilbur"
        wi "Davos… You're awake."
        voice "j30_ImSorryItTook"
        da "I'm sorry it took a while…"
        
        "Wilbur bear hugs Davos and even lifts him off the floor just a little."
        voice "j30_BetterLate"
        wi "Better late than never, my boy… I never doubted that you'd be alright in the end. Strong and gentle, just like your mother."
        voice "j30_IGot"
        da "I got my strength from you, so… Like father, like son?"
        voice "j30_LikeFather"
        wi "Like father, like son."
        scene black with longfade
        hide cg davoshug


        #COLIN (Davos recovered)
        #(Everyone okay)
        scene morganstent with longfade
        show satphone
        voice "j30_br1_PancakeI"
        mo "Pancake, I have some good news!"
        #voice "j30_br1_OhWhats"
        if radio_static == "_s":
            voice "j30_br1_OhWhats_s"
        else:
            voice "j30_br1_OhWhats_c"
        co "Oh, what's up?"
        voice "j30_br1_DavosWoke"
        mo "Davos woke up this morning…and it would seem that he's fully recovered."
        #voice "j30_br1_WilbursKid"
        if radio_static == "_s":
            voice "j30_br1_WilbursKid_s"
        else:
            voice "j30_br1_WilbursKid_c"
        co "Wilbur's kid? The one that was in deep sleep for weeks? That's amazing!"
        voice "j30_br1_HeReally"
        mo "He really had me worried there."
        voice "j30_br1_IKnew"
        mo "I knew he and Jax got it at about the same time I did. But neither Jax or I had such severe symptoms…"
        #voice "j30_br1_SoYoure"
        if radio_static == "_s":
            voice "j30_br1_SoYoure_s"
        else:
            voice "j30_br1_SoYoure_c"
        co "So you're saying that y'all potentially got it from the same source?"
        #voice "j30_br1_IfI"
        if radio_static == "_s":
            voice "j30_br1_IfI_s"
        else:
            voice "j30_br1_IfI_c"
        co "If I were to take a guess, I'd pin the body on the 31st as the source. All three of you were there."
        voice "j30_br1_ItStill"
        mo "It still doesn't explain why the symptoms were different…unless that's a key characteristic of said sickness."
        #voice "j30_br1_WhatAboutEllyThe"
        if radio_static == "_s":
            voice "j30_br1_WhatAboutEllyThe_s"
        else:
            voice "j30_br1_WhatAboutEllyThe_c"
        co "What about Elly? The fake one, I mean."
        voice "j30_br1_HesBeen"
        mo "He's been rattling around in my head for over two weeks… Feels worse than a migraine."
        #voice "j30_br1_IHear"
        if radio_static == "_s":
            voice "j30_br1_IHear_s"
        else:
            voice "j30_br1_IHear_c"
        co "I hear you, Morg. What about the others? How have they dealt with their symptoms?"
        "I think for a moment about Lorenzo and the bear with Aston's voice."
        voice "j30_br1_TheyveJust"
        mo "They've...just learned to deal with them. I think I've just...not acclimated, still."
        #voice "j30_br1_ALots"
        if radio_static == "_s":
            voice "j30_br1_ALots_s"
        else:
            voice "j30_br1_ALots_c"
        co "A lot's happened recently. Don't beat yourself up, soldier."
        #voice "j30_br1_AndI"
        if radio_static == "_s":
            voice "j30_br1_AndI_s"
        else:
            voice "j30_br1_AndI_c"
        co "And I know this goes without saying, but you don't need to be a hero. If it's too much, we have options."
        voice "j30_br1_IGet"
        mo "I get that. Thanks, Pancake."
        #voice "j30_br1_YoureWelcome"
        if radio_static == "_s":
            voice "j30_br1_YoureWelcome_s"
        else:
            voice "j30_br1_YoureWelcome_c"
        co "You're welcome, Morg."
        stop music fadeout 3.0
        stop ambience fadeout 2.0
        scene black with longfade

    else: #"Goodbye Davos HELLO DEATH" - Kylie
        show ja inthought at left
        show wi worried at centerright
        with dissolve
        voice "j30_WhatDo"
        wi "What do you mean…?"
        voice "j30_DavosFell"
        ja "Davos fell asleep and never woke up, Wilbur."

        play music audio.sad
        if pearl_safe:
            scene camp3day with dissolve
            show pe scared with dissolve
            "Pearl runs out of the tent upon hearing about Davos' status."
            voice "j30_PearlVNVR"
            pe "..."
            "She looks at us for confirmation, confused."
            show pe depressed
            voice "j30_DavosI"
            pe "D-Davos… I… What is this…?"
            hide pe
            "She chokes on her words…and then runs back into the tent."
            show ky neutral at left
            voice "j30_IllGo"
            ky "I'll go keep her company."
            "Kyle stands up and leaves to go check in on Pearl."
            hide ky
            "..."
            "She's… {w=0.8}I've never heard Pearl like that…"
            scene camp3day with dissolve
            show ja inthought at left
            show wi worried at centerright
            with dissolve

        show lo scared with dissolve
        voice "j30_ImSorryWilburOvernight"
        lo "I'm sorry, Wilbur… Overnight, his temperature started dropping and we couldn't-"
        stop music fadeout 12.0
        play sound sleeve
        "Wilbur places a hand on Lorenzo's shoulder, but says nothing else."
        hide wi with dissolve
        hide lo with dissolve
        "He walks into the tent by himself."
        show ja serious
        voice "j30_LetsAll"
        ja "Let's all give him some time."
        stop ambience fadeout 2.0
        scene black with longfade

        # Wilbur solo
        "Wilbur hesitantly enters the tent."
        "Nothing could've ever prepared him for the sight awaiting him within."
        play music audio.oof
        show cg byedavos
        "Seeing Davos lying there, silent and still, makes him…{w=0.8}almost unrecognizable."
        "Where were his usual greetings? Where was the bright smile that so often accompanied the sight of his father?"
        "Where has all the light gone in this frail, unmoving body?"
        voice "j30_Davos"
        wi "Davos…"
        "Sitting down next to him, Wilbur brushes the stray strands of hair away from his son's face."
        "His expression shows no trace of suffering - no trace of pain."
        "Wilbur carefully turns Davos to his side."
        "Now…{w=0.6}he truly looks like he's asleep… Just like any other night."
        voice "j30_YouSleep"
        wi "You sleep so soundly, my boy… {w=1.0}Because you know that you are loved."
        play sound WilburCry
        "Wilbur rests a hand gently on the blanket, running his other hand through Davos' hair."
        "His tears fall freely, their impact silenced by Davos' blanket."
        voice "j30_EnyaHes"
        wi "Enya… {w=1.3}He's all yours."
        scene black with longfade
        "No one can ever escape death's grasp forever… {w=1.3}This, Wilbur knows all too well."
        "He just wishes that he had more time."
        "More time with the last of his kin."
        scene black with dissolve
        hide cg byedavos
        "Wilbur never left the tent that day."
        stop music fadeout 3.0

        # Colin
        play music audio.sad
        scene morganstent with longfade
        show satphone
        voice "j30_br2_DoYou"
        mo "Do you have a sec, Pancake?"
        #voice "j30_br2_AreYou"
        if radio_static == "_s":
            voice "j30_br2_AreYou_s"
        else:
            voice "j30_br2_AreYou_c"
        co "Are you alright, Morg? What happened?"
        voice "j30_br2_HeDavos"
        mo "He… Davos didn't make it. And it's not just him that we've lost."
        voice "j30_br2_IKnowImSupposed"
        mo "I know I'm supposed to be stronger than this, but... With the way people are dying, I don't know how long I can keep this up."
        #voice "j30_br2_WhatAboutEllyThe"
        if radio_static == "_s":
            voice "j30_br2_WhatAboutEllyThe_s"
        else:
            voice "j30_br2_WhatAboutEllyThe_c"
        co "What about Elly? The fake one, I mean."
        voice "j30_br2_WhatAbout"
        mo "What about him? He's been rattling around in my head for over two weeks. I'm tired of it."
        voice "j30_br2_IKnowItsNot"
        mo "I know it's not him...not really...but it's not making this any easier."
        #voice "j30_br2_IHear"
        if radio_static == "_s":
            voice "j30_br2_IHear_s"
        else:
            voice "j30_br2_IHear_c"
        co "I hear you, Morg. What about the others? How have they dealt with their symptoms?"
        "I think for a moment about Lorenzo, still being tormented by the bear with Aston's voice."
        voice "j30_br2_TheyveJust"
        mo "They've...just learned to deal with them, even as they worsen. I think I've just...not acclimated, still."
        #voice "j30_br2_ALots"
        if radio_static == "_s":
            voice "j30_br2_ALots_s"
        else:
            voice "j30_br2_ALots_c"
        co "A lot's happened recently. Don't beat yourself up, soldier."
        #voice "j30_br2_SoHowre"
        if radio_static == "_s":
            voice "j30_br2_SoHowre_s"
        else:
            voice "j30_br2_SoHowre_c"
        co "So... How're you feeling in terms of mission status? Do you need us to prep an extraction?"
        voice "j30_br2_NoNot"
        mo "No. {w=0.4}Not yet. {w=0.6}If nothing else, I need to get a better read on Hilda's status. If we can get to her through Gregory..."
        #voice "j30_br2_AndI"
        if radio_static == "_s":
            voice "j30_br2_AndI_s"
        else:
            voice "j30_br2_AndI_c"
        co "And I know this goes without saying, but you don't need to be a hero. If it's too much, we have options."
        voice "j30_br2_IGet"
        mo "I get that. Thanks, Col- Pancake."
        #voice "j30_br2_YoureWelcome"
        if radio_static == "_s":
            voice "j30_br2_YoureWelcome_s"
        else:
            voice "j30_br2_YoureWelcome_c"
        co "You're welcome, Morg."
        stop music fadeout 3.0
        stop ambience fadeout 2.0
        scene black with longfade

label jan_31:
    $ current_day = _("January 31st")
    $ save_name = current_date(_("Arc 3"), current_day)
    show screen date_label with dissolve
    with Pause(0.2)
    play ambience amb_snowmobile
    # Note that the voice "j31_br[x]_" naming convention only exists during this branched section; after that, it's "j31_" as expected
    if davos_safe:
        "Today is another sample delivery day, but it's just me today."
        "Gregory said he's going to stay back at camp to help Wilbur and the rest supervise Davos' recovery."
        "So it's just me and the lovely snowmobile."
        if pearl_safe:
            "Vroom-vroom...but in snow."
        else:
            "Vroom-vroom...but in snow. Pearl would be proud."
        stop ambience fadeout 3.0
        scene black with longfade
        scene rclobby with dissolve
        show ko happy
        "As I opened the front door to the RC, I was greeted by an excited Koda."
        play music audio.light
        voice "j31_br1_MorganI"
        ko "Morgan! I heard the good news!"
        voice "j31_br1_IsIt"
        ko "Is it true? Did Davos wake up? Is he okay now?"
        voice "j31_br1_YesYes"
        mo "Yes, yes, and yes, Koda. He's awake and in good spirits."
        "Davos wasn't kidding when he said Koda would bombard me with questions at first sight."
        "Anyway, since I'm here… I should go digging around at the lab."

    else:
        "Today is another sample delivery day…but it's just me today on the snowmobile."
        "Normally I'd be thrilled but…well, I can't right now."
        "Gregory said he's going to stay back at camp to watch Wilbur."
        "He hasn't eaten anything since yesterday."
        if pearl_safe:
            "And Pearl… She's not having a great time either, grieving the loss of her best friend."
        "And along with sample delivery… I have to go and break the news to Koda in person."
        stop ambience fadeout 3.0
        scene black with longfade
        scene rclobby with dissolve
        show ko sad
        "As I opened the front door to the RC, I was greeted by an anxious Koda."
        play music audio.sad
        voice "j31_br2_MorganI"
        ko "Morgan. I need you to answer truthfully."
        show ko neutral
        voice "j31_br2_PleaseTell"
        ko "Please tell me what happened at the camp..."

        # voice "j31_br2_HeDidnt"
        # mo "He…didn't make it. I'm sorry, Koda."
        scene black with fade
        "I gave Koda a rundown on the events that happened the day before."
        "Koda hangs their head down, letting the news of Davos' passing sink in."

        voice "j31_br2_KodaVNVR"
        ko "..."
        scene rclobby with dissolve
        show ko sad
        voice "j31_br2_ThankYou"
        ko "Thank you for your honesty, Morgan."
        if not pearl_safe:
            "Pearl and now Davos… {w=0.5}I can't begin to imagine how they're feeling right now."
        "..."
        "As much as I would've loved to grieve alongside Koda, I have some digging to do."
        "The faster I get to the bottom of this, the faster I find answers to Davos' death."

    scene rclobby with dissolve
    "I look around the RC, but I see no sign of Isaak."
    "If he isn't here…then that would be a great opportunity to sneak around in his lab."
    voice "j31_IsIsaak"
    mo "Is Isaak not here, Koda?"
    show ko neutral
    voice "j31_NoI"
    ko "No… I think he went out for a walk."
    if davos_safe: #just for music transition
        stop music fadeout 2.0
    
    "Koda pauses for a moment, exhaling shakily." #Confirmed to happen as normal in both branches :')
   
    if davos_safe:
        play music audio.sad
    show ko sad
    voice "j31_MorganI" # Not a duplicate name
    ko "M-Morgan, I have to tell you something, but you absolutely have to keep it a secret from Isaak."
    voice "j31_DidYou"
    mo "Did you find unflattering pictures of him?"
    show ko happy
    voice "j31_IWish"
    ko "I wish-{w=0.7} I mean, no. It's something else."
    voice "j31_ItWas"
    ko "It was about a month ago. Isaak had a phone call with someone."
    show ko neutral
    voice "j31_ThePerson"
    ko "The person on the phone…she was blowing up on him. Saying that there's blood…on his hands?"
    show ko sad
    voice "j31_TheMore"
    ko "The more I think about it, the more I get the sense that something's…not right."
    voice "j31_ThanksFor"
    mo "Thanks for letting me know, Koda. Keep me updated if anything changes?"
    show ko neutral
    voice "j31_YeahIll"
    ko "Y-Yeah. I'll do my best."
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    scene black with longfade

    #Eva beat
    "I wait until they turn to leave before letting myself into Isaak's lab."
    "But upon opening the door to the lab… I see Eva sneaking around in there herself."
    scene isaaklab2 with dissolve
    play ambience amb_rc fadein 1.0
    voice "j31_EvaDo"
    mo "Eva? What do you have there?"
    show ev smile at centerleft
    "Eva tries to hide something small behind her back. Was that a loaded syringe?"
    voice "j31_Hi"
    ev "...{w=0.3} Hi?"
    voice "j31_IsaakWould"
    mo "Isaak would be thrilled to know that you're going through his things."
    show ev inthought
    voice "j31_YesHe"
    ev "Yes, he would…but here, come take a look at this."
    play music audio.neutral
    stop ambience fadeout 3.0
    play sound bandage1 #placeholder-ish? Works OK
    "She pulls the drawer open."
    "Inside is a neatly packed box of tranquilizers."
    voice "j31_IDont"
    ev "I don't recall Heralign ever providing these."
    show ev neutral
    voice "j31_MaybeUpon"
    ev "Maybe upon request? I'd need to cross-check that with Matt…"
    voice "j31_IWouldnt"
    mo "I wouldn't be surprised. Making requests without telling anyone sounds like Isaak."
    show ev serious
    voice "j31_IOnce"
    ev "I once walked into him using one of these on a…{w=0.5}bird."
    voice "j31_ImNot"
    ev "I'm not entirely sure what he's doing with them or where they're being sourced from, but…let's just say I don't feel inclined to check the ice box or follow him on his walks."
    "Animal experimentation, huh?"
    voice "j31_HasHe"
    mo "Has he moved on to anything bigger than birds?"
    show ev worried
    voice "j31_IfYoure"
    ev "If you're talking about the ugly-looking wolves you had the pleasure of meeting, no. At least, not yet…hopefully, I'll never have to see them."
    "I glance down at the box again."
    "Tranquilizers… These might be useful down the line."
    "I suppose it wouldn't hurt to ask."
    voice "j31_CanI"
    mo "Can I have a few?"
    show ev neutral
    voice "j31_AndWhy"
    ev "And why should I even give you these?"
    voice "j31_WellI"
    mo "Well, I know people say that you shouldn't feed the wildlife, but…I think these stray dogs are an exception. Pretty please, Eva?"
    show ev inthought
    voice "j31_StealingIs"
    ev "Stealing is bad, but it's not as bad if I'm not the only one doing it."
    show ev happy
    voice "j31_TakeEm"
    ev "Take 'em. You'll get more use out of them than me."

    play sound flashlight
    scene isaaklab2 with dissolve #auto-hides Eva, gives a little time for sound to play before popup
    "Nice. I have three on me now… These definitely feel like they'll come in handy."
    "I look at the ice box in the corner of the room."
    "... {w=1.0}I should open it."
    "Eva shoots me a glare."
    "Yeah, that's a clear 'Don't do it. I see you looking at it.'"
    "If this was what caused Lorenzo's nightmares…{w=0.7}it'll probably be a good idea to gear up."


    stop music fadeout 3.0
    stop ambience fadeout 3.0
    scene black with longfade

label demo_end:
    show cg kylssie_cutebonus
    "Thank you for playing the Winter Jam Edition of 'Undergrowth' (Demo)!"
    "We have a lot in the works and are working towards the full release!"
    "Please stay tuned for updates on the game! And, with that..."
    "{size=+8}Happy 2025!\n{size=-8}-The 'Undergrowth' Dev Team"


























    









