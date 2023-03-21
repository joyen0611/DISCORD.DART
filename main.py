import discord

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
      print(f'{client.user}로 로그인했습니다.')

@client.event
async def on_message(message):
      if message.author == client.user:
          return
      if message.content.startswith('!'):
            await message.channel.send(f'{message.}님 안녕하십니까.')
            await message.channel.send(f'저는 의 인사 관리 봇입니다.')
            await message.channel.send('무슨 도움이 필요하시나요?')
            await message.channel.send('    명령행동     명령어')
            await message.channel.send('1. 추천인 인증 : !test')
            await message.channel.send('2. 서버 소계   : !geid')

# @client.event
# async def on_member_join(member):
#       await member.send(f'{member.mention}님, 어서오세요!\n저는 {member.guild.name}의 인사 관리 봇이에요!\n도움이 필요하시면 "!help"를 적어주세요!')


      

client.run('NjkyMzI3OTU2ODM1NzI5NDE4.GuOc_T.RNncGZiPEQxR2a2JcLRuFDiot-z8_U_xuwdNwc')