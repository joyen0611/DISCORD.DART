import discord
from discord.ext import commands
from command import Command

bot = commands.Bot(command_prefix="!", help_command=None, intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)
    print(f'{bot.user}로 로그인했습니다.')


if __name__ == '__main__':
    bot.add_cog(Command.Command(bot))
    bot.run(" ")
