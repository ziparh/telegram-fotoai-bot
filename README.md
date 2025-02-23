# Telegram Image Bot

This is a Telegram bot that generates images based on user prompts using the `/img <text>` command.


## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/ziparh/telegram-fotoai-bot.git
   cd telegram-fotoai-bot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Get your API keys:
   - Go to [FusionBrain](https://fusionbrain.ai/keys/) and get your `API_KEY` and `SECRET_KEY`.
4. Create a `.env` file and add your credentials:
   ```sh
   API_KEY=your_api_key
   SECRET_KEY=your_secret_key
   TELEGRAM_BOT_TOKEN=your_bot_token
   ```

## Running the Bot

```sh
python bot.py
```

## Usage
- Send `/img sunset in Tokyo` in Telegram to generate an image of a sunset in Tokyo.
- The bot will reply with the generated image.

## Exemple
![image](https://github.com/user-attachments/assets/28c8cb4c-dbfb-49e3-822c-0737048c995d)


