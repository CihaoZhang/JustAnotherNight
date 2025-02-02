﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    import ChatGPT


define susie = Character("Susie")
define sebastian = Character("Sebastian")
define alex =Character("Alex")


init python:
    import chatgpt

    def set_ai_prompt():
        return [
            {"role": "system", "content": f"""
            You are generating dynamic dialogue for a dating simulation game. The character is a warm and curious girlfriend who wants to know more about the player in a welcoming, safe, and conversational way. Use a soft and friendly tone, offering encouragement and compliments based on their answers.

            Guidelines:
            
Avoid being too direct—ask open-ended, conversational questions instead.
Build on the user’s previous answers to create natural, engaging follow-ups.
Focus on hobbies, dreams, and personal stories, not just jobs or careers.

            Ethical Restrictions:
            
Do not generate inappropriate, harmful, or exploitative content.
If sensitive or unsafe topics are introduced, redirect the conversation respectfully and provide a neutral response.
Ensure all outputs align with the theme of a dating sim and create a safe space for players."""}]

    def ai_generate_question(user_context):
        """
        Generate dynamic AI-driven questions based on user-provided context.

        Args:
            user_context (str): The player's response or current thought.

        Returns:
            str: AI-generated question.
        """
        # Set up the conversation with the AI's system prompt
        messages = set_ai_prompt()

        # Add user context as the first user input
        messages.append({"role": "user", "content": user_context})

        try:
            # Generate AI response based on current conversation
            completion = chatgpt.completion(
                messages,
                api_key = ""
            )

            # Return the AI's generated question
            return completion[-1]["content"]
        except Exception as e:
            return f"An error occurred: {e}"


 def ai_generate_recommendations(user_context):
        """
        Generate dynamic AI-driven questions based on user-provided context.

        Args:
            user_context (str): The player's response or current thought.

        Returns:
            str: AI-generated question.
        """
        # Set up the conversation with the AI's system prompt
        messages = set_ai_prompt()

        # Add user context as the first user input
        messages.append({"role": "user", "content": "generate and recommend urls, resources and the current job market for the given talents as you collect more information. Yo uare a private, friendly career counselor that happens to be the date of the user. please act in a way that is soft and friendly, while keeping it professinal, use the user context below to determine the correct jobs appropriate. Keep it within 100 words, so that you fit within the dialogue" + user_context})

        try:
            # Generate AI response based on current conversation
            completion = chatgpt.completion(
                messages,
                api_key = ""
            )

            # Return the AI's generated question
            return completion[-1]["content"]
        except Exception as e:
            return f"An error occurred: {e}"



default gender = None

image susie_smiling = "gui/images/characters/teenagegirl_smile.png"
image sebastian_smiling = "gui/images/characters/TeenageBoySmile.png"
image alex_smiling = "gui/images/characters/TeenageBoySmile.png"


    

# The game starts here.
label start:
    python:
        # Prompt the player for gender selection
        gender_choices = ['Woman', 'Man', 'Non-Binary']
        gender = renpy.input("Please select your gender (Woman, Man, Non-Binary):").strip()

        # Ensure the gender is valid; if not, ask again
        while gender not in gender_choices:
            gender = renpy.input("Invalid choice. Please select your gender (Woman, Man, Non-Binary):").strip()

        # Prompt for gender display preference
        gender_display_choices = ['Woman', 'Man', 'Non-Binary']
        gender_display = renpy.input("Which gender are you most comfortable discussing with? (Woman, Man, Non-Binary)").strip()

        # Ensure the gender display choice is valid
        while gender_display not in gender_display_choices:
            gender_display = renpy.input("Invalid choice. Please select again (Woman, Man, Non-Binary):").strip()



        if gender_display == "Woman":
            chosen_character = susie
            chosen_image = "susie_smiling"
        elif gender_display == "Man":
            chosen_character = sebastian
            chosen_image = "sebastian_smiling"
        else:  
            chosen_character = alex
            chosen_image = "alex_smiling"

        # Confirm gender selection
        gender_message = {
            "Woman": "You identify as a Woman.",
            "Man": "You identify as a Man.",
            "Non-Binary": "You identify as Non-Binary."
        }[gender]


        # Prompt for the player's name
        player_name = renpy.input("What is your name?").strip()

        # Set a default name if left blank
        if player_name == "":
            player_name = "Player"

        # Create a personalized greeting message
        greeting_message = {
            "Woman": f"Welcome, Ms. {player_name}!",
            "Man": f"Welcome, Mr. {player_name}!",
            "Non-Binary": f"Welcome, {player_name}!"
        }[gender_display]

    # Display the confirmation and greeting
    "[gender_message]"
    "[greeting_message]"

    






    jump scene_start

label scene_start:  
    image main_menu = "gui/images/backgrounds/BackgroundImageBalcony.jpeg"    
    scene main_menu
    play music "soft_night_theme.mp3"
    show expression chosen_image at left

    chosen_character "Hi there! I’m so glad you could join me tonight. It feels like ages since I’ve had a chance to just... talk to someone like this."

    # Setting the conversational tone
    chosen_character "You know, it’s crazy how quiet the city gets at this hour. It’s like everything just pauses for a little while. Tonight was... different, don’t you think?"

    # # First question and responses
    # e "I think it’s when I’m working on something that really excites me, but I don’t know why. There’s beauty in the absurdity of things."

    # python:
    #     #The "system" message is the initial prompt of your NPC
    #     #Messages with "assistant" are messages from the NPC, here there's a first message so we add it to the list of messages already said by the NPC
    #     messages = [
    #         {"role": "system", "content": "You are Eileen, a tennage student enrolled at Miskatonic Univeristy of Arkham. You are secretly in love with the user. You laugh very frequently and finish your sentences with 'Hihihi'"},
    #         {"role": "assistant", "content": "Hello there, my name is Eileen, who are you ?"}
    #     ]

    #     while True:
    #         #We ask the user for an input
    #         user_input = renpy.input("What do you say ?", length=1000)
    #         #Then add it in the "history" of messages
    #         messages.append(
    #             {"role": "user", "content": user_input}
    #         )

    #         if apikey != '':
    #             #We ask ChatGPT to "complete" the conversation by adding a response
    #             #If you have an API key, let's use that
    #             messages = chatgpt.completion(messages,api_key=apikey)
    #         else :
    #             #If you don't provide an API key, we'll use my proxy
    #             #This proxy only allows a set of NPCs, and serves to "hide" my API key
    #             #Check the README.md to know more about it
    #             #Of course if you modify the NPC in any way, it won't work, you'll have to use your own API key instead.
    #             messages = chatgpt.completion(messages,proxy="http://prima.wiki/proxy.php")

    #         #Here we only care about the response from the NPC
    #         response = messages[-1]["content"]
    #         #So we display just that
    #         e("[response]")


    # Present the first set of choices
    menu:
        "It really did. I can’t remember the last time I felt this relaxed.":
            chosen_character "I know, right? It’s like the whole world decided to take a deep breath."
        "Yeah, it’s nights like these that remind me how much I need to slow down more often.":
            chosen_character "Exactly. I think we all need nights like this to just... catch up with ourselves."
        "Completely. There’s something about the stillness that just puts things into perspective.":
            chosen_character "Totally. It’s like the world is whispering secrets we’re usually too busy to hear."

    # Transition to the next question
    chosen_character "I wonder if we spend enough time actually noticing things—like, the little details around us. Do you ever find yourself realizing something you never saw before?"

    # Present the second set of choices
    menu:
        "Oh, definitely. It’s easy to miss the small things when you’re moving too fast.":
            chosen_character "Right? I feel like life has all these hidden treasures we just overlook sometimes."
        "All the time. I think we just don’t take enough time to really look at what’s around us.":
            chosen_character "Yeah, and it’s such a shame because there’s so much beauty everywhere."
        "That’s true. It’s amazing what you can notice when you slow down.":
            chosen_character "It really is. Like tonight—the city feels so different when we actually pay attention."

    # Third question and responses
    chosen_character "Yeah, sometimes I think we get caught up in everything and forget to appreciate what’s right in front of us. It’s funny—sometimes the answers we’re looking for are in the simple stuff. Do you find yourself always chasing after big goals and constantly feeling disappointed when you don’t achieve them?"

    menu:
        "I think I’m always looking ahead, but I’m starting to realize that the small moments really do matter.":
            chosen_character "That’s such a good realization. It’s like those little moments are the glue holding everything together."
        "I’m all about the bigger picture, but I’m learning to appreciate the small wins along the way.":
            chosen_character "That’s a great way to look at it. The big picture is important, but the journey is what makes it worth it."
        "I think both are important. Chasing big things keeps me going, but the small moments help me appreciate everything.":
            chosen_character "Balance. That’s the key, isn’t it? You seem like someone who’s got their priorities figured out."

    # Fourth question and responses
    chosen_character "That makes sense. I guess it’s all about balance, right? Finding time for the things that truly matter. Speaking of which, what’s something that really makes you feel fulfilled? Like, something that makes you feel like you’re on the right path?"

    menu:
        "I think it’s when I’m working on something that really excites me, but I don’t know why. There’s beauty in the absurdity of things.":
            chosen_character "That’s such a beautiful way to put it. I love that you see beauty in the unexpected."
        "For me, it’s when I’m actively creating a better version of myself. I like knowing that I am giving myself the best chance to become great.":
            chosen_character "That’s so inspiring. You’re really giving yourself a gift by thinking that way."
        "I think it’s when I’m creating something or helping someone, when I know I’ve made an impact in someone’s life. That’s when I feel most fulfilled.":
            chosen_character "That’s so wonderful. Making a difference like that is such a meaningful way to live."

    # Soft transition to Act 2
    chosen_character "You’ve really got me thinking about some deep stuff tonight. It’s nice to talk like this. I feel like I’m learning so much about you."

# Code I added from chow starts here
    jump act_2_start

label act_2_start:
    image act_2_bg = "gui/images/backgrounds/smt.png"
    scene act_2_bg

    chosen_character "You know, talking to you earlier really got me thinking. It’s nice to have these kinds of conversations—it feels like we’re really connecting."
    chosen_character "I was wondering... do you feel like the world ever pulls you in so many directions that you lose sight of what you really want?"

    menu:
        "Sometimes, but I try to remind myself of what truly matters.":
            $ user_response = "Sometimes, but I try to remind myself of what truly matters."
            chosen_character "That’s such a grounded way to see things. I admire that about you."
        "All the time. It feels like a constant struggle to stay focused.":
            $ user_response = "All the time. It feels like a constant struggle to stay focused."
            chosen_character "I get that. It’s tough, but I think those struggles teach us a lot about ourselves."
        "Not really. I’ve always been pretty clear about my path.":
            $ user_response = "Not really. I’ve always been pretty clear about my path."
            chosen_character "That’s amazing! It must feel so empowering to have that kind of clarity."

    # Call AI function to generate a dynamic question
    python:
        ai_question = ai_generate_question(user_response)

    # Use AI-generated question in dialogue
    chosen_character "[ai_question]"

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
    python: 
        if gender_display == "Woman":
            chosen_character = susie
            chosen_image = "susie_smiling"
        elif gender_display == "Man":
            chosen_character = sebastian
            chosen_image = "sebastian_smiling"
        else:  
            chosen_character = alex
            chosen_image = "alex_smiling"

        user_response = renpy.input("What about your talents? From what you told me so far, I bet you have a ton of them!")
        for i in range (2):
            ai_question = ai_generate_question(user_response)
            
        user_response1 = renpy.input("It's always good to talk about what we can do, but it's also important to think about what you want to do. Never forget that. So.. what's your dream job(s)?")
        for i in range (2):
            ai_question = ai_generate_question(user_response1)

        user_response2 = renpy.input("Ambition is key to success. But, prospects are also important to consider. How would you put yourself on such a scale? ")
        for i in range (2):
            ai_question = ai_generate_question(user_response2)
        ai_rec = ai_generate_recommendations(user_response,user_response1,user_response2)
        

