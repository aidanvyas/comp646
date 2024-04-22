import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('summaries_with_scores.csv')

# Extract the average scores for each model and metric
average_scores = {
    'google-flan-t5': {
        'bertscore_precision': df['google-flan-t5_precision'].mean(),
        'bertscore_recall': df['google-flan-t5_recall'].mean(),
        'bertscore_f1': df['google-flan-t5_f1'].mean(),
        'rouge1': df['google-flan-t5_rouge1'].mean(),
        'rougeL': df['google-flan-t5_rougeL'].mean()
    },
    'mistral-7b-instruct': {
        'bertscore_precision': df['mistral-7b-instruct_precision'].mean(),
        'bertscore_recall': df['mistral-7b-instruct_recall'].mean(),
        'bertscore_f1': df['mistral-7b-instruct_f1'].mean(),
        'rouge1': df['mistral-7b-instruct_rouge1'].mean(),
        'rougeL': df['mistral-7b-instruct_rougeL'].mean()
    },
    'llama-3-8b-instruct': {
        'bertscore_precision': df['llama-3-8b-instruct_precision'].mean(),
        'bertscore_recall': df['llama-3-8b-instruct_recall'].mean(),
        'bertscore_f1': df['llama-3-8b-instruct_f1'].mean(),
        'rouge1': df['llama-3-8b-instruct_rouge1'].mean(),
        'rougeL': df['llama-3-8b-instruct_rougeL'].mean()
    },
    'claude-3-haiku': {
        'bertscore_precision': df['claude-3-haiku_precision'].mean(),
        'bertscore_recall': df['claude-3-haiku_recall'].mean(),
        'bertscore_f1': df['claude-3-haiku_f1'].mean(),
        'rouge1': df['claude-3-haiku_rouge1'].mean(),
        'rougeL': df['claude-3-haiku_rougeL'].mean()
    }
}

# Convert the dictionary to a DataFrame for visualization
scores_df = pd.DataFrame(average_scores).T

# Format the scores to four decimal places
scores_df = scores_df.astype(float).round(4)

# Create a heatmap with improved color grading
plt.figure(figsize=(10, 8))
sns.heatmap(scores_df, annot=True, fmt=".4f", cmap='RdYlGn', cbar=False)

# Add labels and a title
plt.title('Average Scores Heatmap')
plt.xlabel('Metrics')
plt.ylabel('Models')

# Save the heatmap to a PDF file
plt.savefig('average_scores_heatmap.pdf', bbox_inches='tight')
plt.close()
