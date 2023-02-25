"""
https://towardsdatascience.com/create-chatbot-using-rasa-part-1-67f68e89ddad
"""
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.events import SlotSet


class ActionCheckWeather(Action):
    def name(self) -> Text:
        return "action_check_weather"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Hello World! from custom action")
        return []


if __name__ == "__main__":
    actcw = ActionCheckWeather()
    print(actcw.name())

    cld = CollectingDispatcher()
    trc = Tracker()
