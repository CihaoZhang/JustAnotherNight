﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

label start:
    # Load the background, music, and character
    scene bg_city_night
    play music "soft_night_theme.mp3"
    show girl_smiling

    e "Hi there! I’m so glad you could join me tonight. It feels like ages since I’ve had a chance to just... talk to someone like this."

    # Setting the conversational tone
    e "You know, it’s crazy how quiet the city gets at this hour. It’s like everything just pauses for a little while. Tonight was... different, don’t you think?"

    # Present the first set of choices
    menu:
        "It really did. I can’t remember the last time I felt this relaxed.":
            e "I know, right? It’s like the whole world decided to take a deep breath."
        "Yeah, it’s nights like these that remind me how much I need to slow down more often.":
            e "Exactly. I think we all need nights like this to just... catch up with ourselves."
        "Completely. There’s something about the stillness that just puts things into perspective.":
            e "Totally. It’s like the world is whispering secrets we’re usually too busy to hear."

    # Transition to the next question
    e "I wonder if we spend enough time actually noticing things—like, the little details around us. Do you ever find yourself realizing something you never saw before?"

    # Present the second set of choices
    menu:
        "Oh, definitely. It’s easy to miss the small things when you’re moving too fast.":
            e "Right? I feel like life has all these hidden treasures we just overlook sometimes."
        "All the time. I think we just don’t take enough time to really look at what’s around us.":
            e "Yeah, and it’s such a shame because there’s so much beauty everywhere."
        "That’s true. It’s amazing what you can notice when you slow down.":
            e "It really is. Like tonight—the city feels so different when we actually pay attention."

    # Third question and responses
    e "Yeah, sometimes I think we get caught up in everything and forget to appreciate what’s right in front of us. It’s funny—sometimes the answers we’re looking for are in the simple stuff. Do you find yourself always chasing after big goals and constantly feeling disappointed when you don’t achieve them?"

    menu:
        "I think I’m always looking ahead, but I’m starting to realize that the small moments really do matter.":
            e "That’s such a good realization. It’s like those little moments are the glue holding everything together."
        "I’m all about the bigger picture, but I’m learning to appreciate the small wins along the way.":
            e "That’s a great way to look at it. The big picture is important, but the journey is what makes it worth it."
        "I think both are important. Chasing big things keeps me going, but the small moments help me appreciate everything.":
            e "Balance. That’s the key, isn’t it? You seem like someone who’s got their priorities figured out."

    # Fourth question and responses
    e "That makes sense. I guess it’s all about balance, right? Finding time for the things that truly matter. Speaking of which, what’s something that really makes you feel fulfilled? Like, something that makes you feel like you’re on the right path?"

    menu:
        "I think it’s when I’m working on something that really excites me, but I don’t know why. There’s beauty in the absurdity of things.":
            e "That’s such a beautiful way to put it. I love that you see beauty in the unexpected."
        "For me, it’s when I’m actively creating a better version of myself. I like knowing that I am giving myself the best chance to become great.":
            e "That’s so inspiring. You’re really giving yourself a gift by thinking that way."
        "I think it’s when I’m creating something or helping someone, when I know I’ve made an impact in someone’s life. That’s when I feel most fulfilled.":
            e "That’s so wonderful. Making a difference like that is such a meaningful way to live."

    # Soft transition to Act 2
    e "You’ve really got me thinking about some deep stuff tonight. It’s nice to talk like this. I feel like I’m learning so much about you."

    return

label act_2_start:
    # Opening Scene
    # Load a calm and reflective setting with appropriate background and music.

    # Character sets the tone for a thoughtful and intimate conversation.

    # Player chooses their initial thought from a set of static options.

    # Transition to deeper conversation, referencing earlier Act 1 answers.

    # Introduce AI-generated dialogue:
    # - Generate dynamic follow-up questions based on user input and context.
    # - Ensure responses build on the player’s earlier answers.

    # Player answers questions via menu choices or text input.

    # AI generates further exploration or feedback based on the user’s response.

    # Scene concludes with encouragement and a transition to Act 3.
    return


label act_3_start:
    # Opening Scene
    # Set a reflective and supportive tone with a suitable background and music.

    # Character opens with an encouraging statement to set the stage.

    # AI generates the introduction for personalized guidance based on user context.

    # Use a loop to:
    # - Generate dynamic AI-driven questions or guidance.
    # - Accept player responses (choices or text input).
    # - Update user context dynamically and generate follow-ups.

    # Include conditions to check if the player feels ready to move forward.

    # Scene concludes with a supportive and hopeful closing statement. One of many other endings
    return