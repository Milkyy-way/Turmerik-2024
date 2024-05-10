from imports import *  # Common imports

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# Define the sentiment analysis function
def score_calculator(comment_body):
    tokens = tokenizer.encode(comment_body, return_tensors='pt')
    result = model(tokens)
    return int(torch.argmax(result.logits)) + 1  # Convert logits to rating (1-5)

df = pd.read_csv("../data/reddit_data.csv")

# Apply the sentiment analysis function
df['Score'] = df['Comment_Body'].apply(lambda x: score_calculator(x[:512]))

df.to_csv("../data/scores.csv", index=False)
