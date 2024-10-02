from growth_strategy.repository.growth_strategy_repository_impl import GrowthStrategyRepositoryImpl
from growth_strategy.service.growth_strategy_service import GrowthStrategyService

class GrowthStrategyServiceImpl(GrowthStrategyService):

    def __init__(self):
        self.__growthStrategyRepository = GrowthStrategyRepositoryImpl()

    async def generate_growth_strategy(self, age_group, gender, mbti, topic, platform, target_audience, content_style, post_frequency):

        prompt = f"""
           나이대: {age_group}
           성별: {gender}
           MBTI: {mbti}
           성장하고 싶은 주제: {topic}
           활동하고 싶은 플랫폼: {platform}
           타겟층: {target_audience}
           콘텐츠 스타일: {content_style}
           게시물 주기: {post_frequency}
    
           이 정보를 바탕으로, 해당 인플루언서가 효과적으로 성장할 수 있는 전략을 제시해 주세요. 
           원하는 플랫폼에서 어떤 콘텐츠를 게시해야 하는지, 해당 타겟층을 어떻게 공략해야 하는지, 성공한 인플루언서들의 사례를 들어 구체적으로 설명해 주세요.
           MBTI 특성과 나이대, 성별을 분석하여 인플루언서의 장점과 단점을 분석하고 장점을 극대화할 수 있는 전략을 소개해주세요.
        """

        return await self.__growthStrategyRepository.fetch_growth_strategy(prompt)

