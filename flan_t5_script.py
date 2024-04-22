import csv

# Function to send prompt to Flan T5 and get the response
def get_flan_t5_response(prompt):
    # Placeholder for Flan T5 API interaction
    # Replace YOUR_API_KEY with your actual API key
    # response = requests.post('FLAN_T5_API_ENDPOINT', json={'prompt': prompt, 'key': 'YOUR_API_KEY'})
    # return response.text
    # For now, we'll return a dummy response for demonstration purposes
    return 'Flan T5 Response to: ' + prompt

# Read the CSV file
with open('prompts.csv', mode='r') as infile:
    reader = csv.reader(infile)
    prompts_responses = [row for row in reader]

# Placeholder for sending each prompt to Flan T5 and capturing the response
# The actual sending of prompts and capturing of responses will be handled
# outside of this script using the special <perplexity> command
for i, row in enumerate(prompts_responses[1:], start=1):  # Skip header row
    prompt = row[1]
    # Simulate the response capture
    response = get_flan_t5_response(prompt)
    prompts_responses[i].append(response)

# Write the updated data to a new CSV file
with open('updated_prompts.csv', mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(prompts_responses)

print('Script completed and updated CSV file is saved as updated_prompts.csv.')
