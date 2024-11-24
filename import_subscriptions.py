import praw
import json

# Configure the new Reddit account
reddit_new = praw.Reddit(
    client_id="NEW_ACCOUNT_CLIENT_ID",
    client_secret="NEW_ACCOUNT_CLIENT_SECRET",
    user_agent="script:subreddit_transfer:v1.0 (by u/your_new_username)",
    username="NEW_REDDIT_USERNAME",
    password="NEW_REDDIT_PASSWORD:<2FA Code if Enabled>"
)

def import_subscriptions(input_file="subreddits.json"):
    with open(input_file, "r") as file:
        subreddits = json.load(file)
    
    for subreddit in subreddits:
        reddit_new.subreddit(subreddit).subscribe()
        print(f"Subscribed to {subreddit}")
    
    print("Imported all subscriptions.")

# Import
import_subscriptions()
