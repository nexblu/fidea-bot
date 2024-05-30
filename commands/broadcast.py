import nextcord
from nextcord.ext import commands
import json


class Broadcast(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bc(self, ctx):
        if ctx.author.id != 1123903159346139137:
            return await ctx.send(
                embed=nextcord.Embed(
                    description=f"""**Sorry This Command Only For Developer**"""
                )
            )
        if ctx.message.attachments:
            attachment = ctx.message.attachments[0]
            if attachment.filename.lower().endswith(".json"):
                content = await attachment.read()
                json_data = json.loads(content)
                for i in json_data:
                    try:
                        member = nextcord.utils.get(ctx.guild.members, id=i)
                        await member.send(
                            embed=nextcord.Embed(
                                title="Fidea Project",
                                url="https://github.com/Fidea-Ecommerce",
                                description=f"halo semua selamat malam {member.mention}, sorry mengganggu waktunya, kami selaku tim developer fidea project mengucapkan terimakasih karena telah berpartisipasi dalam projectan kali ini, bagi kamu yang sudah membayar lebih kami mengucapkan terima kasih banyak, kami selaku developer meminta maaf jika ada kekurangan dalam project kali ini, sekali lagi terimakasih karena telah berpartisipasi dalam projectan kali ini\n\n- developer (<@1123903159346139137>, <@386168283386216451>, <@1142640378818854922>)",
                                colour=0x00B0F4,
                            )
                        )
                    except:
                        pass
                return await ctx.send(f"success send messages")


def setup(bot):
    bot.add_cog(Broadcast(bot))
