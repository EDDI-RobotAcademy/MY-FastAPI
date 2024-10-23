import os
import sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from send_result_to_django.controller.request_form.send_result_to_django_request_form import \
    SendResultToDjangoRequestForm
from send_result_to_django.service.send_result_to_django_service_impl import SendResultToDjangoServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))

from template.include.socket_server.utility.color_print import ColorPrinter

sendResultToDjangoRouter = APIRouter()

async def injectSendResultToDjangoService() -> SendResultToDjangoServiceImpl:
    return SendResultToDjangoServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@sendResultToDjangoRouter.post('/send-result-to-django')
async def requestSendResultToDjango(sendResultToDjangoRequestForm: SendResultToDjangoRequestForm,
                                       sendResultToDjangoService: SendResultToDjangoServiceImpl =
                                       Depends(injectSendResultToDjangoService)):

    ColorPrinter.print_important_message("requestSendResultToDjango()")

    success = await sendResultToDjangoService.requestSendCustomStrategyHistory(sendResultToDjangoRequestForm.toSendResultToDjangoRequest())

    return JSONResponse(content=success, status_code=status.HTTP_200_OK)
