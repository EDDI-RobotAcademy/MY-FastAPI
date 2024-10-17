from pydantic import BaseModel


class AiToDbTestPointResponse(BaseModel):
    userToken: str
    aiResult: int

    @classmethod
    def fromValues(cls, userToken: str, aiResult: int):
        return cls(userToken=userToken, aiResult=aiResult)
