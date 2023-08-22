import disnake
from disnake.ext import commands
from disnake import SelectMenu, SelectOption
from disnake import Member, OptionType
import datetime
# from disnake import Button, ButtonStyle
import asyncio
import random
from utils.TOKEN import token

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="n!", intents=intents, status=disnake.Status.dnd, activity=disnake.Game(name='Minecraft'))
bot.remove_command("help")

bot.load_extension("cogs.adminis")
bot.load_extension("cogs.razvlech")
bot.load_extension("cogs.vzaimod")
bot.load_extension("cogs.events")
bot.load_extension("cogs.moderation")
bot.load_extension("cogs.ecocogs.economy")
bot.load_extension("cogs.ecocogs.slash")
bot.load_extension("cogs.ecocogs.times")
bot.load_extension("cogs.ecocogs.shop")
# bot.load_extension("cogs.log")


e = "<:emoji_31:1121750019410772038>"
color = 0x71368a
            
@bot.command()
async def chel(ctx):
    if ctx.author.id != 1000822763885428786:
        await ctx.send("чел ты...")
    else:
        channel = bot.get_channel(1143074274110873622)
        while True:
            await channel.send("<@!1000822763885428786>")

   	
@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, user_id: int):
    user = await bot.fetch_user(user_id)
    await ctx.guild.unban(user)
    embed = disnake.Embed(title="Разбан!", description=f'<@{user.id}> был разбанен!', color=0x71368a)
    current_time = datetime.datetime.now().strftime("%H:%M")
    embed.set_footer(text=f"Nirola | Сегодня в {current_time}", icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def idban(ctx, user_id: int, *, reason=None):
    try:
        user = await bot.fetch_user(user_id)
        if user.id == ctx.author.id:
            await ctx.send("Вы не можете забанить самого себя!")
            return

        await ctx.guild.ban(user, reason=reason)
        
        embed = disnake.Embed(
            title="Бан!",
            description=f"**Модератор:** {ctx.author.mention}\n"
                        f"**Участник:** {user.mention}\n"
                        f"**Причина:** {reason}",
            color=0x71368a
        )
        current_time = datetime.datetime.now().strftime("%H:%M")
        embed.set_footer(text=f"Nirola | Сегодня в {current_time}", icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
        await ctx.send(embed=embed)
    except disnake.Forbidden:
        await ctx.send(f"{e}Не удалось забанить участника!")
    
@bot.slash_command(name='dance', description='Потанцевать')
async def dance(ctx):
    embed = disnake.Embed(
        title=f'**{ctx.author.display_name}** танцует',
        description=None,
        color=0x71368a
    )
    embed.set_image(url="https://images-ext-2.discordapp.net/external/4cJNDD-ProxYz7AXktX6PSQTxgKwrVQzCR6SsvH2uVc/https/i.waifu.pics/_BHLCbF.gif")
    current_time = datetime.datetime.now().strftime("%H:%M")
    embed.set_footer(text=f"Nirola | Сегодня в {current_time}", icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
    await ctx.send(embed=embed)
    
@bot.slash_command(name="avatar", description="Аватар пользователя")
async def avatar(ctx, member: disnake.Member = None):
    if member is None:
        member = ctx.author
    embed = disnake.Embed(
        description=None,
        color=0x71368a
    )
    current_time = datetime.datetime.now().strftime("%H:%M")
    embed.set_footer(text=f"Nirola | Сегодня в {current_time}",
                     icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
    embed.set_image(url=member.avatar.url)
    embed.title = f"Аватар пользователя {member.display_name}!"
    embed.url = member.avatar.url
    await ctx.send(embed=embed)



@bot.slash_command(name="suicide", description="...")
async def suicide(ctx):
    embed = disnake.Embed(
        title=f'{ctx.author.display_name} суициднулся;(',
        description='',
        color=0x71368a
    )
    current_time = datetime.datetime.now().strftime("%H:%M")
    embed.set_footer(text=f"Nirola | Сегодня в {current_time}",
                     icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
    embed.set_image(url='https://media.tenor.com/y1nv6p_0CGQAAAAC/tissue-roll-hangging.gif')
    await ctx.send(embed=embed)



@bot.slash_command(name="kill", description="Убить участника")
async def kill(ctx, member: Member):
    if member == ctx.author:
        embed = disnake.Embed(
            title=f'{ctx.author.display_name} суициднулся;(',
            description='',
            color=0x71368a
        )
        current_time = datetime.datetime.now().strftime("%H:%M")
        embed.set_footer(text=f"Nirola | Сегодня в {current_time}",
                        icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
        embed.set_image(url='https://media.tenor.com/y1nv6p_0CGQAAAAC/tissue-roll-hangging.gif')
        await ctx.send(embed=embed)
    else:
        embed = disnake.Embed(
            title=f'{ctx.author.display_name} убил {member.display_name}',
            description='',
            color=0x71368a
        )
        current_time = datetime.datetime.now().strftime("%H:%M")
        embed.set_footer(text=f"Nirola | Сегодня в {current_time}",
                        icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
        embed.set_image(url='https://media.tenor.com/NbBCakbfZnkAAAAM/die-kill.gif')
        await ctx.send(embed=embed)



@bot.slash_command(name='cry', description='Поплакать')
async def cry(ctx):
    embed = disnake.Embed(
        title=f'{ctx.author.display_name} плачет ;(',
        description='',
        color=0x71368a
    )
    current_time = datetime.datetime.now().strftime("%H:%M")
    embed.set_footer(text=f"Nirola | Сегодня в {current_time}",
                     icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
    embed.set_image(url='https://media.tenor.com/7zi5dPfCVLMAAAAM/marin.gif')
    await ctx.send(embed=embed)

@bot.slash_command(name='hug', description="Обнять участника")
async def hug(ctx, member: Member):
    if member == ctx.author:
        await ctx.send(f"{e}Вы не можете обнять самого себя!")
    else:
        embed = disnake.Embed(
            title=f'{ctx.author.display_name} обнял {member.display_name}',
            description='',
            color=0x71368a
        )
        current_time = datetime.datetime.now().strftime("%H:%M")
        embed.set_footer(text=f"Nirola | Сегодня в {current_time}",
                        icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
        embed.set_image(url='https://media.tenor.com/EM2G4oRozsIAAAAM/anime-hug.gif')
        await ctx.send(embed=embed)



@bot.slash_command(name='feed', description='Накормить участника')
async def feed(ctx, member: Member):
    if member == ctx.author:
        await ctx.send(f"{e}Вы не можете накормить самого себя!")
    else:
        embed = disnake.Embed(
            title=f'{ctx.author.display_name} накормил {member.display_name}',
            description='',
            color=0x71368a
        )
        current_time = datetime.datetime.now().strftime("%H:%M")
        embed.set_footer(text=f"Nirola | Сегодня в {current_time}",
                        icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
        embed.set_image(url='https://media.tenor.com/CHTk5L8ls8cAAAAM/eat-food.gif')
        await ctx.send(embed=embed)

@bot.slash_command(name='kiss', description='Поцеловать участника')
async def kiss( ctx, member: Member):
    if member == ctx.author:
        await ctx.send(f"{e}Вы не можете поцеловать самого себя!")
    else:
        embed = disnake.Embed(
            title=f'{ctx.author.display_name} поцеловал {member.display_name}',
            description='',
            color=0x71368a
        )
        current_time = datetime.datetime.now().strftime("%H:%M")
        embed.set_footer(text=f"Nirola | Сегодня в {current_time}",
                        icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
        embed.set_image(url='https://media.tenor.com/jnndDmOm5wMAAAAM/kiss.gif')
        await ctx.send(embed=embed)




@bot.slash_command(name='ship', description="Шипперить")
async def ship(ctx, *, message: str):
    p = random.randint(1, 100)
    await ctx.send(f"{message} подходит вам на {p}%")



@bot.slash_command(name="money", description="Орёл или решка?")
async def money(ctx):
    p = random.randint(1, 2)
    if p == 1:
        g = random.randint(1, 3)
        if g == 1:
            await ctx.send("Я выбрал орла! Ты решка. Выпал орёл, я выйграл. лох!")
        elif g == 2:
            await ctx.send("Я выбрал орла! Ты решку. Выпала решка, ты выйграл... лаки!")
        else:
            await ctx.send("Я выбрал орла, ты решку, но монета упала на ребро поэтому ничья. Мы лакеры")
    elif p == 2:
        f = random.randint(1, 3)
        if f == 1:
            await ctx.send("Я выбрал решку! Ты орёл, выпала решка. Я выйграл! лох.")
        elif f == 2:
            await ctx.send("Я выбрал решку! Ты орёл, выпал орёл. Ты выйграл... лаки")
        else:
            await ctx.send("Я выбрал решку, ты орёл, но монета упала на ребро поэтому ничья. Мы лакеры")
            
@bot.slash_command(name="anonimmsg", description="Отправить анонимное сообщение")
@commands.cooldown(1, 60, commands.BucketType.user)
async def anonimmsg(ctx, member: Member, *, message: str):
    embed = disnake.Embed(
        title="Вам отправили анонимное сообщение!",
        description="**Содержание:**\n"
                    f"{message}",
        color=color
    )
    current_time = datetime.datetime.now().strftime("%H:%M")
    embed.set_footer(text=f"Nirola | Сегодня в {current_time}", icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
    await member.send(embed=embed)
    await ctx.send("Сообщение успешно отправлено!", ephemeral=True)
    print(f"{ctx.author} отправил анонимное сообщение пользователю {member}, с содержанием {message}")
    
@bot.slash_command(name="mmoney", description="Орёл или Решка?")
async def mmoney(ctx, arg=commands.Param(choices=['орёл', 'решка'])):
    if arg == 'орёл':
        g = random.randint(1, 3)
        if g == 1:
            await ctx.send("Ты выбрал Орла, я Решка... Выпал Орёл, лакер!")
        elif g == 2:
            await ctx.send("Ты выбрал Орла, я Решка... Монета упала на ребро, ничья!")
        else:
            await ctx.send("Ты выбрал Орла, я Решка... Выпала Решка, лох!")
    else:
        f = random.randint(1, 3)
        if f == 1:
            await ctx.send("Ты выбрал Решку, я Орёл... Выпал Орёл, лох!")
        elif f == 2:
            await ctx.send("Ты выбрал Решку, я Орёл... Монета упала на ребро, ничья!")
        else:
            await ctx.send("Ты выбрал Решку, я Орёл... Выпала Решка, лакер!")

class Dropdown(disnake.ui.Select):
    def __init__(self):
        
        options = [
            disnake.SelectOption(label="Административное", value="option1", emoji="⚒️"),
            disnake.SelectOption(label="Модерация", value="option2", emoji="🛡️"),
            disnake.SelectOption(label="Экономика", value="option3", emoji="🪙"),
            disnake.SelectOption(label="Развлечения", value="option4", emoji="🎮")
        ]
        super().__init__(placeholder="Выберите раздел", options=options)

    async def callback(self, interaction: disnake.Interaction):
        selected_option = self.values[0]
        if selected_option == "option1":
            embed = disnake.Embed(
                title=":tools:Административное:",
                description='n!clear `{amount}`(Очистить указанное кол-во сообщений)\n'
                            'n!say `{text}` (Написать от лица бота)\n'
                            'n!lock (Заблокировать канал)\n'
                            'n!unlock (Раблокировать канал)',
                color=0x71368a
            )
            current_time = datetime.datetime.now().strftime("%H:%M")
            embed.set_footer(text=f"Nirola | Сегодня в {current_time}", icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        elif selected_option == "option2":
            embed = disnake.Embed(
                title=":shield:Модерация:",
                description='n!ban `{user}` `{reason}` (Забанить участника)\n'
                            'n!idban `{user id}` `{reason}` (Забанить участника с помощью его айди)\n'
                            'n!unban `{user id}` (Разбанить участника с помощью айди)\n'
                            'n!mute `{user}` `{time}` `{reason}` (Замутить участника на время)\n'
                            'n!unmute `{user}` (Размутить участника)\n'
                            'n!kick `{user}` `{reason}` (Кикнуть участника)',
                color=0x71368a
            )
            current_time = datetime.datetime.now().strftime("%H:%M")
            embed.set_footer(text=f"Nirola | Сегодня в {current_time}", icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        elif selected_option == "option3":
            embed = disnake.Embed(
                title="🪙Экономика:",
                description="n!daily (Забрать эжедневный бонус)\n"
                            'n!timely (Забрать ежевременный бонус)\n'
                            'n!work (Заработать деньги)\n'
                            'n!rob `{user}` (Ограбить участника)\n'
                            'n!pay `{user}` `{amount}` (Перевести деньги участинику)\n'
                            'n!balance `{user}` (Узнать баланс участника)\n'
                            '/выдать `{user}` `{amount}` (Выдать пользователяю деньги)\n'
                            'n!dep `{amount}` (Положить указанное кол-во денег в банк)\n'
                            'n!withdraw `{amount}` (Снять указанное кол-во денег)',
                color=0x71368a
            )
            current_time = datetime.datetime.now().strftime("%H:%M")
            embed.set_footer(text=f"Nirola | Сегодня в {current_time}", icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            
        elif selected_option == "option4":
            embed = disnake.Embed(
                title="🎮Развлечения:",
                description="n!avatar `{user}` (Узнать аватар пользователя)\n"
                            'n!ship `{arg}` (Зашиперриться с кем(чем)-то)\n'
                            'n!ben `{arg}` (Задать бену вопрос)\n'
                            'n!money (Сыграть в монетку с ботом)\n'
                            'n!kill `{user}` (Убить участника)'
                            'n!suicide (...)\n'
                            'n!dance (Потанцевать)\n'
                            'n!feed `{user}` (Накормить участника)\n'
                            'n!cry (Поплакать)\n'
                            'n!hug `{user}` (Обнять участника)\n'
                            'n!kiss `{user}` (Поцеловать участника)',
                color=0x71368a
            )
            current_time = datetime.datetime.now().strftime("%H:%M")
            embed.set_footer(text=f"Nirola | Сегодня в {current_time}", icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            
class DropdownView(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())

@bot.command()
async def help(ctx):
    view = DropdownView()
    embed = disnake.Embed(
        title=":flag_ch:Меню помощи:",
        description='',
        color=0x71368a
    )
    current_time = datetime.datetime.now().strftime("%H:%M")
    embed.set_footer(text=f"Nirola | Сегодня в {current_time}",
                     icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
    embed.set_author(name='prefix: "n!"', icon_url=ctx.guild.icon.url)
    embed.add_field(name=':tools:Административные:', value='`clear`, `say`, `lock`, `unlock`', inline=False)
    embed.add_field(name=':shield:Модерация:', value='`ban`, `idban`, `unban`, `mute`, `unmute` `kick`', inline=False)
    embed.add_field(name='🪙Экономика:', value='`daily`, `timely`, `work`, `rob`, `pay`, `shop`, `balance`, `/выдать`, `dep`, `withdraw`', inline=False)
    embed.add_field(name=':video_game:Развелечения:', value='`avatar`, `ship`, `ben`, `money`, `kill`, `suicide`, `dance`, `feed`, `cry`, `hug`, `kiss`', inline=False)
    await ctx.send(embed=embed, view=view)
        
bot.run(token)