import requests
import json

# Configuration
OLLAMA_API_URL = "http://localhost:11434/api/generate"  # Ollama API endpoint
INPUT_FILE = r"C:\Users\Samuel\Documents\translate large novels\input"  # Path to your input .txt file
OUTPUT_FILE = r"C:\Users\Samuel\Documents\translate large novels\output"  # Path to save the translated output
MAX_CHUNK_LENGTH = 500  # Maximum number of characters per chunk
MODEL_NAME = "deepseek"  # Name of the model you're using (e.g., deepseek)

def chunk_text(text, max_length):
    """
    Split the text into chunks of a specified maximum length.
    """
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

def translate_chunk(chunk):
    """
    Send a text chunk to the Ollama API for translation.
    """
    payload = {
        "model": MODEL_NAME,
        "prompt": f"Translate the following text to English: {chunk}",
        "stream": False
    }
    response = requests.post(OLLAMA_API_URL, json=payload)
    if response.status_code == 200:
        return response.json()["response"]
    else:
        raise Exception(f"Translation failed: {response.text}")

def translate_large_text(text):
    """
    Translate a large text by splitting it into chunks and translating each chunk.
    """
    chunks = chunk_text(text, MAX_CHUNK_LENGTH)
    translated_chunks = []
    for chunk in chunks:
        translated_chunk = translate_chunk(chunk)
        translated_chunks.append(translated_chunk)
        print(f"Translated chunk: {translated_chunk}")  # Optional: Print progress
    return " ".join(translated_chunks)

def main():
    # Read the input text file
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        text = file.read()

    # Translate the text
    translated_text = translate_large_text(text)

    # Save the translated text to the output file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(translated_text)

    print(f"Translation complete! Output saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()