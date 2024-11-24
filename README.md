Here's a simple **`README.md`** for your project:

---

# Reddit Subreddit Transfer Tool

This Python tool helps you transfer your followed subreddits from one Reddit account to another. Since Reddit does not allow username changes, this script provides a way to migrate your subscriptions when creating a new account.

---

## Features

- Export all followed subreddits from your old account.
- Import the list of subreddits into your new account.
- Uses the Reddit API via the `praw` library for seamless automation.

---

## Prerequisites

1. **Python** (version 3.x recommended).
2. Install the required library:
   ```bash
   pip install praw
   ```
3. **Reddit API Credentials**:
   - Create Reddit applications for both accounts:
     1. Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps).
     2. Click **"Create App"** and select "script" as the type.
     3. Note down the `client_id`, `client_secret`, and provide a `user_agent`.

---

## Usage

### 1. Clone or Download the Repository
```bash
git@github.com:BeyondAman/RedditSubMigrator.git
cd RedditSubMigrator
```

### 2. Configure API Credentials
Open the scripts and update the following sections with your credentials:
- `OLD_ACCOUNT_CLIENT_ID`, `OLD_ACCOUNT_CLIENT_SECRET`, `OLD_REDDIT_USERNAME`, `OLD_REDDIT_PASSWORD`.
- `NEW_ACCOUNT_CLIENT_ID`, `NEW_ACCOUNT_CLIENT_SECRET`, `NEW_REDDIT_USERNAME`, `NEW_REDDIT_PASSWORD`.

### 3. Export Subscriptions
Run the following command to export subscriptions from the old account:
```bash
python export_subscriptions.py
```
This will create a `subreddits.json` file containing all followed subreddits.

### 4. Import Subscriptions
Run the following command to import the subscriptions into the new account:
```bash
python import_subscriptions.py
```
The script will subscribe to all subreddits listed in `subreddits.json`.

---

## File Structure

- **export_subscriptions.py**: Script to export followed subreddits to `subreddits.json`.
- **import_subscriptions.py**: Script to import subscriptions from `subreddits.json`.
- **subreddits.json**: The generated file containing the list of subreddits.

---

## Limitations

- The tool does not transfer saved posts, comments, or other user data.
- Subscribing to large numbers of subreddits in a short time may trigger Reddit's API rate limits.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this further! Would you like me to help with other sections, like examples or troubleshooting?