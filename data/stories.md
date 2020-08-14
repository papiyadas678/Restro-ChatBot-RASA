## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye
* goodbye

## interactive_story_1
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "delhi"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "america"}
    - slot{"location": "america"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "america"}
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search
    - action_search_restaurants
    - slot{"location": "Agra"}
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Ahmedabad"}
    - slot{"location": "Ahmedabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search
    - action_search_restaurants
    - slot{"location": "Ahmedabad"}
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search
    - action_search_restaurants
    - slot{"location": "Agra"}
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "North Indian", "location": "Durgapur"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Durgapur"}
    - utter_ask_price
* restaurant_search{"price": "Greater than Rs. 700"}
    - slot{"price": "Greater than Rs. 700"}
    - action_search_restaurants
    - slot{"location": "Durgapur"}
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "Italian", "location": "Ajmer"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Ajmer"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "Ajmer"}
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "Indian", "location": "Allahabad"}
    - slot{"cuisine": "Indian"}
    - slot{"location": "Allahabad"}
    - utter_ask_price
* restaurant_search{"price": "Greater than Rs. 700"}
    - slot{"price": "Greater than Rs. 700"}
    - action_search_restaurants
    - slot{"location": "Allahabad"}
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "Indian", "location": "Durgapur"}
    - slot{"cuisine": "Indian"}
    - slot{"location": "Durgapur"}
    - utter_ask_price
* restaurant_search{"price": "Greater than Rs. 700"}
    - slot{"price": "Greater than Rs. 700"}
    - action_search_restaurants
    - slot{"location": "Durgapur"}
    - utter_ask_email
* send_email{"acknowledge": "yes", "email": "rony.chillout@gmail.com"}
    - slot{"acknowledge": "yes"}
    - slot{"email": "rony.chillout@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "Italian", "location": "mumbai"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "mumbai"}
    - utter_ask_price
* restaurant_search{"price": "Greater than Rs. 700"}
    - slot{"price": "Greater than Rs. 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email
* send_email{"acknowledge": "yes", "email": "rony.chillout@gmail.com"}
    - slot{"acknowledge": "yes"}
    - slot{"email": "rony.chillout@gmail.com"}
    - action_send_email
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bhopal"}
    - slot{"location": "Bhopal"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "Between Rs. 300 to Rs. 700"}
    - slot{"price": "Between Rs. 300 to Rs. 700"}
    - action_search_restaurants
    - slot{"location": "Bhopal"}
* send_email{"acknowledge": "yes", "email": "rony.chillout@gmail.com"}
    - slot{"acknowledge": "yes"}
    - slot{"email": "rony.chillout@gmail.com"}
    - action_send_email
    - slot{"location": "Dehradun"}
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Dehradun"}
    - slot{"location": "Dehradun"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "Between Rs. 300 to Rs. 700"}
    - slot{"price": "Between Rs. 300 to Rs. 700"}
    - action_search_restaurants
    - slot{"location": "Dehradun"}
    - utter_ask_email
* send_email{"acknowledge": "yes", "email": "rony.chillout@gmail.com"}
    - slot{"acknowledge": "yes"}
    - slot{"email": "rony.chillout@gmail.com"}
    - action_send_email
    - slot{"location": "Dehradun"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Indian"}
    - slot{"cuisine": "Indian"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_price
* restaurant_search{"price": "Between Rs. 300 to Rs. 700"}
    - slot{"price": "Between Rs. 300 to Rs. 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email
* send_email{"acknowledge": "no"}
    - slot{"acknowledge": "no"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Ajmer"}
    - slot{"location": "Ajmer"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_cuisine
* restaurant_search{"price": "Between Rs. 300 to Rs. 700"}
    - slot{"price": "Between Rs. 300 to Rs. 700"}
    - action_search_restaurants
    - slot{"location": "Ajmer"}
    - utter_ask_email
* send_email{"acknowledge": "yes", "email": "rony.chillout@gmail.com"}
    - slot{"acknowledge": "yes"}
    - slot{"email": "rony.chillout@gmail.com"}
    - action_send_email
    - slot{"location": "Ajmer"}
* affirm
    - utter_goodbye
