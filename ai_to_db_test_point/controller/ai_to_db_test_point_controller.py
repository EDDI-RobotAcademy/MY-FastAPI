import os
import sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from ai_to_db_test_point.controller.request_form.ai_to_db_test_point_request_form import AiToDbTestPointRequestForm
from ai_to_db_test_point.service.ai_to_db_test_point_service_impl import AiToDbTestPointServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))

from template.include.socket_server.utility.color_print import ColorPrinter

aiToDbTestPointRouter = APIRouter()

async def injectAiToDbTestPointService() -> AiToDbTestPointServiceImpl:
    return AiToDbTestPointServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@aiToDbTestPointRouter.post('/ai2db-testpoint')
async def requestAiResultToDbTestPoint(aiToDbTestPointPointRequestForm: AiToDbTestPointRequestForm,
                                       aiToDbTestPointService: AiToDbTestPointServiceImpl =
                                       Depends(injectAiToDbTestPointService)):

    ColorPrinter.print_important_message("requestAiResultToDbTestPoint()")

    success = await aiToDbTestPointService.requestAiResultToDbTestPoint(aiToDbTestPointPointRequestForm.toAiToDbTestPointRequest())

    return JSONResponse(content=success, status_code=status.HTTP_200_OK)
