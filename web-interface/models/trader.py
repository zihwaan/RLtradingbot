import asyncio
import aiohttp
from config.settings import settings

class Trader:
    def __init__(self):
        self.current_price = 0
        self.portfolio_value = 0
        self.balance = settings.INITIAL_BALANCE
        self.num_stocks = 0
        self.avg_buy_price = 0
        self.trade_history = []

    async def update_price(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{settings.KIS_API_URL}/price") as response:
                if response.status == 200:
                    data = await response.json()
                    self.current_price = data['price']

    async def execute_trade(self, action, amount):
        # KIS API를 사용한 거래 로직 구현
        pass

    def get_state(self):
        return {
            'current_price': self.current_price,
            'portfolio_value': self.portfolio_value,
            'balance': self.balance,
            'num_stocks': self.num_stocks,
            'avg_buy_price': self.avg_buy_price,
            'trade_history': self.trade_history
        }

    async def run(self):
        while True:
            await self.update_price()
            # 거래 로직 구현
            await asyncio.sleep(5)