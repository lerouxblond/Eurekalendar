import discord
from discord.ext import commands


class TaskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def task(self, ctx):
        await ctx.send("that's a task!")


async def setup(bot):
    await bot.add_cog(TaskCog(bot))