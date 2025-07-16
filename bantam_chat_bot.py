import requests

# === Configuration ===
API_KEY = "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"  # TODO: Paste your API key here
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-8b-8192"

# === Chat Function ===
def get_ai_response(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",  # TODO: Use your API key
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        # Send the POST request to the Groq API
        response = requests._____(_____, headers=_____, json=_____)  # TODO: Complete this line
        response.raise_for_status()  # Ensure no HTTP errors
        result = response.____()  # TODO: Extract JSON content
        return result["choices"][0]["message"]["_____"]  # TODO: Get AI's message
    except Exception as e:
        return f"Error: {e}"

# === Main Chat Loop ===
if __name__ == "__main__":
    print("🤖 Welcome to your Groq-powered AI chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break
        reply = get_ai_response(user_input)
        print("AI:", reply)