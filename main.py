import discord
import random
from discord.ui import View, Button

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

class FreqView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.message_to_edit = None

    @discord.ui.button(label="🎛️ Změnit frekvenci", style=discord.ButtonStyle.primary)
    async def change_freq(self, interaction: discord.Interaction, button: Button):
        new_freq = f"{random.randint(30, 99)}.{random.randint(0, 99):02d}"

        if self.message_to_edit:
            try:
                await self.message_to_edit.delete()
            except:
                pass

        # ⚠️ Při odesílání nové zprávy přidáme znovu tlačítko
        new_view = FreqView()
        msg = await interaction.channel.send(
            f"📡 Nová frekvence: `{new_freq}`", view=new_view
        )
        new_view.message_to_edit = msg

        await interaction.response.defer()

@client.event
async def on_ready():
    print(f'✅ Bot je přihlášen jako {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "!start":
        view = FreqView()
        sent = await message.channel.send("Klikni na tlačítko pro změnu frekvence:", view=view)
        view.message_to_edit = sent

client.run("MTQwMTk0MDgxMDk1NzcyMTYyMQ.G8EBW5.Y1WfiDtWwkn4gD8qqqmiwapMpShrlgUjBXw1d8")
