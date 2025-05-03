import discord
from discord.ext import commands
from views import TriviaView, active_games
from trivia import trivia

intents = discord.Intents.default()
intents.messages = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@commands.command(name="trivia")
async def trivia_command(ctx):
    if ctx.author.id in active_games:
        await ctx.send("You already have an open trivia game! Finish it before starting a new one.")
        return

    active_games[ctx.author.id] = True

    question = await trivia.question(amount=1, category=0, difficulty='easy', quizType='multiple')
    question_data = question[0]
    question_text = question_data["question"]
    correct_answer = question_data["correct_answer"]

    view = TriviaView(question_data, correct_answer, ctx.author.id)
    message = await ctx.send(f"📚 **Trivia Question:** {question_text}", view=view)
    view.message = message
    await view.wait()

    if ctx.author.id in active_games:
        del active_games[ctx.author.id]

bot.add_command(trivia_command)