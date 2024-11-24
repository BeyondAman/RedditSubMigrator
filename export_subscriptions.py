import praw
import json

# Configure the old Reddit account
reddit_old = praw.Reddit(
    client_id="OLD_ACCOUNT_CLIENT_ID",
    client_secret="OLD_ACCOUNT_CLIENT_SECRET",
    user_agent="script:subreddit_transfer:v1.0 (by u/your_old_username)",
    username="OLD_REDDIT_USERNAME",
    password="OLD_REDDIT_PASSWORD:<2FA Code if Enabled>"
)

def export_subscriptions(output_file="subreddits.json"):
    subscriptions = []
    for subreddit in reddit_old.user.subreddits(limit=None):  # Fetch all subscribed subreddits
        subscriptions.append(subreddit.display_name)
    
    # Save to a JSON file
    with open(output_file, "w") as file:
        json.dump(subscriptions, file, indent=2)
    print(f"Exported {len(subscriptions)} subscriptions to {output_file}")

# Export
export_subscriptions()
