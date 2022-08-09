# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from . import send_feishu_message
from . import weather


class ActionSendFeishuMessage(Action):

    def name(self) -> Text:
        return "action_send_feishu_msg"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        send_feishu_message.send_feedback_message('this is a test message from pe-bot')
        dispatcher.utter_message(text="问题反馈完毕")

        return []


class ActionLookupWeather(Action):

    def name(self) -> Text:
        return "action_lookup_weather"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city_name = next(tracker.get_latest_entity_values("address"), None)
        date_time = next(tracker.get_latest_entity_values("date-time"), None)

        if city_name is None:
            dispatcher.utter_message(text=weather.weather(city_name))
        else:
            dispatcher.utter_message(text=weather.weather(city_name))

        return []