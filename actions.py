from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import email_config as ec


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "f09be5808671fa125d64a0ea398f5dd5"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        if zomato.is_city_available(loc):
            city_id = zomato.get_city_ID(loc)
            location_detail = zomato.get_location(loc, 1)
            d1 = json.loads(location_detail)
            lat = d1["location_suggestions"][0]["latitude"]
            lon = d1["location_suggestions"][0]["longitude"]
            cuisines_dict = zomato.get_cuisines(city_id)
            results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
            d = json.loads(results)
            response = []
            if d['results_found'] == 0:
               response= "no results"
            else:
                for restaurant in d['restaurants']:
                    response.append(restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+restaurant['restaurant']['user_rating']['aggregate_rating'])
            dispatcher.utter_message(" Showing you top rated restaurants:\n"+("\n".join(response)))
            return [SlotSet('location',loc)]
        else:
            dispatcher.utter_message("We do not operate in that area yet:\n")
            return [SlotSet('location',loc)]
        
class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'
    
    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "f09be5808671fa125d64a0ea398f5dd5"}
        zomato = zomatopy.initialize_app(config)
        receiver_email = tracker.get_slot('email')
        reciever_ack= tracker.get_slot('acknowledge')
        if reciever_ack.lower() == 'yes':
            loc = tracker.get_slot('location')
            cuisine = tracker.get_slot('cuisine')
            city_id = zomato.get_city_ID(loc)
            location_detail = zomato.get_location(loc, 1)
            d1 = json.loads(location_detail)
            lat = d1["location_suggestions"][0]["latitude"]
            lon = d1["location_suggestions"][0]["longitude"]
            cuisines_dict = zomato.get_cuisines(city_id)
            results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
            d = json.loads(results)
            response = []
            if d['results_found'] == 0:
               response= "no results"
            else:
                for restaurant in d['restaurants']:
                    response.append(restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+restaurant['restaurant']['user_rating']['aggregate_rating'])
            zomato.send_email(ec.sender, receiver_email, ec.sender_password, response, ec.smtp_server, ec.smtp_port)
            dispatcher.utter_message("Email has been sent ")        
            return [SlotSet('location',loc)]
        else:
            dispatcher.utter_message("Thanks")
        