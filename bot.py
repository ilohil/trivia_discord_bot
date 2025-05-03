import discord
from discord.ext import commands
from views import TriviaView, active_games, scoreboard
from trivia import trivia
from discord.ext.commands import CommandNotFound

intents = discord.Intents.default()
intents.messages = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        available_commands = [command.name for command in bot.commands]
        command_list = "\n".join(f"/{cmd}" for cmd in available_commands)
        await ctx.send(
            f"❌ Unknown command! Here are the available commands:\n```\n{command_list}\n```"
        )
    else:
        raise error

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

@commands.command(name="highscore")
async def highscore_command(ctx):
    if not scoreboard:
        await ctx.send("📉 No scores yet! Play some trivia first.")
        return

    sorted_scores = sorted(
        scoreboard.items(),
        key=lambda item: item[1]["correct_answers"],
        reverse=True
    )

    top_n = 5
    message = "🏆 **Top Trivia Highscores:**\n"
    for i, (user_id, stats) in enumerate(sorted_scores[:top_n], start=1):
        user = await bot.fetch_user(user_id)
        message += f"{i}. **{user.name}**: {stats['correct_answers']} correct out of {stats['games_played']} games\n"

    await ctx.send(message)

@commands.command(name="help")
async def help_command(ctx):
    embed = discord.Embed(
        title="📖 Trivia Bot Help",
        description="Here are all the available commands:",
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="/trivia",
        value="Start a new trivia game. Answer a multiple choice question before the time runs out!",
        inline=False
    )

    embed.add_field(
        name="/highscore",
        value="Displays the top trivia players based on correct answers.",
        inline=False
    )

    embed.add_field(
        name="/help",
        value="Shows this help message.",
        inline=False
    )

    await ctx.send(embed=embed)

bot.add_command(trivia_command)
bot.add_command(highscore_command)
bot.add_command(help_command)