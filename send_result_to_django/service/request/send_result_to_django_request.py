from pydantic import BaseModel


class SendResultToDjangoRequest(BaseModel):
    userToken: str

    def toUserToken(self) -> str:
        return self.userToken
