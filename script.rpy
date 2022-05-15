# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Aster")
define o = Character("Mom")
image mom = Placeholder("girl")
define e = Character("Eiron")
image eiron = Placeholder("boy")
define s = Character("Sofie")
image sofie = Placeholder("girl")
image bedroom = im.Scale("bedroom.jpg", 1920, 1080)
image bridgenos = im.Scale("bridgenos.jpg", 1920, 1080)
image citynos = im.Scale("citynos.jpg", 1920, 1080)
image town1 = im.Scale("town1.jpg", 1920, 1080)
image park = im.Scale("park.jpg", 1920, 1080)
image livingroom = im.Scale("livingroom.png", 1920, 1080)
image mall = im.Scale("mall.jpg", 1920, 1080)
image arcade = im.Scale("arcade.jpg", 1920, 1080)
image mallbench = im.Scale("mallbench.jpg", 1920, 1080)
image mallexit = im.Scale("mallexit.jpg", 1920, 1080)
image schoolout = im.Scale("schoolout.jpg", 1920, 1080)

label start:

    "Hanahaki by ???"

    jump prologue
