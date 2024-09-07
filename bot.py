from dotenv import load_dotenv
import os
import discord
from discord import app_commands

TOKEN = os.getenv('TOKEN')


@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()#スラッシュコマンドを同期

@tree.command(name="test",description="テストコマンド")
async def test_command(interaction: discord.Interaction):
    await interaction.response.send_message("test",ephemeral=True)#ephemeral=True→「これらはあなただけに表示されています」

client.run(TOKEN)
