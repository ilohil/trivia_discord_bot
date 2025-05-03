import discord
from discord.ui import View, Button
from random import shuffle

active_games = {}

class TriviaView(View):
    def __init__(self, question_data, correct_answer, author_id):
        super().__init__(timeout=30)
        self.author_id = author_id
        self.correct_answer = correct_answer
        self.answered = False

        options = question_data["incorrect_answers"] + [correct_answer]
        shuffle(options)

        for option in options:
            self.add_item(TriviaButton(option, option == correct_answer, self))

    async def on_timeout(self):
        if not self.answered:
            await self.message.channel.send(f"⏰ You're out of time! Right answer was: **{self.correct_answer}**")
            self.clear_items()
            del active_games[self.author_id]

class TriviaButton(Button):
    def __init__(self, label, is_correct, view):
        super().__init__(label=label, style=discord.ButtonStyle.primary)
        self.is_correct = is_correct
        self.view_ref = view

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.view_ref.author_id:
            await interaction.response.send_message("This is not your game! Start your own game with /trivia", ephemeral=True)
            return

        if self.view_ref.answered:
            await interaction.response.send_message("You have already answered!", ephemeral=True)
            return

        self.view_ref.answered = True

        if self.is_correct:
            await interaction.response.send_message("✅ Right answer!")
        else:
            await interaction.response.send_message(f"❌ Wrong answer! Right answer was: **{self.view_ref.correct_answer}**")

        self.view_ref.clear_items()
        await self.view_ref.message.edit(view=self.view_ref)
        del active_games[interaction.user.id]