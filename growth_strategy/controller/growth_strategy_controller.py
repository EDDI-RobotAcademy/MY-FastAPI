from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any
from growth_strategy.service.growth_strategy_service_impl import generate_growth_strategy
import asyncio

# FastAPI용 APIRouter 생성
growthStrategyRouter = APIRouter()


# Pydantic을 사용하여 요청 데이터 구조 정의
class GrowthStrategyRequestForm(BaseModel):
    age_group: str
    gender: str
    mbti: str
    topic: str
    platform: str
    target_audience: str
    content_style: str
    post_frequency: str


# FastAPI의 의존성 주입 사용 예시
async def injectGrowthStrategyService():
    # Service 로직을 의존성으로 전달
    return generate_growth_strategy()


@growthStrategyRouter.post("/growth-strategy")
async def create_growth_strategy(
        request_form: GrowthStrategyRequestForm,
        generate_strategy=Depends(injectGrowthStrategyService)
) -> Any:
    """
    인플루언서 성장 전략 생성 API 엔드포인트
    """
    try:
        # 요청 데이터를 기반으로 서비스 호출
        strategy = await generate_strategy(
            request_form.age_group,
            request_form.gender,
            request_form.mbti,
            request_form.topic,
            request_form.platform,
            request_form.target_audience,
            request_form.content_style,
            request_form.post_frequency
        )

        # 성공 시 JSON 응답 반환
        return JSONResponse(content={"strategy": strategy}, status_code=status.HTTP_200_OK)

    except Exception as e:
        # 오류 발생 시 적절한 예외 처리
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
