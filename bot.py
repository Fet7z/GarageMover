import discord
import config
from discord.ext import commands
from discord import app_commands
from sql_update import *

bot = commands.Bot(command_prefix="/", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} est en ligne")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commande(s) chargée(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="fourriere", description="Permet de déplacer un véhicule dans un garage grace à la plaque")

@app_commands.guild_only()
@app_commands.describe(plate = "Plaque du véhicule")
async def fourriere(interaction: discord.Interaction, plate: str):
    update = update_garage(plate)
    await interaction.response.send_message(update)

bot.run(config.TOKEN)