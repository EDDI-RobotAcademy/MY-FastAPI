from growth_strategy.repository.growth_strategy_repository_impl import GrowthStrategyRepositoryImpl
from growth_strategy.service.growth_strategy_service import GrowthStrategyService

class GrowthStrategyServiceImpl(GrowthStrategyService):

    def __init__(self):
        self.__growthStrategyRepository = GrowthStrategyRepositoryImpl()

    async def generate_growth_strategy(self, gender, age_group, mbti, topic, strength, reveal, platform, interested_influencer):

        prompt = f"""
           성별: {gender}
           나이대: {age_group}
           MBTI: {mbti}
           성장하고 싶은 주제: {topic}
           장점: {strength}
           공개정도: {reveal}
           활동하고 싶은 플랫폼: {platform}
           관심있는 인플루언서: {interested_influencer}
    
           이 정보를 바탕으로, 해당 인플루언서가 효과적으로 성장할 수 있는 전략을 제시해 주세요. 
           원하는 플랫폼에서 어떤 컨텐츠를 게시해야 하는지, 성공한 인플루언서들의 사례를 들어 구체적으로 설명해 주세요.
           MBTI 특성과 나이대, 성별을 분석하여 인플루언서의 장점과 단점을 분석하고 장점을 극대화할 수 있는 전략을 소개해주세요.
           
           아래의 형식에 맞추어서 답변을 출력해주세요.
           
           1. 입력 요약 : 
            (사용자의 입력을 요약해서 유저에게 설명해줌.)
            
           2. 성향 분석 : 
            (사용자의 MBTI, 나이대, 성별을 분석하여 해당 성향의 장점과 단점을 알려주고
             인플루언서로서 활동할 때 장점을 극대화 하고 단점을 극복할 수 있는 전략을 세워줌.)
             
           3. 유사 인플루언서 예시 : 
            (사용자와 성향이 비슷하고 동일한 주제로 성공한 한국인 인플루언서를 소개하고,
             이들이 어떤 컨텐츠를 통해 성공할 수 있었는지 성장 전략을 분석하여 예시를 들어줌.)
             
           4. 컨텐츠 전략 : 
            (사용자가 원하는 주제와 플랫폼, 장점, 본인의 공개정도(얼굴, 목소리 등 공개)를 바탕으로
             어떠한 컨텐츠를 업로드하는 것이 성장에 도움이 될지 구체적인 예시를 들어 전략을 세워줌.)
             
           5. 총정리 :
            (위에서 언급한 성장 전략들을 총정리하여 간단한 로드맵을 작성해주고, 마지막으로 인플루언서로서 성장하고자 하는 사용자를 응원하는 메시지를 출력함.) 
        """

        return await self.__growthStrategyRepository.fetch_growth_strategy(prompt)

