import get_flan_t5_response
import get_claude_haiku_response
import get_llama_3_8b_response
import get_mistral_7b_response
import calculate_scores
import create_visualization

def main():
    # Example prompts for each LLM
    flan_t5_prompt = "Explain the concept of gravity."
    claude_haiku_prompt = "Write a haiku about the rainforest."
    llama_3_8b_prompt = "Summarize the impact of climate change on polar bears."
    mistral_7b_prompt = "Describe the process of photosynthesis."

    # Call each LLM function with the example prompt
    flan_t5_response = get_flan_t5_response.get_flan_t5_response(flan_t5_prompt)
    claude_haiku_response = get_claude_haiku_response.get_claude_haiku_response(claude_haiku_prompt)
    llama_3_8b_response = get_llama_3_8b_response.get_llama_3_8b_response(llama_3_8b_prompt)
    mistral_7b_response = get_mistral_7b_response.get_mistral_7b_response(mistral_7b_prompt)

    # Print the responses
    print("Flan T5 Response:", flan_t5_response)
    print("Claude Haiku Response:", claude_haiku_response)
    print("Llama 3-8b Response:", llama_3_8b_response)
    print("Mistral 7b Response:", mistral_7b_response)

    # Calculate scores
    calculate_scores.calculate('summaries_with_prompts.csv', 'summaries_with_scores.csv')

    # Generate heatmap visualization
    create_visualization.generate_heatmap('summaries_with_scores.csv', 'average_scores_heatmap.pdf')

if __name__ == "__main__":
    main()
