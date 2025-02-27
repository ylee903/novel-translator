import requests

# Configuration
DOCKER_API_URL = "http://localhost:5000/translate"  # Docker API endpoint for Deepseek-r1:8b
INPUT_FILE = "input.txt"  # Path to your input .txt file
OUTPUT_FILE = "output.txt"  # Path to save the translated output
PROMPT = "Translate the following text to French:"  # Customize the prompt here

def read_text(file_path):
    """
    Read text from a file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def translate_text(text, prompt):
    """
    Send text to the Deepseek-r1:8b model via Docker for translation.
    """
    payload = {
        "prompt": f"{prompt} {text}",
        "max_tokens": 100  # Adjust based on your needs
    }
    response = requests.post(DOCKER_API_URL, json=payload)
    if response.status_code == 200:
        return response.json().get("translation", "Translation failed.")
    else:
        raise Exception(f"Translation failed: {response.text}")

def save_text(file_path, text):
    """
    Save text to a file.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

def main():
    # Read the input text file
    input_text = read_text(INPUT_FILE)
    print(f"Input text: {input_text}")

    # Translate the text
    translated_text = translate_text(input_text, PROMPT)
    print(f"Translated text: {translated_text}")

    # Save the translated text to the output file
    save_text(OUTPUT_FILE, translated_text)
    print(f"Translation saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()