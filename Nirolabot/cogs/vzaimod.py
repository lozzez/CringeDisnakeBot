import disnake
from disnake.ext import commands
import datetime
import asyncio
import random
e = "<:emoji_31:1121750019410772038>"
color = 0x71368a

class Vzaim(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command()
    async def dance(self, ctx):
        embed = disnake.Embed(
            title=f'**{ctx.author.display_name}** танцует',
            description=None,
            color=0x71368a
        )
        embed.set_image(
            url="https://images-ext-2.discordapp.net/external/4cJNDD-ProxYz7AXktX6PSQTxgKwrVQzCR6SsvH2uVc/https/i.waifu.pics/_BHLCbF.gif")
        current_time = datetime.datetime.now().strftime("%H:%M")
        embed.set_footer(text=f"Nirola | Сегодня в {current_time}",
                        icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
        await ctx.send(embed=embed)

    @commands.command()
    async def suicide(self, ctx):
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
        
    @commands.command()
    async def kill(self, ctx, member: disnake.Member = None):
        if member is None:
            await ctx.send("<:emoji_31:1121750019410772038>Вы не указали пользователя!")
        elif member == ctx.author:
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
            
    @commands.command()
    async def cry(self, ctx):
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
        
    @commands.command()
    async def hug(self, ctx, member: disnake.Member = None):
        if member is None:
            await ctx.send("<:emoji_31:1121750019410772038>Вы не указали пользователя!")
        elif member == ctx.author:
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
            
    @commands.command()
    async def feed(self, ctx, member: disnake.Member = None):
        if member is None:
            await ctx.send("<:emoji_31:1121750019410772038>Вы не указали пользователя!")
        elif member == ctx.author:
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
            
    @commands.command()
    async def kiss(self, ctx, member: disnake.Member = None):
        if member is None:
            await ctx.send("<:emoji_31:1121750019410772038>Вы не указали пользователя!")
        elif member == ctx.author:
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


def setup(bot: commands.Bot):
    bot.add_cog(Vzaim(bot))