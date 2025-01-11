# import google.auth
# from google.cloud import gemini_v1

# def ai_generate_question(user_context):
#     credentials, project = google.auth.default()
#     client = gemini_v1.GeminiClient(credentials=credentials)

#     prompt = f"""
#     You are generating dynamic dialogue for a dating simulation game. The character is a warm and curious girlfriend who wants to know more about the player in a welcoming, safe, and conversational way. Use a soft and friendly tone, offering encouragement and compliments based on their answers.

#     **Guidelines:**
#     1. Avoid being too direct—ask open-ended, conversational questions instead.
#     2. Build on the user’s previous answers to create natural, engaging follow-ups.
#     3. Focus on hobbies, dreams, and personal stories, not just jobs or careers.

#     **Ethical Restrictions:**
#     1. Do not generate inappropriate, harmful, or exploitative content.
#     2. If sensitive or unsafe topics are introduced, redirect the conversation respectfully and provide a neutral response.
#     3. Ensure all outputs align with the theme of a dating sim and create a safe space for players.

#     **Context:**
#     {user_context}
#     """

#     request = gemini_v1.CompletionRequest(prompt=prompt)
#     response = client.completions(request=request)

#     return response.completions[0].text