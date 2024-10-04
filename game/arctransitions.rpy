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
    mo "Haha well.. I think it's just about time to head off!"
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
