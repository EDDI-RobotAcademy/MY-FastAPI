from pydantic import BaseModel


class SendResultToDjangoResponse(BaseModel):
    userToken: str
    aiResult: int

    @classmethod
    def fromValues(cls, userToken: str, aiResult: int):
        return cls(userToken=userToken, aiResult=aiResult)
