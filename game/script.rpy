# font
# self point
# maybe add transitions of pov fighting with minion

define pov = Character("[povname]",default="Me", image="prot", color="#6f22e3")
define mystery = Character("???")
define mentor = Character("Mentor", color="#4aeb42")
define gui.text_color = '#000000'
define gui.interface_text_color = '#000000'

init:
    transform flip:
        xzoom -1.0

label start: # COMPLETE
    python:
        score = 0
        total_score = 9
        sidequest = False

    scene bg forest
    centered "IF AT ANY TIME YOU CAN NOT FINISH, SAVE THE GAME BY CLICKING \"esc\" ON YOUR KEYBOARD." (what_color="#FFFFFF", what_size=40, what_font="AndyBold.ttf")
    centered "Your overall score has an impact on outcome of story." (what_color="#FFFFFF", what_size=40, what_font="AndyBold.ttf")

    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
             povname = "Me"

    narrator "You wake up from a deep sleep, disoriented, your mind a blank slate..."
    show rogue
    pov "\"Where am I?\""
    "*You look around, trying to piece together your surroundings.*"
    show rogue


    menu:
        "Explore":
            "You walk through the eerie landscape, noticing the chaotic nature of the surroundings—trees."
            "You hear a rustling sound from a nearby bush..."
            pov "WHO'S THERE?" with hpunch
            "The rustling grows louder, and then, emerging from the bushes with a graceful stride, is an older figure clad in flowing robes, adorned with quill and parchment motifs."
            show rogue at left
            with move
            show mentor at right
            with move


        "Wait":
            "You sit quietly, trying to gather their thoughts."
            pause(2.0)
            show rogue at left
            with move
            show mentor at right
            with move
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

    label choice_intro:
        mentor "Are you ready [povname]?"

    menu:
        "Yes":
            mentor "Great, then our journey together shall begin!"
            mentor "Follow me."
            pause(3.0)
            jump level1
        "How do you know my name?":
            mentor "I know many things..."
            jump choice_intro


label level1: # COMPLETE
    show bg portal
    with fade

    "Your feet are sore and your mouth is dry. Time seems to work differently in this universe. You felt as though you have been walking for hours."
    "You and your Mentor stand in front of a grand, mystical portal that swirls with images from the story \"The Fall of a City.\""
    mentor "This seems to be where all the Confusion and Chaos originates from."
    mentor "Your first task is to identify two key character traits of Teddy’s uncle. Their traits hold the power to influence the structure of your paragraph."
    "The portal shows scenes from the story, with the uncle interacting with Teddy."
    "You see the way they speak and act—what do you observe?"

    $ wrong = False
    label level1_task:
        menu:
            "Teddy’s uncle is both dismissive and condescending.":
                if not wrong:
                    $ score += 1
                "The portal reacts. It turns ocean blue. You can't seem to see through to the other side."
                "Do you choose to enter?"
                menu:
                    "Yes":
                        pov "Have you ever been through one of these? Where would we end up?"
                        mentor "Theres only one way to find out. "
                        "You hesitantly step in, one foot at a time."
                        jump level2
                    "No":
                        "The mentor pushes you. You trip on a rock and face plant in. Better luck next time..."
                        jump level2
            "Teddy’s uncle is both nurturing and supportive.":
                "Not quite, give it another go."
                $ wrong = True
                jump level1_task
            "Teddy’s uncle is dismissive and protective.":
                "Not quite, give it another go."
                $ wrong = True
                jump level1_task
            "Teddy’s uncle is both playful and imaginative.":
                "Not quite, give it another go."
                $ wrong = True
                jump level1_task

label level2: # COMPLETE
    show bg castle
    with fade

    "The portal closes behind you, disappearing altogether, without leaving a single trace behind." with hpunch
    "You look around, gray brick walls, ceiling tens of meters high, you appear to be in some sort of castle."
    pause(3.0)
    "A magical Aura leads you to a large, ancient writing desk with a blank parchment lying on it."
    show mentor at right
    show rogue at left
    with move

    label level2_replay:
        mentor "A strong paragraph needs a clear and focused topic sentence. Use the traits you've identified earlier to create one. (Teddy’s uncle is both dismissive and condescending)"
        menu:
            "What was that again?":
                jump level2_replay
            "Got it!":
                pass

    $ sentence = renpy.input("Type away: ", length=500)

    mentor "After finishing, you may turn to your peers and have them enter a rating between 1-5."

    $ wrong = False
    label level2_task:
        centered "[sentence]" (what_color="#FFFFFF", what_size=44)
        $ rating = renpy.input("Rate from 1-5: ", length=1)
        if not (rating == "1" or rating == "2" or rating == "3" or rating == "4" or rating == "5"):
            "Invalid input."
            jump level2_task
        if rating == "1" or rating == "2" or rating == "3":
             $ wrong = True
        else:
            if not wrong:
                $ score += 1

    "The mystery force judges your writing, the parchment glows slightly."
    "You hear movement, turning back, the stone wall shifts, creating an exit."
    pov "Woah! I have no words... this place is crazy."
    mentor "Yes, thank you. Much time has been put into this..."
    pov "..."
    mentor "You'll understand."
    "You proceed followed by your mentor."

    jump level3


label level3: # not complete, finish questions
    show bg shrooms
    show mentor at right
    show rogue at left
    with fade
    pause(1.0)
    show minion
    with fade

    pov "WHAT is that?"
    mentor "That is a Chaos & Confusion Minion that embodies \"Vague Argument.\""
    mentor "To defeat it, you must clearly state a point using the PEE method: Point, Evidence, and Explanation."

    label level3_replay:
        mentor "Out of the following, select the best answer which states a point clearly and concisely, using the first of the previous two traits from Teddy's uncle. (dismissive)"
        menu:
            "What was that again?":
                jump level3_replay
            "Got it!":
                pass

    $ attempts = 0

    label level3_task:
        menu:
            "Notably, the uncle's dismissive nature occurs when he mocks Teddy’s imaginative play.":
                if attempts > 1:
                    "You barely made it out alive."
                else:
                    $ score += 1
                "Your statement weakens the minion, but it’s still standing."
            "Notably, the uncle's dismissive nature occurs when he talks about how all children should stop playing games and focus on schoolwork.":
                "Not quite, give it another go."
                $ attempts += 1
                jump level3_task
            "Notably, the uncle's dismissive nature occurs when he helps Teddy build a fort but criticizes its design.":
                "Not quite, give it another go."
                $ attempts += 1
                jump level3_task
            "Notably, the uncle's dismissive nature occurs when he tells Teddy, \"You should be playing outside like a real boy.\"":
                "Not quite, give it another go."
                $ attempts += 1
                jump level3_task
    jump level4

label level4: # COMPLETE
    mentor "Don't worry kid, I have another trick up my sleeves."
    mentor "Riddle me this: Dawn comes after night like ________ comes after Point."

    $ wrong = False
    label level4_question:
        menu:
            "Explanation":
                mentor "Maybe if you used more than just two fingers..."
                $ wrong = True
                jump level4_question
            "Evidence":
                mentor "Well spoken! Let's defeat the minion using that."
        if not wrong:
            $ score += 1

    label level4_replay:
        mentor "Now tell me, what is a quotation that best demonstrates the point you’ve identified previously? (mocking Teddy’s imaginative play)"
        menu:
            "What was that again?":
                jump level4_replay
            "Got it!":
                pass

    "You instinctively take our the Magical Quill."

#     $ wrong = False
#     label level4_task:
#         menu:
#             "“Look what you’re doing, for heaven’s sake!”":
#                 "Not quite, give it another go."
#                 $ wrong = True
#                 jump level4_task
#             "“He’s got his head in the clouds again.”":
#                 "Not quite, give it another go."
#                 $ wrong = True
#                 jump level4_task
#             "“The next thing we know, you’ll be wanting us to put skirts on you!”":
#                 "Guided by your hands, the quill moves swiftly across the air."
#             "“They looked pretty much like paper dolls to me.”":
#                 "Not quite, give it another go."
#                 $ wrong = True
#                 jump level4_task
#         if not wrong:
#             $ score += 1
#     "It further weakens the minion."

    $ wrong = False
    label level4_task:
        menu:
            "“Look what you’re doing, for heaven’s sake!”":
                "Not quite, give it another go."
                $ wrong = True
                jump level4_task
            "“He’s got his head in the clouds again.”":
                "Not quite, give it another go."
                $ wrong = True
                jump level4_task
            "“The next thing we know, you’ll be wanting us to put skirts on you!”":
                "Guided by your hands, the quill moves swiftly across the air."
            "“They looked pretty much like paper dolls to me.”":
                "Not quite, give it another go."
                $ wrong = True
                jump level4_task
        if not wrong:
            $ score += 1
    "It further weakens the minion."

    mentor "Excellent! But to truly defeat the minion, you must explain how... "
    "The mentor loses track of what he was going to say."

    jump sidequest

label sidequest: # COMPLETE
    "All of a sudden, everything around you freezes."
    show bg bw
    with dissolve
    "The vibrant colors of Literaria dimmed, and the swirling winds came to a halt. The world, once alive with energy, now stood eerily still. "
    pov "What’s happening? Why is everything stopped?" with hpunch
    mentor "The Mentor's eyes, usually so full of wisdom and warmth, now held a deep, almost somber intensity. They took a step closer to you, the silence between you growing heavier with each passing moment."
    "There is something you need to know, something I have kept hidden until now."
    pov "What do you mean? What’s going on?"
    mentor "I am not just a guide in this world, not just a teacher showing you the ways of Literaria. I am its creator."
    "The words hang in the air, their weight sinking in slowly. The Mentor—your trusted companion throughout this journey—created Literaria? The realization stirs a mix of emotions within you: awe, confusion, and a hint of fear."
    pov "You… created this world? But why? Why reveal this to me now?"
    mentor "Literaria is more than just a land of stories; it is a delicate balance of knowledge, creativity, and truth. I brought it into existence to help others learn, to give life to the lessons within stories."
    "The Mentor pauses, looking into your eyes with a seriousness that makes your heart race."
    mentor "I will give you two options. Either forget the ugly truth or keep fighting knowing everything around you is planned and fictional."
    "The Mentor steps back slightly, raising their hand as two glowing orbs appear between you. Each orb pulses with a different energy, radiating a sense of immense power and responsibility."

    "(Pick wisely as this is a determining factor of the outcome of your journey)"
    menu:
        "Keep fighting knowing everything around you is preplanned and has a predetermined outcome.":
            mentor "It might be hard at first, but I thank you for understanding."
            "The world reverts back to normal. You can feel the cool breeze of the wind, it flows around and you feel comfort."
            mentor "Now, where were we?"
            mentor "To truly defeat the minion, you must explain how this evidence supports your point."
            $ sidequest = True
        "Forget what happened.":
            mentor "Very well. Although hard to make, the choice is indeed a valid one at times."
            "Your mind turns blank for a second."
            pause(3.0)
            mentor "Excellent! But to truly defeat the minion, you must explain how this evidence supports your point."
    show bg shrooms
    with dissolve
    jump level5

label level5: # COMPLETE
    pov "Understood."
    "You face the now weakened minion, ready for the final blow."

    label level5_replay:
        mentor "Now, explain how the quote you selected proves the character trait (“The next thing we know, you’ll be wanting us to put skirts on you!”). Choose the best answer."
        menu:
            "What was that again?":
                jump level5_replay
            "Got it!":
                pass

    $ wrong = False
    label level5_task:
        menu:
            "By praising Teddy’s creation, the uncle encourages his imaginative world, boosting his creative expression.":
                "Guided by your hands, the quill moves swiftly across the air."
                $ wrong = True
                jump level5_task
            "By ignoring Teddy’s creation, the uncle passively supports his imaginative world, allowing it to flourish.":
                "Not quite, give it another go."
                $ wrong = True
                jump level5_task
            "By belittling Teddy’s creation, the uncle invalidates Teddy’s imaginative world, discouraging his creative expression.":
                "Well answered!"
            "By belittling Teddy’s artistic talents, the uncle invalidates his drawing skills, discouraging his pursuit of art.":
                "Not quite, give it another go."
                $ wrong = True
                jump level5_task
        if not wrong:
            $ score += 1
    hide minion
    with dissolve
    "The explanation delivers a decisive strike, defeating the Chaos & Confusion Minion."
    "Well done! But your journey is far from over."
    jump level6




label level6: # COMPLETE
    show bg grass
    with fade

    "With the first minion defeated, the protagonist moves forward, encountering another representing \"Weak Transitions.\""
    show skeleton
    with fade

    mentor "To move smoothly between ideas, a strong transition is key. Let’s identify your second character trait and introduce it."
    label level6_replay:
        mentor "Which of the following transitions make the sentences flow while also strengthening the root argument, adding a second point?"
        menu:
            "What was that again?":
                jump level6_replay
            "Got it!":
                pass

    $ wrong = False
    label level6_task:
        menu:
            "Moreover, the uncle's condescending attitude is evident when he says...":
                "Very well, amazing choice. You won't even need me at this point!"
            "The uncle's condescending attitude is evident when he says...":
                "Not quite, give it another go."
                $ wrong = True
                jump level6_task
            "Condescending is also an attitude shown by the uncle...":
                "Not quite, give it another go."
                $ wrong = True
                jump level6_task
            "To add, the uncle's mean attitude towards Teddy is evident...":
                "Not quite, give it another go."
                $ wrong = True
                jump level6_task
        if not wrong:
            $ score += 1
    "Again, The Transition and Point only weakens the new minion."
    pov "I guess we'll have to follow up with Evidence and Explanation."

    jump level7

label level7: # COMPLETE
    label level7_replay:
        mentor "Which of the following is the best choice when transitioning from the previous phrase, remember to think back to PEE. (Moreover, the uncle's condescending attitude is evident when he says)"
        menu:
            "What was that again?":
                jump level7_replay
            "Got it!":
                pass

    $ wrong = False
    label level7_task:
        menu:
            "‘You’re wasting your time with those toys,’ implying that Teddy should outgrow his creative pursuits. This remark not only undermines Teddy’s imagination but also implies that creativity is childish and unworthy of respect."(what_size=22):
                "Not quite, give it another go."
                $ wrong = True
                jump level7_task
            "\"You're too old for such nonsense,\" implying that Teddy should outgrow his creative pursuits. This remark not only undermines Teddy’s imagination but also implies that creativity is childish and unworthy of respect.":
                "Nicely done, good choice!"
#             "‘Only babies build forts,’ implying that Teddy should outgrow his creative pursuits. This remark not only undermines Teddy’s imagination but also implies that creativity is childish and unworthy of respect.":
#                 "Not quite, give it another go."
#                 $ wrong = True
#                 jump level7_task
            "‘Why don’t you read a book instead?’ implying that Teddy should outgrow his creative pursuits. This remark not only undermines Teddy’s imagination but also implies that creativity is childish and unworthy of respect.":
                "Not quite, give it another go."
                $ wrong = True
                jump level7_task
        if not score:
            $ score += 1
    hide skeleton
    with dissolve
    "After selecting and explaining the quote, the protagonist defeats the second minion."
    jump level8


label level8: # COMPLETE

    show bg end
    with fade

    mentor "Having gone through everything, it is time to finish the paragraph."
    label level8_replay:
        mentor "A strong concluding sentence wraps up your ideas and reinforces your arguments. What will yours be?"
        menu:
            "What was that again?":
                jump level8_replay
            "Got it!":
                pass

    $ wrong = False
    label level8_task:
        menu:
            "Overall, the uncle’s neutral stance neither discourages nor encourages Teddy’s creative endeavors, leaving him to develop independently.":
                "Not quite, give it another go."
                $ wrong = True
                jump level8_task
            "Overall, the uncle’s playful and humorous attitude allows Teddy to explore his imagination freely without judgment.":
                "Not quite, give it another go."
                $ wrong = True
                jump level8_task
            "Overall, the uncle’s supportive and encouraging behaviors help nurture Teddy’s imaginative spirit and foster creativity.":
                "Not quite, give it another go."
                $ wrong = True
                jump level8_task
            "Overall, the uncle’s dismissive and condescending behaviors work together to stifle Teddy’s imaginative spirit and reinforce rigid expectations of maturity and conformity.":
                "Good job!"

        if not wrong:
            $ score += 1

    mentor "Now that you have gotten a taste of what it was like to structure a simple paragraph, it is now your turn."
    pov "But I am not ready yet."
    mentor "You won't know unless you actually try."
    mentor "Using the following exemplar paragraph we came up with, write your own, this time, on Teddy from \"The Fall of a City.\""
    pov "Here goes... (I should write my paragraph about Teddy in a Google docs...)"

    label level8_exemplar:
#         centered "Teddy’s uncle in The Fall of a City is portrayed as both dismissive and condescending, which ultimately diminishes Teddy’s sense of imagination and self-worth. Notably, the uncle's dismissive nature occurs when he mocks Teddy’s imaginative play, stating, “Only fools and cowards build forts out of paper boxes” (Nowlan). By belittling Teddy’s creation, the uncle invalidates Teddy’s imaginative world, discouraging his creative expression. Moreover, the uncle's condescending attitude is evident when he says, “You're too old for such nonsense,” implying that Teddy should outgrow his creative pursuits. This remark not only undermines Teddy’s imagination but also implies that creativity is childish and unworthy of respect. In the end, the uncle’s dismissive and condescending behaviors work together to stifle Teddy’s imaginative spirit and reinforce rigid expectations of maturity and conformity." (what_color="#FFFFFF", what_size=40)
        show screen Exemplar
        ""
        hide screen Exemplar
        menu:
            "View exemplar.":
                jump level8_exemplar
            "Finished.":
                hide screen Exemplar

    jump level9

label level9:




    mentor "I see you have finally finished, care to go through a checklist with me?"
    pov "Ok."

    centered "Feel free to switch over to the doc if you need another look at your paragraph. This part will count towards your total score." (what_color="#000000", what_size=44, what_font="AndyBold.ttf")

    $ paragraph_points = 0
    $ paragraph_total_points = 8

    centered "Identified at least two character traits of Teddy?" (what_color="#000000", what_size=44, what_font="AndyBold.ttf")
    menu:
        "Yes":
            $ paragraph_points += 1
        "No":
            pass

    centered "Included a PEE for each of the character traits?" (what_color="#000000", what_size=44, what_font="AndyBold.ttf")
    menu:
        "Yes":
            $ paragraph_points += 1
        "No":
            pass
    centered "Structured the paragraph properly? (Topic sentence, PEE, PEE, concluding sentence)" (what_color="#000000", what_size=44, what_font="AndyBold.ttf")
    menu:
        "Yes":
            $ paragraph_points += 1
        "No":
            pass
    centered "Not included any first person pronouns." (what_color="#000000", what_size=44, what_font="AndyBold.ttf")
    menu:
        "No, there are no first person pronouns in the paragraph.":
            $ paragraph_points += 1
        "Yes, there are first person pronouns present.":
            pass
    centered "Properly cited quotes in MLA format." (what_color="#000000", what_size=44, what_font="AndyBold.ttf")
    menu:
        "Yes":
            $ paragraph_points += 1
        "No":
            pass
    centered "Effectively used transition words throughout the paragraph." (what_color="#000000", what_size=44, what_font="AndyBold.ttf")
    menu:
        "Yes":
            $ paragraph_points += 1
        "No":
            pass
    centered "Paragraph is clear, organized, and easy to follow." (what_color="#000000", what_size=44, what_font="AndyBold.ttf")
    menu:
        "Yes":
            $ paragraph_points += 1
        "No":
            pass
    centered "No grammar, spelling, and/or punctuation errors." (what_color="#000000", what_size=44, what_font="AndyBold.ttf")
    menu:
        "No, the sentence is clear of any grammar, spelling, and punctuation errors.":
            $ paragraph_points += 1
        "Yes, there are mistakes present.":
            pass


    jump level10


label level10:
    python:
        user_score = score + paragraph_points
        total_combined_score = total_score + paragraph_total_points

    if (user_score > 13):
        jump triumphoforder
    elif user_score > 9:
        jump balanceofwords
    else:
        jump fallintochaos

    label triumphoforder:
        show bg triumph
        with fade
        "You stand tall, having mastered every challenge. Chaos & Confusion, weakened and trembling, slowly fade into nothingness."
        pov "It’s over. The chaos is gone."
        mentor "Indeed. You’ve done it. You have restored order and clarity to Literaria."
        if sidequest:
            mentor "Say, remember what I told you earlier, the truth about Literaria?"
            pov "Yes. What now?"
            mentor "Well, it is time to make the decision, you have proved to myself that you yourself, is capable of guarding this land."
            menu:
                "Take over Literaria for all its glory.":
                    "The Mentor smiles gently, the edges of their form starting to fade."
                    mentor "Then you no longer need my guidance. You have learned all I can teach you, and now you are ready to pass on this knowledge to others."
                    pov "What do you mean?"
                    "The Mentor smiles gently, the edges of their form starting to fade."
                    mentor "You no longer need my guidance. You have learned all I can teach you, and now you are ready to pass on this knowledge to others."
                    pov "Wait, you’re leaving?"
                    mentor "It’s time. I have been the guide for many, but the world needs new mentors. You are ready for that role."
                    "The Mentor fades into the pages of a book, leaving the protagonist standing alone, but with a new sense of purpose. A young student approaches, curious about the world of Literaria."
                    centered "ENDING 1/5" (what_color="#FFFFFF", what_size=40, what_font="AndyBold.ttf")
                    jump endscreen

                "Walk away...":
                    "You look at the Magical Quill, feeling its immense power. But something within you stirs—a pull toward a different path."
                    pov "I’m not ready to stay here. This isn’t my place. I belong elsewhere."
                    "The Mentor’s eyes widen slightly in surprise, but then he smiles, understanding dawning in his expression."
                    mentor "You’ve learned much, more than you realize. But perhaps your journey doesn’t end here. Sometimes, the greatest wisdom is knowing when to step away."
                    "The Mentor steps back, the world around you beginning to shimmer and blur."
                    mentor "If you choose to leave, Literaria will continue on its own. But the knowledge you’ve gained here will go with you, shaping you in ways beyond this world. Perhaps... this was never about Literaria at all, but about your own growth."
                    "As the words hang in the air, the scene begins to dissolve. The Mentor’s voice echoes softly as everything fades."
                    mentor "Farewell, traveler. May the words you’ve mastered here guide you wherever you go."
                    "Suddenly, the protagonist wakes up in their own bed, sunlight streaming through the window. The magical world of Literaria is gone, replaced by the familiar sights and sounds of the real world. But something feels different—a newfound clarity, a deeper understanding."
                    "You’ve returned to reality, but Literaria still lingers in your heart. The skills you’ve gained, the lessons you’ve learned—they remain, ready to be applied in your life."
                    centered "Sometimes, the real adventure begins once the dream ends. The world you now face is yours to shape, using the knowledge you’ve earned along the way." (what_color="#FFFFFF", what_size=40, what_font="AndyBold.ttf")
                    centered "ENDING 2/5" (what_color="#FFFFFF", what_size=40, what_font="AndyBold.ttf")
                    jump endscreen

        "The world around you brightens. You stand atop a grand library tower, overlooking a land where words and paragraphs flow like rivers of knowledge."
        mentor "You are now the Master of Composition. Remember, the power of structure and clarity is not just in writing but in all things. What you’ve learned here will guide you, both in Literaria and in the world beyond."
        pov "I didn’t just defeat chaos… I learned how to communicate with purpose."
        "As you gaze upon the restored Literaria, you feel the weight of your accomplishment. A message echoes in your mind: Structure and clarity are the keys to success, both in writing and in life."
        centered "ENDING 3/5" (what_color="#FFFFFF", what_size=40, what_font="AndyBold.ttf")
        jump endscreen

    label balanceofwords:
        show bg balance
        with fade
        "Chaos & Confusion have been weakened, but remnants of disorder still linger. Literaria is partially restored—some areas flourish, while others remain clouded in shadow."
        pov "I tried my best, but it wasn’t enough to completely restore the world."
        mentor "You accomplished much. Literaria is thriving in many places, but remember: perfection isn’t the goal. The process of improvement never truly ends."
        "The protagonist looks out at the partially restored world, with pockets of chaos still swirling in the distance."
        pov "So, there’s still more to learn?"
        mentor "Always. You’ve taken important steps forward, but writing—and learning—are ongoing journeys. Keep refining your skills, and one day, Literaria will fully shine under your care."
        centered "ENDING 4/5" (what_color="#FFFFFF", what_size=40, what_font="AndyBold.ttf")
        jump endscreen

    label fallintochaos:
        show bg lost
        with fade
        "Chaos & Confusion, now strengthened by the protagonist’s failure to grasp key writing principles, swirl in the air. The once vibrant world of Literaria is slowly consumed by darkness."
        pov "No… I can’t stop them."
        "Fragments of sentences and broken paragraphs rise up, engulfing the land. The Mentor watches, their expression somber."
        mentor "This is what happens when the basics are ignored. Without evidence, explanation, or proper structure, even the strongest argument falls apart."
        pov "I… I wasn’t careful enough."
        "The world continues to unravel, spiraling into chaos."
        mentor "Remember this feeling, and take it with you. Diligence, attention to detail—these are the tools to keep chaos at bay. There is always a chance to rebuild, but first, you must learn from your mistakes."
        centered "ENDING 5/5" (what_color="#FFFFFF", what_size=40, what_font="AndyBold.ttf")
        jump endscreen

label endscreen:
    $ display_score = f"{score}/{total_score}"
    $ display_para_score = f"{paragraph_points}/{paragraph_total_points}"

    show bg end
    show screen StatsUI
    with fade
    "You've completed the game, if you would like to save your results, please take a screenshot!"
    "Press \"esc\" and save your game into a slot so you can show off your results!"

    menu:
        "Show stats again.":
            jump endscreen
        "Exit game.":
            return









# you arent here because you are the chosen one, you are here for the journey, and that is all that matters.