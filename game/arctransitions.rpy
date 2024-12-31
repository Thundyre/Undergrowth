label tr_nov_1:
    $ save_name = _("Prologue")
    
    #INT:  Morgan’s Apartment
    #Hilda's voice can be heard from the TV advertisement.
    hi "Glow glow glow with NuGLO, let us help you restore your skin's shiny supple glow!"
    hi "So what are you waiting for? Grab your very own NuGLO samples at your local stores today!"
    #Morgan stands up and switches off the TV abruptly, his phone buzzes.
    #Click!
    #SFX
    mo "Heya."
    co "Got everything you need Morg?"
    mo "Yep, just zipping up here and I'm good to go."
    co "Sure you got everything?" 
    mo "Can't fit you in my bag now, can I?"
    #Morgan zips his backpack.
    co "Wouldn't try to even if you asked. I'd rather not be stuck in that for three days."
    mo "Haha, well.. I think it's just about time to head off!"
    co "Alrighty then. Bring him home and stay safe, soldier."
    mo "I will."
    #With one final look at his living room, Morgan swings his backpack onto his shoulder and then leaves his apartment.

    jump nov_4

label tr_dec_6:
    #INT: Locker Room
    show cg memory
    $ persistent.gallery_memory = True
    #Morgan enters the locker room and sees Elliot there packing up his belongings. 
    mo "Woah Elly, are you going somewhere?"
    el "Yep! It's gonna be a long trip."
    mo "Oh, where to?"
    el "Switzerland. Might stay there for a few months, might travel to other places after a few weeks. Who knows?"
    mo "Wow I'm jealous, take me with you Elly."
    el "Nah you'll ruin the peaceful vibes Morg, absolutely not."
    mo "Touché."

    #Morgan leans against his locker.

    mo "So when are you flying? We could grab some drinks before you go." 
    el "Next morning actually so no drinks for me."
    mo "Awww alright."
    el "Now don't get all sobby on me Morg, I already had to deal with Colin an hour ago."
    el "You won't miss me that much."
    mo "Ew sobby over you? Fat chance Elly." 
    mo "But of course I'll miss you. In fact, I know I'll miss roasting you daily about your taste in fashion."

    #Elliot slaps Morgan's shoulder.

    el "I'll be back before you know it, and you'll regret saying that you miss me."
    el "Heck I'll even bring you souvenirs. How does a jar of Swiss dirt sound, huh?"
    mo "Depends if I get to see you eat some of it."
    el "That's nasty haha!"


    #Elliot shuts his locker.

    el "Morgan."
    mo "Yes, Elliot?"
    el "Nothing just… thanks for always being there for me."
    mo "Of course bud."
    el "Well, I think I'm gonna head out now! See you in a few months!"
    mo "Bye, biscuit. Safe travels!"

    #Elliot leaves the room, leaving Morgan alone in the scene.

    jump dec_6_2

label tr_jan_11:
    #INT: Duo vignette scenes
    show cg coliniscool
    $ persistent.gallery_coliniscool = True
    voice "tr_j11_AnyUpdates"
    co "Any updates from your end today?"
    with Pause(1.0)
    voice "tr_j11_KeepMe"
    co "Keep me posted then."
    "Colin was on the phone with his birdie at Heralign HQ."
    "Radio silence. {w=0.8}Morgan hasn't been in contact for almost two weeks at this point."
    "He looks over to a group photo of Morgan, Elliot and him."
    voice "tr_j11_WhereAre"
    co "Where are you, Morg…"
    voice "tr_j11_ICant"
    co "I can't keep losing my best boys one by one."
    "His gaze then shifts to a brochure on his table."
    "It's an advertisement for one of Heralign's products."
    voice "tr_j11_GlowGlow"
    co "'Glow, glow, glow with Nu-fucking-GLO.'"
    voice "tr_j11_MaybeIf"
    co "Maybe if you didn't reek of corporate malfeasance, my wife could enjoy this."
    scene black with fade
    "He crumples it and throws it into the trash."
    scene black
    voice "tr_j11_JustYou"
    co "Just you wait, Hilda Heralign."
    voice "tr_j11_YouCant"
    co "You can't cover your tracks forever."
    scene black with longfade
    with Pause(1.0)
    hide cg coliniscool

    #HILDA
    show cg hildasucks with dissolve
    $ persistent.gallery_hildasucks = True
    voice "tr_j11_ReadyWhen"
    hi "Ready when you are!"
    "Hilda is on a film set, preparing herself for a commercial shoot."
    play sound phonebuzz
    with Pause(0.5)
    play sound phonebuzz
    voice "tr_j11_OhExcuse"
    hi "Oh, excuse me for just a moment! I have to take this call."
    scene black with fade
    "Hilda walks out from the set."
    scene black
    with Pause(0.5)

    voice "tr_j11_WhatIs"
    hi "What is it?"
    scene black
    voice "tr_j11_IfYou"
    hi "If you have nothing useful to report, end the call."
    scene black
    voice "tr_j11_HildaVNVR"
    hi "..."
    voice "tr_j11_WhatDo"
    hi "...what do you mean, police?"
    voice "tr_j11_CantThis"
    hi "Can't this wait until I'm back?"
    scene black
    voice "tr_j11_YouHave"
    hi "You have my calendar. I can't just drop everything and go running back."
    voice "tr_j11_TellThem"
    hi "Tell them to leave their fan mail at the front desk."
    "The other side of the phone call is filled with more frantic muttering."
    voice "tr_j11_WhatWorried"
    hi "What? Worried that I'll throw you into the Sun?"
    "Silence."
    voice "tr_j11_ThatsA"
    hi "That's a good boy."
    "She hangs up."
    scene black with dissolve
    "After a brief sigh and once again donning her world-famous smile, she walks back inside."
    show cg hildasucks with dissolve
    voice "tr_j11_ImSo"
    hi "I'm so sorry about that. Where were we?"
    voice "tr_j11_FromThe"
    hi "From the top, yes?"
    scene black with longfade
    hide cg hildasucks with dissolve

    jump jan_11
