# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default Yuchao = Character("Yuchao", color="#9f00eebb")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    "This is my first renpy game"
    "Yuchao" "Hi, this is Yuchao."
    "Yuchao" "Welcome to my first renpy game-making project."

label sprites:
    "Yuchao" "But wait, where are you?"
    show yuc delighted
    "Yuchao" "Oh!!"
    show yuc angry
    "Yuchao" "It's not like I was looking for you or anything..."
    show extra normal at right
    "Random Girl" "Tsundere..."
    hide extra
    "Yuchao" "..."

label character:
    show yuc bored
    "Yuchao" "Wow... this is too plain."
    show yuc smile2 with dissolve
    "Yuchao" "I want my color to be dark purple!"
    Yuchao "Wonderful!"  
     
label background:
    Yuchao "Come on! Let's go the gym."
    scene bg gym
    with fade
    
    show yuc smile2 at left
    Yuchao "You got here faster than I did!"  

label bgm:
    play music "audio/bgm_basketball.mp3" fadein 1.0 volume 0.5
    Yuchao "Oh, the basketball team is playing?"
    Yuchao "It's too loud. I'll meet you in the classroom."
    
    stop music fadeout 1.0
    scene bg classroom
    with fade
    
label sfx:
    play sound "audio/sfx_bell.mp3"
    Yuchao "Oh no. It's already time."


label choices:
    default learned = False
    Yuchao "Did you learn a thing or two?"

menu:
    "Yes":
        jump choices1_a
    "...":
        jump choices1_b

label choices1_a:
    Yuchao "Good!"
    $ learned = True
    jump choices1_common

label choices1_b:
    Yuchao "..."
    jump choices1_common

label choices1_common:
    Yuchao "For more effects, you can check out Ren'Py's guides."
    Yuchao "The link can be found in the description."

label flags:
    if learned:
        Yuchao "If you learned a thing or two, please like the video!"
    else:
        Yuchao "You can check out my other videos to learn more about game development!"

    return
