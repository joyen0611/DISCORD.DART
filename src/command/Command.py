import discord
from discord.ext import commands


class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        author = ctx.author

        embed = discord.Embed(title="이름", colour=0xffffff)
        embed.set_author(name="이름")
        embed.add_field(name="추천인 인증", value="tset")
        embed.add_field(name="서버소개", value="geid")
        embed.set_footer(icon_url=author.avatar_url, text=author.name)
