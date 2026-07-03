from config.groq_client import client

def summarize_text(text):

    if not text.strip():
        return "⚠️ No text provided."

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{
                "role": "user",
                "content": f"""
Summarize this legal text in bullet points:

{text}
"""
            }],
            temperature=0.3,
            max_tokens=300
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error: {e}"