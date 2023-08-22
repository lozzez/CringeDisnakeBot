import disnake
from disnake.ext import commands
from utils.databases import UsersDataBase
        
        
class Shopes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = UsersDataBase()

    @commands.command()
    async def shop(self, ctx):
        embed = disnake.Embed(
            title="Магазин ролей!",
            color=0x2F3136
        )
        embed.add_field(name="1 Роль:", value="<@&1067852880377286786>\n" 
                                                "(Цена: 20000)", inline=True)
        embed.add_field(name="2 Роль:", value="<@&1062972981229408316>\n" 
                                                "(Цена: 18500)", inline=True)
        embed.add_field(name="3 Роль:", value="<@&1062972789390319657>\n"
                                                "(Цена: 15000)", inline=True)
        embed.add_field(name="4 Роль:", value="<@&1062747114049900564>\n"
                                                "(Цена: 9500)", inline=True)
        embed.add_field(name="5 Роль:", value="<@&1062973076188450816>\n"
                                                "(Цена: 8000)", inline=True)
        embed.add_field(name="6 Роль:", value="<@&1088050350742847540>\n"
                                                "(Цена: 5000)", inline=True)
        await ctx.send(embed=embed, components=[
                disnake.ui.Button(label="1 Роль", style=disnake.ButtonStyle.grey, custom_id="one"),
                disnake.ui.Button(label="2 Роль", style=disnake.ButtonStyle.grey, custom_id="two"),
                disnake.ui.Button(label="3 Роль", style=disnake.ButtonStyle.grey, custom_id="three"),
                disnake.ui.Button(label="4 Роль", style=disnake.ButtonStyle.grey, custom_id="four"),
                disnake.ui.Button(label="5 Роль", style=disnake.ButtonStyle.grey, custom_id="five"),
                disnake.ui.Button(label="6 Роль", style=disnake.ButtonStyle.grey, custom_id="six")
        ]) 
        
    @commands.Cog.listener("on_button_click")
    async def help_listener(self, inter: disnake.MessageInteraction):
        if inter.component.custom_id not in ["one", "two", "three", "four", "five", "six"]:
            return
        member = inter.author
        await self.db.create_table()
        await self.db.add_user(member) 
        user = await self.db.get_user(member)
        if inter.component.custom_id == "one":
            if not inter.author:
                await inter.response.send_message("Эта команда вызвана другим участником!", ephemeral=True)
            else:
                role = inter.guild.get_role(1067852880377286786)
                if role in inter.author.roles:
                    await inter.response.send_message("Вы уже имеете эту роль!", ephemeral=True)
                else:
                    if user[1] < 20000:
                        await inter.response.send_message("У вас мало денег!", ephemeral=True)
                    else:
                        await self.db.minus_money(member, 20000, 0)
                        await inter.author.add_roles(role)
                        embed = disnake.Embed(title="Покупка роли!", description=f"{inter.author.mention}, вы успешно купили роль {role.mention}!", color=0x2F3136)
                        await inter.response.send_message(embed=embed, ephemeral=True)
                    
        elif inter.component.custom_id == "two":
            if not inter.author:
                await inter.response.send_message("Эта команда вызвана другим участником!", ephemeral=True)
            else:
                role = inter.guild.get_role(1062972981229408316)
                if role in inter.author.roles:
                    await inter.response.send_message("Вы уже имеете эту роль!", ephemeral=True)
                else:
                    if user[1] < 18500:
                        await inter.response.send_message("У вас мало денег!", ephemeral=True)
                    else:
                        await self.db.minus_money(member, 18500, 0)
                        await inter.author.add_roles(role)
                        embed = disnake.Embed(title="Покупка роли!", description=f"{inter.author.mention}, вы успешно купили роль {role.mention}!", color=0x2F3136)
                        await inter.response.send_message(embed=embed, ephemeral=True)
                    
        elif inter.component.custom_id == "three":
            if not inter.author:
                await inter.response.send_message("Эта команда вызвана другим участником!", ephemeral=True)
            else:
                role = inter.guild.get_role(1062972789390319657)
                if role in inter.author.roles:
                    await inter.response.send_message("Вы уже имеете эту роль!", ephemeral=True)
                else:
                    if user[1] < 15000:
                        await inter.response.send_message("У вас мало денег!", ephemeral=True)
                    else:
                        await self.db.minus_money(member, 15000, 0)
                        await inter.author.add_roles(role)
                        embed = disnake.Embed(title="Покупка роли!", description=f"{inter.author.mention}, вы успешно купили роль {role.mention}!", color=0x2F3136)
                        await inter.response.send_message(embed=embed, ephemeral=True)
                    
        elif inter.component.custom_id == "four":
            if not inter.author:
                await inter.response.send_message("Эта команда вызвана другим участником!", ephemeral=True)
            else:
                role = inter.guild.get_role(1062747114049900564)
                if role in inter.author.roles:
                    await inter.response.send_message("Вы уже имеете эту роль!", ephemeral=True)
                else:
                    if user[1] < 9500:
                        await inter.response.send_message("У вас мало денег!", ephemeral=True)
                    else:
                        await self.db.minus_money(member, 9500, 0)
                        await inter.author.add_roles(role)
                        embed = disnake.Embed(title="Покупка роли!", description=f"{inter.author.mention}, вы успешно купили роль {role.mention}!", color=0x2F3136)
                        await inter.response.send_message(embed=embed, ephemeral=True)
                    
        elif inter.component.custom_id == "five":
            if not inter.author:
                await inter.response.send_message("Эта команда вызвана другим участником!", ephemeral=True)
            else:
                role = inter.guild.get_role(1062973076188450816)
                if role in inter.author.roles:
                    await inter.response.send_message("Вы уже имеете эту роль!", ephemeral=True)
                else:
                    if user[1] < 8000:
                        await inter.response.send_message("У вас мало денег!", ephemeral=True)
                    else:
                        await self.db.minus_money(member, 8000, 0)
                        await inter.author.add_roles(role)
                        embed = disnake.Embed(title="Покупка роли!", description=f"{inter.author.mention}, вы успешно купили роль {role.mention}!", color=0x2F3136)
                        await inter.response.send_message(embed=embed, ephemeral=True)
                        
        elif inter.component.custom_id == "six":
            if not inter.author:
                await inter.response.send_message("Эта команда вызвана другим участником!", ephemeral=True)
            else:
                role = inter.guild.get_role(1088050350742847540)
                if role in inter.author.roles:
                    await inter.response.send_message("Вы уже имеете эту роль!", ephemeral=True)
                else:
                    if user[1] < 5000:
                        await inter.response.send_message("У вас мало денег!", ephemeral=True)
                    else:
                        await self.db.minus_money(member, 5000, 0)
                        await inter.author.add_roles(role)
                        embed = disnake.Embed(title="Покупка роли!", description=f"{inter.author.mention}, вы успешно купили роль {role.mention}!", color=0x2F3136)
                        await inter.response.send_message(embed=embed, ephemeral=True)
                            
                    
def setup(bot):
    bot.add_cog(Shopes(bot))