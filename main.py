import requests

# ✅ Set the translation instruction inside the script (fixed parameter)
TRANSLATION_PROMPT = "Translate the following text into Japanese:"

def query_ollama(prompt, text):
    """
    Send a request to the locally running Ollama LLM.
    :param prompt: The instruction for the LLM (e.g., "Translate to Japanese")
    :param text: The actual text to be translated
    :return: The translated text or an error message
    """
    url = "http://localhost:11434/api/generate"  # Ollama API URL
    payload = {
        "model": "deepseek-r1:8b",  # Change this to the correct model
        "prompt": f"{prompt}\n\nTEXT TO TRANSLATE: {text}",  # Structured format
        "stream": False  # Ensures response comes as a single JSON object
    }

    try:
        response = requests.post(url, json=payload)  # Send the request
        response.raise_for_status()  # Raise an error if request fails
        result = response.json()  # Parse JSON response
        
        return result.get("response", "No response found")  # Extract the translated text

    except requests.exceptions.JSONDecodeError as e:
        return f"JSON decoding error: {e}\nResponse text: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# ✅ Fixed prompt, user only inputs the text
text_to_translate = input("Enter the text to be translated: ")

# Call the function with the fixed translation prompt
output = query_ollama(TRANSLATION_PROMPT, text_to_translate)

# Print the response
print("\n🧠 LLM Response:")
print(output)
