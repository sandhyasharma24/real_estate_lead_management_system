import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

try:
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "Hello, AI!"}]
    )
    print(response)
except Exception as e:
    print("Error in OpenAI API:", str(e))
