Version = "1.0"#Version1.0
Generation = "2"

from discord.ext import commands
import os
import traceback
import discord
import random#ランダム
from discord.ext import tasks
from datetime import datetime 
from datetime import datetime, date, time, timezone#現在時間取得用
text_chat = discord.Object(id=743348378011697224)

client = discord.Client()
token = "NzQxOTM5OTg2NDgzMzgwMjY0.Xy-3dQ.iH6NBtDIQbHeCV2KHP57j2NJ3os"

@client.event
async def on_message(message):
    if message.author.bot:
        # もし、送信者がbotなら無視する
        return
    GLOBAL_CH_NAME = "genserver-global" # グローバルチャットのチャンネル名

    if message.channel.name == GLOBAL_CH_NAME:
        # genserver-globalの名前をもつチャンネルに投稿されたので、メッセージを転送する

        await message.delete() # 元のメッセージは削除しておく

        channels = client.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        # channelsはbotの取得できるチャンネルのイテレーター
        # global_channelsは genserver-global の名前を持つチャンネルのリスト

        embed = discord.Embed(title="genserver-global",
            description=message.content, color=0x00FF00)

        embed.set_author(name=message.author.display_name, 
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name}",
            icon_url=message.guild.icon_url_as(format="png"))
        # Embedインスタンスを生成、投稿者、投稿場所などの設定

        for channel in global_channels:
            # メッセージを埋め込み形式で転送
            await channel.send(embed=embed)

    # コマンド
    if message.content == 'g?Gen':
        await message.channel.send('ｎ？')
        
    if message.content == 'g?GenServer':
        await message.channel.send('GenServerについては公式サイトで！\nhttps://www.genserver.work/')

    if message.content == 'g?News':
        await message.channel.send('GenServerのニュースはこちら！\nhttps://www.genserver.work/news/\n\n最新のニュース\n今度GenServerHalloween2020を開催するらしい。\nhttps://www.genserver-event.work/')
        
    if message.content == "g?info":
        InfoEmbed_color = random.randint(0, 16777215)
        info = discord.Embed(color=int(InfoEmbed_color))#{EmbedMain}
        info.set_author(name="GEN3987Pot ℹnformation",icon_url="https://cdn.discordapp.com/avatars/719448030050254888/6c8b80f8eb07279c4baace98687a288d.webp?size=1024")
        info.add_field(name="Name:",value="GEN3987Pot",inline=False)#{Embed add}
        info.add_field(name="ID:",value="```js\n" + str(client.user.id) + "```",inline=True)#{Embed add}
        info.add_field(name="Version:",value="```json\n" + str(Version) + "```",inline=True)#{Embed add}
        info.add_field(name="Generation:",value="```json\n" + str(Generation) + "```",inline=True)#{Embed add}
        info.add_field(name="This bot created:",value="```" + str(client.user.created_at) + "```",inline=True)#{Embed add}
        info.add_field(name="Invitation url:",value="[招待はこちら](https://discord.com/api/oauth2/authorize?client_id=741939986483380264&permissions=8&scope=bot)",inline=False)#{Embed add}
        info.add_field(name="Invitation url:",value="[お問い合わせはこちら](https://discord.gg/UdWztKv)",inline=False)#{Embed add}
        info.add_field(name="Invitation url:",value="[GenServerイベント情報](https://www.genserver-event.work/)",inline=False)#{Embed add}
        info.add_field(name="Developer:",value="```py\n@GEN3987#7707```",inline=True)#{Embed add}
        info.add_field(name="Program language:",value="```css\nPython:3.7.7```",inline=True)
        await message.channel.send(embed=info)

    if message.content == "g?help":
        HelpEmbed_color = random.randint(0, 16777215)
        help = discord.Embed(color=int(HelpEmbed_color))#{EmbedMain}
        help.set_author(name="GEN3987Pot Help",icon_url="https://cdn.discordapp.com/avatars/741939986483380264/11caadb2e55e2a2a63849201826aa280.png?size=128")
        help.add_field(name="Command:",value="g?info\nいろいろ\n\ng?GenServer\nGenServerについて\n\ng?News\nGenServerのニュースが受け取れるよ\n\ng?member\nメンバーの数がわかるよ\n\ng?Gen\nGEN3987を召喚するよ",inline=False)#{Embed add}
        await message.channel.send(embed=help)

    if message.content != 'g?member':
        return

    # message インスタンスから guild インスタンスを取得
    guild = message.guild 

    # ユーザとBOTを区別しない場合
    member_count = guild.member_count
    await message.channel.send(f'メンバー数：{member_count}')

    # ユーザのみ
    user_count = sum(1 for member in guild.members if not member.bot)
    await message.channel.send(f'ユーザ数：{user_count}')

    # BOTのみ
    bot_count = sum(1 for member in guild.members if member.bot)
    await message.channel.send(f'BOT数：{bot_count}')
        
    #メンションに反応
    if client.user in message.mentions:#{メンション来たかif}
        reply = "ヘルプは`g?help`です" #{返信メッセージ変数定義}
        await message.channel.send(reply) # 返信メッセージを送信



client.run(token)
bot.run(token)
