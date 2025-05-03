# trivia_discord_bot

Trivia bot for Discord servers. Users can answer timed multiple-choice questions, track their scores, and view highscores. Built with Python, `trivia.py` and `discord.py`.

![example_trivia](https://github.com/user-attachments/assets/6ce14695-edc4-46c7-b665-1d7f037069f8)

![example_response](https://github.com/user-attachments/assets/fc664c3e-5eef-443e-bfd5-46036e2232f0)


## Features

- `/trivia` — Start a new trivia game with a multiple-choice question
- `/highscore` — See who has the most correct answers
- `/help` — View all available commands  

## Technologies used

- [Python 3.10+](https://www.python.org/)
- [discord.py v2.x](https://discordpy.readthedocs.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [trivia.py - python api wrapper for Open Trivia DB](https://pypi.org/project/trivia.py/)

## Local setup instructions

### Prerequisities

Before setting up the trivia bot, you need to create your own Discord bot (if you haven't done so already). If creating Discord bots is unfamiliar to you you can use [this guide](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal) to help you setup a new bot and invite it to your server.

### 1. Clone the Repository

    git clone https://github.com/ilohil/trivia_discord_bot.git
    cd trivia_discord_bot

### 2. Install Dependencies

    pip install -r requirements.txt

### 3. Create a .env file

Create .env file to root folder. Env file should contain your Discord bot's token like this:

    DISCORD_TOKEN=your_discord_bot_token_here

If creating .env is unfamiliar to you, you can follow the instructions in [this guide](https://www.testdevlab.com/blog/how-to-build-a-discord-bot-using-python)(step 2) to set up the .env-file.

### 4. Invite the Bot to Your Server

To invite your bot to your Discord server, visit the following URL and replace YOUR_CLIENT_ID with your bot’s actual client ID (found in the [Discord Developer Portal](https://discord.com/developers/applications)):

    https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot+applications.commands&permissions=2147483648

The permissions required for the bot are as follows:

    - Send Messages: Required to send trivia questions and answers
    - Embed Links: Needed to send questions and answers in embedded format.
    - Manage Messages: Used to delete old messages during the trivia game.
    - Attach Files: If the bot sends images as part of questions/answers (optional).

Follow the prompts to invite the bot and grant it the necessary permissions.

### 5. Run the Bot

    python main.py

The bot will start, and you should see it logging in to Discord in your terminal. Now you are ready to use the bot!

## Using deployed bot

If you want to use bot in your Discord server without local setup you can invite the bot from this link:

        https://discord.com/oauth2/authorize?client_id=1368274154670915655&permissions=387136&integration_type=0&scope=bot

Paste the link in your browser and select the server you want to invite the bot. Follow the prompts to invite the bot and grant it the necessary permissions.

Note: The deployed bot might occasionally be unavailable due to server limitations. If you experience any issues, try again later.

## Licenses 

This project is licensed with GPL-3.0 license.
