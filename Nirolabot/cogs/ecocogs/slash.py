import disnake
from disnake.ext import commands
import random
from utils.databases import UsersDataBase

class SlashC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = UsersDataBase()
    
    @commands.slash_command(name='баланс', description='Посмотреть баланс')
    async def balance(self, interaction, member: disnake.Member = None):
        await self.db.create_table()
        if member is None:
            member = interaction.author
        await self.db.add_user(member)
        user = await self.db.get_user(member)
        embed = disnake.Embed(color=0x2F3136, title=f'Баланс пользователя - {member}')
        embed.add_field(name='🪙 Деньги', value=f'```{user[1]}```')
        embed.add_field(name=':bank:  Банк', value=f'```{user[2]}```')
        embed.set_thumbnail(url=member.display_avatar.url)
        await interaction.response.send_message(embed=embed)
    
    @commands.slash_command(name='выдать', description='Выдать деньги пользователю')
    @commands.has_permissions(administrator=True)
    async def give(self, interaction, member: disnake.Member, amount: int):
        await self.db.create_table()
        # await self.db.get_user(member)
        await self.db.add_user(member)
        await self.db.update_money(member, amount, 0)
        embed = disnake.Embed(color=0x2F3136, title=f'Выдача денег пользователю - {member}')
        embed.description = f'{interaction.author.mention} выдал {member.mention} {amount} 🪙.'
        embed.set_thumbnail(url=member.display_avatar.url)
        # embed.add_field(name='🪙 Деньги', value=f'```{member[1]}```')
        # embed.add_field(name=':bank:  Банк', value=f'```{member[2]}```')
        await interaction.response.send_message(embed=embed)
    
def setup(bot):
    bot.add_cog(SlashC(bot))