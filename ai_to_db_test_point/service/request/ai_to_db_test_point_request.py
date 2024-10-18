from pydantic import BaseModel


class AiToDbTestPointRequest(BaseModel):
    userToken: str

    def toUserToken(self) -> str:
        return self.userToken
