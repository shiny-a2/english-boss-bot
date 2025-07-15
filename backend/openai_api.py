import os
import openai

openai.api_key = os.getenv("OPENAI_KEY")

async def get_openai_level(answers: list[str]) -> str:
    prompt = "کاربر به سوالات زیر این جواب‌ها را داده:\n\n"
    for i, ans in enumerate(answers):
        prompt += f"سوال {i+1}: {ans}\n"
    prompt += "\nبر اساس این پاسخ‌ها سطح زبان انگلیسی این فرد را یکی از موارد زیر تشخیص بده: Beginner, Intermediate, Upper-Intermediate, Advanced. فقط نام سطح را بده."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=20
    )
    return response.choices[0].message.content.strip()
