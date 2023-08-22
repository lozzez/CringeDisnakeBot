import disnake
from disnake.ext import commands
import datetime
import asyncio
e = "<:emoji_31:1121750019410772038>"
color = 0x71368a
class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        if amount == 1:
            message = await ctx.send(f':wastebasket:Вы удалили {amount} сообщение!')
            await asyncio.sleep(3)
            await message.delete()
        elif amount <= 4:
            message = await ctx.send(f":wastebasket:Вы удалили {amount} сообщения!")
            await asyncio.sleep(3)
            await message.delete()
        else:
            message = await ctx.send(f':wastebasket:Вы удалили {amount} сообщений!')
            await asyncio.sleep(3)
            await message.delete()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lock(self, ctx, channel=None):
        channel = channel.mention if channel else ctx.channel.mention
        # await ctx.message.add_reaction("<:emoji_32:1121750062595313694>")
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed = disnake.Embed(
            title="🔒Заблокировано!",
            description=f"Канал {channel} успешно заблокирован!",
            color=0x71368a
        )
        current_time = datetime.datetime.now().strftime("%H:%M")
        embed.set_footer(text=f"Nirola | Сегодня в {current_time}",
                         icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx, channel=None):
        channel = channel.mention if channel else ctx.channel.mention
        # await ctx.message.add_reaction("<:emoji_32:1121750062595313694>")
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=None)
        embed = disnake.Embed(
            title="🔓Разблокировано!",
            description=f"Канал {channel} успешно разблокирован!",
            color=0x71368a
        )
        current_time = datetime.datetime.now().strftime("%H:%M")
        embed.set_footer(text=f"Nirola | Сегодня в {current_time}",
                         icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, *, message):
        await ctx.send(message)
        await ctx.message.delete()


def setup(bot: commands.Bot):
    bot.add_cog(Admin(bot))