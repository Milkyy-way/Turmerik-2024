# Import necessary libraries
from imports import *  # Common imports
from dotenv import load_dotenv

# Load environment variables
load_dotenv("../config/config.env")

# Set up Reddit connection
agent = "Turmeric_User"
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=agent
)

# Subreddits to scrape
subreddit_names = ["RetatrutideTrial", "clinicalresearch"]
keywords = ["trial", "clinical research", "treatment"]  # Keywords to search in titles

# Initialize data storage
data = []

# Fetch five posts from each subreddit
for subreddit_name in subreddit_names:
    try:
        subreddit = reddit.subreddit(subreddit_name)

        # Fetch the first five new posts
        for post in subreddit.new(limit=5):
            # Check if any of the keywords are in the title
            if any(keyword in post.selftext.lower() for keyword in keywords):
                post_author = str(post.author)
                post_title = post.title
                post_body = post.selftext

                
                post.comments.replace_more(limit=0)  # Avoid pagination issues

                # Extract comments
                for comment in post.comments.list():
                    comment_author = str(comment.author)
                    comment_body = comment.body
                    
                    data.append({
                        "Subreddit": subreddit_name,
                        "Post_Author": post_author,
                        "Post_Title": post_title,
                        "Comment_Author": comment_author,
                        "Comment_Body": comment_body,
                    })

    except prawcore.exceptions.Forbidden as e:
        # Handle forbidden access errors
        print(f"Access forbidden for subreddit '{subreddit_name}': {e}")

    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error for subreddit '{subreddit_name}': {e}")

# Create a DataFrame and save the collected data
if data:
    df = pd.DataFrame(data)
    df.to_csv("../data/reddit_data.csv", index=False)
    print("Data successfully saved")
else:
    print("No data extracted from subreddits.")
