import get_flan_t5_response
import get_claude_haiku_response
import get_llama_3_8b_response
import get_mistral_7b_response
import calculate_scores
import create_visualization
import csv

def main():
    # Read the poemsum_train.csv file to get titles, authors, and poem texts
    with open('poemsum_train.csv', mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            title = row['title']
            author = row['author']
            poem_text = row['poem_text']

            # Form the prompt for each LLM
            flan_t5_prompt = f"Generate a short summary of '{title}' by {author}: {poem_text}"
            claude_haiku_prompt = f"Generate a short summary of '{title}' by {author}: {poem_text}"
            llama_3_8b_prompt = f"Generate a short summary of '{title}' by {author}: {poem_text}"
            mistral_7b_prompt = f"Generate a short summary of '{title}' by {author}: {poem_text}"

            # Call each LLM function with the formed prompt
            flan_t5_response = get_flan_t5_response.get_flan_t5_response(flan_t5_prompt)
            claude_haiku_response = get_claude_haiku_response.get_claude_haiku_response(claude_haiku_prompt)
            llama_3_8b_response = get_llama_3_8b_response.get_llama_3_8b_response(llama_3_8b_prompt)
            mistral_7b_response = get_mistral_7b_response.get_mistral_7b_response(mistral_7b_prompt)

            # Print the responses
            print(f"Flan T5 Response for '{title}':", flan_t5_response)
            print(f"Claude Haiku Response for '{title}':", claude_haiku_response)
            print(f"Llama 3-8b Response for '{title}':", llama_3_8b_response)
            print(f"Mistral 7b Response for '{title}':", mistral_7b_response)

    # Calculate scores
    calculate_scores.calculate('summaries_with_prompts.csv', 'summaries_with_scores.csv')

    # Generate heatmap visualization
    create_visualization.generate_heatmap('summaries_with_scores.csv', 'average_scores_heatmap.pdf')

if __name__ == "__main__":
    main()
