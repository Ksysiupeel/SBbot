import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_any_role("KONUSOWATY", "WAFEL", "Developer💻")
    async def clear(self, ctx, *, amount=5):
        await ctx.channel.purge(limit=amount)
    
    @commands.command()
    @commands.has_any_role("KONUSOWATY", "WAFEL", "Developer💻")
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        if not reason == None:
            await ctx.send(f"{member.mention} został zbanowany przez {ctx.message.author.mention} powód: {reason}")
        else:
            await ctx.send(f"{member.mention} został zbanowany przez {ctx.message.author.mention}")

    @commands.command()
    @commands.has_any_role("KONUSOWATY", "WAFEL", "Developer💻")
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        if not reason == None:
            await ctx.send(f"{member.mention} został wyrzucony przez {ctx.message.author.mention} powód: {reason}")
        else:
            await ctx.send(f"{member.mention} został wyrzucony przez {ctx.message.author.mention}")

    @commands.command()
    @commands.has_any_role("KONUSOWATY", "WAFEL", "Developer💻")
    async def spam(self, ctx, member: discord.Member, amount=10, *, msg=None):
        for _ in range(amount):
            if not msg == None:
                await ctx.send(f"{member.mention} {msg}")
            else:
                await ctx.send(member.mention)
    
    @commands.command()
    @commands.has_any_role("KONUSOWATY", "WAFEL", "Developer💻")
    async def unban(self, ctx, member):
        ban_list = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_user in ban_list:
            user = ban_user.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{member} został odbanowany przez {ctx.author.mention}")
                return


    @commands.command()
    @commands.has_any_role("KONUSOWATY", "WAFEL", "Developer💻")
    async def dodaj(self, ctx, user: discord.Member, role: discord.Role):
        await user.add_roles(role)
        await ctx.send(f"Rola {role} została pomyślnie dodana {user.mention}")

    @commands.command()
    @commands.has_any_role("KONUSOWATY", "WAFEL", "Developer💻")
    async def usun(self, ctx, user: discord.Member, role: discord.Role):
        await user.remove_roles(role)
        await ctx.send(f"Rola {role} została pomyślnie usunięta {user.mention}")

def setup(bot):
    bot.add_cog(Moderation(bot))