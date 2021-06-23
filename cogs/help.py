import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pomoc(self, ctx):
        ed = discord.Embed(color=discord.Color.dark_grey(), title="Komendy dostępne na serwerze:")
        ed.add_field(name=".info", value="Zwraca informację o serwerze.", inline=False)
        ed.add_field(name=".bot", value="Zwraca informację o bocie dostępnym na serwerze.", inline=False)
        ed.add_field(name=".pogoda [nazwa miasta]", value="Zwraca temperaturę wraz z opisem wybranego przez siebie miasta.", inline=False)
        ed.add_field(name=".ping", value="Zwraca ping bota.", inline=False)
        ed.add_field(name=".niespodzianka", value="Losuje śmieszne teksty z określonej listy i zwraca ten tekst.", inline=False)
        ed.add_field(name=".avatar [nazwa użytkownika]", value="Zwraca avatar wybranego przez siebie użytkownika.", inline=False)
        ed.add_field(name=".ktopytal", value="Komenda uwielbiana przez użytkowników. Używana jest gdy samolot powie coś o co nikt nie pytał :).", inline=False)
        ed.add_field(name=".wybor", value="Losuje słowo z listy (['TAK','NIE']).", inline=False)
        ed.add_field(name=".bitcoin", value="Zwraca aktualny kurs bitcoin'a.", inline=False)
        ed.add_field(name=".clear [liczba wiadomości]", value="Usuwa wiadomości z czatu. Domyślna wartość jest ustawioan na 5.", inline=False)
        ed.add_field(name=".spam [nazwa użytkownika] [ilość] [wiadomość]", value="Oznacza użytkownika, domyślnie argument ilośc jest ustawiony na 10, jeżeli nie podamy wiadomości uzytkownik zostanie 'spingowany' bez niej.", inline=False)
        ed.add_field(name=".ban [użytkownik] [powód]", value="Banuje użytkownika, jeżeli nie podamy powodu użytkownik zostanie zbanowany z domyślnym powodem.", inline=False)
        ed.add_field(name=".kick [użytkownik] [powód]", value="Wyrzuca  użytkownika z serwera, jeżeli nie podamy powodu użytkownik zostanie wyrzucony z domyślnym powodem.", inline=False)
        ed.add_field(name=".unban [użytkownik]", value="Odbanowuje użytkownika.", inline=False)
        ed.add_field(name=".losuj [argumenty]", value="Komenda losuje jedną wartość z podanych argumentów", inline=False)
        ed.add_field(name=".dodaj [uzytkownik] [rola]", value="Komenda dodaje rolę użytkownikowi", inline=False)
        ed.add_field(name=".usun [uzytkownik] [rola]", value="Komenda usuwa role użytkownikowi", inline=False)
        await ctx.send(embed=ed)


def setup(bot):
    bot.add_cog(Help(bot))