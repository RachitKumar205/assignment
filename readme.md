
# Twitter Trends Scraper

## Overview

This script logs into Twitter, fetches the top trending topics, and stores them in a MongoDB database. The script utilizes Selenium for web scraping and MongoDB for data storage.

## Features

- **Twitter Login**: Automates the login process to Twitter.
- **Trend Fetching**: Retrieves the top 5 trending topics.
- **MongoDB Integration**: Stores the trending topics in a MongoDB database.
- **User-Agent Rotation**: Uses a random user-agent for each run to avoid detection.
- **Proxy Rotation (Commented Out)**: Includes functionality for rotating proxies using Webshare.io, though it is currently commented out due to running out of free credits.

## Requirements

- Python 3.x
- MongoDB
- Chrome WebDriver
- Selenium
- Requests
- Webdriver Manager

## Setup



1. **Install Python Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Script**
   ```sh
   python script.py
   ```

2. **Data Storage**
   The trending topics will be stored in the MongoDB database specified in the `MONGO_URI`.

## Implementation Details

### Twitter Login

The script uses Selenium to automate the login process to Twitter. The XPaths for the username and password fields are used to enter credentials and log in.

### Trend Fetching

Once logged in, the script navigates to the Twitter trends page and retrieves the top 5 trending topics using their respective XPaths.

### MongoDB Integration

The trending topics are stored in a MongoDB collection named `trends` within the `twitter_trends` database. Each record includes the trend names, timestamp, and IP address.

### User-Agent Rotation

The script rotates through a list of user-agents for each run to avoid detection and reduce the chances of being blocked.

### Proxy Rotation

The script includes functionality for rotating proxies using Webshare.io. However, due to running out of free credits, this part of the code is commented out. You can uncomment the relevant lines and provide your Webshare.io API key to enable this feature.

## Important Notes

- **Credentials Security**: Ensure your credentials are stored securely and not exposed in public repositories.
- **Proxy Usage**: Using proxies can help avoid IP bans, but it is essential to comply with Twitter's terms of service.
- **Error Handling**: The script includes basic error handling to catch exceptions during the scraping process.

