import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not set. Add it to your .env file.")

# Initialize client
client = Groq(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": "Say 'Groq API is working perfectly' in one line."
            }
        ],
        temperature=0.7,
        max_tokens=50
    )

    print("✅ API Key is working!\n")
    print("Response:")
    print(response.choices[0].message.content)

except Exception as e:
    print("❌ Error while testing API:")
    print(e)