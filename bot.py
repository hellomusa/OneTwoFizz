import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

class ServerGame:
    def __init__(self):
        self.current_number = 0
        self.high_score = 0
        self.high_scorer = None

server_games = {}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='start')
async def start_game(ctx):
    server_id = ctx.guild.id
    if server_id not in server_games:
        server_games[server_id] = ServerGame()
    server_games[server_id].current_number = 0
    await ctx.send("FizzBuzz game started! Begin counting from 1.")

@bot.command(name='highscore')
async def show_high_score(ctx):
    server_id = ctx.guild.id
    if server_id in server_games and server_games[server_id].high_scorer:
        game = server_games[server_id]
        await ctx.send(f"Current high score: {game.high_score} by {game.high_scorer.display_name}")
    else:
        await ctx.send("No high score yet!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.name != 'fizzbuzz':
        return

    await bot.process_commands(message)

    server_id = message.guild.id
    if server_id not in server_games:
        return

    game = server_games[server_id]
    user_input = message.content.strip().lower()

    if not is_valid_input(user_input):
        return

    expected_number = game.current_number + 1
    expected_response = get_fizzbuzz(expected_number)

    if user_input == expected_response.lower():
        game.current_number = expected_number
        await message.add_reaction('✅')
    else:
        await message.add_reaction('❌')
        if game.current_number > game.high_score:
            game.high_score = game.current_number
            game.high_scorer = message.author
            await message.channel.send(f"New high score! {game.high_scorer.display_name} reached {game.high_score}!")
        await message.channel.send(f"Game over! The correct response was {expected_response}. Final count: {game.current_number}")
        game.current_number = 0

def get_fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)

def is_valid_input(input_str):
    valid_words = ['fizz', 'buzz', 'fizzbuzz']
    return input_str.isdigit() or input_str in valid_words

bot.run('token')
