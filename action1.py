from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

timezones = {
    "London": "UTC+0:00",
    "Saudi Arabia": "UTC+3:00",
    "United Arab Emirates": "UTC+4:00",
    "Qatar": "UTC+3:00",
    "Oman": "UTC+4:00",
    "Bahrain": "UTC+3:00",
    "Kuwait": "UTC+3:00",
    "Yemen": "UTC+3:00",
    "Iraq": "UTC+3:00",
    "Jordan": "UTC+2:00",
    "Lebanon": "UTC+2:00",
    "Palestine": "UTC+2:00",
    "Syria": "UTC+2:00",
    "Egypt": "UTC+2:00",
    "Sudan": "UTC+2:00",
    "Libya": "UTC+2:00",
    "Morocco": "UTC+0:00",
    "Tunisia": "UTC+1:00",
    "Algeria": "UTC+1:00",
    "Somalia": "UTC+3:00",
    "France": "UTC+1:00",
    "Germany": "UTC+1:00",
    "Spain": "UTC+1:00",
    "Italy": "UTC+1:00",
    "Netherlands": "UTC+1:00",
    "Belgium": "UTC+1:00",
    "Switzerland": "UTC+1:00",
    "Austria": "UTC+1:00",
    "Sweden": "UTC+1:00",
    "Norway": "UTC+1:00",
    "Denmark": "UTC+1:00",
    "Finland": "UTC+2:00",
    "Greece": "UTC+2:00",
    "Portugal": "UTC+0:00",
    "Poland": "UTC+1:00",
    "Czech Republic": "UTC+1:00",
    "Hungary": "UTC+1:00",
    "Romania": "UTC+2:00",
    "Ireland": "UTC+0:00",
    "Slovakia": "UTC+1:00",
    "Croatia": "UTC+1:00",
    "Ukraine": "UTC+2:00",
    "Serbia": "UTC+1:00",
    "Bulgaria": "UTC+2:00",
    "Belarus": "UTC+3:00",
    "Lithuania": "UTC+2:00",
    "Latvia": "UTC+2:00",
    "Estonia": "UTC+2:00",
    "Slovenia": "UTC+1:00",
    "Montenegro": "UTC+1:00",
    "Luxembourg": "UTC+1:00",
    "Cyprus": "UTC+2:00",
    "Malta": "UTC+1:00",
    "Iceland": "UTC+0:00",
    "Andorra": "UTC+1:00",
    "Liechtenstein": "UTC+1:00",
    "Monaco": "UTC+1:00",
    "San Marino": "UTC+1:00",
    "Vatican City": "UTC+1:00",
    "Moldova": "UTC+2:00"
}


class ShowTimeZone(Action):
    def name(self) -> Text:
        return "show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot("city")
        timezone = timezones.get(city)
        if timezone is None:
            error_message = "The error message indicates that there is an issue with the domain configuration in your Rasa project. Specifically, it seems that there is a reference to an action called 'utter_iamabot' in your domain file, but this action is not registered in the domain."
            dispatcher.utter_message(text=error_message)
        else:
            output = "Time zone of {} is {}".format(city, timezone)
            dispatcher.utter_message(text=output)

        return []
