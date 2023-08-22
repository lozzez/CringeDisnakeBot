import disnake
from disnake.ext import commands
import random
import datetime
import asyncio

e = "<:emoji_31:1121750019410772038>"
color = 0x71368a

class Moder(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
      
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: disnake.Member, *, reason=None):
        try:
            if member == ctx.author:
                # await ctx.message.add_reaction("<:emoji_31:1121750019410772038>")
                await ctx.send("<:emoji_31:1121750019410772038>Вы не можете забанить самого себя!")
            else:
                # await ctx.message.add_reaction("<:emoji_32:1121750062595313694>")
                await member.ban(reason=reason)
                embed = disnake.Embed(
                    title="Бан!",
                    description=f"**Модератор:** <@{ctx.author.id}>\n"
                                f"**Участник:** <@{member.id}>\n"
                                f"**Причина:** {reason}",
                    color=0x71368a
                )
                embed.set_footer(text="Nirola", icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
                await ctx.send(embed=embed)
        except disnake.Forbidden:
            # await ctx.message.add_reaction("<:emoji_31:1121750019410772038>")
            await ctx.send("<:emoji_31:1121750019410772038>Не удалось забанить участника!")
            
    # @commands.command()
    # @commands.has_permissions(administrator=True)
    # async def idban(self, ctx, user_id: int, *, reason=None):
    #     try:
    #         user = await ctx.guild.fetch_member(user_id)
    #         if user == ctx.author:
    #             await ctx.send(f"{e}Вы не можете забанить самого себя!")
    #         else:  
    #             embed = disnake.Embed(
    #                 title="Бан!",
    #                 description=f"**Модератор:** <@{ctx.author.id}>\n"
    #                             f"**Участник:** <@{user.id}>\n"
    #                             f"**Причина:** {reason}",
    #                 color=0x71368a
    #             )
    #             embed.set_footer(text="Nirola", icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
    #             await ctx.send(embed=embed)
    #     except disnake.Forbidden:
    #         await ctx.send(f"{e}Не удалось забанить пользователя.")
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: disnake.Member, *, reason=None):
        try:
            if member == ctx.author:
                await ctx.send(f"{e}Вы не можете кикнуть самого себя!")
            else:
                await member.kick(reason=reason)
                embed = disnake.Embed(
                    title="Кик!",
                    description=f"**Модератор:** <@{ctx.author.id}>\n"
                                f"**Участник:** <@{member.id}>\n"
                                f"**Причина:** {reason}",
                    color=0x71368a
                )
                embed.set_footer(
                    text="Nirola",
                    icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473"
                )
                await ctx.send(embed=embed)
        except disnake.Forbidden:
            await ctx.send(f"{e}Не удалось кикнуть пользователя!")
            
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: disnake.Member, duration: str, *, reason=None):
        try:
            if member == ctx.author:
                await ctx.send(":emoji_31: Вы не можете замутить самого себя!")
            else:
                time_units = {"m": 60, "h": 3600, "d": 86400}
                time_str = duration[:-1]
                time_unit = duration[-1]
                if time_unit not in time_units or not time_str.isdigit():
                    await ctx.send(f"{e}Указано некорректное время!")
                    return
                mute_time = int(time_str) * time_units[time_unit]
                if mute_time >= 2505600:
                    await ctx.send(f"{e}Время не может быть больше 28 дней!")
                    return
                await member.timeout(reason=reason, duration=mute_time)
                embed = disnake.Embed(
                    title="Мут!",
                    description=f"**Модератор:** {ctx.author.mention}\n"
                                f"**Участник:** {member.mention}\n"
                                f"**Время:** {duration}\n"
                                f"**Причина:** {reason}\n",
                    color=0x71368a
                )
                current_time = datetime.datetime.now().strftime("%H:%M")
                embed.set_footer(text=f"Nirola | Сегодня в {current_time}", icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
                await ctx.send(embed=embed)
        except disnake.Forbidden:
            await ctx.send(f"{e}Не удалось замутить пользователя!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: disnake.Member):
        try:
            await member.edit(timeout=False)
            embed = disnake.Embed(
                title="Размут!",
                description=f"{member.mention} будет размучен через 10 секунд!",
                color=color
            )
            current_time = datetime.datetime.now().strftime("%H:%M")
            embed.set_footer(text=f"Nirola | Сегодня в {current_time}", icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
            await ctx.send(embed=embed)
        except disnake.Forbidden:
            await ctx.send(f"{e}Не удалось размутить пользователя!")

def setup(bot: commands.Bot):
    bot.add_cog(Moder(bot))