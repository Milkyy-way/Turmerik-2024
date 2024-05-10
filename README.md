This project extracts Reddit data, performs sentiment analysis, and generates personalized messages for users who are interested in or could benefit from clinical trials.


# Create a virtual environment for best practice
- python -m venv myenv
- source myenv/bin/activate  # For MacOS/Linux
- myenv\Scripts\activate     # For Windows

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Set up environment variables in `config/config.env`.
Replace the 'XXXXXXXXXXXXXXX' keys with your own keys

# Run the following scripts in order:
- `imports.py` to import all the libraries.
- `reddit_scrapping.py` to extract Reddit data.
- `sentiment_analysis.py` to analyze sentiment and add scores.
- `personalized_messages.py` to generate personalized messages for users who has high scores of 4 and 5.

# Methodology
### Data Collection from Reddit:
- Used PRAW (Python Reddit API Wrapper) to fetch Reddit posts and comments from specific subreddits.
- Applied keyword-based filtering to select relevant posts and comments.
- Implemented rate limit handling and error logging to ensure robustness.
### Sentiment Analysis:
- Applied sentiment analysis to the collected comments using a pre-trained model.
- Stored the sentiment scores in a DataFrame for further processing.
### Filtering and Data Processing:
- Filtered the DataFrame for comments with high sentiment scores (4 and 5).
- Applied additional data processing and transformation as needed.
### Generating Personalized Messages:
- Used OpenAI's GPT-3.5-turbo model to generate personalized messages based on user comments.
- Created a prompt with specific instructions for the OpenAI API.
- Sent the prompt to OpenAI and extracted the generated messages.
### Storing and Outputting Results:
- Stored the generated personalized messages in a DataFrame.
- Saved the resulting DataFrame to a CSV file for further use.
- Printed the personalized messages for verification and validation.

# Why used hugging face
1) It is recommend to use NLP model which is well trained
2) By using trained model, carbon footprint and compute costs can be reduced 
3) Used Hugging face it provides the largest collection of models and datasets publicly available, including over 27,000 models shared by the AI community.
4) Used nlptown/bert-base-multilingual-uncased-sentiment whcih is bert-base-multilingual-uncased model finetuned for sentiment analysis. This will give the output form 1(worst) to 5(best)


# Challenges
- My first challenge was exploring the PRAW API because I have never used it. It wasn't too difficult to understand because I have worked with other APIs.
- One challenge was deciding which data to extract to ensure relevance. Should I extract all posts or only select a few? Should I focus on 'hot,' 'new,' or 'top' posts? Should I limit extraction to a single subreddit or use multiple subreddits? Would it be helpful to use Natural Language Processing (NLP) to identify relevant posts and comments?
- Choosing the right sentiment analysis model was another challenge. Should I train a new model, or should I use an existing one?
- Framing the received response and storing it in the corresponding row of the same DataFrame was quite difficult
- Providing my credit card details to use OpenAI was more of an issue than a challenge.

# How I overcame
- Went through the document of PRAW API.
- Initially, I applied one keyword to a single subreddit. Then, I created a list to pass multiple keywords to extract posts more relevant to health and medical trials. Later, I thought it would be useful to cover multiple subreddits, so I created another list. This way, I could cover multiple subreddits and use any number of keywords for more effective filtering.
- I debugged the error, revisited the workflow to understand it better, and learned the basic concept of sentiment analysis through a LinkedIn article.

### Data Collection
- All the data are colledted in CSV formate.
- For each stage new CSV file has been stored so that we can trace the record 
- Inside the data folder you will get all the three files
### Analysis Performed
- Check the 'scores.csv' file; the last column contains the final results from the sentiment analysis.
### Messages Generated
- Check the 'personalized_messages.csv' file; the last column contains the final results from the messages generated.

# Ethical Considerations
1) Included restrictions by taking 1st 5 new post whcih satisfy the rate limit
2) Exception handler is implemented so that it will not create the issue to reddit server.
3) Did not shared personally identifiable information
4) Used a unique user agent when interacting with the Data APIs
5) Sticked to the plan of extracting post and comments and avoid the scraping that could be disruptive or harm the Reddit community

