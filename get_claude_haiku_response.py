import requests

# Function to send prompt to Claude Haiku and get the response
def get_claude_haiku_response(prompt):
    # Placeholder for Claude Haiku API interaction
    # Replace YOUR_API_KEY with your actual API key
    # response = requests.post('CLAUDE_HAIKU_API_ENDPOINT', json={'prompt': prompt, 'key': 'YOUR_API_KEY'})
    # return response.text
    # For now, we'll return a dummy response for demonstration purposes
    return 'Claude Haiku Response to: ' + prompt

# Example usage
if __name__ == "__main__":
    test_prompt = "Write a haiku about the sea."
    print(get_claude_haiku_response(test_prompt))
