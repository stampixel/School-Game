# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define pov = Character("[povname]", image="prot")
define narrator = Character("")
define mystery = Character("???")
define mentor = Character("Mentor")


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.


    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
             povname = "Me"

    narrator "You wake up from a deep sleep, disoriented, your mind a blank slate..."

    show povname

    pov "\"Where am I?\""

    "*You look around, trying to piece together your surroundings.*"

    menu:
        "Explore":
            "You walk through the eerie landscape, noticing the chaotic nature of the surroundings—trees shaped like question marks, rivers flowing backward."
            "You hear a rustling sound from a nearby bush..."
            pov "WHO'S THERE?" with hpunch
            "The rustling grows louder, and then, emerging from the bushes with a graceful stride, is an older figure clad in flowing robes, adorned with quill and parchment motifs."

        "Wait":
            "You sit quietly, trying to gather their thoughts."
            pov "AHHHHHHHHHHHHHHHHHHHHHHHH!! Where on earth did you come from???" with hpunch





    mystery "Ah, I see you've awakened at last. Welcome to Literaria, young one."

    "The figure steps fully into view, revealing themselves, a wise and kindly face etched with years of knowledge."

    pov "Who... who are you??? Where am I??? What is going on???"

    mentor "I am known as the Mentor, a guide for those chosen by the ancient Order of Composition. And you, my dear student, are one such chosen. The fate of Literaria rests upon your ability to master the art of Script Weaving."

    mentor "Come, there is much to learn, and time is of the essence. The forces of Chaos & Confusion grow stronger by the day, and only through the power of words can we hope to restore balance to our land."

    "The Mentor gestures to a nearby path, winding deeper into the heart of the forest, where the journey will begin."

    pov "Why me? I don't even know who I am..."

    mentor "That is something you will discover on this journey. But know this, the power within you is immense, waiting to be unlocked. You are the one destined to wield the Magical Quill, to bring order where there is none."

    "With a nod, the Mentor begins to lead the way, and you, though uncertain, feels a growing determination within."

    mentor "Follow me, and I will teach you the ways of composition. Together, we will restore harmony to Literaria. Once and for all!"

    mentor "Are you ready [povname]?"

    label choice_intro:
        mentor "Are you ready [povname]?"

    menu:
        "Yes":
            jump choice_intro_a
        "... how do you know my name again?":
            jump choice_intro_b

    label choice_intro_a:
        mentor "Great, then our journey together shall begin!"
        mentor "Follow me."
        pause 3
        jump level1

    label choice_intro_b:
        jump choice_intro



label level1:
    "Your feet are sour and your mouth is dry. Time seems to work differently in this universe. You felt as though you have been walking for hours."
    "You and your Mentor stand in front of a grand, mystical portal that swirls with images from the story \"The Fall of a City.\""
    mentor "This seems to be where all the Confusion and Chaos originates from."
    mentor "Your first task is to identify two key character traits of Teddy’s aunt or uncle. Their traits hold the power to influence the structure of your essay."
    "The portal shows scenes from the story, with the aunt and uncle interacting with Teddy."
    "You see the way they speak and act—what do you observe?"

    label level1_task:
        menu:
            "The aunt is controlling and dismissive.":
                "The portal reacts. It turns ocean blue. You can't seem to see through to the other side."
                "Do you choose to enter?"
                menu:
                    "Yes":
                        pov "Have you every been through one of these? Where would we end up?"
                        mentor "Theres only one way to find out. "
                        "You hesitantly step in, one foot at a time."
                        jump level2
                    "No":
                        "The mentor pushes you. You trip on a rock and face plant in. Better luck next time..."
                        jump level2
            "The uncle is stern and critical.":
                "Not quite, give it another go."
                jump level1_task
            "The aunt is nurturing and supportive.":
                "Not quite, give it another go."
                jump level1_task
            "The uncle is playful and encouraging.":
                "Not quite, give it another go."
                jump level1_task

    return

label level2:
    "The portal closes behind you, disappearing altogether, without leaving a single trace behind."
    "You look around, gray brick walls, ceiling tens of meters high, you appear to be in some sort of castle."
    pause 3
    "A magical Aura leads you to a large, ancient writing desk with a blank parchment lying on it."
    mentor "A strong essay needs a clear and focused topic sentence. Use the traits you've identified earlier to create one."

    $ sentence = renpy.input("Type away: ", length=500)
    centered "[sentence]"

    mentor "After finishing, you may turn to your peers and have them enter a rating between 1-5."

    label level2_task:
        $ rating = renpy.input("Rate from 1-5: ", length=1)
        if rating != 1 or rating != 2 or rating != 3 or rating != 4 or rating != 5:
            "Invalid input."
            jump level2_task

            # have them describe your sentence

    "The mystery force judges your writing, the parchment glows slightly."
    "You hear movement, turning back, the stone wall shifts, creating an exit."
    "You proceed followed by your mentor."
    jump level3

label level3: # not complete, finish questions
    "You see something unfamiliar, though you still couldn't remember anything before, you are sure you have never seen something like it before."
    pov "What the hell is that?"
    mentor "That is a Chaos & Confusion Minion that embodies \"Vague Argument.\""
    mentor "To defeat it, you must clearly state a point using the PEE method: Point, Evidence, Explanation."
    mentor "Out of the following, select the best answer which states a point clearly and concisely, take your team and read each one carefully."

    $ attempts = 0

     label level3_task:
        menu:
        # first, pick a character trait
            "The aunt is controlling and dismissive.":
                if attempts > 0:
                    "You barely made it out alive."
                "Your statement weakens the minion, but it’s still standing."
            "The uncle is stern and critical.":
                "Not quite, give it another go."
                attempts += 1
                jump level3_task
            "The aunt is nurturing and supportive.":
                "Not quite, give it another go."
                attempts += 1
                jump level3_task
            "The uncle is playful and encouraging.":
                "Not quite, give it another go."
                attempts += 1
                jump level3_task
    ""
    jump label4

label level4:
    mentor "Don't worry kid, I have another trick up my sleeves."
    mentor "Riddle me this: Dawn comes after night like ________ comes after Point."

    label level4_question:
        menu:
            "Explanation":
                "Maybe if you used more than just two fingers..."
                jump level4_question
            "Evidence":
                mentor "Well spoken! Goodly done, young one! Let us employ that as our stratagem to vanquish the minion."

    mentor "Now tell me, what is a quotation that best demonstrates the point you’ve identified previously? (POINT GOES HERE)"

    "You instinctively take our the Magical Quill."

    label level4_task:
        menu:
            "The aunt is controlling and dismissive.":
                "Guided by your hands, the quill moves swiftly across the air."
            "The uncle is stern and critical.":
                "Not quite, give it another go."
                jump level4_task
            "The aunt is nurturing and supportive.":
                "Not quite, give it another go."
                jump level4_task
            "The uncle is playful and encouraging.":
                "Not quite, give it another go."
                jump level4_task
    "It further weakens the minion."

    mentor "Excellent! But to truly defeat the minion, you must explain how... "
    "The mentor loses track of what he was going to say."

    jump sidequest

label sidequest:
    "All of a sudden, everything around you freezes."
    "The vibrant colors of Literaria dimmed, and the swirling winds came to a halt. The world, once alive with energy, now stood eerily still. "
    pov "What’s happening? Why is everything stopped?" hpunch
    mentor "The Mentor's eyes, usually so full of wisdom and warmth, now held a deep, almost somber intensity. They took a step closer to you, the silence between you growing heavier with each passing moment."
    "There is something you need to know, something I have kept hidden until now."
    pov "What do you mean? What’s going on?"
    mentor "I am not just a guide in this world, not just a teacher showing you the ways of Literaria. I am its creator."
    "The words hang in the air, their weight sinking in slowly. The Mentor—your trusted companion throughout this journey—created Literaria? The realization stirs a mix of emotions within you: awe, confusion, and a hint of fear."
    pov "You… created this world? But why? Why reveal this to me now?"
    mentor "Literaria is more than just a land of stories; it is a delicate balance of knowledge, creativity, and truth. I brought it into existence to help others learn, to give life to the lessons within stories. But every world needs a guardian, someone to maintain that balance and protect it from chaos.""
    "The Mentor pauses, looking into your eyes with a seriousness that makes your heart race."

    mentor "I will give you two options. Either forget the ugly truth or keep fighting knowing everything around you is planned and fictional."
    "The Mentor steps back slightly, raising their hand as two glowing orbs appear between you. Each orb pulses with a different energy, radiating a sense of immense power and responsibility."

    "(Pick wisely as this is a major determining factor of the outcome of your journey)"
    menu:
        "Keep fighting knowing everything around you is preplanned and has a predetermined outcome.":
            mentor "It might be hard at first, but I thank you for understanding."
            "The world reverts back to normal. You can feel the cool breeze of the wind, it flows around and you feel comfort."
            mentor "Now, where were we?"
            mentor "To truly defeat the minion, you must explain how this evidence supports your point."
        "Forget what happened.":
            mentor "Very well. Although hard to make, the choice is indeed a valid one at times."
            "Your mind turns blank for a second."
            mentor "... you must explain how this evidence supports your point."

    jump level5

label level5:
    pov "Understood."
    "You face the now weakened minion, ready for the final blow."
    mentor  "Now, explain how the quote you selected proves the character trait. Choose the best answer."

    label level5_task:
        menu:
            "The aunt is controlling and dismissive.":
                "Guided by your hands, the quill moves swiftly across the air."
            "The uncle is stern and critical.":
                "Not quite, give it another go."
                jump level5_task
            "The aunt is nurturing and supportive.":
                "Not quite, give it another go."
                jump level5_task
            "The uncle is playful and encouraging.":
                "Not quite, give it another go."
                jump level5_task
    "The explanation delivers a decisive strike, defeating the Chaos & Confusion Minion."
    "Well done! But your journey is far from over."
    jump level6

label level6:
    "With the first minion defeated, the protagonist moves forward, encountering another representing \"Weak Transitions.\""
    mentor "To move smoothly between ideas, a strong transition is key. Let’s identify your second character trait and introduce it."

    mentor "Which of the following transitions make the sentences flow while also strengthening the root argument?"
    label level6_task:
        menu:
            "The aunt is controlling and dismissive.":
                "Very well, amazing choice. You won't even need me at this point!"
            "The uncle is stern and critical.":
                "Not quite, give it another go."
                jump level6_task
            "The aunt is nurturing and supportive.":
                "Not quite, give it another go."
                jump level6_task
            "The uncle is playful and encouraging.":
                "Not quite, give it another go."
                jump level6_task
    "Again, The Transition and Point only weakens the new minion."
    pov "I guess we'll have to follow up with Evidence and Explanation."

    jump level7

label level7:
    mentor "Which of the following is the best choice when transitioning from the previous sentence? (PREVIOUS SENTENCE)"
    label level7_task:
        menu:
            "The aunt is controlling and dismissive.":
                "Nicely done!"
            "The uncle is stern and critical.":
                "Not quite, give it another go."
                jump level7_task
            "The aunt is nurturing and supportive.":
                "Not quite, give it another go."
                jump level7_task
            "The uncle is playful and encouraging.":
                "Not quite, give it another go."
                jump level7_task
    "After selecting and explaining the quote, the protagonist defeats the second minion."


label level8:
    "The protagonist stands before the parchment once more, ready to finish the paragraph."
    mentor "A strong concluding sentence wraps up your ideas and reinforces your argument. What will yours be?"

    label level8_task:
        menu:
            "The aunt is controlling and dismissive.":
                "Nicely done!"
            "The uncle is stern and critical.":
                "Not quite, give it another go."
                jump level8_task
            "The aunt is nurturing and supportive.":
                "Not quite, give it another go."
                jump level8_task
            "The uncle is playful and encouraging.":
                "Not quite, give it another go."
                jump level8_task
    "You follow the mentor."
    mentor "Now that you have gotten a taste of what it was like to structure a simple paragraph essay, it is now your turn."
    pov "But I am not ready yet."
    mentor "You won't know unless you actually try."
    mentor "using the example essay we came up with, write your own, this time, on Teddy from \"The Fal of a City\""
    pov "Here goes..."

    jump level9

label level9:

#     character writes their own essay
    mentor "I see you have finally finished, care to go through a checklist with me?"
    pov "Ok."
    # show essay


label level10:
    return






# you arent here because you are the chosen one, you are here for the journey, and that is all that matters.