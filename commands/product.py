from nextcord.ext import commands
import json
import aiohttp
import nextcord
from utils import token_seller, fidea_api
import asyncio


class Product(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add_product(self, ctx):
        if ctx.author.id != 1123903159346139137:
            await ctx.send(
                embed=nextcord.Embed(
                    description=f"""**Sorry This Command Only For Developer**"""
                )
            )
        if ctx.message.attachments:
            attachment = ctx.message.attachments[0]
            if attachment.filename.lower().endswith(".json"):
                content = await attachment.read()
                json_data = json.loads(content)
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token_seller}",
                }
                for data in json_data:
                    async with aiohttp.ClientSession() as session:
                        async with session.post(
                            f"{fidea_api}/fidea/v1/product",
                            json=data,
                            headers=headers,
                        ) as response:
                            resp = await response.json()
                            if resp["status_code"] == 201:
                                await ctx.send(
                                    embed=nextcord.Embed(
                                        description=f"""**Success Add Product `{data['title']}`**
```yml
Product : {data['title']}
Description : {data['description']}
Price : {data['price']}
Stock : {data['stock']}```""",
                                        color=ctx.author.color,
                                    ).set_thumbnail(data["image_url"])
                                )
                                await asyncio.sleep(5)


def setup(bot):
    bot.add_cog(Product(bot))
