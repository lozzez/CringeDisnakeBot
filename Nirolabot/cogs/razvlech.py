import disnake
from disnake.ext import commands
import datetime
import asyncio
import random

e = "<:emoji_31:1121750019410772038>"
color = 0x71368a

class Razvl(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        
    @commands.command()
    async def ben(self, ctx, kkk):
        kkk = random.randint(1, 3)
        if kkk == 1:
            await ctx.send("Хохохо")
        elif kkk == 2:
            await ctx.send("Yes")
        elif kkk == 3:
            await ctx.send('No')
        
    @commands.command()
    async def avatar(self, ctx, member: disnake.Member = None):
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
        embed.title = "Аватар пользователя!"
        embed.url = member.avatar.url
        await ctx.send(embed=embed)
        
    @commands.command()
    async def ship(self, ctx, *, message):
        mm = await ctx.send('Шипперю...:purple_heart:')
        await asyncio.sleep(3)
        p = random.randint(1, 100)
        await mm.edit(content=f'{message} подходит вам на {p}%')
        
    @commands.command()
    async def money(self, ctx):
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


def setup(bot: commands.Bot):
    bot.add_cog(Razvl(bot))