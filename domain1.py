intents:
  - greet
  - goodbye
  - find_time_zone
  - find_time_zone_for_location
  - city_info
  - thanks
actions:
  - show_time_zone 

entities:
  - city

slots:
  city:
    type: text
    auto_fill: True
responses:
  utter_greet:
  - text: "Hey! I am Time Zone Bot"

  utter_ask_location:
  - text: "Wich city do you need the time zone of?"

  utter_finding_time_zone:
  - text: "Ok, give me a second to look up the time zone of {city} :)"
 

  utter_you_are_welcome:
  - text: "You are very welcome dear :)"

  utter_goodbye:
  - text: "Bye, take care! "


session_config:
  session_expiration_time: 60
  carry_over_slots_to_new_session: true
