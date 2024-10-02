from pydantic import BaseModel
class GrowthStrategyRequestForm(BaseModel):
    age_group: str
    gender: str
    mbti: str
    topic: str
    platform: str
    target_audience: str
    content_style: str
    post_frequency: str