import aiosqlite
import disnake


class UsersDataBase:
    def __init__(self):
        self.name = 'Nirolabot/dbs/users.db'

    async def create_table(self):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = '''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                money INTEGER,
                bank INTEGER
            )'''
            await cursor.execute(query)
            await db.commit()

    async def get_user(self, user: disnake.Member):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'SELECT * FROM users WHERE id = ?'
            await cursor.execute(query, (user.id,))
            return await cursor.fetchone()

    async def add_user(self, user: disnake.Member):
        async with aiosqlite.connect(self.name) as db:
            if not await self.get_user(user):
                cursor = await db.cursor()
                query = 'INSERT INTO users (id, money, bank) VALUES (?, ?, ?)'
                await cursor.execute(query, (user.id, 0, 0))
                await db.commit()

    async def update_money(self, member: disnake.Member, money: int, bank: int):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'UPDATE users SET money = money + ?, bank = bank + ? WHERE id = ?'
            await cursor.execute(query, (money, bank, member.id))
            await db.commit()
            
    async def minus_money(self, member: disnake.Member, money: int, bank: int):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'UPDATE users SET money = money - ?, bank = bank - ? WHERE id = ?'
            await cursor.execute(query, (money, bank, member.id))
            await db.commit()