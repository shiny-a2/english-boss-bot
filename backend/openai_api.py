import openai
import os

openai.api_key = os.getenv("OPENAI_KEY")

def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # یا gpt-4 اگه اکانت داری
            messages=[
                {"role": "system", "content": "You are a helpful English tutor."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("OpenAI Error:", e)
        return "❌ مشکلی در ارتباط با هوش مصنوعی پیش آمد."
