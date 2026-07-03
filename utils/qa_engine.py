from config.groq_client import client

def ask_question(text, question):

    prompt = f"""
Answer based on legal document:

{text}

Question: {question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content