import disnake
from disnake.ext import commands
import datetime
import asyncio

e = "<:emoji_31:1121750019410772038>"
color = 0x71368a

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("====Bot started====")
        voice_channel = self.bot.get_channel(1138112476647534693) 
        voice_client = await voice_channel.connect()
        await voice_client.disconnect()
        await voice_channel.connect()
        await voice_client.move_to(voice_channel)
        await voice_client.guild.change_voice_state(channel=voice_channel, self_mute=True, self_deaf=True)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def join(self, ctx):
        voice_channel = self.bot.get_channel(1138112476647534693) 
        voice_client = await voice_channel.connect()
        await voice_client.disconnect()
        await voice_channel.connect()
        await voice_client.move_to(voice_channel)
        await voice_client.guild.change_voice_state(channel=voice_channel, self_mute=True, self_deaf=True)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1121765682007248906)
        role = member.guild.get_role(1087107282166349834)
        if member.bot:
            rol = member.guild.get_role(1062708580123414548)
            await member.add_roles(rol)
        else:
            await member.add_roles(role)
            embed = disnake.Embed(
                title=None,
                description=None,
                color=0x71368a
            )
            # embed.set_author(name='Nirola', icon_url='https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473')
            embed.set_image(url="https://media.tenor.com/FhtL5SNaHvMAAAAM/touhou-keine.gif")
            await channel.send(f"Привет, {member.mention}!", embed=embed)


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(1121765682007248906)
        if member.bot:
            print("Бот кикнут/забанен")
        else:
            embed = disnake.Embed(
                title=None,
                description=None,
                color=0x71368a
            )
            embed.set_image(url="https://media.tenor.com/dwiQGuovsA8AAAAM/cry.gif")
            await channel.send(f"Пока, {member.mention}!", embed=embed)


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            # await ctx.message.add_reaction("<:emoji_31:1121750019410772038>")
            await ctx.send('<:emoji_31:1121750019410772038>У мужлан нет прав!')
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            # await ctx.message.add_reaction("<:emoji_31:1121750019410772038>")
            await ctx.send("<:emoji_31:1121750019410772038>Отсутствует обязательный аргумент!")
        elif isinstance(error, commands.errors.BadArgument):
            # await ctx.message.add_reaction("<:emoji_31:1121750019410772038>")
            await ctx.send("<:emoji_31:1121750019410772038>Неверный аргумент!")
        elif isinstance(error, commands.errors.CheckFailure):
            # await ctx.message.add_reaction("<:emoji_31:1121750019410772038>")
            await ctx.send("<:emoji_31:1121750019410772038>Вы не имеете права использовать эту команду!")
    
    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after
            if remaining_time:
                seconds = round(remaining_time % 60)
                if seconds == 1:
                    await ctx.send(f"{e}На эту команду стоит кд! Подожди ещё {seconds} секунду!", ephemeral=True)
                elif seconds <= 4:
                    await ctx.send(f"{e}На эту команду стоит кд! Подожди ещё {seconds} секунды!", ephemeral=True)
                elif seconds >= 5:
                    await ctx.send(f"{e}На эту команду стоит кд! Подожди ещё {seconds} секунд!", ephemeral=True)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('<:emoji_31:1121750019410772038>У мужлан нет прав!', ephemeral=True)
        return


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = self.bot.get_channel(1121065615831072778)
        if message.author.id == 1137451055987310715:
            print("Ошибка!")
        else:
            embed = disnake.Embed(
                title=":no_entry_sign:Сообщение удалено!",
                description='',
                color=0x71368a
            )
            current_time = datetime.datetime.now().strftime("%H:%M")
            embed.set_footer(text=f"Nirola | Сегодня в {current_time}",
                            icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
            embed.add_field(name=':bust_in_silhouette:Автор:', value=message.author.mention, inline=True)
            embed.add_field(name=':envelope_with_arrow:Сообщение:', value=message.content, inline=False)
            embed.add_field(name=':speech_balloon:Канал:', value=message.channel.mention, inline=False)
            await channel.send(embed=embed)


    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_aften):
        channel = self.bot.get_channel(1121065615831072778)
        if message_before.author.id == 1137451055987310715:
            print("Ошибка!")
        else:
            embed = disnake.Embed(
                title=":pencil2:Сообщение обновленно!",
                description='',
                color=0x71368a
            )
            current_time = datetime.datetime.now().strftime("%H:%M")
            embed.set_footer(text=f"Nirola | Сегодня в {current_time}",
                            icon_url="https://images-ext-1.discordapp.net/external/ssWuHwdBk-D_v9KhXzDKSL_4mXxUIb6R-dR5TWgFZHw/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1128967077634519080/bb503956522ea98b2a8d2c079e40a316.png?width=473&height=473")
            embed.add_field(name=':bust_in_silhouette:Автор:', value=message_before.author.mention, inline=True)
            embed.add_field(name=':envelope_with_arrow:Было:', value=message_before.content, inline=False)
            embed.add_field(name=':email:Стало:', value=message_aften.content, inline=False)
            embed.add_field(name=':speech_balloon:Канал:', value=message_before.channel.mention, inline=False)
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Event(bot))