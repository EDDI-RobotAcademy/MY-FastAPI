import os
import sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from growth_strategy.service.growth_strategy_service_impl import GrowthStrategyServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

growthStrategyRouter = APIRouter()

async def injectGrowthStrategyService() -> GrowthStrategyServiceImpl:
    return GrowthStrategyServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@growthStrategyRouter.post('/igrowth-strategy')
async def requestGrowthStrategyResult(GrowthStrategyService: GrowthStrategyServiceImpl =
                                 Depends(injectGrowthStrategyService)):

    ColorPrinter.print_important_message("requestGrowthStrategyResult()")

    generatedGrowthStrategyResult = GrowthStrategyService.requestGrowthStrategyResult()

    return JSONResponse(content=generatedGrowthStrategyResult, status_code=status.HTTP_200_OK)