from pydantic import BaseModel

from send_result_to_django.service.request.send_result_to_django_request import SendResultToDjangoRequest


class SendResultToDjangoRequestForm(BaseModel):
    userToken: str

    def toSendResultToDjangoRequest(self) -> SendResultToDjangoRequest:
        return SendResultToDjangoRequest(userToken=self.userToken)
