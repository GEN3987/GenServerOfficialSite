Version = "1.0"#Version1.0
Generation = "2"

#Imports
import discord
import datetime#データタイム
import locale#ローカル
import random#ランダム
import re#置換
#グローバル定義
client = discord.Client()
locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")
dt_now = datetime.datetime.now()

#起動時のイベントハンドラ
@client.event
async def on_ready():
    ReadyDate = str(dt_now.strftime("%A, %d %B %Y %p%I:%M:%S.%f"))
    #起動通知inコンソール
    print(str(Generation) + "代目 GenServerBot ver" + str(Version))
    print("Client id:" + str(client.user.id))
    print(ReadyDate)
    print("----------------------------")
    #起動通知inDiscord
    channel = client.get_channel(719451472483319853)
    await channel.send("**" + str(Generation) + "代目 GenServerBot ver" + str(Version) + " 起動**\n```" + str(ReadyDate) + "```")#出力
    #アクティビティ
    await client.change_presence(activity=discord.Game(name="https://www.genserver.work/"))
#メッセージに反応するイベントハンドラ
@client.event
async def on_message(message):
    #Botの発言は無視
    if message.author.bot:#{MSG送信者がbotなのかif}
        return#(帰る)
    #cmd%help
    if message.content == "%help":
        help_cmd = discord.Embed(title="**GenServerBot command list**",description="CommandPrefix:`%`", color=0xB87C53)#{Embed main}
        help_cmd.add_field(name="Ⅰ",value="```\nhelp\nCMD一覧表示```",inline=True)#{Embed add}
        help_cmd.add_field(name="Ⅱ",value="```\ninfo\nBotのinfo表示```",inline=True)#{Embed add}
        help_cmd.add_field(name="Ⅲ",value="```\nAdminCmd\n運営専用CMD一覧表示```",inline=True)#{Embed add}
        await message.channel.send(embed=help_cmd) #{送信}
    #cmd%AdminCmd
    if message.content == "%AdminCmd":
        help_cmd = discord.Embed(title="**Admin command list**",description="CommandPrefix:`%`", color=0xB87C53)#{Embed main}
        help_cmd.add_field(name="Ⅰ",value="```\nopen\n開放通知```",inline=True)#{Embed add}
        help_cmd.add_field(name="Ⅱ",value="```\nclose\n終了通知```",inline=True)#{Embed add}
        help_cmd.add_field(name="Ⅲ",value="```\n%say <ChannelId:int> <Text:str> <Embed:bool>\n喋らせる```",inline=True)#{Embed add}
        await message.channel.send(embed=help_cmd) #{送信}
    #cmd%info
    if message.content == "%info":
        InfoEmbed_color = random.randint(0, 16777215)
        info = discord.Embed(color=int(InfoEmbed_color))#{EmbedMain}
        info.set_author(name="GenServerBot ℹnformation",icon_url="https://cdn.discordapp.com/avatars/719448030050254888/6c8b80f8eb07279c4baace98687a288d.webp?size=1024")
        info.add_field(name="Name:",value="[公式]GenServerBot✔#2816",inline=False)#{Embed add}
        info.add_field(name="ID:",value="```js\n" + str(client.user.id) + "```",inline=True)#{Embed add}
        info.add_field(name="Version:",value="```json\n" + str(Version) + "```",inline=True)#{Embed add}
        info.add_field(name="Generation:",value="```json\n" + str(Generation) + "```",inline=True)#{Embed add}
        info.add_field(name="This bot created:",value="```" + str(client.user.created_at) + "```",inline=True)#{Embed add}
        info.add_field(name="Invitation url:",value="[非公開](https://discord.com/GenServerBot)",inline=False)#{Embed add}
        info.add_field(name="Developer:",value="```py\nRinrin.py#5671\nGEN3987#7707\nたんぽぽ#9090```",inline=True)#{Embed add}
        info.add_field(name="Program language:",value="```css\nPython:3.7.7```",inline=True)
        await message.channel.send(embed=info)
    #メンションに反応
    if client.user in message.mentions:#{メンション来たかif}
        reply = "ヘルプは`%help`です" #{返信メッセージ変数定義}
        await message.channel.send(reply) # 返信メッセージを送信
    #cmd/open(開放通知)
    if message.content == "%open":
        if message.author.guild_permissions.administrator:#{アドミンが入力したかif}
            tuuti_role = "<@&712193009013227550>"
            open_date_r = str(dt_now.strftime("%A, %d %B %Y %p%I:%M:%S.%f"))#{変数定義}
            open_date2_r = discord.Embed(title="【Open】" + str(open_date_r), color=0x00BC16)#{変数定義}
            open_date2_r.set_thumbnail(url=message.guild.icon_url)
            await message.channel.send(tuuti_role, embed=open_date2_r) #{メッセージ送信}
            await message.delete()
        else:#{失敗したかif}
            await message.channel.send("このコマンドを使用する権限はありません。")#{否定}
    #cmd/close(終了通知)
    if message.content == "%close":
        if message.author.guild_permissions.administrator:#{アドミンが入力したかif}
            tuuti_role_2 = "<@&712193009013227550>"
            close_date_r = str(dt_now.strftime("%A, %d %B %Y %p%I:%M:%S.%f"))#{変数定義}
            close_date2_r = discord.Embed(title="【Close】" + str(close_date_r), color=0x7f007f)#{変数定義}
            close_date2_r.set_thumbnail(url=message.guild.icon_url)
            await message.channel.send(tuuti_role_2, embed=close_date2_r) #{メッセージ送信}
            await message.delete()
        else:#{失敗したかif}
            await message.channel.send("申し訳ありませんが、あなたにこのコマンドを使用する権限はありません。")#{否定}
    #cmd%say <ChannelId:int> <Text:str> <Embed:bool>
    if message.content.startswith("%say "):#{始まり}
        if message.author.id == 724976600873041940 or message.author.id == 563328775211974677:
            print_split = message.content.split(" ")#{Split}
            if "True" in print_split or "true" in print_split:
                print_channel = client.get_channel(int(print_split[1]))#{チャンネルid取得}
                print_text = (str(print_split[2:]))#{Text取得}
                print_text = print_text.replace("['", " ")
                print_text = print_text.replace("', '", " ")
                print_text = print_text.replace("']", " ")
                print_text = print_text.replace("[\"", " ")
                print_text = print_text.replace("\", """, " ")
                print_text = print_text.replace("\"]", " ")
                print_text = print_text.replace("True", " ")
                print_text = print_text.replace("true", " ")
                print_embed = discord.Embed(description=str(print_text),color=0x2f3136)#{Embed main}
                await print_channel.send(embed=print_embed)#{発言(埋め込みメッセージ)}
            else:
                print_channel = client.get_channel(int(print_split[1]))#{チャンネルid取得}
                print_text = (str(print_split[2:]))#{Text取得}
                print_text = print_text.replace("['", " ")
                print_text = print_text.replace("', '", " ")
                print_text = print_text.replace("']", " ")
                print_text = print_text.replace("[\"", " ")
                print_text = print_text.replace("\", """, " ")
                print_text = print_text.replace("\"]", " ")
                print_text = print_text.replace("False", " ")
                print_text = print_text.replace("false", " ")
                print_text = print_text.replace("\u3000", " ")
                await print_channel.send(print_text)#{発言(ノーマルメッセージ)}
        else:
            await message.channel.send("申し訳ありませんが、あなたにこのコマンドを使用する権限はありません。")#{否定}

client.run("NzE5NDQ4MDMwMDUwMjU0ODg4.Xt3y-w.Lfg0rR2rXshSePf0sqA9clOrepA")