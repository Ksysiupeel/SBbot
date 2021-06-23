import discord
import random
from discord.ext import commands
from utils.weather import Weather
from utils.bitcoin import Bitcoin


class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        ed = discord.Embed(title="Informacje o serwerze", description="Serwer Boży jest serwerem z super atmosferą", color=discord.Color.green())
        ed.set_thumbnail(url=ctx.guild.icon_url)
        ed.add_field(name="Właściciel serwera:", value=ctx.guild.owner)
        ed.add_field(name="Użytkowników na serwerze:", value=ctx.guild.member_count)
        ed.add_field(name="Wszystkie kanały:", value=str(len(ctx.guild.channels)))
        ed.add_field(name="Kanały głosowe:", value=str(len(ctx.guild.voice_channels)))
        await ctx.send(embed=ed)

    @commands.command()
    async def bot(self, ctx):
        ed = discord.Embed(title=f"Informacje na temat {self.bot.user.name}", color=discord.Color.blue())
        ed.set_thumbnail(url=self.bot.user.avatar_url)
        ed.add_field(name="Nazwa:", value=self.bot.user)
        ed.add_field(name="Twórca:", value="ksysiupeel#0810")
        ed.add_field(name="Język programowania:", value="Python")
        ed.add_field(name="Biblioteka:", value="discord.py")
        ed.add_field(name="Wersja biblioteki:", value="1.5.1")
        ed.add_field(name="Repozytorium:", value="https://github.com/Ksysiupeel/SBbot")
        await ctx.send(embed=ed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Ping bota wynosi {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def niespodzianka(self, ctx):
        with open("teksty.txt", "r") as f:
            list_elements = []
            for el in f:
                list_elements.append(el.splitlines())
            await ctx.send("".join(random.choice(list_elements)))

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        show_avatar = discord.Embed(color=discord.Color.blue())
        show_avatar.set_image(url="{}".format(member.avatar_url))
        await ctx.send(embed=show_avatar)

    @commands.command()
    async def ktopytal(self, ctx):
        await ctx.send("<@511953805991215114> **KTO PYTAŁ?!** <:ragey:734900366193328168>")

    @commands.command()
    async def wybor(self, ctx):
        wybory = [
            "TAK",
            "NIE"
        ]
        await ctx.send(random.choice(wybory))

    @commands.command()
    async def pogoda(self, ctx, *, city):
        await ctx.send(Weather.show_weather(city))

    @commands.command()
    async def bitcoin(self, ctx):
        await ctx.send(f"1 BTC kosztuje {Bitcoin.show_price_bitcoin()} PLN")

    @commands.command()
    async def losuj(self, ctx, *args):
        await ctx.send(random.choice(args))


def setup(bot):
    bot.add_cog(Commands(bot))