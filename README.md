
# Genius Bot - AI Chatbot with GPT-3.5 Integration

Genius Bot is an advanced AI-powered chatbot that leverages the power of OpenAI's GPT-3.5 model to provide intelligent and human-like responses to user inputs. This repository contains the source code and instructions to set up and run Genius Bot on your local machine.

## Features

- Seamless integration with OpenAI's GPT-3.5 model.
- Natural language understanding for engaging conversations.
- Interactive and dynamic responses tailored to user input.
- Easily customizable for specific use cases and scenarios.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- `openai` library (install using `pip install openai`)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Kiruthika162003/genius-bot.git
   cd genius-bot
   ```

2. Obtain your OpenAI API key:

   Sign up on the OpenAI platform (if you haven't already) and obtain an API key. Replace `'YOUR_OPENAI_API_KEY'` in the `chatbot.py` script with your actual API key.

### Usage

1. Run the chatbot:

   ```bash
   python chatbot.py
   ```

2. Start chatting with Genius Bot! Enter your messages as prompts, and the bot will respond with AI-generated text.

3. To exit the chat, type `'exit'`.

### Customization

You can customize the behavior and appearance of Genius Bot by modifying the `chatbot.py` script:

- Change the conversation engine by modifying the `engine` parameter in the `openai.Completion.create()` call.
- Adjust the `max_tokens` parameter to control the length of generated responses.
- Implement additional features like conversation history or user context management.

