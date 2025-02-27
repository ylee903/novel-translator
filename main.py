import requests

# Define the function to send a request to Ollama
def query_ollama(prompt):
    url = "http://localhost:11434/api/generate"  # Ollama API URL
    payload = {
        "model": "deepseek-r1:8b",  # Change to your actual model name
        "prompt": prompt,
        "stream": False  # Ensures response comes as a single JSON object
    }

    try:
        response = requests.post(url, json=payload)  # Send the request
        response.raise_for_status()  # Raise an error if request fails
        result = response.json()  # Parse JSON response

        # Debug: Print the entire response to see the structure
        print("\n🔍 Full Response from Ollama:", result)

        # Extract response text safely
        return result.get("response", "No response found")  # Get the generated text

    except requests.exceptions.JSONDecodeError as e:
        return f"JSON decoding error: {e}\nResponse text: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Example usage: Send a prompt to the model
prompt_text = "Hello! How are you today?"
output = query_ollama(prompt_text)

# Print the response
print("\n🧠 LLM Response:")
print(output)
