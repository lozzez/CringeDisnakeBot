import disnake
from disnake.ext import commands
import random
from utils.databases import UsersDataBase

class Time(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = UsersDataBase()
        
    @commands.command()
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def rob(self, ctx, member: disnake.Member):
        if member:
            await self.db.create_table()
            await self.db.add_user(ctx.author)
            await self.db.add_user(member)
            user = await self.db.get_user(ctx.author)
            user2 = await self.db.get_user(member)
            if user[1] < 100:
                await ctx.send(":emoji_31: У вас на балансе должно быть больше 100 :coin:")
            elif user2[1] < 100:
                await ctx.send(":emoji_31: У участника должно быть больше 100 :coin:")
            else:
                @commands.cooldown(1, 1800, commands.BucketType.user)
                async def _rob():
                    g = random.randint(1, 3)
                    if g == 1:
                        await ctx.send("У вас не получилось ограбить участника!")
                    elif g == 2:
                        h = random.randint(100, user[1])
                        await self.db.minus_money(ctx.author, h, 0)
                        await ctx.send(f"Во время ограбления вы потеряли {h} :coin:")
                    else:
                        j = random.randint(100, user2[1])
                        await self.db.update_money(ctx.author, j, 0)
                        await self.db.minus_money(member, j, 0)
                        embed = disnake.Embed(
                            title="Ограбление!",
                            description=f'{ctx.author}, вы ограбили {member} на {j} :coin:',
                            color=0x2F3136
                        )
                        embed.set_thumbnail(url=member.display_avatar.url)
                        await ctx.send(embed=embed)
                        
                    pass
                await _rob()
        else:
            await ctx.send("<:emoji_31:1121750019410772038>Укажите участника!")    
               
    @rob.error
    async def rob_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after
            minutes = round(remaining_time / 60)
            if minutes == 1:
                await ctx.send(f"На эту команду стоит задержка! Подожди ещё {minutes} минуту!")
            elif minutes <= 4:
                await ctx.send(f"На эту команду стоит задержка! Подожди ещё {minutes} минуты!")
            else:
                await ctx.send(f"На эту команду стоит задержка! Подожди ещё {minutes} минут!")

    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def work(self, ctx):
        await self.db.create_table()
        member = ctx.author
        await self.db.add_user(member)
        await self.db.update_money(member, 500, 0)
        user = await self.db.get_user(member)
        embed = disnake.Embed(
            title="Работа!",
            description=f"Пользователь {member.display_name} заработал 500 🪙",
            color=0x2F3136
        )
        embed.add_field(name='🪙 Деньги', value=f'```{user[1]}```')
        embed.add_field(name=':bank: Банк', value=f'```{user[2]}```')
        embed.set_thumbnail(url=member.display_avatar.url)
        await ctx.send(embed=embed)    

    @work.error
    async def work_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after
            minutes = round(remaining_time / 60)
            if minutes == 1:
                await ctx.send(f"На эту команду стоит задержка! Подожди ещё {minutes} минуту!")
            elif minutes <= 4:
                await ctx.send(f"На эту команду стоит задержка! Подожди ещё {minutes} минуты!")
            else:
                await ctx.send(f"На эту команду стоит задержка! Подожди ещё {minutes} минут!")

    @commands.command()
    @commands.cooldown(1, 7200, commands.BucketType.user)
    async def timely(self, ctx):
        await self.db.create_table()
        member = ctx.author
        await self.db.add_user(member)
        await self.db.update_money(member, 700, 0)
        user = await self.db.get_user(member)
        embed = disnake.Embed(
            title="Ежевременный бонус!",
            description=f"Пользователь {member.display_name} получил 700 🪙",
            color=0x2F3136
        )
        embed.add_field(name='🪙 Деньги', value=f'```{user[1]}```')
        embed.add_field(name=':bank: Банк', value=f'```{user[2]}```')
        embed.set_thumbnail(url=member.display_avatar.url)
        await ctx.send(embed=embed)

    @timely.error
    async def timely_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after
            minutes = round(remaining_time / 60)
            if minutes == 1:
                await ctx.send(f"На эту команду стоит задержка! Подожди ещё {minutes} минуту!")
            elif minutes <= 4:
                await ctx.send(f"На эту команду стоит задержка! Подожди ещё {minutes} минуты!")
            else:
                await ctx.send(f"На эту команду стоит задержка! Подожди ещё {minutes} минут!")
                

    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        await self.db.create_table()
        member = ctx.author
        await self.db.add_user(member)
        await self.db.update_money(member, 900, 0)
        user = await self.db.get_user(member)
        embed = disnake.Embed(
            title="Ежедневный бонус!",
            description=f"Пользователь {member.display_name} получил 900 🪙",
            color=0x2F3136
        )
        embed.add_field(name='🪙 Деньги', value=f'```{user[1]}```')
        embed.add_field(name=':bank: Банк', value=f'```{user[2]}```')
        embed.set_thumbnail(url=member.display_avatar.url)
        await ctx.send(embed=embed)
        
    @daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after
            hours = round(remaining_time / 3600)
            minutes = round(remaining_time / 60)
            if hours < 1:
                if minutes == 1:
                    await ctx.send(f"На эту команду стоит задержка! Подожди ещё {minutes} минуту!")
                elif minutes <= 4:
                    await ctx.send(f"На эту команду стоит задержка! Подожди ещё {minutes} минуты!")
                else:
                    await ctx.send(f"На эту команду стоит задержка! Подожди ещё {minutes} минут!")
            elif hours == 1:
                await ctx.send(f"На эту команду стоит задержка! Подожди ещё 1 час!")
            elif hours <= 4:
                await ctx.send(f"На эту команду стоит задержка! Подожди ещё {hours} часа!")
            elif hours == 21:
                await ctx.send(f"На эту команду стоит задержка! Подожди ещё 21 час!")
            elif hours <= 24:
                await ctx.send(f"На эту команду стоит заддержка! Подожди ещё {hours} часа")
            else:
                await ctx.send(f"На эту команду стоит задержка! Подожди ещё {hours} часов!")   
        
def setup(bot):
    bot.add_cog(Time(bot))