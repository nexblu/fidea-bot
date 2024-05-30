import nextcord
from nextcord.ext import commands
from utils import prefix, token


bot = commands.Bot(
    command_prefix=prefix,
    intents=nextcord.Intents.all(),
    case_insensitive=True,
)


extensions = ["events.on_ready", "commands.product", "commands.broadcast"]

if __name__ == "__main__":
    for ext in extensions:
        bot.load_extension(ext)
    bot.run(token)
