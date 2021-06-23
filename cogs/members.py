from discord.ext import commands


class Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        specific_channel = self.bot.get_channel(556184005632851989)
        await specific_channel.send(f"{member.mention} dołączył na serwer!! Witamy! <:taktycznyjanek:710758736989257738>")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        specific_channel = self.bot.get_channel(556184005632851989)
        await specific_channel.send(f"{member} wyszedł z serwera! Żegnamy! <:pepehands:734900321272332409>")    


def setup(bot):
    bot.add_cog(Members(bot))