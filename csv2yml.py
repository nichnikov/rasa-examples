import os
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv
import pandas as pd


class ActionReadCSV(Action):
    def name(self) -> Text:
        return "action_csv"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        df = pd.read_csv(os.path.join("data", "intents.csv"), sep="\t")

        for i, j in df.iterrows():
            dispatcher.utter_message(text=(str(j['ID']) + " " + str(j['Title'])))
        return []

