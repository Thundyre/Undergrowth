label nov_28:
    $ current_day = _("November 28th")
    $ save_name = current_date(_("Arc 1"), current_day)
    scene isaaklab2 with dissolve
    play ambience amb_rc fadein 3.0
    show screen date_label with dissolve
    show isa inthought at centerright with dissolve
    "In the RC, Isaak is seen handling samples."
    "The same ones Gregory had delivered a while ago."

    play music audio.sad
    voice "n28_HasIt"
    isa "... Has it begun already? At this time of year?"
    "He continues muttering to himself as he annotates each bag."
    "Relabelling each one as 'wet dirt.'"
    show isa neutral with move:
        xpos 650
    voice "n28_TheyMust"
    isa "They must already know."
    "He pauses for a moment, staring at the wall…before resuming his tasks."

    "Unbeknownst to him, Eva peeks in from the outside, watching as he tosses bag after bag of dirt onto the table." 
    voice "n28_Isaak"
    ev "Isaak?"
    show isa serious
    voice "n28_What"
    isa "What?"
    "Isaak follows Eva's gaze to the dirt samples on the table."
    voice "n28_WellIf"
    isa "Well… {w=2.5}If you want one, take one. The rest will be kept at the usual shelf, should you need more."
    voice "n28_GreatThank"
    ev "Great. Thank you, Isaak…"
    voice "n28_I"
    ev "I-"
    hide isa
    "Isaak turns away, not realizing Eva is calling out to him."

    "She decides to save the question for another time and leaves \nthe room."
    scene black with fade
    stop music fadeout 4.0
    voice "n28_GuessI"
    isa "Guess I don't have to do it myself..."
    voice "n28_Perfect"
    isa "Perfect time for a stroll."
    play sound cloth
    "Isaak swaps his lab coat out for another coat, one that is much more fitting for the weather."
    scene black
    stop ambience fadeout 4.0
    with Pause(1.0)

    #scene rclobby with dissolve # This can eventually be swapped with Eva's station, but it's like this for now in case we don't have coverage
    scene evalab with dissolve
    show ko neutral at centerright
    play music audio.neutral
    voice "n28_NoQuestions"
    ko "No questions? No classic Isaak 'ughh's?"
    show ko happy
    voice "n28_ThatWas"
    ko "That was relatively easy. Easier than if I attempted what you did."
    voice "n28_CarefulNow"
    ev "Careful now, Koda. The door's still open."
    show ko scared with sdissolve
    voice "n28_OOhYeah"
    ko "O-Oh yeah."
    hide ko
    play sound labdoor
    "Koda closes the lab door behind Eva."
    voice "n28_HeWont"
    ev "He won't bite if I'm here."
    show ko neutral at centerright
    voice "n28_WhatWas"
    ko "What was he doing, anyway?"
    voice "n28_JustIsaak"
    ev "Just Isaak things… Muttering to himself while he works."
    "Koda signals Eva to toss the bag to them."
    play sound dirtbag
    voice "n28_WantedTo"
    ev "Wanted to ask why he'd be interested in these, but I guess finding out ourselves will also get us answers."
    voice "n28_AndThe"
    ko "And the best case scenario is…?"
    voice "n28_LakeWater"
    ev "Lake water. Not the best scenario, but the most logical explanation right now."
    play sound gloves
    "With one snap of her rubber gloves, Eva is now all geared up."
    voice "n28_WellThen"
    ev "Well then… Shall we begin?"
    voice "n28_ReadyWhen"
    ko "Ready when you are!"

    scene black with fade
    "And thus, they began their little experiments, fully utilizing the bag of dirt from Isaak."
    "Comparing their findings with the records of lake water samples."
    "It's a match, but not fully…"

    voice "n28_ThisIs"
    ko "This is new… Eva, come take a look at this. There's something odd."
    stop music fadeout 8.0
    voice "n28_ItsStructured"
    ev "It's structured like fungi?"
    "She moves away from the microscope and rereads the labels."
    "'Lake Water - 11/27'"
    stop ambience fadeout 2.0
    voice "n28_GuessWed"
    ev "Guess we'd need a few more days to figure out what this is…"
    scene black
    with Pause(2.5)
    jump nov_29

label nov_29:
    with Pause(0.5)
    play ambience amb_campday fadein 0.5
    $ current_day = _("November 29th")
    $ save_name = current_date(_("Arc 1"), current_day)
    show screen date_label with dissolve
    voice "n29_Ughhh"
    ca "Ughhh…"
    voice "n29_GeezIts"
    ca "Geez, it's morning already?"
    "Cassie cracks open her tent and takes a peek outside."
    scene camp2day with dissolve
    "The sun rays peek back through the tree branches. It's morning alright."
    "No one's awake yet, though."
    voice "n29_OnDays"
    ca "On days like these… I wish I could have a cup of warm milk…"
    voice "n29_ThatUsually"
    ca "That usually helps."
    scene maintentday with dissolve
    "With groggy footsteps, she makes it to the main tent."
    "She scans the food shelf, but is indecisive on what to eat."
    voice "n29_ICould"
    ca "I could just wait around for them while I… {w=3.8}What was it that I wanted to do today…?"
    "Unable to remember what her tasks were for the day, she reaches for her notepad and flips through it." 
    "However, there wasn't anything specific penned in for the day."
    "Cassie rubs her temples and tries her best to recall."
    play sound cloth
    stop ambience fadeout 1.0
    play music audio.light
    show ru happy at left
    voice "n29_OhCassie"
    ru "Oh, Cassie, good morning!"
    "Ruran walks into the main tent, surprised to see her already up."
    voice "n29_GoodMorning"
    ca "Good morning, Ruran."
    "Ruran picks up on her energy levels immediately."
    show ru worried
    voice "n29_IsSomething"
    ru "Is something wrong, dear?"
    voice "n29_II"
    ca "I… I can't sleep? I shut my eyelids and it doesn't do the whole \n'sleep thing.'"
    show ru with MoveTransition(0.8):
        xpos 300
    "Ruran rushes to her side to feel her forehead."
    show ru neutral
    voice "n29_TemperatureSeems"
    ru "Temperature seems normal enough."
    voice "n29_AnyOther"
    ru "Any other issues…? Has your appetite changed?"
    voice "n29_NoIm"
    ca "No, I'm just… I'm so tired."

    show ru happy
    voice "n29_SureIts"
    ru "Sure it's not someone keeping you awake?"
    voice "n29_IDontKnowWho"
    ca "I don't know who you're talking about."
    show ja happy at centerright
    voice "n29_SureYou"
    ja "Sure you do."
    "Cassie shoots a sleepy glare at Jax."
    voice "n29_IDontWantTo"
    ca "I don't want to hear that from you first thing in the morning, Jax."
    show ja confused
    voice "n29_ReallyThough"
    ja "Really, though… Are you alright, Cassie?"
    "He hands a water bottle to her."
    voice "n29_NoAnd"
    ca "No…and I'm sure the bags under my eyes look awful."
    "She buries her face in her hands."
    show ru happy
    voice "n29_PandasAre"
    ru "Pandas are cute."
    voice "n29_ImSureA"
    show ja neutral
    ja "I'm sure a certain someone would love to snap a photo of them."
    voice "n29_DoI"
    ca "Do I look like a bear to you?"
    voice "n29_MaybeWhen"
    ja "Maybe when you're angry."
    voice "n29_IfYou"
    ca "If you weren't a friend, I'd wear a bear costume to scare ya!"
    show ja happy
    voice "n29_IDontThinkThatll"
    ja "I don't think that'll do much."
    voice "n29_CassieVNVR"
    ca "..."

    show ru neutral
    voice "n29_IllLet"
    ru "I'll let Wilbur know that you're resting for the day."
    voice "n29_But"
    ca "But-"
    voice "n29_NoButs"
    ru "No buts! Into the tent you go."
    voice "n29_IWas"
    ca "I was sure I had something important to do today…"
    show ru happy
    voice "n29_ImSureItll"
    ru "I'm sure it'll resurface when the time comes."
    show ja neutral
    voice "n29_GoOn"
    ja "Go on, Cassie. I'll bring you breakfast in a bit."
    voice "n29_JustYell"
    ja "Just yell if you need anything."

    "She flashes them a meek smile before retreating to her tent."
    scene black with fade
    "Lying down on her sleeping bag, she stares at the tent's fabric walls…"
    "Hoping to at least catch a wink of sleep."
    
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    scene black
    with Pause(1.2)
    jump nov_30

label dec_1:
    scene village2 with dissolve # Village; either no Susie, no kids OR Susie but no kids
    $ current_day = _("December 1st")
    $ save_name = current_date(_("Arc 1"), current_day)
    play ambience amb_village fadein 1.4
    show screen date_label with dissolve
    "Back at the farm, two villagers look towards their cattle with worried expressions."
    voice "d1_TheyveBeen"
    so "They've been starting to act up, dear."
    voice "d1_ThisEarly"
    fe "This early? Thought we still had a month…"
    voice "d1_ImSureHeAlready"
    fe "I'm sure he already knows, then… It's about time for his stupid medicine to work."
    voice "d1_YoureAlways"
    so "You're always so hard on him."
    voice "d1_TheLonger"
    fe "The longer we wait, the more of 'em we're going to lose."
    voice "d1_SweetOl"
    fe "Sweet ol' Susie… Even she's feeling it."
    scene village2 #slightly scuffed workaround to make the pause not look WONK

    with Pause(1.0)
    play sound snowrun
    "A child is seen running towards the man, package in hand." # Flipped this from after "We've got mail"
    voice "d1_FatherWeve"
    v2 "Father! We've got mail!"
    
    voice "d1_GiveIt"
    fe "Give it here."
    play sound bandage1
    stop ambience fadeout 2.0
    "He hastily rips open the box. Within it is an unlit stick of dynamite and an unopened letter."
    play music audio.anxious
    voice "d1_IsHe"
    fe "Is he out of his mind?"
    voice "d1_ImSureTheresAn"
    so "I'm sure there's an explanation for this…"
    "He moves on to the letter and reads aloud."
    voice "d1_DearUncle"
    fe "'Dear Uncle,'"
    voice "d1_HappyDecember"
    fe "'Happy December. The time has come.'"
    voice "d1_HereAre"
    fe "'Here are your Christmas fireworks.' {w=1.6}...{w=1.6} 'Have fun with them.'"
    voice "d1_LightIt"
    fe "'Light it up when you're at the highest point so that everyone can...enjoy them together.'"
    voice "d1_BlindThe"
    fe "{w=0.4}'Blind the metal bird.' {w=2.6}…blind the metal bird?"
    voice "d1_AgainWith"
    fe "Again with these damn riddles…"
    voice "d1_WoahFather"
    v2 "Woah. Father… Can I help?"
    voice "d1_IDont"
    fe "I don't think these are for you."
    voice "d1_ButIll"
    fe "But I'll get something your size for you to handle, okay?"
    voice "d1_Okay"
    v2 "Okay…"
    voice "d1_MetalBird"
    so "Metal bird… Does he want you to do it earlier than planned?"
    voice "d1_FiveDays"
    fe "Five days after receiving the letter, whenever that is… I'd assume so."
    voice "d1_ThisBetter"
    fe "This better be worth it."
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    scene black with dissolve
    pause(0.6)
    if days404testing:
        $ aston_safe = False
        jump dec_19
    else:
        jump dec_2

label dec_19:
    $ current_day = _("December 19th")
    $ save_name = current_date(_("Arc 2"), current_day)
    show screen date_label with dissolve
    scene maintentday with dissolve
    play music audio.neutral
    if not aston_safe:
        show da scared at center
        show ja pissed at left
        show wi neutral at right 
        voice "d19_br2_What"
        da "What…"
        voice "d19_br2_IsHe"
        ja "Is he serious?"
        show da sad with dissolve
        show ja with move:
            xpos 110
        voice "d19_br2_HonestlyYou"
        ja "Honestly, you know what… Fuck Heralign."
        voice "d19_br2_ThisIs"
        ja "This is a life or death situation we're talking about."
        voice "d19_br2_IKnow"
        wi "I know, Jax. This doesn't sit right with me either."
        show wi inthought
        voice "d19_br2_GregoryWhat"
        wi "Gregory… What is he thinking?"
        voice "d19_br2_AreWe"
        da "Are we…actually gonna stop searching?"
        show ja inthought
        "Their attention momentarily shifts towards Ruran."
        "She has been restlessly pacing around the tent ever since the news dropped."
        "Everyone in C2 now has orders to discontinue the search for missing people."
        show da depressed
        voice "d19_br2_Ruran"
        da "Ruran…"
        show ru scared at centerright
        voice "d19_br2_ICant"
        ru "I can't believe this is happening."
        voice "d19_br2_WhatIf"
        ru "What if they're out there in the cold waiting on us?"
        show ru angry
        voice "d19_br2_HowAre"
        ru "How are we supposed to continue on like nothing's happened?"
        voice "d19_br2_WilburI"
        ru "Wilbur, I-"
        show wi neutral with move:
            xpos 1750
        "He places his hands on her shoulders."
        voice "d19_br2_WeAre"
        wi "We're not going to stand idly by."
        hide wi neutral
        show wi serious at right
        show ru worried
        "He turns towards Davos and Jax, nodding with resolve."
        "And with that, he makes a decision."
        voice "d19_br2_DivideAnd"
        wi "Divide and conquer, my boys. Half of us on research, half of us on the search."
        show ja serious
        voice "d19_br2_YouCan"
        ja "You can count on us."
        show da sad
        voice "d19_br2_RuranYoure"
        da "Ruran… You're not alone in this, okay?"
        voice "d19_br2_WeWill"
        wi "We will make it happen... We must."


    else: # Aston is OK!
        show da scared at center
        show ja serious at left
        show wi neutral at right
        voice "d19_br1_What"
        da "What…"
        voice "d19_br1_IsHe"
        ja "Is he serious?"
        voice "d19_br1_AndWhat"
        ja "And what about Heralign, huh? Is she just gonna sit in her dainty little office?"
        show ja pissed at left
        show da sad
        with dissolve
        voice "d19_br1_ThisIs"
        ja "This is a life or death situation we're talking about."
        voice "d19_br1_IKnow"
        wi "I know, Jax. This doesn't sit right with me either."
        show wi inthought
        voice "d19_br1_GregoryWhat"
        wi "Gregory… What is he thinking?"
        voice "d19_br1_AreWe"
        da "Are we…actually gonna stop searching?"
        show ja inthought
        "Their attention momentarily shifts towards Ruran."
        "She has been restlessly pacing around the tent ever since the news dropped."
        "Everyone in C2 now has orders to discontinue the search for missing people."
        show da neutral
        voice "d19_br1_Ruran"
        da "Ruran…"
        show ru worried at centerright
        voice "d19_br1_ICant"
        ru "I can't believe this is happening."
        voice "d19_br1_WhatIf"
        ru "What if Lorenzo is out there in the cold, waiting on us?"
        show ru angry
        voice "d19_br1_HowIs"
        ru "How is Aston supposed to take this? How are we supposed to continue on like nothing’s happened?"
        show ru worried
        voice "d19_br1_WilburI"
        ru "Wilbur, I-"
        show wi neutral with move:
            xpos 1750
        "He places his hands on her shoulders."
        voice "d19_br1_WeAre"
        wi "We're not going to stand idly by."
        hide wi neutral
        show wi serious at right
        show ru worried
        "He turns towards Davos and Jax, nodding with resolve." 
        "And with that, he makes a decision."
        voice "d19_br1_DivideAnd"
        wi "Divide and conquer, my boys. Half of us on research, half of us on the search."
        show ja neutral
        voice "d19_br1_YouCan"
        ja "You can count on us."
        show da happy
        voice "d19_br1_ThatSounds"
        da "That sounds like a plan!"
        show wi neutral
        voice "d19_br1_WeWill"
        wi "We will make it happen… Trust me."
        show ru neutral
        voice "d19_br1_ThankYou"
        ru "Thank you, Wilbur." 
    stop music fadeout 1.0
    scene black with dissolve
    if days404testing:
        jump dec_29
    else:
        jump dec_20

label dec_29:
    play music audio.light
    $ current_day = _("December 29th")
    $ save_name = current_date(_("Arc 2"), current_day)
    scene evalab with fade # Can be Eva's station or RC lobby?
    show screen date_label with dissolve

    show ev happy at centerleft
    voice "d29_MindGetting"
    ev "Mind getting some extra dishes for me, Koda? Think we ran out."
    voice "d29_ThereShould"
    ev "There should be some at Isaak's station."
    "Over at the RC, the research never stops. "

    if not pearl_safe:
        "Even if your friends have gone missing."
    
    voice "d29_OnIt"
    ko "On it."
    scene black with fade

    voice "d29_AlrightyPetri"
    ko "Alrighty! Petri dishes, here I come."
    "The walk to the opposite lab is a short one."

    scene black
    with Pause(1.0)
    stop music fadeout 8.0
    scene isaaklab2 with dissolve # Please do not sprite the Isaak
    "Koda cracks open the door to Isaak's lab, unintentionally walking in on a heated conversation through the phone."
    "They debated when to make their presence known to Isaak…but couldn't find a chance to."
    play music audio.sad
    #voice "d29_IsaakHave"
    if radio_static == "_s":
        voice "d29_IsaakHave_s"
    else:
        voice "d29_IsaakHave_c"
    who "Isaak, have you no remorse?"
    voice "d29_HadHe"
    isa "Had he followed the instructions, I'm sure he would've come home safely."
    #voice "d29_YoureAwful"
    if radio_static == "_s":
        voice "d29_YoureAwful_s"
    else:
        voice "d29_YoureAwful_c"
    who "You're awful."
    #voice "d29_HeWas"
    if radio_static == "_s":
        voice "d29_HeWas_s"
    else:
        voice "d29_HeWas_c"
    who "He was supposed to come home for Christmas."
    voice "d29_IKnow"
    isa "{w=2.5}I know."
    #voice "d29_IsThis"
    if radio_static == "_s":
        voice "d29_IsThis_s"
    else:
        voice "d29_IsThis_c"
    who "Is this what you call 'helping us?'"
    #voice "d29_WeBabysit"
    if radio_static == "_s":
        voice "d29_WeBabysit_s"
    else:
        voice "d29_WeBabysit_c"
    who "We babysit, we do your bidding, and it's just 'all in the name of science?'"
    #voice "d29_YouMade"
    if radio_static == "_s":
        voice "d29_YouMade_s"
    else:
        voice "d29_YouMade_c"
    who "You made it out, came back…and what did you bring? {w=0.7}Nothing."
    #voice "d29_YourFamily"
    if radio_static == "_s":
        voice "d29_YourFamily_s"
    else:
        voice "d29_YourFamily_c"
    who "Your family, your mother…"
    voice "d29_LeaveMy"
    isa "Leave my mother out of this."
    #voice "d29_YouYou"
    if radio_static == "_s":
        voice "d29_YouYou_s"
    else:
        voice "d29_YouYou_c"
    who "You… You have blood on your hands, you-"
    play sound phonesnatch
    "Incoherent noises could be heard from the other side of the call."
    "Another person seems to have taken hold of the phone."
    stop music fadeout 15.0
    #voice "d29_IsaakIm"
    if radio_static == "_s":
        voice "d29_IsaakIm_s"
    else:
        voice "d29_IsaakIm_c"
    who "Isaak, I'm... {w=1.7}Isaak, I'm sorry about that. I'll talk to her." 
    #voice "d29_LookWe"
    if radio_static == "_s":
        voice "d29_LookWe_s"
    else:
        voice "d29_LookWe_c"
    who "Look, we may not know exactly what it is you're doing, but there are some people that are still very proud of you."
    #voice "d29_WereStill"
    if radio_static == "_s":
        voice "d29_WereStill_s"
    else:
        voice "d29_WereStill_c"
    who "We're still family… Right?"
    voice "d29_ThatWould"
    isa "That would be ideal."
    "Eva's voice rings out from behind."
    voice "d29_KodaDid"
    ev "Koda? Did you find it?"
    "Isaak turns around surprised as he hurriedly hangs up on the phone."
    voice "d29_IsaakVNVR"
    isa "..."
    show isa inthought:
        ypos 50
        zoom 2.2
    voice "d29_YouHave"
    isa "You have two hands. Maybe you can use one of them to knock on the door next time?"
    show isa serious with None
    voice "d29_YYesSir"
    ko "Y-Yes sir! I'm just here to grab stuff and I'll be on my way!"
    scene black with dissolve
    "Koda rushes to the cabinet to take what they need…"
    "And then sprints out the door, nearly dropping the goods on the way out."

    stop music fadeout 3.0
    stop ambience fadeout 1.0
    scene black with longfade
    with Pause(1.0)
    jump dec_30