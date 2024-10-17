from pydantic import BaseModel

from ai_to_db_test_point.service.request.ai_to_db_test_point_request import AiToDbTestPointRequest


class AiToDbTestPointRequestForm(BaseModel):
    userToken: str

    def toAiToDbTestPointRequest(self) -> AiToDbTestPointRequest:
        return AiToDbTestPointRequest(userToken=self.userToken)
