import csv
from bert_score import score as bert_score
from rouge_score import rouge_scorer

# Function to calculate BERTScore and ROUGE scores
def calculate_scores(given_summary, generated_summary):
    # Ensure inputs are lists of strings
    if not isinstance(given_summary, list):
        given_summary = [given_summary]
    if not isinstance(generated_summary, list):
        generated_summary = [generated_summary]

    # Calculate BERTScore
    P, R, F1 = bert_score(given_summary, generated_summary, lang="en", verbose=True)
    bert_scores = {'precision': P.mean().item(), 'recall': R.mean().item(), 'f1': F1.mean().item()}

    # Calculate ROUGE scores
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    rouge_scores = scorer.score(given_summary[0], generated_summary[0])

    # Extract ROUGE-1 and ROUGE-L F1 scores
    rouge1_f1 = rouge_scores['rouge1'].fmeasure
    rougeL_f1 = rouge_scores['rougeL'].fmeasure

    return bert_scores, rouge1_f1, rougeL_f1

# Read the CSV file and calculate scores
with open('summaries_with_prompts.csv', mode='r') as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Skip header row
    # Prepare new header with score columns for each LLM
    new_header = header + sum(([f"{llm}_precision", f"{llm}_recall", f"{llm}_f1", f"{llm}_rouge1", f"{llm}_rougeL"] for llm in ["google-flan-t5", "mistral-7b-instruct", "llama-3-8b-instruct", "claude-3-haiku"]), [])
    evaluation_scores = [new_header]

    for row in reader:
        given_summary = row[0]
        # Calculate scores for each LLM's generated summary
        for i, llm in enumerate(["google-flan-t5", "mistral-7b-instruct", "llama-3-8b-instruct", "claude-3-haiku"], start=2):
            generated_summary = row[i]
            bert_scores, rouge1_f1, rougeL_f1 = calculate_scores(given_summary, generated_summary)
            # Append scores to the row
            row.extend([bert_scores['precision'], bert_scores['recall'], bert_scores['f1'], rouge1_f1, rougeL_f1])
        evaluation_scores.append(row)

# Write the evaluation scores to a new CSV file
with open('summaries_with_scores.csv', mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(evaluation_scores)

print("BERTScore and ROUGE scores have been calculated for each LLM and saved to 'summaries_with_scores.csv'.")
