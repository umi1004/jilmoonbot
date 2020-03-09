import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("질문봇을 플레이"))
  print("I'm Ready!")
  print(client.user.name)
  print(client.user.id)
  
@client.event
async def on_message(message):
  if message.author.bot:
    return None

# 임베드
  if message.content == "/도움":
    embed = discord.Embed(icon_url="https://imgur.com/RIj2AXg", title="질문봇의 사용방법!", color=0x62c1cc)
    embed.add_field(value="사이트", name="네이버, 네이트, 다음, 유튜브, 티빙, 왓챠, 넷플릭스, 메이플 인벤, 메이플지지", inline=False)
    embed.add_field(value="메이플", name="헤이븐, 세계수, 크리티아스, 여로, 모라스, 에스페라, 어빌리티, 재획준비, 재획비, 앱솔추옵, 파프추옵", inline=False)
    embed.add_field(value="배그, 롤전적", name="ㅇㅇ 배그, 배그전적, 롤전적", inline=False)
    #embed.add_field(value="", name="", inline=False)
    #embed.add_field(value="", name="", inline=False)
    await message.channel.send("/를치고 검색해 주세요 :)", embed=embed)

  

  if message.content == "/도움말":
    await message.channel.send("각종 사이트,유튜브, 메이플 인벤,메이플지지, 롤전적, 배그전적 등등.. ")
  if message.content == "/유미":
    await message.channel.send("천사 그저 빛")
  if message.content == "/현호":
    await message.channel.send("노돼 : 노잼 돼지라는 뜻")
  if message.content == "/슬기":
    await message.channel.send("슬기 몽키")
  if message.content == "/혜원":
    await message.channel.send("힘만 센 언니")
  if message.content == "/유진":
    await message.channel.send("고뚱 : 고릴라 뚱땡이라는 뜻")
  if message.content == "/메이플":
    await message.channel.send("재획비, 재획, 어빌리티, 헤이븐, 세계수, 크리티아스, 여로, 모라스, 에스페라, 파프추옵, 앱솔추옵을(를) 입력해 주세요.")
  if message.content == "/헤이븐":
    await message.channel.send("https://cdn.discordapp.com/attachments/562160059786985472/684900134554697728/i14525276264.png")
  if message.content == "/세계수":
    await message.channel.send("https://cdn.discordapp.com/attachments/562160059786985472/684900137251897348/i14234148433.png")
  if message.content == "/크리티아스":
    await message.channel.send("https://cdn.discordapp.com/attachments/562160059786985472/684900140917719080/i14238232989.png")
  if message.content == "/여로":
    await message.channel.send("https://cdn.discordapp.com/attachments/562160059786985472/684900140095504452/i14203587876.png")
  if message.content == "/모라스":
    await message.channel.send("https://cdn.discordapp.com/attachments/562160059786985472/684900142465548328/i14297826071.png")
  if message.content == "/에스페라":
    await message.channel.send("https://cdn.discordapp.com/attachments/562160059786985472/684900145086857461/i14210168484.png")
  if message.content == "/깡충":
    await message.channel.send("갓길드")
  if message.content == "/하이":
    await message.channel.send("(^^)/")
  if message.content == "/야":
    await message.channel.send("왜")
  if message.content == "/예쁜척":
    await message.channel.send("(*ૂ❛ัᴗ❛ั*ૂ)")
  if message.content == "/치킨":
    await message.channel.send("✦‿✦")
  if message.content == "/치킨추천":
    await message.channel.send("뿌링클")
  if message.content == "/노래틀어줘":
    await message.channel.send("다른 봇을 이용해 주세요")
  if message.content == "/노래":
    await message.channel.send("다른 봇을 이용해 주세요")
  if message.content == "/최고 아이돌":
    await message.channel.send("방탄소년단")
  if message.content == "/아이돌":
    await message.channel.send("방탄소년단")
  if message.content == "/파프추옵":
    await message.channel.send("https://cdn.discordapp.com/attachments/549251241549758467/656786274224439298/ED8C8CED9484EB8B88EBA5B4ECB694EC98B5.png")
  if message.content == "/네이버":
    await message.channel.send("https://www.naver.com/")
  if message.content == "/다음":
    await message.channel.send("https://www.daum.net/")
  if message.content == "/네이트":
    await message.channel.send("https://www.nate.com/")
  if message.content == "/유튜브":
    await message.channel.send("https://www.youtube.com/?hl=ko&gl=KR")
  if message.content == "/메이플 인벤":
    await message.channel.send("http://maple.inven.co.kr/")
  if message.content == "/메이플지지":
    await message.channel.send("https://maple.gg/")
  if message.content == "/배그전적":
    await message.channel.send("https://pubg.op.gg/")
  if message.content == "/롤전적":
    await message.channel.send("http://www.op.gg/")
  if message.content == "/재획비":
    await message.channel.send("https://cdn.discordapp.com/attachments/549251241549758467/556649088410583041/9876f09e0a720f9c.png")
  if message.content == "/어빌리티":
    await message.channel.send("https://cdn.discordapp.com/attachments/549251241549758467/655659319051681813/1.png")
  if message.content == "/앱솔추옵":
    await message.channel.send("https://cdn.discordapp.com/attachments/549251241549758467/570575927130587136/dee113d2e133c5ef.PNG")
  if message.content == "/안녕":
    await message.channel.send("안녕하세요:)")
  if message.content == "/뭐해?":
    await message.channel.send("생각하고 있어요")
  if message.content == "/아이돌 좋아해?":
    await message.channel.send("방탄소년단 좋아해요~")
  if message.content.startswith("/안녕하세요"):
    await message.channel.send("반갑습니다:D")
  if message.content == "/유미 배그":
    await message.channel.send("https://pubg.op.gg/user/t_OuO_r")
  if message.content == "/유진 배그":
    await message.channel.send("https://pubg.op.gg/user/bigboss1227")
  if message.content == "/혜원 배그":
    await message.channel.send("https://pubg.op.gg/user/Hye_n52")
  if message.content == "/현호 배그":
    await message.channel.send("https://pubg.op.gg/user/Captain_Of_Best")
  if message.content == "/슬기 배그":
    await message.channel.send("https://pubg.op.gg/user/S_OwO_K")
  if message.content == "/뷔":
    await message.channel.send("유미 남친")
  if message.content == "/유미 남친":
    await message.channel.send("김태형=V")
  if message.content == "/질문봇":
    await message.channel.send("똑똑이 (ง •̀_•́)ง")
  if message.content == "/티빙":
    await message.channel.send("http://www.tving.com/")
  if message.content == "/넷플릭스":
    await message.channel.send("https://www.netflix.com/")
  if message.content == "/왓챠":
    await message.channel.send("https://play.watcha.net/")
  if message.content == "/왕코":
    await message.channel.send("ㄱㅇㅈ..?")

# 2020.03.05 업데이트 이전
  if message.content == "/재획준비":
    await message.channel.send("재획, 링크, 유니온, 경쿠, 경뿌, 몬스터파크 물약, 혈맹의 반지, 정령의 펜던트")
  if message.content == "/혜띄":
    await message.channel.send("(❁´▽`❁)")
  if message.content == "/혀노":
    await message.channel.send("노잼 아저씨")
  if message.content == "/":
    await message.channel.send("")
  if message.content == "/":
    await message.channel.send("")

# 2020~ 나중에 다른거 추가 준비


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
