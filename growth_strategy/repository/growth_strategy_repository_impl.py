import openai
import os
from dotenv import load_dotenv
from fastapi.responses import StreamingResponse

from growth_strategy.repository.growth_strategy_repository import GrowthStrategyRepository

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("API Key가 준비되어 있지 않습니다!")

os.environ["OPENAI_API_KEY"] = openai.api_key

class GrowthStrategyRepositoryImpl(GrowthStrategyRepository):

    async def fetch_growth_strategy(self, prompt: str):
        messages = [
            {"role": "system", "content": "You are a helpful assistant that provides influencer growth strategies."},
            {"role": "user", "content": prompt}
        ]
        async def stream_response():
            try:
                # 비동기 OpenAI ChatCompletion API 호출
                response = await openai.ChatCompletion.acreate(
                    model="gpt-4",
                    messages=messages,
                    max_tokens=1500,
                    temperature=0.7,
                    stream=True
                )

                async for chunk in response:
                    if "choices" in chunk:
                        content = chunk['choices'][0]['delta'].get('content', '')
                        if content:
                            yield f"data: {content}\n\n"

            except Exception as e:
                yield f"오류 발생: {e}"

        return StreamingResponse(stream_response(), media_type="text/event-stream")
