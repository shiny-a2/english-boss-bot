import os
import openai
openai.api_key = os.getenv("openai_key")

async def get_openai_level(answers):
    joined = " ".join(answers)
    prompt = f"Determine the English proficiency level (A1–C2) for this user: {joined}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"
