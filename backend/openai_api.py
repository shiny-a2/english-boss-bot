import os
import openai

openai.api_key = os.getenv("openai_key")

async def get_openai_level(user_answers: list[str]) -> str:
    prompt = "Determine CEFR level (A1–C2) based on these answers: " + "; ".join(user_answers)
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You assess English language level."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"OpenAI error: {e}"
