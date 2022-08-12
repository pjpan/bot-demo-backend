# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.utils import send_feishu_message, weather
from actions.utils.coins import CoinDataManager
import json
import logging
from rasa_sdk.events import AllSlotsReset

logger = logging.getLogger("actions")

class ActionSendFeishuMessage(Action):

    def name(self) -> Text:
        return "action_send_feishu_msg"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        logger.info(f"{tracker.latest_message.get('text')}")
        send_feishu_message.send_feedback_message(tracker.latest_message.get('text'))
        dispatcher.utter_message(text="问题反馈完毕")

        return []


class ActionLookupWeather(Action):

    def name(self) -> Text:
        return "action_lookup_weather"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city_name = tracker.slots['address']
        date_time = tracker.slots['date-time']
        logger.info(f"{tracker.slots}")
        logger.info(f"cityname is {city_name}, date is {date_time}")
        if city_name is None:
            dispatcher.utter_message(text="请说一下要查询的的城市")
        elif city_name is not None:
            result = weather.weather(city_name)
            logger.info(f"result is {result}")
            if date_time is None or date_time == "今天":
                data_result = json.dumps(dict(城市=city_name, 数据=json.loads(result).get("数据",{})[1]),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': '))
            elif date_time == "明天":
                data_result = json.dumps(dict(城市=city_name, 数据=json.loads(result).get("数据",{})[2]),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': '))
            elif date_time == "后天":
                data_result = json.dumps(dict(城市=city_name, 数据=json.loads(result).get("数据",{})[3]),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': '))
            dispatcher.utter_message(text=data_result)

        return [AllSlotsReset()]


class CoinSearchAction(Action):
    def name(self) -> Text:
        return "action_search_coin_history"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        img_msg = await CoinDataManager().get_img()
        dispatcher.utter_message(image=img_msg)
        return []