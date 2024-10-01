import openai
import os
from dotenv import load_dotenv

from growth_strategy.repository.growth_strategy_repository import GrowthStrategyRepository

load_dotenv()

openaiApiKey = os.getenv("OPENAI_API_KEY")
if not openaiApiKey:
    raise ValueError("API Key가 준비되어 있지 않습니다!")

os.environ["OPENAI_API_KEY"] = openaiApiKey

class GrowthStrategyRepositoryImpl(GrowthStrategyRepository):

    async def fetch_growth_strategy(self, prompt: str) -> str:
        """
        OpenAI API를 비동기로 호출하여 성장 전략을 생성하는 레포지토리 함수.
        """
        messages = [
            {"role": "system", "content": "You are a helpful assistant that provides influencer growth strategies."},
            {"role": "user", "content": prompt}
        ]

        try:
            # 비동기 OpenAI ChatCompletion API 호출
            response = await openai.ChatCompletion.acreate(
                model="gpt-4",
                messages=messages,
                max_tokens=1500,
                temperature=0.7
            )

            strategy = response['choices'][0]['message']['content'].strip()
            return strategy
        except Exception as e:
            return f"오류 발생: {e}"