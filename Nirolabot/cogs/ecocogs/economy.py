import disnake
from disnake.ext import commands
import random
from utils.databases import UsersDataBase


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = UsersDataBase()
        
    @commands.command()
    async def balance(self, ctx, member: disnake.Member = None):
        if member is None:
            member = ctx.author
        await self.db.add_user(member)
        user = await self.db.get_user(member)
        embed = disnake.Embed(color=0x2F3136, title=f'Баланс пользователя - {member}')
        embed.add_field(name='🪙 Деньги', value=f'```{user[1]}```')
        embed.add_field(name=':bank:  Банк', value=f'```{user[2]}```')
        embed.set_thumbnail(url=member.display_avatar.url)
        await ctx.send(embed=embed)         
            
    @commands.command()
    async def dep(self, ctx, amount: int):
        member = ctx.author
        await self.db.create_table()
        await self.db.add_user(member)
        user = await self.db.get_user(member)
        if amount < 10:
            await ctx.send("<:emoji_31:1121750019410772038>Сумма не может быть меньше 10!")
        elif amount > user[1] + 1:
            await ctx.send("<:emoji_31:1121750019410772038>Сумма не может быть больше вашего баланса!")
        else:
            await self.db.update_money(member, 0, amount)
            await self.db.minus_money(member, amount, 0)
            embed = disnake.Embed(
                title="Депозит!",
                description=f"{member.mention}, вы положили в банк {amount} 🪙",
                color=0x2F3136
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            await ctx.send(embed=embed)
            
    @commands.command()
    async def withdraw(self, ctx, amount: int):
        member = ctx.author
        await self.db.create_table()
        await self.db.add_user(member)
        user = await self.db.get_user(member)
        if amount < 10:
            await ctx.send("<:emoji_31:1121750019410772038>Сумма не может быть меньше 10!")
        elif amount > user[2]:
            await ctx.send("<:emoji_31:1121750019410772038>Сумма не может быть больше баланса банка!")
        else:
            await self.db.update_money(member, amount, 0)
            await self.db.minus_money(member, 0, amount)
            embed = disnake.Embed(title="Снятие денег!", description=f"{member.mention}, вы сняли {amount} 🪙", color=0x2F3136)
            embed.set_thumbnail(url=member.display_avatar.url)
            await ctx.send(embed=embed)
            
    @commands.command()
    async def pay(self, ctx, member: disnake.Member, amount: int):
        await self.db.create_table()
        await self.db.add_user(member)
        await self.db.add_user(ctx.author)
        user = await self.db.get_user(ctx.author)
        if amount < 5:
            await ctx.send("<:emoji_31:1121750019410772038>Сумма не может быть меньше 5!")
        elif amount > user[1]:
            await ctx.send("<:emoji_31:1121750019410772038>Сумма не может быть больше вашего баланса!")
        else:
            await self.db.update_money(member, amount, 0)
            await self.db.minus_money(ctx.author, amount, 0)
            embed = disnake.Embed(
                title="Перевод!",
                description=f"{ctx.author.mention} перевёл {member.mention} {amount} 🪙",
                color=0x2F3136
            )
            embed.set_thumbnail(url=ctx.guild.icon.url)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Economy(bot))