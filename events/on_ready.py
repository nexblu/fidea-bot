import nextcord
from nextcord.ext import commands


class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} is ready")


def setup(bot):
    bot.add_cog(OnReady(bot))
