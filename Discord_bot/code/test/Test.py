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

class Test:
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