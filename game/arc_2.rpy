label dec_6_2:
    #Arc 2 start
    $ save_name = _("Arc 2")
    #Scene transition: Fade to black, then fade back in slowly
    scene bg maintent_night with longfade
    play ambience amb_intcampnight fadein 1.0
    "I don't know how long it has been."
    "The pounding pain in the back of my head radiates as I try to take in my surroundings."
    "This is... the main tent?"
    "There was an avalanche and I... I was trying to hide from the snow and..."
    show ast happy at centerleft

    show pearl smile at centerright
    ast "Morgan!"
    pe "He's awake!"

    "I'm relieved that Aston and Pearl are here... but where are the rest?"

    show ast neutral
    ast "You are okay, Morgan. We're in the main tent."
    pe "Or main tent 2.0."
    ast "You have a wound at the back of your head, perhaps caused by falling debris. You were an unlucky target."
    show ast inthought
    ast "And you've been out for about 5 hours now."
    mo "Where's Lorenzo... Kyle... and Gregory?"

    show pearl sad
    show ast sad
    
    "Pearl looks down... and Aston, he's looking up?"
    "That was not the reaction I'd hope to see."
    "I never thought I'd see him emotional, but it looks like Aston's on the verge of breaking down."

    show pearl neutral
    pe "Gregory... He's outside the tent. He's fine."
    show pearl sad
    pe "Kyle is also fine. He's sorting through our supplies and setting up our sleeping space for tonight."

    show pearl depressed
    pe "Lorenzo... We haven't found him."
    pe "We've tried beeping his Walkie, but we haven't received anything."
    show pearl neutral
    pe "That's how we found you! Yours beeped under the snow and we heard it."

    hide ast with sdissolve
    "Aston turns away from us."

    mo "Let's go find him."
    ast "You should rest Morgan, and... it's too dark outside to see right now."
    ast "We've already searched the area around us before sundown."

    show pearl sad
    "His voice is cracking. Pearl reaches out to hold his hand."

    mo "First thing at dawn then, Aston."
    mo "Lorenzo is strong, and I am positive that he'll be okay."

    show ast neutral at centerleft
    "Aston turns around and gives me a light nod."
    "We fall silent, looking at each other I can sense that we're all determined to find him."
    "The worry lingers, but I know we'll do the best we can."
    "He's a tough cookie. He'll survive this."
    stop ambience fadeout 3.0

label dec_7:
    scene bg forest3 with longfade
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


    wt_ja "How's the status of your camp? Heard you got knocked out, Morgan."
    wt_mo "Yep. It still hurts too."
    wt_mo "Pearl, Gregory and Kyle are at base, and Aston is here with us to find Lorenzo."
    $ chibi_davos = "images/chibi/davos_worried.png"
    wt_da "I promise we'll do our best, Aston. We'll find him."
    $ chibi_jax = "images/chibi/jax_neutral.png"
    wt_ja "On C2's side, Cassie sprained her ankle. Wilbur had a few scrapes."
    $ chibi_jax = "images/chibi/jax_worried.png"
    wt_ja "Ruran and I got pushed out pretty far from the rest. Took a while for us to locate where we were."
    wt_da "I was lucky enough to avoid most of the hits."

    "Aston has been trying to reach Lorenzo through his Walkie."

    wt_ja "Eva and Koda were pretty worried about us."
    $ chibi_jax = "images/chibi/jax_neutral.png"
    wt_ja "Even Isaak called. That was pretty unlike him."
    ast "Any sign of him?"
    wt_da "We haven't seen anything out of the ordinary, Aston."
    $ chibi_jax = "images/chibi/jax_worried.png"
    wt_ja "Let's keep calling out."
    mo "Lorenzo!"
    da "Lorenzo! Where are you!"

    "We called his name. No response."

    ast "Where are you, my love...?"

    show black with dissolve
    "The search mission went on for hours, but we were unsuccessful. It had to come to a halt for the day."
    "The sun was setting and we had to head back to camp before it became dark."

    "Lorenzo has been missing for about 24 hours now... It's not a good sign."

    #EXT: Camp 1A
    scene bg camp2_day with fade
    show ky smile at centerright
    show ast neutral at centerleft
    ky "Morgan, Aston! You're back!"

    show ast with move:
        xpos 1800
    hide ast
    "Aston doesn't respond and heads straight into the tent."
    show ky sad
    "Kyle sees that Lorenzo still hasn't come home."

    mo "It's not a 'you' problem Kyle. Don't worry."
    ky "Yeah, I just wish there was something I could do for him right now."
    mo "You haven't fully recovered from whatever you're dealing with, either. You need to rest."
    show ky confused
    ky "I know, which sucks. The best I can do is just hold the fort until everyone comes home."
    show ky smile
    ky "Gregory and Pearl are gonna help out tomorrow, I think."

    mo "Yep. Hopefully it'll make the search much easier."
    stop music fadeout 3.0
    #INT: Main tent
    scene bg maintent_night with dissolve
    play ambience amb_campnight fadein 1.0

    "The sleeping bags have all been moved to the main tent for now."
    "Some of our smaller tents were destroyed, so everyone's gotta share the big tent for the time being."
    "I need to call Colin."
    "Time for the waiting game, I guess. Once everyone's asleep, I'll step outside."

    #EXT: Camp 1A
    show bg camp2_night
    show satphone
    mo "Hey Pancake."
    co "Woah, you sound horrible. So my birdie in Heralign HQ was right about the situation?"
    mo "If they heard 'avalanche', then...yes they're right."
    co "Was anyone hurt? Are you hurt, Morg?"
    mo "I passed out for a few hours after getting hit by a rock or something."
    mo "My head still hurts, but otherwise I'm fine."
    mo "We do have someone that went missing, though. That's the worrying part."

    co "Judging from your tone, time's ticking and you still haven't found them?"
    mo "Yeah. Lorenzo has been missing for a little over 24 hours at this point."
    co "Rough spot there, bud. I hope he's okay."
    co "But still, I'm glad you're in one piece Morg."
    mo "The things I do for Elly... and you too!"
    co "What do you want from me this time? The snowmobile again?"
    mo "You're the best, thank you."
    co "How about the welcome home party that we talked about? I'll even cook for you."
    mo "Okay, alright. I'll take that, but you've gotta give papa a kiss."
    co "No."
    mo "Aww, are you shy?"
    co "You enjoy terrorizing me, don't you, Morg?"
    mo "Goodnight, Pancake. Sweet dreams!"
    co "Did you just kiss the damn ph-"
    hide satphone with sdissolve
    #phone end

    "I hung up on Colin."
    "I do enjoy terrorizing him...keeps me sane from the mess I'm dealing with here."
    stop ambience fadeout 3.0

label dec_8:
    #INT: Cabin
    scene cottage with longfade
    play ambience amb_cabin fadein 1.0
    #Lorenzo's POV

    lo "Let's see here... I've got food that will last me for a week."
    lo "Two... Two weeks if I can handle eating just one meal per day."

    show black with dissolve
    "On the day of the avalanche, Lorenzo slipped and tumbled down the hill."
    "He escaped death in exchange for a few bruises here and there."
    "He ended up further away from the rest...hence why Aston couldn't find him."
    "To make things worse, his Walkie's receiver snapped off during the fall."
    "With no map on hand, it would be hard to navigate back to camp."
    "When time is ticking and the sun threatens to set, you don't have a lot of options."
    "Shelter is the first prerequisite for survival in this situation."
    "Fortunately, he found himself close to a tiny deserted cabin."
    hide black

    lo "The furniture in here reminds me a lot of the village up north... Maybe this is one of their hunting huts."

    "Looking around, there's a shelf of perishables, a mini fireplace, lots of blankets and a sole rifle leaning against the wall."
    "Lorenzo made a makeshift bed with an armchair and its matching ottoman."

    "The silver lining is that it's much more comfortable than a sleeping bag."

    lo "I need to start finding my bearings tomorrow. Cassie's map never had a cabin on it, so this must be an area that we haven't been to yet."
    lo "I'm sure he's worried sick about me."
    lo "Hang tight, amore. I'll find you."
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
    lo "Wait, what was that?"
    play music audio.anxious
    "Out of the corner of his eye, Lorenzo swears that he saw something huge."
    "Something... unpleasantly familiar."
    show cg bearwindow2
    "He pinches himself."

    lo "I am still wide awake... so then why?"

    hide cg
    "He looks out the window again."

    #BG Window with bear
    show cg bearwindow3 
    if persistent.screenshake:
        with hpunch
    $ persistent.gallery_bearwindow = True
    lo "..."

    show black with pushupquick
    hide cg
    "He crouches under the window to catch his breath."

    lo "The door! The door... Locked, yes. The window... that won't do. I need to cover it up."

    hide black
    show bg cottage2
    "He runs to the blankets and quickly drapes it over the window."
    "After pacing around the room nervously, he decided that he'll hold the rifle in hand while he sleeps tonight."
    "Not sure if the rifle would do any damage but, it's safer to have it than not."
    stop music fadeout 3.0


label dec_9:
    #start scene black
    scene black with dissolve
    "The search today went on longer than the other days."
    "Still no sign of Lorenzo."
    "We've cleared the area around the lake, the surrounding area of the village."
    "Even where I was first dropped off but still nothing."
    "The site of the avalanche yielded no results either."
    "The guys at Camp 2 have been digging around the area."
    "I heard that Eva and Koda were there too to support the camp."
    "We've never found any of Lorenzo's belongings."
    "He must've been pretty far when we separated."
    "*rustle*"
    #SFX sleeping bag
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
            mo "Aston."
            show ast confused
            "I think I startled him."
            ast "Go back to sleep, Morgan."
            "Aston is doing exactly what I think he's doing."
            "He's going to go out at night, in the pitch dark silence, alone."
            "I stand up next to him."

            menu:
                "Convince him not to go":
                    mo "I don't think it's a good idea."
                    show ast angry
                    ast "If you're not going to help me, please do not stop me."

                "Join him":
                    mo "I know what you're doing, but please let me come along. It's dangerous to go alone."
                    show ast sad
                    "Aston looks worriedly at me."

        #choice branch 2 ends
            show gr neutral at right
            gr "Are you guys heading out?"
            "Gregory sits up, tiredly."
            show gr angry
            gr "You're not supposed to go out after night remember? I'm liable for your safety."
            show ast angry
            ast "Lorenzo is out there, I can't possibly sleep it off like it's nothing."
            show gr neutral
            gr "Look, you can try if you want."
            gr "But it is cold as shit out there, and your flashlight is not gonna be helpful."
            "Aston doesn't say anything else."
            "Determined, he turns to leave."
            hide ast
            mo "He's usually not that reckless. Let me go check on him."
            gr "Morgan, let him be. He'll come back tomorrow."
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
                    mo "I don't think it's a good idea."
                    show ast angry
                    ast "If you're not going to help me, please do not stop me."
                    ast "Don't even bother following me."
                    hide ast with sdissolve
                    "Aston took off from the camp."
                    "I can't gear up quick enough to catch up to him."
                    mo "Wait, Aston!"
                    "Damn it."
                    "I counted my losses and stayed in the tent all night. I didn't get any sleep."

                "Join him":
                    $ aston_safe = True
                    $ joined_aston = True
                    mo "I know what you're doing, but please let me come along. It's dangerous to go alone."
                    show ast sad
                    "Aston looks worriedly at me."
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
    #To Sharkie, this sequence only happens if you fail to join Aston on his adventure, then it just continues downwards
    #(STRIKE 1 added to Gregory sus meter, whenever you see this Sharkie lmk cause I have questions to ask)
    #EXT: Camp 1A
    scene bg camp2_day with longfade
    play ambience amb_campday fadein 1.0
    if not joined_aston:
        "The search commences today."
        "Gregory was right about Aston, he made it back before dawn."
        show ast neutral
        "The dark circles under his eyes and his expressions tell me that his search was unsuccessful."

        mo "Aston?"
        ast "Good morning, Morgan."
        show ast sad
        ast "I'd like to apologize for yesterday."
        mo "No please don't, you're good."
        mo "Just that, if you're planning on doing that again tonight, please let me know."
        show ast neutral
        ast "Alright, I shall."
        show ast sad
        ast "My search... was unsuccessful."
        mo "It's okay, we'll keep trying. You have an ally here."
        show ast happy
        "Aston flashes me a weak smile, and nods."
        stop ambience fadeout 3.0

    #To Sharkie, skip to this sequence if you successfully join Aston on his adventure
    label find_lorenzo:
        scene forest3 with fade
    #EXT: Forest
        play ambience amb_campnight fadein 1.0
        "Did I ever mention loving night walks?"
        "Well, I hate this."
        "A night walk in the forest is never fun, unless you live for the thrill."
        "I don't particularly find putting myself at risk of getting mauled by animals 'thrilling' so to speak."
        "The only thing comforting is that it isn't snowing."
        "And also the fact that Aston is with me, we're not alone in this dreaded cold."
        "We took an entirely different path this time."
        "Gregory did say the east side of the mountains is a big no-no."
        "But that's exactly the way we're going to go."
        "After walking for a bit, my flashlight reflects off a different surface."
        "It's not trees or snow. Is that a window?"

        show ast neutral
        mo "Aston, look."

        "We shined our flashlights towards the same spot."
        "A cabin, it looks kinda small."
        "Maybe for hunting supplies?"
        "We walked up to the cabin and inspected the door up close."

        mo "I suppose we should give a polite knock before entering?"
        stop ambience fadeout 5.0

        "Aston knocks on the door."
        #SFX knock
        show ast sad
        ast "Lorenzo, are you in here?"
        lo "Aston?"

        show cg findinglorenzo
        $ persistent.gallery_findinglorenzo = True
        play music audio.light

        hide ast
        "Aston barges into the cabin to see a petrified Lorenzo."

        ast "Lorenzo!"
        lo "A-Amore... I thought I'd never see you again."

        "I closed the door behind Aston and let them have their moment."
        "The two of them share a long awaited embrace."
        "It fills me with the purest form of emotional warmth to see them like this."

        hide cg
        show bg cottage2
        show ast happy at centerleft
        show lorenzo sad at centerright
        ast "Thank goodness."
        lo "I knew you'd find me, amore."
        lo "I'm sorry for worrying you, and everyone as well."

        "With tears forming in his eyes, Lorenzo beams at me as well."
        show lorenzo smile
        lo "It's good to see you too, Morgan."

        "I gave him a gentle pat on his shoulder."

        mo "And I'm glad that you're okay."
        show ast sad
        ast "I don't want you to stay here alone, love."
        show lorenzo sad
        ast "But I'm worried about bringing you back to camp."
        mo "What's that about?"

        "The two look at me, and then at each other."
        "Lorenzo breaks the silence first."
        show lorenzo neutral
        show ast neutral
        lo "There was this person at camp before you, his name is Elliot."

        "Elliot!"
        "I have never been this happy to hear a name spoken out loud."

        lo "One day he just disappeared without a trace."
        lo "His belongings all have been rummaged through, as if he was rushing to somewhere."
        show ast inthought
        ast "And the reason why I don't want Lorenzo to go back to camp is because of Gregory."
        ast "Elliot had a descriptively similar rash forming on the back of his right shoulder."
        ast "Ruran was treating him back then. I never had a peek at it so I can't be sure."
        show ast neutral
        ast "On the night before he disappeared, I overheard Gregory on the phone."
        ast "His very words were 'I'll take care of him, ma'am.' I didn't pay any mind to that at the time."

        show ast angry
        ast "But ever since Elliot disappeared, I didn't like what I was realizing when I put two and two together."
        show lorenzo pondering
        lo "We didn't have any evidence, but we have been really cautious about Gregory ever since."
        show lorenzo neutral
        lo "But I still don't want to believe that he'd do something to Elliot."
        mo "But Gregory doesn't seem suspicious of Kyle?"
        show lorenzo pondering
        lo "I'd like to believe that it's because Kyle was bitten by Susie."
        show lorenzo sad
        lo "Whereas Elliot and I... I don't even know how I got it in the first place."
        mo "Do you... think that it's the same infection, but from multiple sources?"
        show ast inthought
        ast "That would be probable, yes."
        mo "Speaking of infections, how are you doing Lorenzo?"
        lo "My arm is still red... but I think something worse has been happening to me."
        show lorenzo sick
        lo "I-I don't know, I want to believe that I was just seeing things."

        show ast neutral with move:
            xpos 600
        show lorenzo neutral
        "Aston squeezes Lorenzo's hand to help ease his nerves. Lorenzo takes a deep breath before he continues."

        lo "It's the bear but... But I was sure I saw it right outside the window."
        lo "I pinched myself while looking directly at it, and no, I wasn't dreaming."
        show lorenzo sad
        lo "Aston, Morgan... I really don't enjoy the uneasiness I feel running down my spine every time I hear something outside these walls."
        show ast sad
        ast "Do you want me to stay the night, love?"
        lo "Gregory would be the problem. Both of you can't stay here."
        show ast neutral
        mo "We'd need a plan then."
        mo "The game ends if Gregory gets suspicious before Lorenzo's arm heals."
        mo "This would mean that Aston and I can only visit you during the night."
        mo "And this would mean that you have to tank through the day without us here."
        show lorenzo neutral
        lo "...I think I can do that."
        show ast sad
        ast "Will you be okay?"
        show lorenzo smile
        lo "For you amore, I will be strong for you."
        mo "Have I ever told you guys that y'all are awfully cute?"
        hide ast
        ast "..."
        show lorenzo happy
        lo "Haha! Amore, why did you turn away?"
        show ast neutral at centerleft
        ast "It's nothing."
        mo "Alright, let me know when you're ready to go back Aston."
        mo "We have about 5 hours till dawn, but ideally we should get some sleep in too."
        mo "Wouldn't want to look suspiciously groggy the next day."
        show ast sad
        ast "That's very true."
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
            "It was something I've noticed for the past few days, heard him tossing and turning in his sleep."
            "All is well now."
    stop music fadeout 3.0

label dec_11:
    #EXT: Camp 1A
    scene bg camp2_day with longfade
    play ambience amb_campday fadein 1.0
    show gr neutral at centerleft
    gr "Guys, we've received an extra mission."
    "Gregory interrupts breakfast with urgent news."
    show pearl smile at centerright
    pe "What is it, what is it?"
    gr "Someone from the village is missing."
    gr "So while we look for Lorenzo, we'll also have to keep our eyes peeled for another person."

    "Someone else is missing?"
    "We exchanged quiet glances, letting the weight of the situation sink in."
    "While everyone has been worried about Lorenzo, there's now potentially another victim."
    "Lorenzo was lucky."
    "I hope they survive this as well."
    show pearl confused
    pe "Did someone report it?"
    show gr confused
    gr "Yeah, Isaak is in contact with the village. There's a hotline for complaining if we ever get too rowdy here."

    "So someone told Isaak this information?"
    "I mean, I already knew that the whole 'the village hates us' facade was probably a lie."
    "But why would they be anywhere near our camp when the avalanche happened?"
    "Just casually strolling to our camp?"
    "We've been on the search for a few days now, there wasn't any sign of another survivor."
    "It would seem that Aston also shares the same sentiment."
    "He looked at me, reflecting the same expression that I have."
    "Doubt."
    "The search, now for two, commences."
    stop ambience fadeout 3.0

    scene bg cottage2 with fade
    #Lorenzo's POV
    "Lorenzo is wide awake and feeling restless."

    "The bear's presence has been weighing heavily on his mind."
    "Hearing growling right out the door every once in a while."
    "The knocking on the window is starting to get annoying too."

    lo "I'd like to sleep, if you would be so kind?"

    "No response."

    lo "Grazie."

    "He pulls the blanket higher up to cover his shoulders."
    play ambience amb_lobear fadein 1.0

    ha "Lo-Lorenzo."

    "The unexpected voice sends a shiver down his spine. That sounded like Aston."
    show lorenzo scared
    "Lorenzo jolts up from his bed."

    lo "Amore? Is that you?"
    ha "L-Lenzo."

    show lorenzo pondering
    "Nevermind. The fear dissipates and it turns into confusion."

    ha "Lorenzo."
    show lorenzo sad
    "Lorenzo's face scrunches up in disappointment."
    "Aston has always pronounced his name the proper way, and this is just insulting."
    "This realization sparked a defiant fire within him."
    show lorenzo neutral
    lo "Lorenso- I'm hallucinating, aren't I?"


    "For once instead of fear, Lorenzo is frankly, really sick of this."
    "The torment needs to stop."

    lo "Okay, I'll play your game."
    lo "If you're not going to leave me alone, I might as well get to know you."
    "He grabs his journal and turns to a blank page and jots down some notes."

    "Characteristics:"
    "Black bear, no fur, goop-like."
    "Green stuff looks like a fluid of some sort dripping from its mouth."
    "Doesn't act like a normal bear."


    lo "And, this... This is a new feature."

    "Mimics speech, but it's not very smart."

    ha "*growl*"
    show lorenzo smile
    lo "Salve, imitatore."
    stop ambience fadeout 1.0


label dec_12:
    #EXT: Camp 1A
    scene bg camp2_night with longfade
    play ambience amb_campnight fadein 1.0
    #Gregory's POV
    "Gregory sits on a rock some distance away from the main tent."
    show gr neutral
    "It's time for his weekly check in."
    hi "You're a day late."
    gr "I know, lots of stuff happening at camp at the moment."
    hi "Right. First an avalanche, then what?"
    show gr confused
    gr "Missing people. Lorenzo and one of the villagers."
    hi "The financier? Do you need me to send a replacement?"
    show gr angry
    gr "What?"
    gr "Listen here lady, I don't care what you rich people think about us."
    gr "But Lorenzo isn't someone you can just replace like that."
    hi "The 'rich people' like the one you're talking to right now can buy you a liver."
    show gr worried
    gr "..."
    hi "Think about it Gregory, once your job here is done, you'll have all the time in the world to be with your little girl."
    hi "Forfeit the rescue mission if it's too time consuming."
    hi "I want results, not excuses or sob stories."
    show gr neutral
    "Gregory takes a moment to readjust."

    gr "Is there something you told Isaak but you're not telling me?"
    hi "No, I haven't spoken to him in weeks."
    hi "That boy never picks up."
    show gr worried
    gr "I'm worried about the mold."
    gr "What happens if the whole camp falls ill?"
    hi "Be a darling and make the right decisions then. You already know how to prevent it."
    hi "If Isaak could do it, you can too."
    hi "Good luck Gregory. You know what's best for your family."

    "She hangs up on him."
    show gr neutral
    "Gregory takes a look at the tent and sighs."
    "They may not be family, they may not even be friends."
    "But they are people Gregory spends the most time with."
    "And that doesn't discredit the fact that deep down, he cares."
    stop ambience fadeout 3.0

label dec_13:
    #EXT: Camp 1A
    scene bg camp2_day with longfade
    play ambience amb_campday fadein 1.0
    "Early this morning, Gregory announced that the rescue mission will take a break for now."
    "Even though Aston and I found Lorenzo."
    "This still leaves a bitter taste in our mouths."
    "Aston wears his usual nonchalant expression as Gregory pats him on the shoulder."
    "Kyle and Pearl were obviously saddened by the news."
    "They weren't in their cheery mood for the rest of the day."
    "Later in the day, I overheard Gregory on the Walkie with Wilbur."
    "It would seem that C2 isn't taking this decision lightly."
    "On one hand, I understand that there's a quota to meet."
    "On the other... Well, I hate it."
    "That means giving up on Lorenzo."
    "With nothing much to do for the rest of the day, I think this would be a good day to drop updates."

    #EXT: Camp 1A
    show bg camp2_night
    stop ambience fadeout 3.0
    "Right. Now that everyone's sleeping, 'tis the time."
    play ambience amb_campnight fadein 1.0

    show satphone
    mo "Pancake!"
    co "The number you have dialed is unavailable, please tr-"
    mo "Okay pancake batter, I have something for you."
    co "That's even worse."
    mo "Do you want to be goopy or fluffy? Pick one."
    co "Fluffy..."
    mo "Nice. Anyway, you need to hear this."
    mo "Lorenzo's in a cabin in the forest, but his symptoms are getting worse."
    mo "Then Elly's name popped up in conversation."
    mo "Greggy's involved in some way, but we don't have evidence."
    mo "Aston overheard him talking to someone the night before he disappeared."
    mo "And now Lorenzo is going to camp at the cabin because they don't want to take any chances."

    mo "Elly's rash apparently looks exactly like the rashes we're dealing with, and it didn't come from a bite."
    mo "Which is why Kyle is safe, he's an outlier."
    co "Now you're talking Morg! That's a lot that you've gathered here."
    co "Elly and Greggy, huh? I'll see if I can dig up more info about that mysterious caller that he reports to."
    mo "Alright nice! Good talk Pan-"
    hide satphone
    #phone ends

    "He hung up on me."
    "Damn it, he knows my tricks. That ain't fun."
    "I'll need new ways to annoy him."
    stop ambience fadeout 1.0

label dec_14:
    #EXT: Forest
    scene bg forest3 with longfade
    play ambience amb_asthalu fadein 1.0

    show ast neutral
    "Aston and I are once again on our way to meet Lorenzo."
    "This time, we brought supplies and some tools to fix his Walkie."
    "I was walking ahead of him with my flashlight illuminating the dense forest."
    "When suddenly, the footsteps behind me stopped abruptly."

    show ast confused
    ast "Morgan, did you hear that?"

    "I turn to face Aston."

    mo "What did you hear?"

    show ast inthought
    "He shakes his head, signaling me to stay quiet as he focuses on the sound."
    "His gaze glued to a tree to our right."

    show ast sad
    ast "Lorenzo?"
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
            mo "Aston, I don't know what you're hearing."
            mo "But do you want to investigate the sound?"
            show ast sad
            ast "Yes, please."
            "We inch closer to the tree, supposedly that's where the source is coming from."
            "There was no one there."
            show ast inthought
            ast "I swore I heard him."
            ast "But you're right, let's head t-"
            show ast sad
            "Aston freezes up again."
            mo "What is it? Talk to me."
            "As I try to get a hold of him, my flashlight dies."
            show black
            "I swapped my batteries out as fast as I could."
            hide black
            show ast scared
            "When the lights turn back on, Aston stands there uneasily."
            ast "...Morgan, can you take me to Lorenzo?"
            mo "Say no more."

        "Continue on without investigating.":
            mo "Aston, I don't know what you're hearing."
            mo "But we've got to get to Lorenzo."
            show ast sad
            "I had to practically drag him along."
            show ast inthought
            ast "I swore I heard him."
            ast "But you're right, let's head t-"
            show ast sad
            "Aston freezes up again."
            mo "What is it? Talk to me."
            "As I try to get a hold of him, my flashlight dies."
            show black
            hide ast
            "I swapped my batteries out as fast as I could."
            hide black
            "When the lights turn back on, Aston has gone missing."
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
        lo "I'm glad to see you both!"
        show ast with move:
            xpos 400
        "Aston runs to Lorenzo and gives him a quick hug."
        show ast with move:
            xpos 300
        show lorenzo smile
        "Lorenzo then reaches out to grab his journal."
        lo "Have a seat, I have some info for you guys."
        "He flips to his recent notes in his journal."
        show ast neutral
        mo "Have you been studying it?"
        show lorenzo neutral
        lo "Yes. That and all my symptoms."
        mo "You've had hallucinations that called your name? In Aston's voice?"
        show lorenzo scared
        lo "I did not enjoy that one bit. It was horrifying at first but now I am sick of its games."


        show lorenzo sad
        lo "Because I know for a fact that you don't sound like that, amore."
        show ast inthought
        "Aston looks like he's deep in thought."
        mo "Aston... Are you alright?"

        show ast neutral
        ast "I wasn't, but I am feeling a lot better now."
        show ast inthought
        ast "If what you're saying is true, then what I heard outside was... not you."
        ast "If you weren't there to accompany me Morgan, I think I would've been a goner."

        "I gave Aston a gentle pat."
        show ast sad
        ast "But will you be okay, love?"
        ast "What if the hallucinations get worse?"
        show lorenzo smile
        lo "I'll be fine amore, no need to worry about me."
        "Lorenzo reaches out to cup Aston's face."
        show lorenzo with move:
            xpos 900
        show ast happy
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
            lo "I'm glad to see you Morgan but where's Aston?"
            mo "He... He ran off. I tried to stop him but he said he kept hearing things."
            mo "When I finally got my flashlight working again, Aston was gone."
            "Just then the door swings open again, Aston is standing there trying to catch his breath."
            play music audio.light
            show ast neutral at left
            ast "Sorry I'm late."
            show lorenzo scared
            lo "Aston! Don't scare me like that."
            show lorenzo sad
            show ast sad with move:
                xpos 400
            "Aston runs to Lorenzo and gives him a quick hug."
            show ast with move:
                xpos 300
            show ast happy with dissolve
            show lorenzo smile
            "Lorenzo then reaches out to grab his journal."
            lo "Have a seat, I have some info for you guys."
            "He flips to his recent notes in his journal."
            show ast neutral
            mo "Have you been studying it?"
            show lorenzo neutral
            lo "Yes. That and all my symptoms."
            mo "You've had hallucinations that called your name? In Aston's voice?"
            show lorenzo scared
            lo "I did not enjoy that one bit. It was horrifying at first but now I am sick of its games."

            show lorenzo sad
            lo "Because I know for a fact that you don't sound like that, amore."
            show ast inthought
            "Aston looks like he's deep in thought."
            mo "Aston... Are you alright?"

            show ast neutral
            ast "I'm sorry I ran off, but I am feeling a lot better now."
            show ast inthought
            ast "If what you're saying is true, then what I heard outside was... not you."
            ast "If you hadn't reminded me that Lorenzo was safe Morgan, I think I would've been a goner."

            "I gave Aston a gentle pat."
            show ast sad
            ast "But will you be okay, love?"
            ast "What if the hallucinations get worse?"
            show lorenzo smile
            lo "I'll be fine amore, no need to worry about me."
            "Lorenzo reaches out to cup Aston's face."
            show lorenzo with move:
                xpos 900
            show ast happy
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
            lo "I'm glad to see you Morgan but where's Aston?"
            mo "He... He ran off. I tried to stop him but he said he kept hearing things."
            mo "When I finally got my flashlight working again, Aston was gone."
            show lorenzo sick
            lo "..."
            "Lorenzo then reaches out to grab his journal."
            show lorenzo sad
            lo "Well have a seat, I have some info for you Morgan."
            "He flips to his recent notes in his journal."
            mo "Have you been studying it?"
            show lorenzo neutral
            lo "Yes. That and all my symptoms."
            mo "You've had hallucinations that called your name? In Aston's voice?"
            show lorenzo scared
            lo "I did not enjoy that one bit. It was horrifying at first but now I am sick of its games."
            show lorenzo sad
            lo "Because I know for a fact that he doesn't sound like that."
            mo "What Aston heard outside was definitely not you then."
            lo "It would seem that way, yes."
            lo "Morgan. Will you help me find him?"
            mo "I will, Lorenzo."
            stop ambience fadeout 3.0


    #@ Sharkie the way it works:
    #If on the 9th, you follow Aston, then it's +1
    #If on the 9th, Aston goes away himself it's +0
    #If on the 14th, you investigate it's +1
    #If on the 14th, you don't investigate it's +0
    #Aston will die if you end up with 0, Aston won't die if you end up with 1 or 2

label dec_15:
    #EXT: Forest
    scene bg forest3 with longfade
    #If Aston is safe
    if aston_safe:
        "Today is my turn to accompany Kyle on his photography session."
        "I can't take my mind off what happened last night."
        "Hallucinations and... all of Lorenzo's symptoms?"
        show ky smile
        ky "Oh dear Morgan! There's lots of deer."
        "That horrible pun snapped me back into reality."
        show ky happy
        "Kyle seems amused with my reaction."
        show ky smile
        ky "What's wrong, Morgan? Do you want to head back to camp?"
        mo "I'll be alright Kyle. I've just got lots of things on my mind."

    #If Aston is not safe
    else:
        "Today is my turn to accompany Kyle on his photography session."
        "I can't take my mind off what happened last night."
        "Hallucinations and... all of Lorenzo's symptoms?"
        "And Aston... I haven't seen him since last night."
        show ky smile
        ky "Oh dear Morgan! There's lots of deer."
        "That horrible pun snapped me back into reality."
        show ky happy
        "Kyle seems amused with my reaction."
        show ky sad
        ky "Still thinking about Aston?"
        mo "Yeah.. but I'll be alright Kyle."

    #continue script from here

    "Click click!"
    #SFX camera
    ky "Do you want to talk about it or...?"
    show ky confused
    ky "Actually hold that thought Morgan, are you seeing what I'm seeing over there?"
    hide ky
    show bg forest3_animals
    "Amongst the herd of deer lies a disturbing goop of an animal."
    play music audio.anxious 

    "It looks like a dead bird."
    show ky sad
    ky "Nooooo what happened here?"
    mo "Might be worth taking pictures of that."

    "Although hesitant at first, Kyle begins snapping a few pictures."
    "Now that I'm actually taking in my surroundings, I realized that there were more of these piles."
    "I gave Kyle a nudge on his shoulder."
    show ky shaken
    ky "..."

    "Yeah that's a valid reaction."
    "It seems to be mostly birds?"
    "They've definitely been here long enough to start rotting."
    show ky sad
    "\"Do not attempt to handle animal carcasses without protective gear.\""
    "Gotta respect the rules in \"The Camp Guide's Guide.\""
    "It'll definitely be worthwhile to pick some of them up."

    mo "Let's head back to camp Kyle, I've got samples to grab."
    show ky shaken
    ky "A-Are you gonna pick all of them up?"
    mo "One should suffice I hope?"
    stop music fadeout 3.0

label dec_16:
    #EXT: Camp 1A
    #If Aston safe
    if aston_safe:
        scene cottage2 with longfade
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
        mo "In good spirits today?"
        show lorenzo happy
        lo "Getting better day by day. How are you Aston?"
        ast "It's bothering me, but Morgan has been keeping me sane."

        "I kept an eye on him whilst doing our camp duties."
        "Occasionally, he'll pause what he's doing and look towards the forest."
        "Aston doesn't tell me what he hears or when, but he always looks to me for confirmation."
        "If I don't hear anything, then there's no cause for concern."
        "This is a system that we've set up."
        show ast neutral
        show lorenzo pondering
        lo "I've studied the thing a bit more."
        show lorenzo neutral
        lo "An odd question but, have you seen any animals that look like this?"

        "He points at his journal, to sketches of animals covered with black viscous substance."

        mo "It's funny you say that, but yes I did. Birds, many dead birds."
        show lorenzo scared
        lo "Y-You didn't use your bare hands right?"
        mo "\"The Camp Guide's Guide\" said that I couldn't so I've got gear, don't worry."
        show lorenzo neutral
        lo "Okay good for you, amico. I didn't have gear when I saw what was in the icebox in the RC."
        ast "What was in it?"
        show lorenzo sick
        lo "Unidentifiable mass, but it looks exactly like the drawing and the bear that I'm dealing with."
        show ast inthought
        show lorenzo sad
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

        ast "Just for precaution, Morgan."

        "Aston and Lorenzo didn't have a bite. Kyle is an outlier."

        mo "Do you think... Elliot had also been exposed the same way?"
        show ast inthought
        ast "I wouldn't be surprised, he spent a lot of time at the RC. Eva and him were close."

        "Was Elliot trying to dig around at the RC?"
        "Something of importance must be happening there."
        "I wonder how the water-fungi testing is going."
        "Time to make a trip down there, but I can't show up uninvited."
        "I'll find a reason to."
        stop music fadeout 3.0


    #If Aston not safe
    else:
        scene bg camp2_day with longfade
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
        pe "Hey, can you hear me?"
        "Pearl's voice brings me back."
        show pearl smile
        "With a concerned look on her face, she extends her arms out and offers a hug."
        "I accepted the hug and she gave me a few pats on the back."
        show pearl neutral
        pe "You looked like you needed it Morgan."
        pe "And you're not alone here, we're all here with you."
        pe "We are going to find them."
        show pearl smile
        pe "And then I'm going to force feed Aston some greens for running away from camp like that."
        "The image of Pearl running after him with a can of pea soup is hilarious."
        show pearl happy
        "Seeing that her comment elicited a chuckle out of me, she nodded, satisfied with her work."
        stop ambience fadeout 3.0

label dec_17:
    scene bg forest3 with longfade
    play ambience amb_campday fadein 1.0

    #Kyle's POV
    show ky smile at centerleft
    show pearl smile at centerright
    "Kyle and Pearl paired up today to grab some pictures."
    "Click click click!"
    pe "Let's see squirrels, squirrels, squirrels... and one napping wolf!"
    show ky happy
    show pearl happy
    ky "Good eye, Pearl!"
    show pearl smile
    "Click click click!"
    show ky neutral
    "He looks down at his camera, proud of his shots."

    show ky happy
    ky "Looks like our harvest today is bountiful!"
    show pearl happy
    pe "Aww yeah!"

    "All of a sudden, something caught Kyle's attention."
    show ky confused
    "An animal moving in his peripheral vision?"

    ky "Pearl, I'm gonna check out that tree."
    show pearl neutral
    pe "Okay! I'll be here."
    hide pearl

    "Kyle positions himself behind a large tree, peeking to observe the animal at a safe distance."
    "A large chunk of fur phases through the trees."
    "He approaches the animal with caution."

    show ky shaken
    ky "Oh shit that's a bear."
    stop ambience fadeout 1.0
    play music audio.anxious fadein 3.0

    "The bear doesn't notice Kyle's presence."
    "Click!"
    #SFX camera
    show cg glitchedphoto
    "He checks his camera."
    "It's a tad blurry."
    hide cg

    show ky neutral
    ky "Let me try that again."

    "Click!"
    #SFX camera
    "He checks his camera once again."
    "The bear isn't in the picture."
    show ky confused
    ky "What."

    "Seems like the bear was moving about and now it's clawing a tree."
    show ky neutral
    ky "Okay, third time's the charm!"

    "Click!"
    #SFX flash

    show ky shaken
    ky "Shit."

    "The flash turned on."

    ky "Please don't see me, please don't see me..."

    "Kyle breaks vision from the bear, hiding behind a large tree."
    "*growl*"

    ky "..."
    show pearl smile at centerright
    pe "Heya Kyle! How's the photo taking going?"
    ky "Pearl! Keep it down. There's a bear behind this tree."
    ky "It was growling."
    show pearl confused
    pe "G-Growling? Don't pull my leg Kyle, why would a bear be out and about this time of the year?"
    pe "Aren't they hibernating?"
    show ky sad
    ky "I have pictures. Let's go back to camp and I'll show you."
    show pearl neutral
    pe "If you saw a bear, I'll believe you! But you need to take a deep breath now, your breathing is ragged."

    "Pearl is right."
    "Kyle takes a few deep breaths and the two head back to camp."

    #EXT: Camp 1A
    show bg camp2_day
    show ky confused
    "Kyle flips through the camera's gallery once more."
    "There's a blurry shot."
    "One out of frame."
    "And the last one... distorted."
    show pearl smile
    pe "Ooh! What's this glitchy effect on this blob?"

    "Kyle takes another picture on the spot."
    "There's no distortion."
    show pearl confused
    pe "Is it broken?"
    ky "My camera's fine, but my pictures are not."
    show ky neutral
    ky "Could you grab my laptop Pearl? I need backups of these before I lose 'em."
    show pearl smile
    pe "On it!"
    stop music fadeout 3.0

label dec_18:
    #INT: Main tent
    scene bg maintent_day with longfade
    play ambience amb_intcampday fadein 1.0
        #Kyle's POV
    show ky smile
    "Kyle's Walkie starts beeping."
    "It's from Koda."
    #radio starts
    $ chibi_koda = "images/chibi/koda_happy.png"
    wt_ko "Hi Kyle! Is now a good time?"
    wt_ky "I'm all ears!"
    $ chibi_eva = "images/chibi/eva_neutral.png"
    wt_ev "It would seem that most of the animals are okay."
    $ chibi_eva = "images/chibi/eva_worried.png"
    wt_ev "But there were two strange things you've encountered?"
    wt_ky "Yeah, the bird stuff and a bear."
    $ chibi_eva = "images/chibi/eva_neutral.png"
    wt_ev "You saw a bear? Sure it wasn't something else?"
    $ chibi_koda = "images/chibi/koda_worried.png"
    wt_ko "Wouldn't they be hibernating?"
    wt_ky "That's what Pearl has been saying... but I am convinced that I saw one."
    wt_ky "If there really was one, I'll try snagging pictures again."
    wt_ko "Safety's first Kyle! Don't end up on the headlines."
    wt_ky "I am a professional, don't you worry Koda!"
    wt_is "And the bird pictures... Those were the same ones like the one that Morgan picked up, yes?"
    wt_ky "Oh hey Isaak! And yes."
    wt_is "How many birds were there?"
    wt_ky "About 8 to 10? Have you guys found out why this is happening?"
    wt_is "No. We haven't got an inkling."
    wt_ky "And its appearance? The globby slimy icky stuff?"
    wt_is "Same answer."
    wt_ky "Do you think it has something to do with the water?"
    wt_is "..."
    wt_ko "U-Uh, we don't know just yet, but we'll let you know when we do!"
    wt_ky "Sorry sorry. Just want to make sure that we're all safe while we're out there."
    $ chibi_eva = "images/chibi/eva_happy.png"
    wt_ev "Anyway, thanks Kyle. Really great shots by the way, stunning photos."
    wt_ky "I take pride in that! Thank you!"
    stop ambience fadeout 3.0
    #radio ends
    nvl clear

label dec_20:
#20th Aston safe

    play music audio.light
    scene bg camp2_day with longfade
    if aston_safe:
        "While enjoying a cup of cocoa by myself, I received a Walkie beep from Wilbur."
        #radio start
        wt_wi "Hello Morgan! Are you there?"
        wt_mo "What's up?"
        $ chibi_ruran = "images/chibi/ruran_worried.png"
        wt_ru "How is Aston?"
        wt_mo "He's hanging in there I think. I'm looking out for him, don't worry."
        wt_ru "Aston is strong, perhaps too strong. He takes on everything and bottles up his own emotions."
        wt_ru "Lorenzo is the only person who he confides with, and with him missing..."
        $ chibi_wilbur = "images/chibi/wilbur_worried.png"
        wt_wi "Keep an eye on him will you, son? He needs all the support he can get."
        wt_mo "Of course."
        #radio ends
        nvl clear
        "I look towards Aston who's taking a quick nap in the corner of the tent."
        "He'll be okay under my watch."

    #20th Aston not safe
    #EXT: Camp 1A
    else:
        "While enjoying a cup of cocoa by myself, I received a quick Walkie beep from Wilbur."
        #radio start
        $ chibi_wilbur = "images/chibi/wilbur_worried.png"
        wt_wi "Hello Morgan! Are you there?"
        wt_mo "What's up?"
        $ chibi_ruran = "images/chibi/ruran_worried.png"
        wt_ru "Any updates on Aston?"
        wt_mo "Aston... hasn't come back."
        wt_ru "So there's no sign of both of them yet..."
        $ chibi_wilbur = "images/chibi/wilbur_worried.png"
        wt_wi "Keep us updated will you, son? Let us know if you've seen them."
        wt_mo "Of course."
        #radio ends
        nvl clear
        "I look towards the empty corner of the tent."
        "I'm sorry, Lorenzo."

label dec_21:
    scene bg maintent_day with longfade
    #INT: Main tent
    show ky confused
    "Kyle is looking through his camera gallery."
    show ky smile
    ky "Hmmm... Oh, Morgan! Hello!"
    "He notices me walking into the tent."
    ky "Can I get your opinion on something?"
    "He tilts the camera towards me."
    show cg glitchedphoto

    "I don't... like what I am seeing here."
    ky "Weird, huh? My camera glitched out on this photo."
    mo "That looks like a bear, no?"
    ky "I mean, yeah, I saw it with my eyeballs."
    show ky sad
    ky "But it looked nothing like the picture here."
    hide cg
    "I touched Kyle's forehead to feel his temperature."
    show ky happy
    ky "No fever!"
    "I'm not sure if Kyle is infected."
    show ky neutral
    "But I can't cross out the chance that he might be hallucinating as well."
    "Another bear of all things."
    "Hibernation doesn't seem like a popular activity here."
    mo "Could I get a copy of that?"
    show ky smile
    ky "Absolutely, give me just a moment!"
    "Great, another delivery for Colin."

label dec_22:
    #EXT: Camp 1A
    scene bg maintent_day with longfade
    show pearl confused
    "Pearl seems frantic today."
    "Searching high and low for something... Her compass, maybe?"

    mo "Searching for your compass again, Pearl?"
    show pearl sad
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
    mo "Pearl? I found it, but... why was it in the crock pot?"
    show pearl confused
    pe "What, really? That's pretty odd, but thanks Morgan!"
    hide pearl
    "She took her compass from my hands and ran off into the main tent."
    "Is it just me, or does Pearl seem off today?"

label dec_23:
    scene bg maintent_day with longfade
    #INT: Main tent
    show pearl smile
    da "Pearl? Are you okay?"
    show pearl neutral
    pe "I'm good! Think I've been feeling a lot more tired these days."
    da "Don't make me hike 2 hours to get to you, you know that I will."
    ko "Don't make me hike 4 hours to get to you, you know I'm not fit to do that."
    show pearl smile
    pe "I swear that I'm fine guys!"

    "I walked into a conversation that the trio were having."
    "She says that she's fine. I genuinely hope so."
    "Time to add another person to the 'worry' list."

label dec_24:
    #24th Aston safe
    if aston_safe:
        scene cottage2 with longfade
        "Aston heads over to the cottage again, this time without Morgan."
        "Lorenzo and Aston spend their evening chatting away over a packet of instant meat and potatoes."
        "And when it was almost time to sleep, Aston routinely brought the blankets over to the armchair."
        #CG: Aston and Lorenzo cuddling
        show cg christmas
        $ persistent.gallery_christmas = True
        "The two cuddle up together on the armchair."
        "It just barely fits the two of them."
        "As the clock struck midnight, it was finally time."

        ast "Happy Christmas, love."
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
        "He hugs his legs close to his chest."
        show black
        show ast happy:
            zoom 2.0
            xalign 0.5
        "Eyes closed, Aston's face flashes by."

        lo "Buon Natale, amore."
        lo "I miss you."

        hide black
        hide lorenzo
        hide ast

        "If one goes down, the other shall follow. This has always been the case for them."
        "But it would seem that for the first time, Lorenzo was truly alone."
        "Christmas just isn't the same without your beloved."

label dec_25:
    scene bg camp2_day with longfade
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

    menu christmas:
        "Beep Wilbur":
            if not christmas_wi:
                $ christmas_wi = True
                wt_mo "Merry Christmas, Wilbur!"
                $ chibi_wilbur = "images/chibi/wilbur_happy.png"
                wt_wi "Morgan! Thank you and Merry Christmas to you too!"
                $ chibi_wilbur = "images/chibi/wilbur_neutral.png"
                wt_wi "Make sure to have a great feast today and call your family, yes?"
                wt_mo "You bet I will."
                nvl clear
            else:
                "I've already talked to him."

        "Beep Ruran":
            if not christmas_ru:
                $ christmas_ru = True
                wt_mo "Merry Christmas, Ruran!"
                $ chibi_ruran = "images/chibi/ruran_happy.png"
                wt_ru "Merry Christmas to you too Morgan!"
                wt_ru "I hope that your wishes come true."
                wt_mo "Likewise to you Ruran."
                nvl clear
            else:
                "I've already talked to her."

        "Beep Davos":
            if not christmas_da:
                $ christmas_da = True
                wt_mo "Davos! Merry Christmas!"
                $ chibi_davos = "images/chibi/davos_neutral.png"
                wt_da "Merry Christmas Morgan! I heard the moon's going to be bright tonight!"
                $ chibi_davos = "images/chibi/davos_happy.png"
                wt_da "You wouldn't want to miss out on that!"
                wt_mo "That sounds lovely, I'll be sure to look up tonight."
                nvl clear
            else:
                "I've already talked to him."

        "Beep Cassie":
            if not christmas_ca:
                $ christmas_ca = True
                wt_mo "Merry Christmas, Cassie!"
                $ chibi_cassie = "images/chibi/cassie_happy.png"
                wt_ca "Aww thank you Morgan! Merry Christmas to you too!"
                wt_mo "Hope your ankle has been healing well."
                $ chibi_cassie = "images/chibi/cassie_neutral.png"
                wt_ca "Thankfully it has! Give it another week or two and I'll be up and running!"
                wt_mo "It's a Christmas miracle!"
                $ chibi_cassie = "images/chibi/cassie_happy.png"
                wt_ca "You're so right."
                nvl clear
            else:
                "I've already talked to her."

        "Beep Jax":
            if not christmas_ja:
                $ christmas_ja = True
                wt_mo "Merry Christmas!"
                $ chibi_jax = "images/chibi/jax_neutral.png"
                wt_ja "And Merry Christmas to you!"
                wt_mo "How's Christmas for you so far?"
                $ chibi_jax = "images/chibi/jax_happy.png"
                wt_ja "I slept in today, so now I'm all refreshed."
                wt_mo "Nothing beats those extra hours of sleep."
                "Nice, Jax and I are like-minded in that regard."
                nvl clear
            else:
                "I've already talked to him."

        "Beep Koda":
            if not christmas_ko:
                $ christmas_ko = True
                wt_mo "Hey Koda! Merry Christmas!"
                $ chibi_koda = "images/chibi/koda_happy.png"
                wt_ko "Morgan! Merry Christmas! I hope your day has been great!"
                wt_mo "It has been, yes. Hope you're taking time off to actually relax!"
                $ chibi_koda = "images/chibi/koda_neutral.png"
                wt_ko "Eva kicked me out of the lab today just for that reason!"
                $ chibi_koda = "images/chibi/koda_happy.png"
                wt_ko "Time for some well earned rest!"
            else:
                "I've already talked to them."

        "Beep Eva":
            if not christmas_ev:
                $ christmas_ev = True
                wt_mo "Merry Christmas, Eva!"
                $ chibi_eva = "images/chibi/eva_happy.png"
                wt_ev "Thanks! Merry Christmas to you too, Morgan."
                $ chibi_eva = "images/chibi/eva_neutral.png"
                wt_ev "I hope you prepared presents."
                wt_mo "Oh, I didn't."
                $ chibi_eva = "images/chibi/eva_happy.png"
                wt_ev "Really? That's a shame."
                wt_mo "Where's mine then?"
                "Eva just doesn't respond after that."
                "No presents then, I guess."
                nvl clear
            else:
                "I've already talked to her."

        "Beep Isaak":
            if not christmas_is:
                $ christmas_is = True
                wt_is "Hello?!"
                wt_mo "Merry Christmas... Isaak?"
                wt_is "Oh, it's you."
                wt_is "Merry Christmas to you too, Morgan."
                "I think he might've been expecting someone else."
                nvl clear
            else:
                "I've already talked to him."

        "Beep Lorenzo":
            if not christmas_lo:
                $ christmas_lo = True
                wt_mo "Merry Christmas, Lorenzo."
                if aston_safe:
                    "He won't respond because it's daytime, but I know that he can hear me, and that's all that matters."
                else:
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
    mo "Merry Christmas to my lovely Pancake!"
    co "Merry Christmas Morg!"
    mo "So about the snowmobi-"
    co "No."
    co "I'll get you something else when you're back."
    mo "Ooh, a surprise gift from Pancake? I'll take that."
    hide satphone
    #phone ends
    "I wonder what he meant by that, now he's got me curious."
    "Oh well, time for my fellow camp mates."

    #INT: Main tent
    scene bg maintent_day with dissolve
    mo "Merry Christmas everyone!"
    show gr neutral at left
    gr "Merry Christmas. You're done with the calls?"

    "I gave a light nod to Gregory."

    show ky happy at right
    show pearl happy at centerright
    ky "Merry Christmas Morgan!"
    pe "Merry Christmas Morgan!"

    "These two, I swear. They really do share the same brain cells."

    #IF Aston not safe skip the lines below
    if aston_safe:
        show ast happy at centerleft
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

    mo "Merry Christmas, Elly."
    stop music fadeout 3.0

label dec_26:
    scene bg camp2_day with longfade
    play music audio.neutral

    "Ah yes, it's time for my favorite hobby."
    "Tormenting my beloved 37 year old child."
    "But first, I should send him some pictures."
    "And... Sent!"
    #SFX ding
    #TODO phone start
    show satphone
    co "Heya Morg, calling again so soon?"
    mo "Pancake! I've missed you, and I feel like I haven't gotten you up to speed yet."
    co "Wow that's sweet. So what's good, Morg?"
    mo "Big things happened, lots of new discoveries over the past week. Did you see the goods?"
    co "I'm looking at a handwritten list and a glitched out picture, what's the deal with 'em?"
    mo "List contains Lorenzo's observations. The bear he's hallucinating about."
    mo "We're dealing with more than just physical symptoms now."
    co "You're saying that it's both visual and auditory shit?"
    mo "Yeah, and I have a feeling that Kyle almost caught it on camera."
    mo "I doubt he'd lie about seeing a bear, but it is weird that that's the only thing that's distorted in the photo."
    co "Hmmm... Think I'll have to consult my doctors to see if there's a possibility."
    mo "I do have some bad news though. Aston is also infected."
    mo "And I'm pretty sure that he hears things that I don't."

    if not aston_safe:
        mo "He went missing a day after our last update and hasn't come back since..."
        mo "I... I was there and I should've stopped him from running off, but my flashlight died and-"
        co "Morgan."
        mo "..."
        co "Chin up, Morg. If he's missing, you do whatever you can to find them."
        mo "Mmhmm."
    co "Okay and what about Elly? Do you think it's also related?"
    mo "It may very well be the same thing, yes."
    co "Sorry Morg, you're cutting off."
    mo "Hello? Can you hear me?"
    co "There's something wrong with your line."
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
    play ambience amb_campnight fadein 1.0
    "In the dead of the night, I heard someone rummaging through their backpacks."

    if aston_safe:
        "That's not Aston I'm hearing. He's usually very quiet about it."

    show pearl neutral
    "I sat up to see Pearl frantically packing her gear."

    mo "Pearl, what are you doing?"
    show pearl smile
    pe "Morgan! I, uh...couldn't sleep at all."

    mo "...and the gear?"
    show pearl sad
    pe "...Fine, you caught me... but don't tell the others."
    show pearl neutral

    if aston_safe:
        pe "I'm going to find Lorenzo."
    else:
        pe "I'm going to find them."

    #choice branch
    if aston_safe:
        menu:
            "Let's think about it for a second":
                $ pearl_safe = True
                #aka the treat her like a sensible adult route, tell her that's not possible
                mo "Pearl, no. Think about it for a second."
                show pearl sad
                mo "It's cold, dark and you could get mauled by an animal. I can't let that happen to you."

            "It's dangerous, you won't survive the cold":
                $ pearl_safe = True
                #aka the treat her like a child route, tell her that it won't work and that you don't want her walking out by herself
                mo "Pearl, no. You won't survive out there."
                show pearl sad
                mo "How are you going to find Lorenzo if you don't even know where to begin searching? It's reckless."
        #choice branch ends

        pe "I'm not gonna just stay here, I need to do something."
        pe "One day the search for Lorenzo happens, then it ends abruptly."
        show pearl depressed
        pe "I'm not going to wait till more of us go missing. I can't take it."

        show ast neutral at right
        "Aston wakes up and tries to get a hold of the situation."
        "He gives her a quick pat on the head."
        show ast sad
        show pearl sad
        ast "Pearl, it's gonna be okay. You just have to trust us."
        mo "Pearl, you are brave and kind, and I know you want to help."
        show pearl depressed
        pe "..."
        "Tears welled up in her eyes."
        pe "I wish I could do more."
        show ast neutral
        ast "You're doing enough Pearl. Let's go back to sleep okay?"
        stop ambience fadeout 1.0

    #If Aston not safe
    else:
        menu:
            "Let's think about it for a second":
                $ pearl_safe = True
                mo "Pearl, no. Think about it for a second."
                show pearl sad
                mo "It's cold, dark and you could get mauled by an animal. I can't let that happen to you."
                pe "I'm not gonna just stay here, I need to do something."
                show pearl depressed
                pe "One day the search for Lorenzo happens, then it ends abruptly."
                pe "And now it's happening to Aston."
                pe "I'm not going to wait till more of us go missing. I can't take it."

            "It's dangerous, you won't survive the cold":
            #aka the treat her like a child route, tell her that it won't work and that you don't want her walking out by herself
                mo "Pearl, no. You won't survive out there."
                show pearl sad
                mo "How are you going to find them if you don't even know where to begin searching? It's reckless."
                # pe "I'm not gonna just stay here, I need to do something."
                # show pearl depressed
                # pe "One day the search for Lorenzo happens, then it ends abruptly."
                # pe "And now it's happening to Aston."
                # pe "I'm not going to wait till more of us go missing. I can't take it."
                #straight to pearldeath
        #choice branch ends

    #Pearl survives
        if pearl_safe:
            #If Aston is safe
            if aston_safe:
                mo "Pearl, you are brave and kind, and I know you want to help."
                show pearl sad
                pe "..."
                "Tears welled up in her eyes."
                pe "I wish I could do more."
                ast "You're doing enough Pearl. Let's go back to sleep okay?"
                stop ambience fadeout 1.0


        #If Aston is not safe
            else:
                show pearl sad
                mo "Pearl, you're brave and kind, and I know you want to help."
                show pearl depressed
                pe "..."
                "Tears welled up in her eyes."
                pe "I wish I could do more."
                mo "You're doing enough, but right now you need to get some sleep."
                stop ambience fadeout 1.0


        #Pearl's dead end
        else:
            show pearl confused
            pe "Being calculative hasn't brought anywhere has it now, Morgan?"
            show pearl depressed
            pe "Everyone thinks I'm reckless when I'm just trying to help..."
            mo "That's not what I me-"
            show gr confused at right
            gr "Where's this attitude coming from?"
            show ky confused at left
            ky "Pearl? What's happening?"

            "Gregory and Kyle have been awoken by the sound."

            show pearl sad with move:
                subpixel True
                zoom 0.99
                parallel:
                    xpos 900
            pe "No you stay away. I'll prove you wrong."

            "Shit, not again."
            show pearl neutral with move:
                xpos -300
            with Pause(0.1)
            hide pearl with sdissolve
            show ky shaken
            "With a swift movement, she knocks over the tool rack blocking the flap of the tent."

            show gr angry with move:
                linear 0.3 xpos 1700
            gr "Pearl! Get back here this instant!"

            "Crap, she forgot her compass."
            "Kyle rushes to move the rack out the way while we quickly gear up."

            #EXT: Camp 1
            scene bg camp2_night with dissolve
            show ky shaken at centerleft
            ky "Pearl! Where are you?"
            show gr angry at centerright
            gr "This is not a fucking game Pearl, come back now!"
            "This is all my fault."
            "If anything happens to her, I-"
            "...I won't be able to forgive myself."
            

            #Scene transition: Fade to black > Fade in forest BG
            scene bg forest3 with longfade

            #Pearl's POV
            show pearl neutral
            "The wind picks up tremendously as Pearl trudges through the snow."

            show pearl sad
            pe "Ugh... I knew I should've checked my pockets. Now I'm out here lost and without my compass."
            pe "And here I thought circling the base of the mountain was a great idea."
            #I can ANIMATE THIS (RUMI)
            pe "I look left? Trees and snow. Look right? Trees and snow. Look straight ahead and oh wow! Trees and snow."
            show pearl depressed
            pe "The snow is... unrelenting too. It's cold."
            show pearl neutral
            pe "Come on Pearl! Focus focus!"
            stop ambience fadeout 1.0
            play ambience amb_icebody fadein 5.0

            show cg pearldeath
            $ persistent.gallery_pearldeath = True
            "Pearl finds herself in front of a large forest clearing. Oddly shaped stones stick out from the ground in a disorderly manner."
            "She walks up to one and inspects it up close."

            pe "Oh yeah that's stone alrig-"
            pe "..."

            "It was in fact not stone."
            "Or at least to Pearl."
            "Disfigured and grotesque looking... humans."
            "Frozen in time, freezing the frame of their unfortunate fate."
            "Pearl collapses onto the ground, unable to make sense of what she just saw."

            pe "Nope! Nope nope nope-"

            "After successfully scrambling to her feet, she takes off in another direction."
            "The snow fall gets heavier by the second, and snow blindness makes it worse to navigate the path."
            "But fortunately she was lucky. She squints her eyes to see a large rock wall ahead."

            pe "The mountain! Now I just have to make it back."

            "Pearl starts sprinting towards it, but unbeknownst to her, the terrain ahead was a rather dangerous one."

            pe "Shi-"
            show black with pushupquick
            "Pearl loses her footing and slips down a ravine."
            stop ambience fadeout 1.0

        #@ Sharkie the way it works:
        #If is Aston is present and safe, then Pearl will be safe
        #If Aston is not safe, choosing Let's think about it, Pearl will be safe
        #If Aston is not safe, choosing You won't survive the cold, Pearl skips to death scene

label dec_28:
    scene bg camp2_day with longfade
    play music audio.neutral

    #Gregory's POV
    show gr neutral
    "Gregory is alone at the campsite."
    "Morgan and the rest are out on a search mission again."

    show gr angry
    gr "Pick up damn it."

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
    gr "Plan B it is."

    "Gregory gives up and decides to call the supply crew."
    "They're more likely to pick up."

    ex2 "Now that's a name I haven't seen in months. What do you need?"
    gr "I need you to get our CEO lady on the phone."
    ex2 "Hey if you forgot, I'm just the supply guy."
    ex2 "If you're not here to get stuff like Lorenzo usually does, then I'm gonna hang up."
    show gr angry
    gr "Did she not tell you about Lorenzo?"
    ex2 "Is there something I should know?"
    gr "That damn b-"
    gr "And you've never realized that he's missing?"
    ex2 "Woah there. I'm just doing my job. Lorenzo ain't the only person I deal with."
    show gr neutral
    ex2 "If there's an order, I will complete it. Simple as that."
    ex2 "But no, she never mentioned anything about Lorenzo or whatever."
    gr "Well, let her know that Gregory's calling."
    ex2 "I'll do my best, but no promises."

    show gr worried
    "Gregory exhales deeply."
    "Stuck in this predicament that nobody wants to be in."
    "Knowing the true nature of this operation, and then deceiving the ones that he's working closely with."
    "The choice that he made now affects everyone around him."
    "But to Gregory, it's a necessary burden to bear."
    stop music fadeout 3.0

label dec_30:
    scene bg maintent_night with longfade
    with vpunch
    "*CRASH*"
    "I was rudely woken up by a horrendous noise."
    "What the hell was that?"

    #show ky confused with sdissolve
    ky "Wuh huh?"

    "Seems like Kyle was also abruptly pulled out of dream land."
    show gr neutral at centerleft
    with Pause(1.0)
    show gr neutral with move:
        xpos -100
    hide gr neutral
    "I see Gregory running out the tent to go have a look."
    "At least it doesn't sound like an avalanche this time."

    #EXT: Camp 1A
    scene bg camp2_night with sdissolve
    play ambience amb_campnight fadein 1.0

    "Gregory's Walkie starts beeping the moment I step foot outside."

    show gr neutral at centerleft
    ca "Heya Gregory, I was gonna say that we got the new maps but it seems like we have a new problem."
    ca "Any idea where that was coming from?"
    show gr worried
    gr "My guess is that the radio tower's down."
    ca "Oh that's bad news alright. I'll relay the message to Wilbur and the rest."
    show gr neutral
    gr "Yeah. Thanks."

    "Is that why the signal has been trash lately?"
    "Gregory turns to see the confusion on my face."

    mo "So what I'm getting is that the radio tower crashed?"
    gr "We'd need to check it out tomorrow. Best case scenario is that we can fix it ourselves."
    show gr confused
    gr "Worst case scenario is that we have to wait for backup."
    mo "How long does that usually take?"
    gr "Two weeks."
    mo "Are we basically stranded here?"
    show gr neutral
    gr "Yeah. We've lost contact with HQ."
    show ky sad at centerright
    ky "What if HQ forgets about us?"

    #If Pearl is safe
    if pearl_safe:
        show pearl sad at right
        pe "We could leave camp by ourselves if they don't reach us, right?"
    gr "We'll think about it when it happens."

    scene bg maintent_night with sdissolve
    stop ambience fadeout 3.0
    play ambience amb_intcampnight fadein 1.0
    "I ran back into the main tent to grab my satellite phone."
    "Yep. Signal's completely dead."
    "The gravity of the situation finally sinks in. Which means Colin... he can't reach me."
    "But I'm not too worried, since Colin does have my location."
    "It's just that, well... It'll probably jeopardize the mission."
    "Whoever Gregory is calling at HQ... Guess he won't be able to reach them anytime soon."


    #If Aston is safe
    if aston_safe:
        show ast neutral
        ast "We'll have to check on Lorenzo tonight."
        "Aston, who's also now awake, checks his phone."
        "I should also go to the cabin tonight."
        stop ambience fadeout 1.0


        scene bg cottage2 with fade
        show lorenzo sad
        play music audio.light 
        "We're paying Lorenzo a visit."
        show ast neutral at centerleft
        lo "So the loud crash I heard was real then?"
        ast "Yes, we took a look at the radio tower on our way here. There's a piece missing from it."
        show ast inthought
        ast "Might've been the receiver."
        mo "Has this ever happened before?"
        show lorenzo pondering
        lo "I don't think so, amico. The maintenance crew usually comes in every three months."
        show ast neutral
        ast "We've never had issues prior, so I'm hoping it'll be resolved quickly."
        show ast sad
        ast "How have you been feeling?"
        show lorenzo smile
        lo "The bear is still around, but that's about it. Hasn't been speaking to me anymore."
        "Lorenzo's state seems to be improving."
        "Aston touches his forehead."
        show ast inthought
        ast "I think your temperature seems fine now too."
        show ast happy
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
        lo "So the loud crash I heard was real then?"
        show lorenzo neutral
        mo "The radio tower is broken, yeah."
        mo "Has this ever happened before?"
        show lorenzo sad
        lo "I don't think so, amico. The maintenance crew usually comes in every three months."
        mo "How are you feeling Lorenzo?"
        show lorenzo sick
        lo "I... think it's getting worse."
        hide lorenzo
        "Lorenzo's state is becoming significantly unstable."
        ha "L-Laren... Lorezo... "
        "He seems like he's shaking under the covers."
        "I wish I could do something for him, maybe get Ruran here to check on him while I'm away."
        "I know Aston would've done the same."
        stop ambience fadeout 1.0

label dec_31:
    scene bg forest2 with longfade
    play music audio.neutral
    "The next morning comes."
    show gr neutral
    "Gregory and I are checking up on the radio tower today."

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
    gr "Morgan, I'm going to take a look at the fuse. Mind bringing Davos and Jax over here when they're up?"
    hide gr
    mo "To the midpoint then. I'll meet them there."
    "I beep Jax on the Walkie."

    #If everyone safe
    if aston_safe and pearl_safe:
        #TODO radio start
        $ chibi_jax = "images/chibi/jax_neutral.png"
        wt_ja "Good morning. We're on our way."
        $ chibi_davos = "images/chibi/davos_happy.png"
        wt_da "Just 5 minutes or so left! We'll be there soon."
        wt_mo "The view's great up here guys."
        $ chibi_jax = "images/chibi/jax_happy.png"
        wt_ja "Hell yeah, nice to finally watch you in action, Mr. Rusty with rifles."
        wt_mo "Is that going to be my new nickname?"
        $ chibi_jax = "images/chibi/jax_happy.png"
        wt_ja "Yeah."
        wt_mo "I'm ready to be humbled then, Mr. Great with guns."
        $ chibi_davos = "images/chibi/davos_neutral.png"
        wt_da "What's with the rifle thing? Are you getting private lessons from Jax?"
        wt_mo "I wish."
        $ chibi_davos = "images/chibi/davos_happy.png"
        wt_da "Oh Morgan! I think I see you up there!"
        wt_mo "Nice! Let's meet up at the midpoint in 5."
        #radio ends
        "I look away from my Walkie to see someone waving."
        "It's Davos, I think, since he's the shorter one."
        "They still have a ways to get here."

    #If Pearl is missing
    else:
    #radio start
        $ chibi_jax = "images/chibi/jax_neutral.png"
        wt_ja "Good morning. We're on our way."
        $ chibi_davos = "images/chibi/davos_neutral.png"
        wt_da "Just 5 minutes left. We'll be there soon."
        wt_mo "The view's great up here guys."
        $ chibi_jax = "images/chibi/jax_neutral.png"
        wt_ja "Hell yeah, nice to finally watch you in action, Mr. Rusty with rifles."
        wt_mo "Is that going to be my new nickname?"
        $ chibi_jax = "images/chibi/jax_happy.png"
        wt_ja "Yeah."
        wt_mo "I'm ready to be humbled then, Mr. Great with guns."
        $ chibi_davos = "images/chibi/davos_happy.png"
        wt_da "I think I see you Morgan!"
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
    "..."
    play music audio.anxious
    "I kicked something."
    "Something under the snow, maybe?"

    da "Morgan, we're here!"
    "I heard Davos calling out from behind me."
    "But I'm far too concerned about what I see on the ground in front of me to respond."
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
        ja "The day always turns into an eventful one when I least expect it."
        da "This... looks like a horrible way to die."
        da "I-I'm gonna go call my pops."
        mo "Well then... we're stranded and now there's a dead body."
        mo "What else could possibly go wrong?"

    #If either Pearl or Aston is missing
    else:
        "I'm not ready to identify who it is."
        "Davos turns away from the sight."
        ja "The day always turns into an eventful one when I least expect it."
        da "This... looks like a horrible way to die."
        da "I-I'm gonna go call my pops."
        mo "Well then... we're stranded and now there's a dead body."
        mo "What else could possibly go wrong?"

    scene black with fade
###----------SPOOKTOBER DEMO END----------###
label demo_end:
    show cg endscreen
    "Thank you for playing Undergrowth (demo)!"
    "We have a lot in the works and are working towards the full release!"
    "Please look forward to it!"
    "And with that, we shall leave you with a Happy Spooktober!"
    "- Sincerely, the Undergrowth Dev Team"









