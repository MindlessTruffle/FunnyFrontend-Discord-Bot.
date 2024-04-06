# FunnyFrontend Discord Bot

## Overview
FunnyFrontend is Discord bot that offers various fun and utility commands powered by AI models and external APIs. It includes functionalities such as generating AI chat responses, creating AI-generated images, translating text into different styles, searching for images and GIFs, finding YouTube videos, and more. The bot is in very early development, and doesn't have very optimised code!

Note: Some features use the stable diffusion pipeline, if you dont have atleast 4-6gb of dedicated GPU memory (Different from RAM*) and 3gb of storage; feel free to remove the features that utilise it!

## Features
- AI chat responses
- AI-generated images
- Music generation (through Replicated API)
- Translation of text into different styles (Gen Z, Gen Alpha, Kawaii)
- Image and GIF searching
- YouTube video searching

## Installation
1. Clone the repository:
    ```bash
    git clone git clone https://github.com/MindlessTruffle/FunnyFrontend-Discord-Bot-.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up environment variables:
    - Obtain a Gemini API key and set it as `GEMENI_API_KEY` in your environment.
    - Obtain a Discord bot token and set it as `DISCORD_TOKEN` in your environment.
    - OPTIONAL: Obtain a Replicate API key, though it is only used by commented (not being used) code and set it as `REPLICATE_API_TOKEN` in your environment

## Usage
### Commands
#### General Commands
- `!pls`: Display a list of available commands.
- `!what`: View recent updates.

#### AI Commands
- `!yap <prompt>`: Get a chat response from the AI model.
- `!yapbypass <prompt>`: Bypass AI content filtering (not functional, placeholder).
- `!sus <prompt>`: Generate AI images based on the prompt.
- `!amogh <prompt>`: Generate AI images with a semi-nerdy and egotistical theme.

#### Translation Commands
- `!genz <prompt>`: Translate text to Gen Z slang.
- `!genalpha <prompt>`: Translate text to Gen Alpha terms.
- `!nya <prompt>`: Translate text to kawaii terms.

#### Misc Commands
- `!gyat <query>`: Search for images related to the query.
- `!gyatgif <query>`: Search for GIFs related to the query.
- `!youtube <query>`: Search for YouTube videos related to the query.

#### Moderation Commands
- `!uwu <amount>`: Bulk message delete/purge (requires manage messages permission).
- `!uwuself <amount>`: Bulk delete your own messages.

#### Other Commands
- `!invite`: Get the invite link for the bot.

## Contributors
- MindlessTruffle, Owner (Contact: themindlesstruffle@gmail.com)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
