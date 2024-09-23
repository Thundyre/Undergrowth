# characters normal
define gr =  Character("Gregory")
define pe = Character("Pearl")
define mo = Character("Morgan")
define hi = Character("Hilda")
define ast = Character("Aston")
define da = Character("Davos")
define ko = Character("Koda")
define co = Character("Colin")
define lo = Character("Lorenzo")
define isa = Character("Isaak")
define wi = Character("Wilbur")
define ru = Character("Ruran")
define ca = Character("Cassie")
define ja = Character("Jax")
define ev = Character("Eva")
define ky = Character("Kyle")
define el = Character("Elliot")
define ex1 = Character("Driver")
define v1 = Character("Child 1")
define v2 = Character("Child 2")
define vs = Character("Susie")

# characters walkie-talkie
define wt_mo = Character("Morgan", kind=nvl, callback=Phone_SendSound)
define wt_ca = Character("Cassie", kind=nvl, callback=Phone_ReceiveSound)
define wt_is = Character("Isaak", kind=nvl, callback=Phone_ReceiveSound)
define wt_ky = Character("Kyle", kind=nvl, callback=Phone_ReceiveSound)
define wt_ko = Character("Koda", kind=nvl, callback=Phone_ReceiveSound)
define wt_wi = Character("Wilbur", kind=nvl, callback=Phone_ReceiveSound)
define wt_da = Character("Davos", kind=nvl, callback=Phone_ReceiveSound)
define wt_ru = Character("Ruran", kind=nvl, callback=Phone_ReceiveSound)
define wt_ev = Character("Eva", kind=nvl, callback=Phone_ReceiveSound)
define wt_ja = Character("Jax", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

# characters other
define tv_hi = Character(None, image= "pando1", kind = bubble, retain = True)

label start:
    $ save_name = _("Arc 1")    
    jump nov_1
