from discord.ext import commands


class ErrorHandle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Nie znaleziono takiej komendy!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Musisz podać argument! {ctx.message.author.mention}")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Nie masz wystarczających uprawnień! {ctx.message.author.mention}")
        elif isinstance(error, commands.RoleNotFound):
            await ctx.send(f"Nie znaleziono takiej roli! {ctx.author.mention}")
        else:
            print("Znaleziono inny błąd!")
            raise error

def setup(bot):
    bot.add_cog(ErrorHandle(bot))