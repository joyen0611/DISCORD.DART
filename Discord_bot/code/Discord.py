import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None, intents=discord.Intents.all())

#파일 불러오기
test_cord = open("test.txt", 'r')
cord = test_cord.read()
test_cord.close()
inp_aut = open("inaut.txt",'r', encoding='UTF8')
inaut = inp_aut.read()
inp_aut.close()
outp_aut = open("outaut.txt",'r', encoding='UTF8')
outaut = outp_aut.read()
outp_aut.close()

#Help명령어
@bot.command()
async def help(ctx):
    server = ctx.guild
    await ctx.send(f"안녕하세요.\n저는 \"**{server.name}**\"의\n인사 관리봇\"**{bot.user.name}**\"입니다.")
    await asyncio.sleep(1.5)
    await ctx.send(f"입장 인증 명령어는 \"**!test**\"")
    await asyncio.sleep(0.5)
    await ctx.send(f"서버 내 법 확인은 명령어는 \"**!law**\"\n입니다.")


#법 확인을 위한 명령어
@bot.command()
async def law(ctx):
    await ctx.send(f"{ctx.guild.name}의 법은 다음과 같습니다.")
    await asyncio.sleep(1.5)
    await ctx.send(f"https://docs.google.com/document/d/1ISBm3k_MKV4IRR9hbBmJmvk5wlFg9OfUWSIlUklF6bw/edit?usp=sharing")

#인증을 위한 함수
@bot.command()
async def test(ctx, * ,inp=None):
    role_name = inaut#출력하고 싶은 역할의 이름

    #특정 역할을 갖고 있는 인원 출력
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    if not role:
        print(f"{role_name} 역할이 존재하지 않습니다.")
        return
    members = role.members
    if not members:
        print(f"{role_name} 역할을 가진 멤버가 존재하지 않습니다.")
        return
    members_list = [f"{member.name}@{cord}" for member in members]

    #!test (사용자 인증코드)의 입력시 출력
    if 1 == members_list.count(inp):
        await ctx.send("인증되었습니다.")
        print("{}님 승인되었습니다.".format(ctx.author.name))
    
        role_name = outaut #추가할 역할
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if role:
            await ctx.send(f"{ctx.author.mention}님 안녕하십니까\n{ctx.guild.name}에 오신것을 축하드립니다.")
            await asyncio.sleep(1.5)
            await ctx.send(f"곧 {role_name} 역할을 부여하겠습니다.")
            await asyncio.sleep(0.75)
            await ctx.author.add_roles(role)
        else:
            await ctx.send("오류가 있습니다.\n곧 해결하겠습니다.")
            print(f"{role_name} 역할을 찾을 수 없습니다.")

    #!test (공백)의 입력시 출력
    elif inp == None:
        await ctx.send(f"{ctx.author.name}님 안녕하세요.\n**!test**명령어는 {ctx.guild.name}의 입장을 하기위한 명령어 입니다.")
        await asyncio.sleep(2)
        await ctx.send(f"\"**!test _추천인@인증코드_ **\" 형식으로 명령어를 작성해주세요.")

    #!test (난수의 값)의 입력시 출력
    else:
        await ctx.send("인증에 실패 했습니다.")
        print("{}님이 승인에 실패 했습니다.".format(ctx.author.name))
        
        print(f"인증 코드: ")
        for i in range(len(members_list)):
            print(f"{i + 1}번 \t{members_list[i]}")


#사용자가 들어오면 출력하는 챗팅
@bot.event
async def on_member_join(member):
    await member.send(f"안녕하세요, **{member.name}**님!\n\n\"**{member.guild.name}**\"에 오신 것을 환영합니다.\n만약 도움이 필요하시면 {member.guild.name}에 \" **!help** \"를 입력해주세요.")
    print("{}님 {}에 입장 했습니다.".format(member.name,member.guild.name))


#봇의 작동시 출력되는 CMD 출력 문자
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)
    await bot.change_presence(activity=discord.Game(name="인사 업무를 진행중 입니다.    지금은 \"!help\" 명령어를 입력받을수 있습니다."))
    print(f'{bot.user}로 로그인했습니다.')


#Error 커맨드 예외처리
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print(f"{ctx.author.name}님이 알 수 없는 명령어를 입력하였습니다.")


#Ctrl+C 입력시 코드 정지
async def start_bot():
    try:
        await bot.start('YOUR_TOKEN')
    except KeyboardInterrupt:
        await bot.logout()
        
run = open("ryn.txt",'r')
bot.run(run.read())
run.close()