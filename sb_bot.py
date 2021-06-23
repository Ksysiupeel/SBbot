import discord
import os
from discord.ext import commands
from config import TOKEN, PREFIX

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Bronie serwera SB Official!"))
    print(f"{bot.user} już pracuje!")


# cogs command
@bot.command()
@commands.has_any_role("KONUSOWATY", "WAFEL", "Developer💻")
async def load(ctx, extension):
    await ctx.send(f"Ładowanie rozszerzenia {extension}")
    try:
        bot.load_extension(f"cogs.{extension}")
    except Exception as e:
        await ctx.send(f"Nie udało się załadować {extension}")
        print(f"[EXCEPTION]: {e}")
    await ctx.send(f"Załadowano rozszerzenie {extension}")

@bot.command()
@commands.has_any_role("KONUSOWATY", "WAFEL", "Developer💻")
async def reload(ctx, extension):
    await ctx.send(f"Przeładowuje rozszerzenie {extension}")
    try:
        bot.reload_extension(f"cogs.{extension}")
    except Exception as e:
        await ctx.send(f"Nie udało się przeładować rozszerzenia {extension}")
        print(f"[EXCEPTION]: {e}")
    await ctx.send(f"Przeładowano rozszerzenie {extension}")


@bot.command()
@commands.has_any_role("KONUSOWATY", "WAFEL", "Developer💻")
async def unload(ctx, extension):
    await ctx.send(f"Wyładowanie rozszerzenia {extension}")
    try:
        bot.unload_extension(f"cogs.{extension}")
    except Exception as e:
        await ctx.send(f"Nie udało się wyładować rozszerzenia {extension}")
        print(f"[EXCEPTION]: {e}")
    await ctx.send(f"Udało się wyładować rozszerzenie {extension}")


if __name__ == "__main__":
    for ext in os.listdir("./cogs"):
        if ext.endswith(".py"):
            try:
                bot.load_extension(f"cogs.{ext[:-3]}")
                print(f"Załadowano rozszerzenie {ext[:-3]}")
            except Exception as e:
                print(f"[EXCEPTION]: {e}")
    bot.run(TOKEN)