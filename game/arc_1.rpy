label nov_1:

    stop music
    $ save_name = _("Prologue")
    show cg morganhome1
    $ persistent.gallery_morganhome = True

    tv_hi "Glow glow glow with NuGLO, let us help you restore your skin's shiny supple glow!"
    tv_hi "So what are you waiting for? Grab your very own NuGLO samples at your local stores today!"

    $ hidebubbles = True
    scene black
    #Morgan stands up and switches off the TV abruptly, his phone buzzes.

    #Click!
    #SFX
    show cg morganhome2
    mo "Heya."
    co "Got everything you need Morg?"
    mo "Yep, just zipping up here and I'm good to go."
    co "Sure you got everything?"
    mo "Can't fit you in my bag now, can I?"
    #Morgan zips his backpack.
    co "Wouldn't try to even if you asked. I'd rather not be stuck in that for three days."
    mo "Haha, well... I think it's just about time to head off!"
    co "Alrighty then. Bring him home and stay safe, soldier."
    mo "I will."

    #With one final look at his living room, Morgan swings his backpack onto his shoulder and then leaves his apartment.
label nov_4:
    $ save_name = _("Arc 1")
    scene black
    mo "I'm Morgan. Undercover cop and proud member of the Special Operations Division."
    mo "Here on a mission to unravel the secrets behind an operation held by Heralign Inc. far out in the snowy mountains."
    mo "And to find out what happened to my partner in crime."
    mo "He too was tasked to investigate the company and its operations before he was completely wiped off the radar."
    mo "And what does Heralign Inc. do you may ask?"
    mo "Behind that pristine image of a pharmaceutical company, lies Heralign Inc.'s poster business lady."
    mo "Hilda. Hilda Heralign. CEO of Heralign, daughter of some billionaire."
    mo "Why would a company like that set out an operation so far away from HQ?"
    mo "I guess I'm here to find out."
    ex1 "We're here."
    mo "Whew, alright!"
    
    scene bg snowyplain with dissolve
    play ambience amb_campday fadein 1.0

    "A vast stretch of white greets me as I exit the car."
    "The cold wind stings a little as it brushes my cheek. Might take a while before I get used to it."
    mo "Hey thanks for the ride!"
    ex1 "No worries, Gregory should be up ahead waiting for ya."
    "I gaze towards the direction where he pointed, and sure enough, there was an older man waving his hand at me."
    "I slowly make my way towards him. Trudging the snow is a feat for sure."
    "It also doesn't help that I've been in the car for hours on end."
    show gr neutral
    gr "You're Morgan, yes? I'm Gregory. Hope the ride up here wasn't too much for you to handle."
    mo "Well walking in snow is definitely much more difficult than sitting in a car, I think. It's nice to meet you, Gregory."
    "He gives me a firm handshake."
    gr "Let's head to camp."

    scene bg forest1 with dissolve

    "Along the way, Gregory fills me in on the operation and the rest of the people at camp."
    "The Mission? Collecting samples from the environment."
    "Be it sources of water, dirt, trees and maybe foliage once the snow melts."
    "We're basically here to run errands for the scientists here to find new sources of penicillin."
    "The good stuff in antibiotic medication."
    "A.K.A things that Heralign Inc. needs."
    "The Camp. Well there's two camps actually."
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
    gr "Good job keeping up, let me call the others over 'ere."
    play music audio.light
    gr "Everyone gather round 'ere, we got a new recruit!"

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

    pe "Oh my goodness hello! My name is Pearl, it's super nice to meet you!"
    "Pearl, chipper and welcoming. She looks like she's in her early 20s."

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

    lo "I'm Lorenzo! Pleased to meet you!"
    "Lorenzo, he exudes an aura of a gentleman. Looks a little older than me."

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

    ast "Hello, I'm Aston."
    "Aston, quick and concise. Gregory said we're the same age."

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

    mo "Hello! I'm Morgan, thanks for having me."
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

    lo "Sure thing."
    gr "Pearl, Aston, go help Morgan out will ya?"
    pe "You got it sir! I'll show you around Morgan!"
    stop ambience fadeout 1.0
    scene bg maintent_day with dissolve

    "I followed them into one of the bigger tents, it is much more spacious than I thought."
    "A small table, a shelf full of equipment and perishables, and some unlit lanterns on the ground."
    show pearl smile at centerleft
    show ast neutral at centerright
    pe "Welcome to our little cave, we put lots of our equipment in here!"
    pe "The rest outside are all personal tents for all your personal stuff."
    pe "There's extra blankets, flare guns and thingies. Aston organizes everything here cause I always misplace stuff."
    show pearl confused with dissolve
    pe "... I think that's all we needed to show Morgan right?"
    ast "Walkie talkie, Pearl."
    show pearl happy with dissolve
    pe "Oh yes! The Walkie talkie!"
    "Pearl whips out a walkie talkie deep in her jacket pockets and hands it to me."
    show ast inthought with dissolve
    ast "We should probably test it before you head out. Our codes have all been saved, you can reach any one of us anytime."
    ast "Try talking to me."

    #radio selection stuff happens here
    wt_mo "Testing testing, hello hello."
    nvl clear
    show ast neutral with dissolve
    show pearl smile with dissolve
    ast "Alright it works."
    pe "Ooh Morgan, do you wanna try reaching people from other camps?"
    mo "Sure, anyone in particular that I should reach out to?"
    show pearl happy with dissolve
    pe "Davos from Camp 2 and Koda from the Research Centre! They're both my best buds, I reminded them today that we have a newcomer so they should pick up instantly!"
    #choice branch start
    #radio selection stuff happens here
    $ pancake = False
    menu n4_call:
        "Call Davos" if not n4_call_da:

            hide ast
            $ n4_call_da = True
            wt_mo "Hello this is Morgan, is Davos here?"
            wt_da "Oh hello! Morgan, was it? It's nice to meet you!"
            wt_da "I'm in Camp 2, which is a little down south from where you're at!"
            wt_mo "Pleased to meet ya! There's also five of you there, yes?"
            $ chibi_davos = "images/chibi/davos_happy.png"
            wt_da "Haha yes! I'm here with my pops Wilbur, Cassie, Ruran and Jax. They're kinda busy right now though."
            wt_wi "Davos? Could you lend me a hand here?"
            wt_da "Oops gotta go! Talk to you next time Morgan!"
            nvl clear
        "Call Koda" if not n4_call_ko:
            hide ast
            $ n4_call_ko = True
            wt_mo "Hello this is Morgan, is this Koda?"
            wt_ko "Oh! I'm Koda, yes! I heard from Pearl you were arriving today."
            wt_ko "I'm over here at the RC with Eva and Isaak, they're both scientists. They're also both my supervisors."
            wt_mo "Are you not a scientist yourself Koda?"
            wt_ko "Well, not quite yet... but I'm a lab assistant for now!"
            wt_ko "Oh I think I have to go now, Isaak is looking for me. Bye Morgan!"
            nvl clear
    #choice branch end
    if not n4_call_da or not n4_call_ko:
        jump n4_call
    #back to Pearl after calling
    show pearl smile with dissolve
    pe "So how did it go?"
    mo "Walkie talkie works for sure. Thanks Pearl... and Aston?"
    pe "Aston went out to look for Lorenzo and Gregory."
    pe "It's getting late and the sun is going down, I think all that's left is to show you your tent!"
    show bg camp1_night
    "Pearl walks me out to an orange tent, ensures I have all my supplies and then heads to her own for the night."

    scene bg morganstent with dissolve

    "Home sweet home. For the next few months."
    "The sleeping tent is much smaller, but it's enough for me."
    "I waited till the sun fully set, and watched the sky turn dark."
    "The others are in their tents all zipped up, which means it's probably time to update Colin on my whereabouts."

    show satphone
    co "So are you all snuggled in with blankets Morg?"
    mo "Yeah, I'm pretty sure I'll freeze out here if I don't."
    co "Yeah that won't be ideal man."
    mo "Co- Actually no, you don't get to be him now. Hmm... How about Pancake?"
    co "You and Elly I swear... He calls me Pangolin and you call me Pancake. Y'all are not creative."
    mo "It's kinda your fault you know."
    co "It's my kiddo's drawing! Can't pay me to change it."
    co "But anyway, I'm sure you're tired Morg, rest up you hear?"
    mo "Alright alright, goodnight Pancake. I'll catch you later."
    hide satphone
    stop music

label nov_5:
    play music audio.neutral
    scene bg morganstent with longfade
    #INT: Morgan's tent

    "I woke up to the sound of Pearl calling for me outside my tent."
    "Man, do I miss the comfort of an actual bed. My back is still sore from all the traveling."

    pe "Wake up Morgaaannnn. Gregory's about to start!"

    show bg camp1_day with dissolve

    show pearl smile at center

    "I barely had a second to adjust to the sunlight before Pearl dragged me to the center of the campsite."
    hide pearl with dissolve
    show lorenzo smile at left
    show ast neutral at centerleft
    "Lorenzo and Aston are already up, looks like they're making breakfast."
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

    gr "Alright nice, you're up. I'll cut you some slack since it's your first day."
    gr "And because it's your first day here, we gotta make sure you understand the rules."

    "He hands me a booklet."
    "'{i}The Camp Guide's Guide{/i}'"
    "That's not a very creative name."

    show pearl confused at centerleft
    pe "I've been through this a thousand times, do I still need to be here?"
    gr "Yeah...because you need reminding every time you attempt to do something reckless."
    pe "..."
    show pearl sad

    "Gregory runs us through the list of basic camp rules."
    "All of which I'm already familiar with."
    "Time to put that 3 months of camp training knowledge to work."
    "\"Do not interact with animals.\""
    "Sure, I can do that."
    "\"Do not consume berries or plants you see without proper identification.\""
    "The closest hospital is 4 hours away, I won't like that ending."
    "\"Do show up for roll call before sundown.\""
    "A necessary routine yada yada."
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
    "Oh lovely, those sounds like bright red flags."

    gr "Got any questions?"
    mo "Yeah uh... what's with the location specific ones? Wasn't the village to our right yesterday?"
    gr "Well yeah, but I just follow HQ's orders. So it's best we don't try anything funny."
    gr "Heard the villagers there weren't too keen with this whole makeshift camp base situation we're having here."
    mo "And we're not supposed to call anyone from HQ? Unless we get permission from...?"
    gr "That would be me. Easier to have one person to gather reports from, they said."

    "Those were pretty vague answers."
    "But I don't think I should push my luck with the questions for now."

    gr "Alright... Pearl? Any questions from ya?"
    show pearl happy
    pe "Is it time for breakfast? Cause I smell something!"
    gr "..."
    gr "Let's eat I guess."

    "Aston hands us all a breakfast burrito."
    "Pearl's burrito has a ridiculous amount of tomato sauce."


    "The rest of the day was spent on learning how to use camp gear and equipment."
    "Basic first aid."
    "Little survival skills to brave the cold."
    "Nothing too complicated."

    "The days definitely seem much shorter here."
    "Looks like I'll have to get used to not having much daytime for the time being."
    stop music

label nov_6:
    #INT: Morgan's tent
    scene morganstent with longfade

    "Nice, I woke up on time."
    "Today is sample collection day. Wouldn't want to miss that."
    "Wonder what that's all about?"
    "I should go look for the rest."

    scene bg maintent_day with dissolve
    show lorenzo pondering
    "As I entered the tent, I saw a lone Lorenzo scribbling away at his notebook."
    "The rest were outside around the campfire. Preparing breakfast."

    mo "So how's your morning going?"
    lo "Just liaising with the supply crew at HQ. A financier's job never ends until everyone gets supplies."
    lo "And as you may notice... I'm not exactly fit to be a camp guide. So this is the best I can do."
    mo "Nah, I wouldn't have guessed."
    show lorenzo smile
    lo "You flatter me Morgan. Aston, on the other hand, would've been a much better fit."
    mo "But he chose to be a field medic?"
    lo "Many ways to help others he said, plus being a medic means that we get to spend more time together."
    mo "That's awfully cute."
    show lorenzo happy
    "Lorenzo beams at me."
    "I wonder how long they've been together."
    "Our conversation was interrupted by Gregory calling us over to gear up."
    "Alrighty, I guess it's time."


    scene bg forest3 with dissolve
    play ambience amb_campday fadein 1.0
    show gr neutral at centerright

    "Gregory begins by going through a long checklist of items to collect for the day."
    "He hands Pearl and I some bags and tools."
    show pearl neutral at centerleft
    gr "Alright. The plan is simple. We go out, grab dirt samples, and then I'll send them back to the lab."
    gr "Today... let's see... We'll start by gathering some over 'ere."

    "Holding the map up, Gregory points to a location marked by his pens."
    "This is the first time I've seen the full picture, I wish I could get one myself but it seems like they ran out of maps."
    "The ones in the main tent haven't been updated since summer. The terrain looks entirely different from what we're dealing with now."

    mo "So I reckon Camp 2 does the same?"
    gr "Same tasks, different area. Environmental study or some shit. I'm not exactly the guy to ask, but if that helps the research team, I ain't complaining."
    show pearl smile with sdissolve
    pe "Never thought I'd be excited to play with dirt again."
    gr "Please don't tarnish the samples with your hands."
    show pearl sad with sdissolve
    pe "Okaaay."
    hide gr with dissolve
    hide pearl with dissolve
    "Snow and dirt. Alright let's see."
    "Scoop."
    #Scoop SFX

    "To my eyes, it looks like plain old dirt."
    "Not gravelly, just wet cold soil with no bugs in it."
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

    pe "Morgan!"
    show pearl happy with sdissolve

    "That made me jump."

    mo "Goodness, you scared me."
    pe "Heh, want some water or snacks?"
    mo "That would be nice, thanks Pearl."
    show pearl smile with sdissolve
    "She hands me a small box of trail mix and a flask filled with water."

    mo "So how long have you been here Pearl?"

    pe "Actually I've only been here for two months! Just a little later than Davos and Koda at least."
    pe "Met Davos at the academy waaaay before and he introduced me to Koda! I kinda miss them now though."
    pe "Gregory's usually the one in charge of delivering stuff, especially during the stormy season. So I haven't seen them in two weeks."
    mo "You've never followed him to the RC?"
    pe "Not really, I prefer staying at camp than riding the snowmobile. Motion sickness ain't my best friend so..."
    mo "Snowmobile?"
    show pearl happy with sdissolve
    pe "Yeah the one that goes vroom vroom but in snow! Gregory has one, I don't remember where he parks it though, it's a tiny walk from camp."

    "That's interesting to know."
    hide pearl with dissolve
    "I finished up the remainder of my trail mix, and got back to work."
    "Gregory seems pleased with my reports."
    "Not bad Morgan, maybe I am suited to be a camp guide."
    stop ambience fadeout 1.0

label nov_7_11:
    #7th
    play music audio.light
    scene bg waterbody with longfade

    "Another sample collection day."
    "Today we're breaking some of the ice at the lake."
    "As we approached the body of frozen water, Pearl almost slipped on the ice."
    "I'm not sure if it's my imagination, but the lake looks like it has a slight tinge of green hues."
    "Science ain't my forte anyway. I guess if the water is green, then the water is green."
    show pearl smile at centerleft
    show gr neutral at centerright
    gr "Pearl could you get me the-"
    show pearl happy
    pe "The pick? I got it sir!"
    gr "No the-"
    pe "OH the ice saw thingy? Here you go sir!"
    gr "..."
    gr "Actually Pearl... I just want the checklist."
    pe "You got it!"

    "Gregory seems like he's having a great time."

    #8th
    #INT: Main tent
    scene bg maintent_night with longfade

    "After a long day, Aston decided that we should have canned soup for tonight."
    "He walks over to Pearl and hovers two different flavors in her face."
    show cg tomatosoup with sdissolve
    $ persistent.gallery_tomatosoup = True
    ast "We have tomato soup and.. pea soup. Which one do you want?"
    pe "Hmmmm..."
    pe "..."
    ast "Well?"
    pe "I kinda want to try pea soup today but..."
    ast "Alright, tomato it is."
    pe "Hehe."

    "Judging from his reaction, he hates pea soup, doesn't he?"

    #9th
    #INT: Main tent
    scene bg maintent_day with longfade

    "Lunch time, time to grab a quick snack from the food shelf."
    "I noticed Lorenzo was in the midst of counting meat and potato meal packets."
    show lorenzo pondering

    lo "46... 47... 48..."
    lo "Oh wait, where did I put my pen...? Ah!"
    show lorenzo smile

    "Lorenzo found his pen, but at what cost?"
    show lorenzo neutral
    lo "..."
    mo "You stopped at 48."
    show lorenzo smile with sdissolve
    lo "Oh! Thank you Morgan. 49... 50... 51..."
    show lorenzo pondering with sdissolve
    lo "57? That's not nearly enough for a month! I'll need to call support."
    mo "Isn't 57 plenty?"
    lo "Not if Gregory and Aston keep inhaling them so quickly."
    mo "I have to agree that it's probably the best thing we have."
    lo "Si amico. So 57 isn't nearly enough."

    #10th
    #EXT: Camp 1
    scene bg camp1_day with longfade

    "While on the way back to my tent. Gregory looks like he's about to go to the RC on his snowmobile."
    show gr neutral
    "Never actually paid attention to how cool it looks."
    "Maybe I should demand one from Colin."

    gr "Isaak, samples are coming in about 30 minutes. Do you need anything else?"
    isa "No, that'll do. I'll have Koda retrieve it for me later."
    gr "You're really working that kid to the bone huh?"
    isa "They're helpful. I don't see why not?"
    show gr angry with sdissolve
    gr "You're an ass you know that?"
    isa "..."
    gr "Alright I'll be on my way."

    "They're not friends. Noted."

    #11th
    #INT: Main tent
    scene bg maintent_day with longfade

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
                wt_wi "Hello Morgan! I heard lots about you from Pearl and Davos!"
                wt_mo "I'm surprised you already knew about me, they sure are close."
                wt_wi "Well yes! News travels fast around here lad! Oh Ruran my friend, would you like to say hi?"
                wt_ru "Is it Morgan? It is nice to meet you Morgan, I'm Ruran."
                wt_mo "Oh the other camp medic? Aston told me that you're his mentor."
                wt_ru "Yes I am. He's great, and it's always nice to have extra hands in case of emergencies."
                wt_wi "Hope Aston will warm up to you soon, that boy has always been a man of few words. Know him long enough and you'll realize he's a big softie!"
                wt_mo "'Aston' and 'softie' were two words I never expected in the same sentence, but thank you for telling me."
                wt_mo "I'll let y'all go for now, tell Davos I said hi!"
                wt_ru "Call us anytime Morgan!"
                wt_wi "If only this darn wind would let up, I'd love to meet you in person soon!"
                nvl clear
            else:
                "I don't think I need to do that now."

        "Beep Cassie":
            if not wt_intro_ca:
                $ wt_intro_ca = True
                wt_ca "What a coincidence! I was just about to beep ya! I'm Cassie!"
                wt_mo "It's nice meeting you Cassie, I'm Morgan."
                wt_ca "Well I just want to let you know that I have a map ready for you! The next time Lorenzo or Gregory comes by, I'll have them be our courier pigeon."
                wt_mo "Thanks! I appreciate it!"
                wt_ca "Anytime Morgan!"
                nvl clear
            else:
                "I don't think I need to do that now."

        "Beep Jax":
            if not wt_intro_ja:
                $ wt_intro_ja = True
                wt_ja "Yeah, is this the new guy?"
                wt_mo "Hi Jax, I'm Morgan. Just thought I'd check on everyone."
                wt_ja "That's nice of you."
                wt_ja "Just doing a routine cleanup on my rifles, nothing much."
                wt_mo "Oh nice, didn't know we had rifles at camp."
                wt_ja "You know how to handle one?"
                wt_mo "I'm a little out of practice."
                wt_ja "Usually people say that to sound humble."
                wt_mo "Nah. I am actually pretty rusty."
                wt_ja "We'll have to see about that."
                wt_mo "Bet."
                nvl clear
            else:
                "I don't think I need to do that now."

        "Beep Isaak":
            $ wt_intro_isa += 1
        #Isaak won't pick up the first or second time
            if wt_intro_isa <= 2:
                "Nothing. There doesn't seem to be any response."

        #beeping Isaak for the third time
            elif wt_intro_isa == 3:
                wt_is "This better be an emergency."
                wt_mo "Not really. I'm just calling to say hi."
                wt_is "I'm Isaak, you're Morgan. I don't like small talk nor do I like people who try to make me engage in small talk."
                wt_is "Goodbye."
                nvl clear

            elif wt_intro_isa == 4:
                "Isaak stops responding to you."
                "Rude."

            else:
                "I don't think I need to do that now."

        "Beep Eva":
            if not wt_intro_ev:
                $ wt_intro_ev = True
                wt_ev "Yes?"
                wt_mo "It's Morgan, just thought I'd call to say hello!"
                wt_ev "Ah yes, the new guy. I'm Eva, I think Koda already told you."
                wt_ev "I can't talk for long though. Gotta run some errands."
                wt_mo "I'll leave you to it then."
                nvl clear
            else:
                "I don't think I need to do that now."

        "Beep Ruran":
            if wt_intro_ru == 0:
                $ wt_intro_ru += 1

                "Oh, well. It looks like her Walkie may be charging right now."

        #beep Ruran after the first beep
            else:
                "Probably still charging."

        #everyone has to be called once, if not the player shouldn't be able to leave the selection screen
        "That's everyone" if wt_intro_ca and wt_intro_ev and wt_intro_isa >= 1 and wt_intro_ja and wt_intro_ru == 1 and wt_intro_wi:
        #exit radio to end branch
            nvl clear
            jump wt_intro_end
        #choice branch ends
    if not wt_intro_ca or not wt_intro_ev or wt_intro_isa < 1 or not wt_intro_ja or wt_intro_ru < 1 or wt_intro_wi:

        jump wt_intro

    label wt_intro_end:
        "I think that's all of them."
        "Wilbur, Davos' father. Like Gregory, a senior camp guide. Friendly and welcoming."
        "Ruran. The camp medic. She seems like a nice lady."
        "Cassie. I assume the cartographer. Also nice."
        "Jax. Another senior camp guide I think. Sounds like he knows his stuff about weapons."
        "Eva. Koda's senior at the RC. She seems busy."
        "Isaak. Also at the RC. That's really all I know for now."
        "That brings us to a total of 12 people here."
        "I should update Colin when I have the chance."
        stop music

label nov_12:
    #EXT: Village
    scene bg village1 with longfade
    play ambience amb_village fadein 1.0
    #Kyle's POV
    show ky smile at centerleft with dissolve
    ky "Just one more shot of y'all together... yep, that's cute!"

    "Click click!"

    ky "One more... and done!"

    v1 "I wanna see, I wanna see!"
    v2 "Susie's so pretty, thanks for this Mr. Kyle!"
    show ky happy
    ky "Kyle is just fine! And you're welcome!"
    vs "Moo."

    ky "Do you want a portrait of just yourself Susie?"
    vs "Moo!"
    hide ky
    show bg village1_kyle with sdissolve

    "Kyle rolled up his sleeves and got to work."
    "Click click click!"

    ky "Here you go Susie!"

    "Kyle tilts his camera towards Susie."

    vs "..."

    "Susie studies her portrait."

    v1 "What's wrong Susie?"
    
    ky "Was it... not to her liking?"
    v2 "Are you okay?"

    "The kids start petting Susie's back."
    "Kyle reached out his hand to pet Susie's head, but before he could even reach her-"

    "CHOMP"
    show bg village1 with sdissolve
    show ky shaken
    "Susie bit his forearm."

    vs "Moooo!"
    ky "Owwie."
    v1 "Haha! It means Susie likes it! She's happy."
    show ky confused
    ky "I'm not sure if that's normal cow behavior."
    v2 "Did it hurt Mr. Kyle?"

    "Gazing down at his forearm, it seems like Susie's bite managed to break the skin."
    "It's red, but it doesn't hurt that much."
    "Simple first aid should do the trick."

    show ky smile
    ky "I think I'll be alright!"
    vs "Mooo..."
    show ky happy
    ky "Apology accepted Susie!"

    "Kyle reaches out again, this time with his sleeves down."
    "Achievement unlocked, he pets the cow!"
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

    "It's been roughly a week since I've been here."
    "Everything seems normal, perhaps a little too normal."
    "Collected samples again earlier this afternoon."
    "Dinner ended two hours ago and everyone is about to head to bed soon."
    "I don't feel sleepy yet."
    "I think I'll just walk a circle around camp."

    scene bg camp1_night with dissolve

    "Night walks are my happy place."
    "The scenery is different than in the city, but at least the air is fresher here."
    "Quiet city to quiet campsite."
    "City lights to the lanterns and stars."
    "My sneakers to snow boots."
    "Only thing different is that Elly isn't here."
    "He'd join me sometimes. I miss that."
    "I wish he'd just-"

    show gr neutral

    gr "I understand ma'am, but that's not possible."
    play music audio.anxious


    "Oh, is he on the phone?"

    gr "We'll have to wait till the lake unfreezes."
    hi "So nothing new to report? It's getting pretty boring Gregory."
    gr "I can't move mountains nor change the seasons."
    hi "What about the boy? The coppers would've been onto it by now."

    "Hey, that's me."

    gr "What boy? What d'ya mean?"
    gr "You told me to take care of 'em, but Isaak insisted on helping me out."
    hi "And you never questioned him?"
    gr "Look, you hired the guy, not me. And you told me to work with him."
    gr "I never had a choice."
    hi "And you never will until you get this done. Remember what's at stake here Gregory. I am not repeating myself."
    gr "Okay, okay. If pressure is what you want, I'll do it."
    hi "Find him. I don't want to be the one playing clean up every time."

    "Whoever he's talking to sounds full of themselves."
    show gr angry
    gr "Her? Playing clean up? What a load of bullshit. I'm the one here cleaning up every damn time."

    hide gr

    "I hope he ended the call before he said that."
    "Looks like the night walk did yield some great intel."
    "Someone Gregory and Isaak report to."
    "And a boy... Elly?"
    "Nope. I'm not gonna think about the worst case scenario just yet."
    "Let's head to bed."
    stop music


label nov_14:
    #INT: Morgan's tent
    scene bg morganstent with longfade

    "WRRRRRRRR"

    "What in the world was that?"
    "Is it coming from the radio?"

    #EXT: Camp 1
    scene bg camp1_day with dissolveh
    play ambience amb_campday fadein 1.0

    show lorenzo sad with dissolve

    lo "Oh Morgan, good morning!"

    "Lorenzo greets me as I crawl out my tent."
    "A worried expression plastered on his face."

    mo "I take it that there's bad news?"
    lo "Snow storm warning. Looks like we have one coming real soon."
    mo "Any idea when that'll be?"
    lo "Could happen in a matter of the next few hours, could happen in a day or two."
    show gr neutral at right
    gr "Anyhow we should start preparing ourselves. I'll give Wilbur a call."
    mo "I suppose we should also do our part yeah?"
    show ast neutral at left

    "Aston hands me a hammer and some ropes."

    ast "Help me secure the tents to the trees."
    show lorenzo with move:
        xpos 700
    lo "Amore, I've locked the supply crates, anything else you need me to do?"
    ast "Could you help me keep the crockpot away? Thank you."
    show pearl smile at centerright with sdissolve
    pe "Man, imagine if the wind blows and we all end up flying. That would be horrible!"
    lo "Don't put that image in my head Pearl, that's terrifying."
    show pearl sad
    pe "Sorry."

    "With the tents fully secured, we went about our day at the campsite."
    "Can't collect samples when there's a storm that could strike at any moment."
    "Roll call happened much earlier today, and everyone went back to their respective tents to hunker down for the night."
    "This would probably be a great time to call Colin for updates."
    stop ambience fadeout 1.0

    scene bg morganstent with fade
    play ambience amb_campnightwofire fadein 1.0

    show satphone
    mo "How's my Pancake doing?"
    co "Doing great Morg. Any updates?"
    mo "Well one thing's for sure, Gregory reports to someone higher up in Heralign."
    mo "I can't say it's Hilda for sure, but he seems inexplicably respectful. A little out of character."
    co "I'd say it's a possibility, yeah."
    mo "And it looks like there's a lot more people than when Elly was last here."
    co "A bunch of new faces, eh? Tell me more."

    #players only get one choice to pick
    menu:
        "Tell Colin about the people at Camp 1":
            mo "There's five of us in C1, think you probably haven't heard of someone named Pearl. She's new, just like me."
            co "Oh she's definitely new alright."
            mo "She's a silly one, I doubt she's involved in anything messy."

        "Tell Colin about the people at Camp 2":
            mo "There's five in C2, though I haven't actually met them in person yet. Don't think I'll be able to anytime soon."
            co "We have one new guy huh? In Elly's notes I've got a Wilbur, a Jax, a Cassie and a Ruran."
            mo "That would mean you're missing Davos, Wilbur's kid."

        #choice branch ends
        #phone ends

    "*rustle rustle*"

    "Was that from outside?"

    menu:
        #choice branch starts
        "Tell Colin goodnight":

            mo "Alright daddy's tired, you better go get some sleep too Pancake. Listen to mommy okay?"
            co "Wha-"

            "I hung up on Colin."
            "Last thing I want is someone eavesdropping on me."
            "I paused to listen, but the sound doesn't seem to happen again."
            "I should text Colin real quick."
            "\"Sorry. I thought I heard someone outside.\""
            "Ding!"
            #SFX
            "\"Oh yeah, better be safe than sorry. Updates for another time then.\""
            hide satphone
            "I guess it's time to hit the bed."

        "Check outside":
            hide satphone
            mo "One moment."

            "I unzipped my tent just enough to peer outside."
            show black
            "Pitch black. Can't see shit."

            "rustle rustle"
            #SFX

            mo "Who's there?!"
            show gr neutral
            "Out from the shadows comes Gregory."
            "Crap."

            gr "Sorry kid, did I wake ya? Just taking a quick piss."
            mo "Nah, you're good. I'm gonna head back to bed."
            hide gr
            hide black
            "I zipped my tent up quickly."
            "Looks like Colin hung up on me."
            "\"I am okay. Gregory was outside.\""
            "Ding!"
            #SFX
            "\"Aight careful out there Morg.\""
            "I guess it's time to hit the bed."

            #choice branch ends
    stop ambience

label nov_15:
    #INT: Morgan's tent
    scene bg morganstent with longfade

    "Another day, another round of sore backs."
    "I don't think I'll ever get used to sleeping on packed snow."
    "But it looks like the storm didn't hit us last night."

    scene bg camp1_day with dissolve
    #EXT: Camp 1

    "For once, I'm the first one up today."
    "Aston and Lorenzo are usually the earliest."
    "Followed by Gregory."
    "And then it's always a battle between Pearl and I."

    show bg maintent_day
    #INT: Main tent

    "I guess I could go snoop around in the main tent for a bit."

    menu:
        "Check the food shelf":
            "Meat and potatoes. Love that."
            "Canned soup. 80\% of these are tomato flavored. I think I already know why."
            "Instant rice meals. Maybe I should request some today."
            "Instant noodles. I eat that way too much at home."
            "Different kinds of jerky. Would love those if they weren't so hard to chew."
            "Freeze dried fruit and vegetables. Healthy."
            "I'd say this shelf is pretty well stocked."

        "Check the weapon and tool rack":
            "Knives, picks and axes."
            "Pistols and pistol ammo."
            "Flares and... nothing much."
            "Jax said that they have rifles in C2."
            "Is this unfairness I smell?"

    #choice branch ends

    "I turn to the large table in the middle that we use for meals if we're not outside near the campfire."
    "Think Lorenzo uses it the most if not for meals. Lots of writing and calculations he needs to do for his job."
    "And what do we have here?"
    "There are documents strewn across the table, they weren't here last night."
    "Huh?"

    play music audio.anxious

    "These are... Everyone's profiles?"
    "Name: Pearl"
    "Age: 24"
    "Gender: Female"
    "Status: Uninfected"
    "Uninfected?"
    "That's an odd way to label someone."
    "Would Elliot's copy be in here then?"

    menu:
        "Dig through the documents":
            $ dig_thru_docs= True
            "Name: REDACTED"
            "Age: REDACTED"
            "Gender: REDACTED"
            "Status: Infected"
            "Well, reading that makes me suuuper comfortable."
            "There are multiple people with similar profiles like these, and their pictures have been torn out too."
            "No sign of Elliot. I really hope he's not one of them."
            "Better clean this up real quick."

        "Don't dig through them":
            "Someone left it out here, and that someone might find out I'm snooping."
            "It's best to think about it for a second."
    #choice branch ends

    "Whatever those records are, if people at camp have one, then I'll most likely get one too."
    "I'd much rather stay healthy thanks."

    show ast neutral with sdissolve
    ast "Morgan?"

    "Crap, that scared me."

    mo "Morning Aston, was just thinking about what to eat for breakfast. Slept well?"

    ast "Yes. What were you looking at?"

    "Uh oh."

    mo "Well, I'm not sure who left these here and I was gonna just keep them away to make space for breakfast."
    show ast inthought
    ast "I think that might be Gregory's. Pearl's still asleep, Lorenzo was with me and you found them here."

    "Gregory's... huh, what's he doing with everyone's records?"
    show ast neutral
    ast "Is something wrong?"
    mo "Nothing, I think I just woke up on the wrong side of the bed."

    "Aston takes a moment to read my expressions."

    show gr neutral at left
    gr "Oh, up early are we?"

    "Gregory's voice booms from behind Aston."

    ast "Gregory did you leave these here?"

    show gr angry
    "A slight uneasiness coming from Gregory's hurried footsteps could be heard."

    ast "We were just about to go look for you. Morgan and I were deciding what to eat for breakfast."
    show gr neutral
    "Almost instantaneously, Gregory's face softened from relief."
    "Aston covered for me. I shall remember that."
    "He didn't have to lie."

    mo "Anything you'd like in particular Gregory?"
    gr "I'll leave it up to you guys."

    show gr with move:
        xpos -200

    hide gr
    "He quickly grabbed all those files and went back to his tent."
    "Major alarms are blaring in my head."
    "Aston and I share glances for a moment, before he decides to go on about his daily routine."
    "He doesn't question me, nor does he ever bring it up again for the day."
    stop music

    scene bg camp1_day with dissolve
    #EXT: Camp 1

    "The records have been occupying my mind all day."
    "At least there's meat and potatoes for tonight for a temporary distraction."
    "Can't solve cases on an empty stomach."
    show lorenzo pondering at centerleft
    lo "Morgan, are you feeling alright? You haven't been touching your food."
    mo "The food's great Lorenzo, I just have a headache."
    show pearl smile at centerright
    pe "Aston should have some meds for that! I can go get them for-"
    show pearl neutral
    "A strong gust of wind begins to pick up, cutting Pearl's sentence short."
    "The campfire embers dance violently around the pit."

    "WRRRRRRRRRRRRR"

    "Oh that's bad news."
    "The radio turns on."

    ev "Hello? I sure hope you guys can hear me."
    ev "Snowstorm's happening, if you're outside get in, like, RIGHT now."

    "I didn't know Eva did weather reporting too."

    gr "You heard her! IN. NOW."

    "Oh fuck."
    "They weren't kidding when they said snow storms mean business in these parts."
    scene bg maintent_day with dissolve
    "Each one of us sat in a corner of the main tent. Holding it down with our body weight."
    show gr angry at centerleft
    gr "Everyone hold tight, lest we start flying!"

    "If anyone were to move, I feel like we would actually start flying upwards."
    "I'm glad we secured the tents yesterday. Getting hit like this without warning? Lethal for sure."
    "But I wonder how those ropes and weighted bags will fare in this storm."
    "It would be a problem if my tent flies, I can't let anyone read my journal."

    #SFX wind dies down

    "I don't know how much time has elapsed."
    "It's still snowing outside, but it would seem that the storm finally decided to calm down."
    show pearl sad at left
    pe "Is everyone okay...? Are we okay?"
    show gr neutral
    gr "Looks like it, everyone is still in one piece, aye?"

    "Lorenzo is already on his Walkie, checking in on Camp 2."
    show lorenzo pondering at centerright
    lo "Everyone okay? We're safe here I think!"
    ru "We're all safe too! Cassie got a tiny cut from falling but she's okay now."
    da "That was some wind wasn't it? Hope none of your tents flew away."
    show ast inthought at right
    ast "We should call the RC too."
    mo "I'll do just that."
    ast "Alright, I'm going to check outside for a bit."
    hide ast
    hide pearl
    "Pearl follows Aston outside."
    "I should beep Eva."

    #radio selection stuff
    menu:
        "Beep Eva":
            wt_mo "Eva! Is everyone at the RC okay?"
            wt_ev "The three of us are fine. We're the ones with a roof here, we should be asking if you're okay."
            wt_mo "We're okay. And it sounds like Camp 2 is alright too!"
            wt_ko "Thank goodness... Update us if anything happens okay?"

            pe "Noooooooo! My tent collapsed."

            "Pearl's voice could be heard coming from the outside."

            wt_mo "Well... If you heard that, that's the update I guess. Pearl's tent collapsed."
            wt_ko "O-Oh no, poor Pearl."
            wt_ev "You don't sound all that sorry for her Koda."
            wt_ko "I am, it's just... It's very Pearl of her."
            wt_ev "It looks like the storm actually did some damage."
            wt_ev "Anyway, I'm sure you're busy Morgan, help the girl out will you?"
            nvl clear
            #radio selection stuff end

    scene black with dissolve

    "The night ended after we did a round of damage inspection."

    scene bg morganstent
    "Looks like everything is okay in my tent."
    "Pearl's going to be sleeping in the main tent for the night."
    "Surviving a snowstorm, huh? Well, that's one check off my extreme bucket list."
    "Now I have a reason to demand a snowmobile from Colin."

label nov_16:
    #EXT: Camp 1
    scene bg camp1_day with moveindissolve
    "The next day after the storm, we got to work rebuilding the campsite."
    "Other than fixing Pearl's tent, we've got some shoveling to do, the snow piled up real high and we lost our campfire."
    show pearl sad at centerright
    pe "Still can't believe it was my tent of all things. Now I need to redecorate again."
    show lorenzo smile at centerleft
    lo "I'll help you out Pearl, don't worry!"
    show pearl happy
    pe "Grazie, Lorenzo!"

    hide pearl
    hide lorenzo

    "Dig dig digging, this is a lot of snow. We'll be here all day."
    "Lorenzo said that they once had to deal with fallen trees, it was not a fun experience."
    "Snow is much easier to remove, so I appreciate the lack of trees."
    "Gregory went towards Camp 2 earlier, checking for trees. Maybe I should also do the same facing north?"

    show bg forest1
    "Well no fallen trees but...?"
    "Wait, is that an igloo? It's too perfectly shaped to be natural."

    mo "Guys... I'm going to be back real quick. I see something up ahead."

    "Definitely not natural, it even has a little entrance."
    show cg meetingkyle
    $ persistent.gallery_meetingkyle = True
    play music audio.light

    ky "Hello!"

    "An unfamiliar face greets me as I approach the igloo-like structure."

    ky "Oh, geez, the snowstorm yesterday was rough, huh? My tent ended up flying away last night!"
    mo "Wait you're telling me you spent the night in... that?"

    "I gesture towards the igloo."
    hide cg meetingkyle
    show ky smile
    ky "Looks pretty neat huh? I made it myself! It's cold but it does the trick."
    ky "I wouldn't want to do that for another night though."
    ky "Say, do you happen to have more tents?"
    mo "I'm not sure but I could go check?"
    ky "That would be awesome sauce! Oh wait, where are my manners? I'm Kyle, nice meeting you out here!"
    mo "Morgan, nice meeting you too. Why were you out here alone anyway?"
    show ky happy
    ky "Long story short, I'm a wildlife photographer! I'm on a solo expedition to capture the animals around here."

    "He proudly raises the camera hanging around his neck."

    ky "So like 2 days ago, I was at the village up north. Met the locals, some farm kids, and then I also got bitten by a cow. Pictures turned out great though!"
    mo "A cow? Looks like you had an eventful day. The villagers were friendlier I hope?"
    ky "Oh yes, super friendly and they actually offered me to stay with them, but I thought it'd be counterintuitive to stay there with farm animals when I'm looking to find wild ones."
    ky "They gave me extra blankets as a parting gift! I'd be a goner without them last night."

    "Friendly huh? Gregory said they didn't like outsiders. Maybe they just hate us in particular?"

    mo "Well it's a damn miracle that you're still talking. Wanna follow me back to camp? Can't leave you out here by yourself."
    ky "Aww yeah thank you, that'll be great!"

    scene bg camp1_day with dissolve

    mo "Heya guys, I'm back with a new friend."
    show ky smile:
        xpos 650
        yalign 1.0

    ky "Hellooo! I'm Kyle!"
    show gr neutral:
        xpos 1000
        yalign 1.0
    "A frown forms almost instantaneously on Gregory's face upon seeing the two of us."
    show pearl happy at left
    pe "Helloooo! I'm Pearl! This is Aston, Lorenzo, and Gregory!"
    show ky with move:
        xpos 300
    show gr with move:
        xpos 650
    show lorenzo smile:
        xpos 1000
        yalign 1.0
    show ast neutral at right

    "I have a feeling Pearl and Kyle will get along just fine."

    gr "Where did you come from, son?"
    ky "Oh, just up ahead! I was camping in a tent before it flew away last night."
    show pearl happy
    pe "YES! I'm not the only- uh I-I mean, {nw}"
    show pearl sad with None
    extend "that really sucks. Where did you end up sleeping?"
    mo "You're not gonna believe it."
    ky "A man made igloo."
    show ast inthought
    ast "All igloos are man made."
    ky "Oh damn you're right. I took some pictures, wanna see?"
    show lorenzo sad
    lo "Santo cielo, you survived the night in that?"
    ky "Yeah! I was at the village two days ago and they gave me blankets! Thanks to them, I survived the cold!"
    ky "Then I also got bitten by a cow named Susie. Which reminds me, do you guys also have extra bandages?"
    show ast neutral
    ast "Let me have a look at it."
    show lorenzo smile
    lo "Aston here is our camp medic! He'll fix you right up."

    gr "So how long do you plan on staying?"

    "Gregory asking the important questions here."

    ky "I was wondering if you had extra tents that I could borrow? I wouldn't want to just impose myself here."
    lo "I don't think we'll have any extras until next month."
    gr "I guess you'll have to leave then."
    show ky shaken
    ky "Oh, but please sir Gregory, if I could just have a few days of your time? I really can't afford to leave the mountains when it took so much for me to get up here."
    ky "I just need some time to capture all the wildlife here."
    pe "I can give you my tent! Then I could sleep in our main tent."
    show ky happy
    ky "Really? Thank you Pearl!"
    show gr angry
    gr "I didn't even-"
    ky "Thank you to the rest of you too! Once I get the photos I need, I'll leave the camp. I promise I won't interfere with your... vacation?"
    gr "We're working here. It ain't a vacation."
    ky "Cool cool! If you need anything at all, please do ask. I'd like to be helpful especially since I'm gonna be crashing here for a while!"
    ast "We should treat the cow bite first."
    ky "Ah yes! Totally forgot about that."

    scene bg camp1_day with dissolve
    "Snow shoveling day turned out to be much more eventful than we expected."
    "But now I am worried about dragging another civilian into a mess whose depth even I'm unsure of."
    "Sounds like I made a bad choice, but the only other option was to leave him to fend for himself."
    "I'm sure it'll be fine for now."
    stop music

label nov_17:
    #INT: Main tent
    scene bg maintent_day with longfade
    "It's been three days since we were stuck at camp."
    "Lorenzo and Gregory said that they'll be sending in new samples together. The batch we accumulated over the days was a little too much for one person to handle."
    "While Aston, Pearl and I were tasked to reallocate food portions for an extra person and reset camp to its original form."
    "Which means rebuilding the campfire, fixing our crockpot stand and restabilizing the main tent because Pearl heard creaking in one of the legs last night."
    "Kyle was a freebird. Without a map, it'll be hard to navigate around here."
    show ky smile at left
    show gr neutral at centerleft
    ky "Heya, do you need some help?"
    gr "No, not really. Go bother someone else, will ya?"
    ky "I could help you guys with heavy stuff? Delivering? Lifting?"
    show ast neutral at centerright
    show lorenzo smile at right
    ast "You could head to Camp 2 and grab us some food, an extra mouth to feed after all."
    show ky happy
    ky "Sure! Leave it to me!"
    show ast confused
    ast "Camp 2 is pretty far by foot, are you sure?"
    show gr confused
    gr "The snowmobile can fit two people, so unless you'd like to be dragged like a ragdoll along with our other supplies, walking is the way."
    ky "I mean sure! You guys know what's best."

    "The bewilderment on Gregory's face is loud."
    show gr happy
    gr "We'll give you a lift then. Come outside in 5."

    lo "Think I have everything I need. I'll see you later, amore. Bye friends!"
    hide lorenzo with dissolve
    hide gr with dissolve
    show ast neutral with move:
        xalign 0.5
    "Lorenzo bids Aston and us farewell and follows Gregory outside."
    show ky smile
    show pearl smile at right
    ky "I forgot to ask if they had helmets."
    pe "I'm sure you'll be fine Kyle."

    #INT: Main tent
    show black
    hide ky

    "We made lots of progress within two hours."
    "Tent? Fixed. Crockpot? Fixed."
    "Reorganized the shelves and storage? All done."
    "The camp has been restored to its former glory."
    hide black
    show pearl happy
    pe "Great work guys! We did amazing!"

    #Cassie beeps you
    "Beep!"
    "Oh, it looks like I've got a message."
    wt_ky "Woah Cassie does this mean he received it?"
    wt_mo "Loud and clear Kyle."
    wt_ca "Haha hello Morgan! I was just teaching him how the Walkie works, we happened to have a spare!"
    wt_ca "And it looks like we have a different courier pigeon. I'll get Kyle to deliver your map tomorrow!"
    wt_mo "Sweet! Thanks again Cassie, hope the new pigeon doesn't cause you too much trouble."
    wt_ca "Oh, I'm gonna put him to work. Don't you worry!"
    wt_ky "I don't have a say in this, do I?"
    wt_ca "Nopeeee, that's what you get for making me do extra work, I have to draw a new map for you."
    wt_da "You two should get a room, it's blinding!"
    pe "Spill the tea Davos, what are we looking at?"
    wt_da "You should've been here just now! H-H-Hi my name is K-Kyle, I think you're c-cute."
    wt_ky "That is not what I said Davos!"
    wt_ja "It was definitely close enough, right Cassie?"
    wt_ca "D-Don't drag me into this!"
    wt_mo "Well, it sounds like you guys are having fun without us alright."
    ast "Remember to grab food supplies too Kyle."
    wt_wi "All packed and ready Aston. He won't starve on my watch!"
    wt_ru "Oh Aston, did you also need med supplies? Kyle has a bite on his arm, doesn't he?"
    ast "Yes, he got bitten by a cow. I think we have enough supplies though."
    wt_wi "A cow? My, you're full of surprises aren't you lad?"
    nvl clear
    #beeps end

    "They're such a silly bunch."
    "We all ended up talking for hours and had to swap Walkies multiple times cause the batteries kept running out."

    #Lorenzo's POV
    scene bg isaaklab1 with longfade
    play ambience amb_rc fadein 1.0

    show lorenzo smile at centerleft
    lo "Hngggg... phew.. I think that's the last box for Isaak? Koda's usually the one that collects boxes but I think they're with Gregory and Eva now."
    lo "Isaaaaak? Are you there?"
    lo "Hmm... Why is the ice box open- oh."

    "An unidentifiable animal carcass could be found in the box, covered in ice."
    "Looks about the size of a wolf pup or a large bird."
    "There doesn't seem to be any smell."
    show lorenzo sick
    lo "W-Well I guess at least it doesn't stink... maybe I should close it up still."

    "Lorenzo closes the lid of the ice box."
    #SFX thud
    show bg isaaklab2
    lo "I'll let Koda know that his supplies are here I guess."

    "Unable to shake off the feeling of uneasiness, Lorenzo decides to leave the lab to go look for the others."
    stop ambience fadeout 1.0

label nov_18:
    #EXT: Camp 1
    scene  bg camp1_day with dissolve

    "The next day, Kyle returns home from Camp 2. Gregory had to pick him up 'cause the ragdoll idea wasn't as great as he thought."

    show pearl smile at centerright
    show ky smile at centerleft
    pe "You're finally back! Thought you didn't want to leave Cassie."
    ky "I am a man of my words Pearl! Gotta send these supplies back here, and this, for you!"

    "Kyle hands me a newly drawn map."
    "Perfect. I should send Colin a shot of this later, this map is unlike the one that Elly had before."
    show lorenzo smile at left
    lo "Cassie? I feel like I'm missing some context here."
    show ky flustered
    ky "It's nothing Lorenzo, don't listen to Pearl."

    "The day goes on with lots of fun and banter."

    scene bg morganstent with sdissolve
    play music audio.neutral

    "Night time."
    "First things first, the map."

    #SFX Camera shutter

    "And... sent! Colin now has a copy of this."
    show satphone
    mo "Hiiii Pancake, I just sent you a picture."
    co "Nice one Morg. So what have you been up to?"
    mo "I survived a snowstorm, my highlight of the week."
    co "Are you serious? Well, I'm glad you're still in one piece, soldier."
    mo "Say... do we get bonuses for surviving? I've been eyeing this cool snowmobile that the guys have."
    co "We don't even have snow back home Morg."
    mo "Just thought I'd put in a request. Anyway, I think you'd want to hear this."
    mo "Profiles of the people at camp... sounds normal enough, yeah? But under all the necessary info, there's a part that lists whether the person is infected."

    co "I beg your pardon? Infected? Those are some glaring red flags if I've ever seen one."

    #IF MORGAN CHOSE TO DIG FURTHER ON DAY N15th he says this
    if dig_thru_docs:
        mo "Flipping through, I also found profiles with redacted info, with faces torn out. I didn't see any sign of Elly."
    #branch ends

    co "Don't suppose you know who owns 'em?"
    mo "Gregory. Would've taken pictures but I was almost caught snooping around."
    co "Better luck next time! But Gregory huh? Perhaps I should do some digging out here."
    mo "Yeah. Oh, we did get another new member too."
    co "New recruit?"
    mo "Nah, a wildlife photographer! Guy survived the storm in a makeshift igloo."
    co "Hah! He's insane, I like him. If I had a snowmobile I think he'd deserve it much more than you."
    mo "I thought I was your favorite."
    co "I love everyone the same."
    mo "Sure, I'll believe it if a snowmobile spawns in my apartment."
    co "I'll do you one better, how about I throw you a welcome back party once this is over?"
    mo "That sucks."
    co "Come on, can't you act a tiny bit grateful?"
    mo "My mother didn't teach me to lie, but for you Pancake, I'll tolerate the party."
    co "That's very kind of you."
    co "Aight good talk, you sleep tight Morg."
    mo "Nighty night, Pancake."
    hide satphone
    "I fell asleep soon after."
    stop music

label nov_19_23:
    #19th
    scene bg camp1_day with longfade
    play music audio.light


    "It's my favorite time of the day, meal time."
    "Looks like there's already a crowd gathered in here."

    #INT: Main tent
    show bg maintent_day
    show lorenzo smile at left
    show ast neutral at centerleft
    show pearl confused at centerright
    lo "Amore, you need to eat more greens!"
    ast "I don't eat green vegetables."
    pe "But what about corn? Or carrots? Eggplants?"
    ast "Normally I'd choose not to, but I know it's healthy so I tolerate them."
    pe "So no to pea soup?"
    ast "No to pea soup, they're green."

    "Lorenzo notices me walking in."

    lo "Morgan! Do you like vegetables?"
    mo "I love them roasted or stir fried, but not too much if they're boiled."
    show pearl smile
    pe "See Aston, you're the pickiest!"
    ast "...I've survived this long without vegetables. I can live without it."
    show lorenzo pondering
    lo "There are two kinds of people, survive to eat, and eat to survive. Amore, I think you're the latter."
    ast "Hey, it's not like I avoid everything green. I eat basil on pizza."
    mo "What are your favorite pizzas?"
    show ast inthought
    ast "A meatasaurus. If it has mushrooms and onions it'll smell better, but I'd still prefer meat and nothing else."
    pe "Hmmm, I like pep and cheese, or... Oh! A margherita with extra tomato!"
    show lorenzo smile
    lo "I like pesto with seafood, paired with wine? Mmm! That would be my ideal dinner night."
    mo "I'm not that picky but I do love me some extra onions, olives and anchovies. I love stinky stuff."
    pe "What are your stances on pineapple on pizza?"
    show ast neutral
    ast "Tolerable. It's a nice touch."
    lo "With pesto and seafood, absolutely not! With other savory meats then yes, I can see the vision!"
    pe "What about you, Morgan?"
    mo "Three for three, I love pineapple on pizza. Especially if they're sweet."
    mo "Do you know any pizza places that do delivery here?"

    "*gurgle*"
    #SFX
    "Someone's stomach lets out a deafening growl."

    mo "I guess the answer is no."

    #20th
    #INT: Main tent
    scene bg maintent_day with longfade
    "It's my first time seeing someone else using the table other than Gregory or Lorenzo."
    show ky smile
    mo "Morning Kyle, what are you up to?"
    ky "Morning! I'm planning my routes on the map that Cassie gave me."
    mo "So are you guys a thing yet?"
    show ky flustered
    ky "W-What? I mean, I haven't even taken her out to dinner yet, and I don't even know if she's available, you know?"

    "The fluster in his voice is evident, looks like the cat really got his tongue."
    show ky smile
    ky "Cassie is really cute though! She seemed interested when I showed her my album, there's lots of pictures of my previous adventures."
    ky "There's also Susie and all the other farm animals."

    "Kyle has his map laid out openly. It was then I noticed something different."

    mo "Wait... Why do you have extra drawings on your map?"
    show ky happy
    ky "She drew some animals for me! Waypoints for common sightings of animals."
    ky "So there's apparently wolves here, bears here if they are not already hibernating, birds of some kind that gather here, deers everywhere..."

    "Kyle explains everything with a large smile painted across his face."
    "He's such a golden retriever."

    #21st
    #EXT: Camp 1
    scene bg camp1_night with longfade
    "Campfire mealtime."
    show lorenzo smile at left
    show ast neutral:
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

    mo "You good Gregory?"
    gr "Yes, I just wasn't expecting to babysit twice the amount of kids all of a sudden."
    mo "Got any kids of your own Gregory?"
    show gr worried
    "A flicker of sadness shows on his face."
    gr "I have a daughter, yes. She's about Pearl's age."
    gr "Sometimes I wish I didn't have this job."
    mo "Why would you think so?"
    gr "Well you know... More time for family, more time for her."
    gr "Thankfully, I'm retiring soon. I hope that she doesn't hate her old man for being away for so long."
    show gr neutral
    "He recollects himself and continues."
    gr "What about you, got any kids yourself?"
    mo "I actually have a 4 year old running around back at home."
    show gr happy
    gr "A 4 year old? Hah, your wife must be having a real hard time taking care of the little bugger!"
    gr "That's the age when they tear your house down."

    "Colin's face flashes in my mind."
    "Yeah, my 4 year old child."

    #22nd
    #INT: Main tent
    scene bg maintent_day with longfade
    "*crash*"
    "Did I walk into something uninvited?"
    show pearl smile:
        xalign 0.5
        ypos 600
    pe "I'm okay!"
    "Pearl fell and accidentally knocked over the tool rack."
    "I rushed over to help her to her feet."
    show pearl smile with move:
        yalign 1.0
    mo "Looking for something?"
    pe "Yeah... My compass, I don't remember where I put it."

    #choice branch starts
    menu pearl_compass:
        "Ask her to check her pockets" if not pe_check_pockets:
            mo "Have you checked your pockets?"
            show pearl happy
            pe "Oh yeah, good idea."
            show pearl confused
            "She thoroughly searches her pockets, but to no avail. Guess it's not there."
            $ pe_check_pockets = True
            jump pearl_compass

        "Check the food shelf" if not pe_check_shelf:
            "Maybe at the food shelf?"
            "I reached over to the tomato soup section."
            show pearl neutral
            pe "Morgan! I know everyone knows that I love tomato soup but it's not there!"
            "Whoops."
            $ pe_check_shelf = True
            jump pearl_compass

        "Check the storage boxes":
            hide pearl with dissolve
            "Storage with all the important documents. A compass would be too clunky to fit in here."
            "Storage for extra ammo. I doubt she would be flipping through here anyway. We haven't had the need to use guns."
            "Storage with all the small tools... Oh!"
            "A compass with... a tomato sticker behind it. Classic Pearl."

    #choice branch ends
    show pearl smile
    mo "Here you go Pearl. It was with all the screwdrivers and hammers."
    show pearl happy
    pe "Oooh! Thank you Morgan, you're the best!"

    "If we're out in the forest, it would be pretty dangerous to leave your compass back at camp."
    "I'll need to make sure I remind her every time, then."
    stop music

    #23rd
    scene bg camp1_day with longfade
    show ky happy at centerleft
    ky "-and then splash! The otter family all jumped into the river together!"
    ky "Gosh I love their little paws."

    "Kyle and I were talking about his otter family encounters."
    "Of course, being the great photographer that he is, he's got a whole album designated for them."
    show ast neutral at centerright
    ast "Kyle? It's time."

    "Aston calls from inside the main tent."
    show ky smile
    ky "Ooh yeah, bandage time. Join us Morgan."

    #INT: Main tent
    show bg maintent_day with sdissolve
    play music audio.neutral

    "Aston skillfully unwraps Kyle's bandage and examines the wound."
    "He turns around and gives Kyle a packet of anti-inflammatory meds."
    show ast inthought
    ast "The wound closed up long ago, but I'm not sure why it is still red here."
    show ky sad
    ky "It kinda hurts when I touch it."
    show ast neutral
    ast "Oh well, we'll just monitor the rash for a few more days. If it gets worse, I'm sending you to the hospital."

    "The rash is concerning, considering that the original bite wound was only a quarter of its size."

    mo "Can cows carry rabies?"
    show ast inthought
    ast "I think so, but I'm pretty sure the farm animals here are all vaccinated against it."
    "Aston swiftly wraps a new bandage around Kyle's forearm."
    show ast neutral
    ast "Good as new. Remember to take those meds."
    show ky happy
    ky "Sure thing, thanks Aston!"

label nov_24:
    #EXT: Camp 1
    scene bg camp1_day with longfade
    "Today is rest day at camp."
    "Or in Pearl's words, tonight is marshmallow night!"
    "Can't remember the last time I've had a marshmallow, let alone a toasted one."
    "We were just waiting for sundown and for Kyle to come back from his photography session."
    "He seemed pretty excited to put his new map to use this morning."
    "He should be back soon."
    "In the meantime, I should probably mingle around the campfire."
    "Who should I approach first?"

    menu nov24_approach:
        "Approach Pearl" if not approach_pe:
            $ approach_pe = True
            show pearl smile
            "Pearl seems to have a 3-way Walkie setup going on right now."
            da "I'm waiting for my second growth spurt. You'll see Pearl."
            da "I'm gonna be as tall as or taller than my pops! Within the next few years... I hope?"
            pe "We love our short king."
            ko "I'm not sure we can even beat genetics Davos. That's a high bar to reach."
            show pearl happy
            pe "High bar to reach... Pfft."
            da "Hey!"
            mo "So Davos is short?"
            ko "He's 5'3, our beloved short king."
            da "Aww don't join them Morgan."
            ko "You win some, you lose some Davos. But hey, at least you have a great sense of direction."
            show pearl confused
            pe "Excuse me?"
            ko "Didn't say who but I guess you outed yourself Pearl."
            mo "I can confirm that Pearl doesn't do well when we're out collecting."
            pe "Morgaaaaaaaaaannnnnn."
            da "Run Morgan, run!"
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
    mo "Aston, I think Lorenzo is having a nightmare. What do you th-"
    show ast scared
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
    ky "Hey Morgan! You wouldn't believe what I just saw!"
    show ky happy
    ky "I saw a wolf! It was a silly one, kept bumping into trees."
    "I suppose I'll have to leave snooping in Gregory's tent for another time."
    "Marshmallow night is about to start soon."
    stop music
    
    scene bg camp1_night with dissolve
    play music audio.light

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
    "Kyle is... on the Walkie with Cassie? Nice one, I'm rooting for you two."
    hide ky
    show gr happy at right
    "Gregory too seems to be enjoying his time, savoring the toasted goodies."
    hide gr
    "At this moment, it's serene and peaceful."
    "Everyone is having a good time."
    "Unknowingly, their personalities have left an imprint on me."
    "For a while, I let myself bask in the feeling of having new companions."
    "The feelings, however, were short lived. My gut feeling had other plans."
    "Like a premonition, I knew I was just waiting for something bad to happen."
    "I don't like this unshakeable feeling of anxiousness."
    "I remind myself of my mission: Elliot still needs me."
    "The smell of something burnt tickles my nose and pauses my train of thought."
    "Whoops. Looks like I burnt mine."
    "I chucked the burnt marshmallow away and replaced it with a new one. Paying more attention to it this time."
    "Right now, with the knowledge I have, I'm inclined to believe that Gregory isn't innocent."
    "There has to be something. Something... or someone else in the picture that I'm not seeing."
    "What is it? Who is it?"
    "I need to gather more info for Colin."
    stop music

label nov_25:
    #EXT: Forest
    scene bg waterbody with longfade
    "Marshmallow night was a success, I had a great night's sleep."
    "New day, new samples."
    "New samples, from the same old lake."
    "It wasn't my imagination, the lake really is green."
    "Is there something in the water that makes it look green?"

    show pearl confused
    pe "Is it just me or does the soil feel different?"
    "Pearl calls me over."
    mo "Sure it's not the melting snow you're feeling?"
    pe "No, like, I've dug downwards three times, I don't remember the soil being hydrated."
    "Looks like there's a new observation to be made."
    show pearl neutral
    "If the soil is wet, water flow must be present."
    "The ice shouldn't really start melting this early. At least that's what it says in '{i}The Camp Guide's Guide{/i}'."
    show gr neutral at right
    gr "You found anything?"
    mo "Wetter soil apparently."
    gr "Wetter soil? That can't be right."

    "Gregory removes his glove to feel the moisture."
    gr "Yep, that's something new to report. Scrap the extra dirt collecting for now and let's head back. We have what we need for today."
    "He looks at me, who's evidently confused, and continues."
    gr "Isaak's orders. He needs wet soil more than anything else."
    gr "Told me to bring it to him immediately if we found any."
    mo "It can't be from the lake can it?"
    gr "We have to dig pretty deep down before we hit water, remember?"

    "It makes sense, but at the same time it doesn't make sense to me."
    "I think I need to ask someone with qualifications on this topic."
    "Maybe Eva?"

    scene bg camp1_day with dissolve
    play music audio.neutral

    "We quickly returned to the campsite and Gregory hastily drove his snowmobile to the RC."
    "I guess it will be an early day for Pearl and I."
    "Time to return to my tent."
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

    mo "You alright?"
    lo "I'm... I'm alright, amico. Thank you."
    hide lorenzo
    "He rushes back into his tent."
    "I'm worried. This is the second time I've seen him acting all weird."

    #INT: Morgan's tent
    show bg morganstent
    "Alright, better beep Eva."
    menu:
        "Beep Eva":
            wt_ev "What's up?"
            wt_mo "I have questions if you're up for it right now. It's about the samples."
            wt_ev "Shoot."
            wt_mo "Gregory is on his way to deliver wet soil to Isaak, it sounded urgent."
            wt_mo "We found it near the lake. Does that mean anything serious?"
            wt_ev "Wet soil around the frozen lake? If it's not the snow melting on top of it..."
            wt_ev "Then that would mean the lake is eroding."
            wt_ev "And if it erodes, that would mean bad news for us."
            wt_ev "Worst case scenario is it dries up or it becomes a threat for geological hazards."
            wt_ev "It's unfortunate, but it is a natural occurrence."
            wt_ev "As for why Isaak needs it urgently... I have no clue. He has never brought that up to us."
            wt_ev "Perhaps I should grab some from him and have a look at it myself."
            wt_mo "Well thanks for that Eva, that's good info."
            wt_ev "You're welcome."
            nvl clear
    #beep end

    "Lake erosion huh?"
    "That does sound bad."
    "But worrying about it won't do anything right now."
    stop music

label nov_26:
    #INT: Main tent
    scene bg maintent_day with longfade
    "Kyle, Lorenzo and I were having a discussion about animals."
    show ky smile at centerleft
    ky "Favorite animal I've photographed? Definitely toucans!"
    show ky happy
    ky "I mean, just look at them. Silly banana beaked birds."
    show lorenzo smile at centerright
    lo "Then what animal would you like to photograph that you haven't had the opportunity to before?"
    show ky smile
    ky "Oh that's such a cool question. I'd love to capture a picture of a Loch Ness monster or a kraken one day."
    mo "Are they even real?"
    show ky happy
    ky "I don't really know, which makes it the fun part!"
    ky "Maybe that should be my next adventure, and maybe after my arm has healed."
    mo "The bite from Susie hasn't healed yet?"
    show ky neutral
    ky "It's not like I haven't been bitten before, but this is the first time that it has gotten this bad."
    ky "It's about time for Aston to help me with a new bandage, anyway. Here, let me show you."


    "Kyle unwrapped his bandage to show a nasty rash. It hurts just looking at it."
    show cg rash
    $ persistent.gallery_rash = True
    lo "That... looks bad Kyle."

    "I caught Lorenzo pulling on his sleeve."
    show lorenzo neutral
    hide cg
    show ky sad
    ky "I know, and honestly, I've been feeling a lot groggier recently. Is it the weather or just me?"
    mo "I don't think it's a matter of the weather."
    mo "What about you Lorenzo? Are you feeling alright?"
    mo "I'm worried, you nearly collapsed yesterday."
    show lorenzo sad
    lo "I'm not exactly sick but... I've been having weird dreams recently."
    mo "Do you want to talk about it?"

    "Lorenzo hesitates for a second."
    show lorenzo neutral
    lo "Let me draw them real quick."

    "Lorenzo begins to scribble on his notebook."
    show cg lorenzosdrawing
    "A bear-shaped thing?"

    lo "See this... This bear thing, it has been following me night after night."
    show lorenzo sad
    lo "I'm sorry if it sounds silly, I just..."
    hide cg

    show ky neutral
    ky "It's not silly Lorenzo, fears are valid!"
    show ky shaken
    ky "Plus, I'd be scared shitless if a normal bear was in front of me, let alone this one."
    show ky neutral
    mo "Does it act like a normal bear?"
    show lorenzo neutral
    lo "Oh, that's the thing! It doesn't. It's always standing on its hind legs."
    lo "I can't read its expression but it doesn't feel like a friendly presence."
    lo "I'm not even sure if it has fur or some kind of... substance? I can't put it into words."
    show lorenzo sad
    lo "It's becoming a nightly event."
    show ky sad
    ky "That sounds rough Lorenzo..."


    "Kyle's rash is worrying. Lorenzo's dreams are worrying."
    "That's two things that happened within a week."
    show lorenzo scared
    lo "I've woken Aston up way too many times during the night. I feel horrible for disrupting his sleep."
    mo "I doubt he'd be worrying about his sleep when you're in distress my friend."
    show ky smile
    ky "Yeah, he's doing exactly what a good partner should be doing!"

    "A smile dawned on his face."
    show lorenzo smile
    lo "I'm lucky to have him."

    "We gave him pats on his back."
    show ky happy
    ky "Let us know if there's anything we can do to help!"
    lo "Thank you my friends."

label nov_27:
    #INT: Morgan's tent
    scene bg morganstent with longfade
    "It's time for a check in with my beloved Pancake."
# TODO PHONE
    show satphone
    mo "Who's the sweetest Pancake in the world?"
    co "Hey Morg, I know it's just a nickname, but don't get too used to it, you hear?"
    co "I don't wanna feel like I have to call you my pappy!"
    mo "Aw come on, humor me. Who's the sweetest Pancake in the world?"
    co "Meeeee. Okay done. What's the update?"
    mo "Two updates. Regarding the well-being of my campmates."

    menu nov27_about:
        "Talk about Lorenzo" if not about_lo:
            $ about_lo = True
            mo "Lorenzo has been having night terrors, the same recurring nightmare about a bear-like monster."
            co "That doesn't sound fun."
            mo "My gut tells me that he's not telling me the full picture, but he looks awfully distressed, so I doubt he's lying about the bear."

        "Talk about Kyle" if not about_ky:
            $ about_ky = True
            mo "Kyle has a rash on his arm. It's been about two weeks since he got bitten."
            co "Rashes you say? Describe it to me."
            mo "Bite site looks infected. The surrounding areas are red, peeling slightly. Kyle said it hurts to touch but it's also itchy."

    if not about_lo or not about_ky:
        jump nov27_about
        #choice branch ends
    else:
        mo "Did Elly ever say anything about these symptoms?"
        co "Nada Morg, first I'm hearing of it."
        co "Though, Elly did sound sick when we last talked..."
        co "He never mentioned anything about an animal bite, nor having nightmares."
        co "Which now begs the question: where do you get it from?"
        mo "There must be another source then."

        "Suddenly, I hear footsteps from the outside."

        gr "Morgan? You there?"

        "He has the worst possible timing."

        mo "I love you Pancake, but Papa's gotta get back to work. I'll call you back okay? "
        hide satphone
        "I hung up on Colin."

        show gr happy
        gr "You call your kid Pancake? That's sweet."
        show gr neutral
        gr "Sorry for interrupting family time, but I've got a favor to ask of ya."
        mo "Yeah?"
        show gr worried
        gr "Well, I'm just worried about Lorenzo? You think he's down with the cold or somethin'?"

    #choice branch starts, one choice only
    menu:
        "Lie":
            mo "Sick? Nah I don't think so. Maybe he just lacks some sleep."

        "Tell the truth":
            $ greg_sus += 1
            mo "Well... maybe, yes. Lorenzo told me that he has been having nightmares, but that's about it."
    #choice branch ends

    show gr neutral
    gr "Hmmm... Oh well. Just keep an eye out will ya?"
    gr "Let me know if you notice anything different about him. Thanks Morg."
    hide gr
    mo "Yes sir."

    "Now that was a peculiar request. I didn't like the sound of that."
    "Anyhow, I should look out for Lorenzo."
    "I sincerely hope that his nightmares subsides soon."

label nov_30:
    #INT: Main tent
    scene bg maintent_day with longfade
    "The past few days have just been the usual routine."
    "Wake up. Eat. Collect samples. Repeat."
    "Today was no different, but as we were about to hunker down for the night, the radio buzzed."

    #radio goes brrr connects to camp 1 and 2

    play music audio.neutral
    wt_ev "Hello campers, is now a good time?"
    wt_ja "Another weather report Eva? Camp 2's all here."
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

    pe "We're all here too!"
    wt_ev "Alright, good... but it's not about the weather, though."
    wt_ev "I have bad news and bad news."
    wt_ev "The other day Camp 1 found abnormal amounts of moist dirt."
    wt_ev "We have confirmed that the lake bed is probably giving way. The contents of the water do match up."
    wt_ev "Which ultimately means that the lake might dry up over time."
    wt_da "So the first bad news is that the lake is just gonna go poof on us?"
    wt_ev "Basically yes, Davos. We doubt it will happen anytime soon though."
    wt_mo "What's the other bad news?"
    wt_is "The lake's water has an unknown strand of fungi-like contaminants."
    wt_is "But it may just be what Heralign Inc. needs."
    wt_ko "The best case scenario is that we'll find a new source to gather something like penicillin."
    wt_ko "Fungi and the like are important ingredients for antibiotic medication!"
    wt_is "I'm sure you all know survival rules, but I'll just say this."
    wt_is "Do not, under any circumstances, drink the lake water."
    wt_is "Unless you'd like to find out why, in which case be my guest."
    wt_ko "L-Let's stay with boiled fresh snow and bottled water to be safe."
    wt_ja "So the water's deemed undrinkable then."
    wt_ja "Any idea how it would affect the wildlife here once the lake fully melts?"
    wt_ja "I'd hate it if something were to happen to them."
    wt_ko "That's definitely something to look out for now while we figure out what we have on our end."
    wt_is "Gregory, Wilbur and the rest. You have a new extra task - observe the behaviour of the wildlife."
    wt_is "Get pictures if possible."
    stop music
    "Gregory looks at Kyle, and Kyle points to his camera expectantly."
    gr "Kyle has a camera we can use."
    wt_wi "Hah! It looks like that camera will be useful after all, lad!"
    wt_wi "Gregory won't have a reason to kick you out anymore!"
    play music audio.light
    "Pearl and Kyle fist pump the air together."

    wt_da "Good for you Cassie!"
    wt_ja "Congrats Cassie!"
    wt_ev "Not sure why we're cheering for Cassie, but... yay Cassie."
    wt_ca "I-I can't with you all."
    show lorenzo smile
    lo "Kyle seems pretty happy about that."
    pe "Should've seen him in person, he was cheering!"
    ast "Weren't you also fist pumping the air?"
    show pearl happy
    pe "Well yeah, I'm excited for him too!"
    wt_mo "Cassie did you catch that? Kyle's going to stay for longer."
    wt_ru "She's hiding behind me."
    wt_ru "Looks like the message has been well received."
    wt_ca "Not you too, Ruran."
    wt_da "Aww Cassie, don't hide."
    show ky happy
    ky "I'll do my best guys! I'm glad that my skills will be of some value now!"
    nvl clear
    "Well, if I do indirectly end up contributing to modern medicine study, that's a win in my books."
    "I wonder if the weather had something to do with the fungi appearing."
    stop music

label dec_2:
    #INT: Main tent
    scene bg maintent_day with longfade
    #Aston and Lorenzo's POV
    show lorenzo sick at centerright with dissolve
    show ast sad at centerleft with dissolve
    "While the rest of them were out for the day, Aston and Lorenzo were alone in the main tent."
    "It seems like the bear hasn't stopped its torment on Lorenzo."
    "Waking up in a cold sweat countless times, he developed a fever overnight."

    ast "Your temperature... When did it start? Last night?"
    show lorenzo scared
    lo "How bad is it?"

    "Aston removes the thermometer from Lorenzo's mouth."

    ast "38 degrees, that's a fever."
    show ast scared
    ast "Do you want me to take you to the hospital?"
    show lorenzo sad
    lo "I don't know if that's feasible right now."
    lo "We'd need to tell Gregory."
    show ast angry
    ast "No, I'm not willing to take that risk."
    lo "Still worried about what happened to Elliot?"
    ast "The issue is that we don't know what happened."
    show ast inthought
    ast "One day he's at camp, the next day he goes missing."
    ast "Call me paranoid, but I don't want to find out. Not when Gregory is here."
    show lorenzo pondering
    lo "That makes two of us then."

    show lorenzo sad
    "Lorenzo fumbles with his sleeve, finding it increasingly difficult to resist the urge to scratch the itch on his arm."
    "His actions draws Aston's attention, who now prompts him for an answer."
    show ast sad
    ast "What's wrong?"

    "Lorenzo rolls his sleeve on his left arm."
    "A rash. Less severe than Kyle's but the similarities are undeniable."

    show ast with move:
        xpos 650
    show lorenzo with move:
        xpos 800
    "Aston cups Lorenzo's face with one hand and then pulls him into an embrace."

    show lorenzo scared
    lo "I don't know what this means, and truthfully... I am afraid of it."
    lo "Seeing Kyle's arm... I wish it was just a coincidence, but it's starting to look the part."

    show ast inthought
    "Aston ponders for a moment."

    ast "If it spreads on contact, then it wouldn't make sense."
    ast "I'm the one changing his bandages every day."
    ast "Any idea where you could've gotten this?"
    show lorenzo sad
    lo "I'm not too sure myself."

    show ast with move:
        xpos 500

    "Aston gently releases Lorenzo from the hug, and begins cleaning the affected area."
    show ast sad
    ast "Promise me you'll keep this between us for now?"
    ast "At least... not until we figure out what's really happening."
    show lorenzo smile
    lo "You have my word, amore."

    "Holding Lorenzo's hands in his, Aston takes a deep breath."
    show ast sad
    ast "You're going to be okay, love."
    ast "We'll figure something out."

label dec_3:
    #INT: Main tent
    scene bg maintent_day with longfade
    show ast neutral
    "Today I was tasked with lunch duties, helping Aston out in the main tent."
    "A certain someone really wanted tomato soup, so I'm on 'can opening' duty."
    "Suddenly, Aston's Walkie goes off on the table."
    ast "Morgan, could you help me with that?"
    mo "Sure thing bud."

    wt_wi "Aston my boy, are you there?"
    wt_mo "His hands are full but he's listening, Wilbur."
    wt_wi "Okay, wonderful! We just want to check in on Kyle."
    ast "Yes?"
    wt_ru "Has Kyle had trouble sleeping recently?"
    show ast inthought
    ast "I don't think so."
    wt_wi "You wanna tell him yourself lass?"
    wt_ca "It's like narcolepsy, but the other way around."
    wt_ca "Bummer... I don't remember what the word was..."
    wt_ru "It's insomnia, and you've been having that for..."
    wt_ru "Has it been a week yet?"
    wt_ca "A little over a week."
    wt_ca "I wish this was a problem I could sleep off."
    wt_wi "But yes, my boy, we were checking in just to see if everything is in order."
    wt_wi "Glad to hear that Kyle is okay!"
    wt_ru "Another thing Aston, have you noticed anyone else with these rashes?"
    wt_ru "If more of these pop up we would have to start sending people to a hospital."
    wt_ru "It may be something that we're not equipped to handle out here."
    show ast neutral
    "Aston freezes up."
    "That's... quite unlike him."
    wt_mo "Not that we've noticed here. You worried that it's contagious?"
    wt_ru "Always a possibility. It would be better to cover all our bases."
    wt_mo "Well, we'll let you know if anything new happens Ruran."
    wt_ru "That would be ideal, thank you Morgan."
    wt_mo "And take care Cassie!"
    wt_ca "I shall."
    nvl clear
    #radio end

    "First Kyle's arm, then Lorenzo's nightmares and now Cassie's insomnia?"
    show ast sad
    ast "Morgan, I-"
    mo "It's okay Aston, I know."
    mo "And I trust that you have your reasons."
    ast "..."
    show ast happy
    ast "Thanks."
    hide ast
    "That was the most heartfelt 'thanks' I've heard from him."
    "I figure Aston has his own reasons too, but I won't pry for now."
    "It's not hard to imagine Aston covering for Lorenzo, though."
    "I've caught him scratching his arm through his sleeve more times than I can count in the past few days."
    "If it's contagious then... This could get ugly really fast."

    #EXT: Camp 1
    show bg camp1_day
    show ky neutral
    "I bump directly into Kyle, who happened to be right outside the tent."
    mo "Is eavesdropping your new hobby?"
    show ky confused
    ky "N-No, I didn't mean to."
    mo "I'm just kidding. You must be worried about her."
    show ky smile
    ky "That obvious, huh?"
    "Kyle's too easy to read. It's not hard to guess how he's feeling."
    "He looks down at his forearm worriedly."
    mo "Hey, don't you start blaming yourself. We don't even know what's happening to Cassie yet."
    show ky sad
    ky "What if it was me?"
    mo "Then I would've gotten it too, but I've been sleeping like a baby every night."
    "The tension in his shoulders visibly relaxed."
    mo "Wanna help me out with lunch?"
    show ky smile
    ky "Yeah! I'd love to, Morgan."

label dec_4:
    scene bg camp1_night with longfade
    play music audio.light

    "Night falls in camp."
    "With the info I've gathered over the past few days, I think it's time for another update."
    "After being interrupted by Gregory multiple times, I waited for the signal before dialing up Colin."
    "And great, it looks like Gregory's snoring. The signal has been initiated."
    "Time to call my 4 year old."

    #INT: Morgan's tent
    show bg morganstent

    #TODO PHONE
    "Alrighty, Pancake time."
    show satphone
    co "Great timing, Morg."
    mo "Hey Panc-"
    co "Ah ah! We don't have to do this every time."
    mo "But we have to."
    co "Says who?"
    mo "Yours truly."
    mo "Jokes aside, you sound like you got some info for me."
    co "Yeah, I did find something interesting. It's about Gregory."
    co "Did Greg ever tell you that he has a daughter?"
    mo "Vaguely, why?"
    co "She's bedridden, in the hospital and she's in desperate need of a new liver."
    mo "That... was definitely not the news I was expecting to hear tonight."
    mo "Explains why he wants to retire so soon."
    co "He told you that?"
    mo "Yep, in a few months or so."
    mo "Said that, he'd finally be able to spend time with her."

    "The both of us fall silent upon this newfound revelation."
    "A heart wrenching one in fact."

    co "Still that doesn't mean he's off the suspect list."
    mo "You're right."
    mo "Anyway, my turn now, Pancake. I've got two for you today."
    co "Hell yeah, what's up?"
    mo "We might have a third case of the sickness."
    co "So it's rashes, nightmares and what now?"
    mo "Insomnia."
    mo "Cassie doesn't seem to have any other physical ailments."
    co "What do the other camp medics say?"
    mo "They don't know if it's contagious."
    mo "But what I do know is that Aston is hiding something."
    co "Is that so?"
    mo "My best guess is that he's covering for Lorenzo. He might also have a rash."
    mo "Seen him scratching his forearm through his coat way too many times now."
    mo "As for why he's hiding it, I have no clue yet."
    co "Might be worth prying that out of him or Lorenzo himself."
    co "So what's the second one?"
    mo "Other than the fact that the lake's eroding... Apparently, they found a new fungi-like microorganism present in the water."
    mo "The best case scenario is that we find a new source of antibiotic medication."
    co "Sounds like Heralign's gonna strike a pot of gold with that."
    co "But the worst case scenario I'm hearing is that it does the opposite?"
    mo "Yeah, and as of now, we can't drink that until they find out what the fungi does."
    co "Y'all got enough supplies up there?"
    mo "I'd say plenty, Lorenzo's got that covered for us at least."
    co "Aight that's good. And good work Morg, you've been working hard!"
    mo "Of course, Pancake. I'm the best."
    co "Think I should stop inflating your ego."

    hide satphone
    "I hung up on Colin."
    "Fungi, rashes... I hate the image that my mind's painting right now."
    "Putting the two and two together, it does sound plausible that it's related."
    "I trust that the guys at the RC will find out soon enough."
    stop music

label dec_5:
    #INT: Main tent
    scene bg maintent_day with longfade
    show ky sad at left
    show lorenzo sick at centerleft
    show pearl neutral at right
    show ast neutral at centerright
    show ky with move:
        xalign -0.5
    hide ky
    show lorenzo with move:
        xalign -0.4
    hide lorenzo with sdissolve

    "The next morning, I walk into the main tent just in time to see Aston and Pearl shoo-ing Lorenzo and Kyle back into their tents."
    "Lorenzo looks a lot worse for wear."
    "And Kyle looks like he's sleepier today."

    mo "Are those two alright?"
    ast "A little worse than yesterday. I'll check in on them in a bit."
    show pearl sad
    pe "I'm worried for them."

    "Oop, looks like the radio is on again."
    show gr neutral at left
    "And Gregory walks in right on time."
    #TODO RADIO

    wt_ko "Hello hello! Is everyone here?"
    wt_ja "Hey Koda, C2's here."
    show pearl smile
    pe "Koda! Camp 1's here!"
    pe "And hello Jax! Looks like you beat Davos to the radio again."
    wt_ja "Davos just needs to try harder next time."
    wt_da "You know I can't reach the radio if you raise it up high like that. That's cheating."
    wt_ja "They don't need to know that."
    wt_ko "Haha! Wonderful that everyone's here, I come bearing a new mission, friends!"
    wt_ko "Isaak and Eva decided it's time to move camp!"
    wt_ko "So remember when we said stuff about animals and lake dirt stuff?"
    wt_ko "They want dirt samples from the east side mountain, just so we can be sure that it's definitely coming from the lake."
    wt_ko "And to kill two birds with one stone, moving to higher ground means that you have more vantage over the forest on ground level."
    wt_ko "Perfect for scouting animals."
    gr "So uh... Are we joining camps again kid?"
    wt_is "Only if you want to."
    wt_is "It is imperative that you grab samples on the mountains."
    wt_is"Whichever is efficient I guess?"

    "I'm secretly hoping that our camps can merge so that I can meet the rest."
    "But on the other hand, calling Colin may prove more difficult with more ears around."
    "I'm not the one making decisions here so... No point thinking about it until it happens."

    wt_ja "Joining camps would be really fun."
    wt_ja "What say you, Wilbur and Gregory?"
    gr "I have no objections, it is the most efficient way."
    wt_wi "That settles it then!"
    wt_wi "And it looks like we'll finally see Morgan in the flesh!"
    show pearl happy
    pe "Oh my goodness, that means everyone will meet Morgan for the first time!"
    wt_mo "About time for that big reveal, huh?"
    wt_mo "And here I thought I could stay mysterious forever."
    wt_wi "That is perhaps the most exciting news, yes!"
    wt_wi "The more friends to camp with, the merrier!"
    wt_da "We can do campfire story nights again, can't wait!"
    wt_ko "I'd love to join too, Davos."
    wt_da "Hehe, we can bet on how many marshmallows Pearl will burn."
    show pearl smile
    pe "I can just eat the marshmallows you toast, problem solved."


    "Alright, so that's plan A...merging of camps."
    "Lots of new faces and hopefully lots of info."

    wt_ca "I'll go check the coordinates real quick, let's establish a meet up point for tomorrow!"
    wt_ca "I'll Walkie you later Gregory!"
    gr "That'll be lovely, Cassie."

    gr "How long do you reckon we'll be up there, Isaak?"
    wt_is "Until I have enough, there's no rough estimate right now."
    wt_ko "We'll leave you guys to it for now! Big day tomorrow!"
    nvl clear
    #radio ends

    gr "Well, you heard the man. Let's start packing the essentials."
    gr "We're moving at dawn."
    mo "Aye aye, captain."

label dec_6_1:
    scene bg camp1_day with longfade
    play music audio.neutral
    "Essentials and equipment have all been well packed."

    "Today is moving day."
    "New terrain to conquer, new friends to meet."
    "I'm sure it'll be lovely."
    show gr neutral at left
    gr "Got everything ya need, Pearl? Personal belongings, what not?"
    show pearl happy at centerright
    pe "I would hope so!"
    mo "Did you remember your compass?"
    show pearl sad
    pe "Aww..."
    show lorenzo smile at right
    hide pearl
    lo "Looks like she forgot."
    show ast neutral
    ast "How is the route up going to be?"
    show gr with move:
        xpos 200
    show lorenzo with move:
        xpos 1600
    gr "Alrighty so...here's the route that Cassie drew for us."


    "Gregory holds out his map with outstretched hands for us to see."

    gr "We're gonna start climbing the mountain over 'ere. It's less steep of an angle to trek, she said."
    gr "Once we've reached the midpoint, we're gonna pivot to this area here. A nice flat area to set up camp."
    mo "Do you know how long that might take us?"
    gr "A few hours at least. We should be able to get there before sundown."
    lo "And we're meeting them at the midpoint, yes?"
    gr "That is correct."

    show ky smile at left:
        xpos -100
    ky "Are we going to come back later to retrieve everything?"
    gr "Yes, that's why the essentials are the only things that we're carrying today. We've gotta make multiple trips over the next few days."
    ky "Cool, cool! I'm happy to help wherever needed!"
    mo "We'll definitely be needing the extra hands, Kyle."

    show pearl happy at right
    pe "I'm back and ready to go! Double checked my pockets this time."
    lo "Shall we?"

    scene bg forest2 with dissolve
    #EXT: Forest mountain
    "In a single file, we followed Gregory up the trail."
    "Hiking up the snow doesn't seem too bad now that I had a whole month of practice."
    "The snow crunches under our feet in a nice rhythmical pattern."
    show ky smile at left
    show pearl smile:
        xpos 300
        yalign 1.0
    show gr neutral at center
    show lorenzo smile:
        xpos 1000
        yalign 1.0
    show ast neutral at right

    #SFX radio beeps
    wt_wi "Hello my friends! Checking in to see if everyone's on their merry way!"
    show ky smile
    ky "We've started trekking a while ago, Wilbur! We're on our way!"
    wt_da "Glad to hear you're excited, Kyle!"
    show ky happy
    ky "I mean, it's photography! Of course I'm excited."
    show ky flustered
    ky "I'm also excited to see you guys... Cassie especially."

    show ky smile
    wt_ru "Cassie is once again hiding behind me, but she's got the message."
    wt_ca "Ruran! How could you!"
    wt_ru "Haha!"
    wt_da "Also, I hope Pearl didn't forget her compass today."
    wt_mo "She did."
    show pearl neutral
    pe "Morgan! I am a good camp guide, I swear!"
    lo "We believe in you, Pearl."
    show pearl smile
    pe "Thank you."
    wt_ja "On the topic of photography... What animal do you think we'll see most of Kyle?"
    ky "You know, I'm not exactly sure since this is the first time we'll be up here."
    ky "My guess would be wolves or coyotes, any non-friendly but friend-shaped doggos."
    wt_da "I'm hoping we can capture birds. We've never really seen them on lower ground."
    wt_da "Bird watching's about to get interesting!"
    wt_wi "How far more till the meet up point, Cassie?"
    wt_ca "Well, with our current pacing, we'll see them in about an hour or less!"
    wt_ru "That sounds great. We'll be just on time for lunch. This time, together."
    wt_mo "I should get Pearl to do a curtain reveal for me."
    pe "Well, I don't have curtains, but you can crouch behind all of us!"
    wt_mo "Sounds like a plan."
    gr "Morgan, can you hold the map for me? I just need to grab my compass real quick."
    stop music
    if persistent.screenshake:
        with hpunch

    show lorenzo neutral
    show pearl confused
    show ky confused
    show ast confused
    show gr confused

    "{b}{i}{size=+5}*boom*"

    #SFX
    "That sounded like a gun, but louder."

    wt_ja "Y'all hear something?"
    ast "It wasn't just you."
    mo "Was that a gun, or-"


    if persistent.screenshake:
        with hpunch
    show ast scared
    show lorenzo scared
    show pearl scared
    show ky shaken
    show gr scared
    
    "{b}{i}{size=+5}*rumble*"

    #SFX
    #TODO start shakingggg
    "The ground beneath us starts shaking."
    "That doesn't feel... right?"
    "Instinctively, Gregory and I look towards the top of the mountain."
    gr "What the-"
    "Oh no."
    "Actually, that's an understatement. We're fucked."
    "From the peak of the mountains, the snow is gushing down at us at breakneck speed."

    wi "{size=+5}AVALANCHE!! TAKE COVER!!"

    "Wilbur's voice rings out and brings us back to center."
    "Run, hide and survive, or get swallowed alive."

    show cg avalanche
    $ persistent.gallery_avalanche = True
    gr "{size=+5}{i}DON'T JUST STAND THERE, RUN!!"

    "Camp dad's voice is loud and clear."
    hide cg
    scene bg forest2 with sdissolve
    "He's right, I have to survive this."
    "Elliot... If we're both still alive, you best bet I'm gonna extort free meals from you every day."
    "The things I do... or rather the things I have to go through for you."

    "I ran as fast as my legs could take me."
    "The snow below my feet keeps giving way. I'll trip if I'm not careful."
    "I can't outrun the snow...it'll catch up to me soon."
    "There's a rock formation up ahead, tall enough to shelter me from the onslaught."
    "Bingo! That's my ticket out of here."
    "Almost there, just a few more steps and I'll-"

    #SFX thud
    show bg forest2:
        zoom 2
        linear 0.2 blur 20
        parallel:
            linear 0.2 ypos 1080


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
#Insert Candy's animated sequence here, Dec 6th Elliot's scene


