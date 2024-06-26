# OneTwoFizz Discord Bot

OneTwoFizz is a fun Discord bot that brings the classic counting game to your server with a twist! 

Challenge your friends to see who can count the highest while following the FizzBuzz rules.

## Features

- Play FizzBuzz across multiple Discord servers
- Track high scores for each server

## How to Play

1. Start the game in the `#fizzbuzz` channel in your server by typing `!start`
2. Users take turns counting up from 1
3. Replace numbers divisible by 3 with "Fizz"
4. Replace numbers divisible by 5 with "Buzz"
5. Replace numbers divisible by both 3 and 5 with "FizzBuzz"
6. The words are case insensitive
7. If a user makes a mistake, the game ends and the count resets

## Commands

- `!start`: Begin a new FizzBuzz game in the current channel
- `!highscore`: Display the current high score for the server

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/OneTwoFizz.git
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Replace `token` with your Discord bot token in `bot.py`:
4. Run the bot:
   ```
   python bot.py
   ```

Use the [Discord developer portal](https://discord.com/developers/docs/intro) to create a bot and get your token
