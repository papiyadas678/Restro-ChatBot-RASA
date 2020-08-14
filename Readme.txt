===== Welcome to the Restaurant Chatbot Using RASA ====
An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. You have been hired as the lead data scientist for creating this product.
The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience.

===== Cities it works for ======
The chatbot works for only Tier1 & Tier2 cities of india.
Link to all the Tier1 & Tier2 Cities are:
https://en.wikipedia.org/wiki/Classification_of_Indian_cities

===== Installing & Requirements =====
To work with RASA Chatbot you only need to extract the rasa_chatbot_assignment.zip file
and install few python requirements for its seemless working.

Step 1: Extract the zip file in a certain location on your machine.
Step 2: pip install -r requirements.txt

===== Configurations =====
Change the email_config.py file in the extracted location to input your mail sending credentials.
sender = "xxxx.xxxxx@gmail.com" # Mention your email ID for sending mail
sender_password = "xxxxxxxxxxxxx" # Mention your password for sending mail

===== Steps to Run the Chatbot via interactive shell =====
1. Navigate to the extracted folder on the machine
2. Run the actions for Rasa to perform defined custom actions: rasa run actions
3. Run the RASA interactive shell: rasa shell

===== To Train more stories ====
1. Train the RASA NLU : rasa train nlu
2. Train the RASA CORE: rasa train core
3. Run it using: rasa interactive

===== Play Around & Have Fun =========