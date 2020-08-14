## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- thanks mate
- thanks bot
- thanks babe
- thanks man
- Thanks mate
- Thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Mexican](cuisine:mexican)
- [mexican](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- can you book me a table for [4](people)
- can you book me a table for [2](people)
- can you find me a restaurant for [4](people)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a range Rs. 300 to 700(price:Rs. 300 to 700) price range with [british](cuisine) food for [four](people:4) people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- can you find me restaurants in [mumbai](location)
- can you find me resturants in [delhi](location)?
- can you help me find restaurants?
- can you find me restaurants?
- [kolkata](location)
- can you find me a restuarant
- [america](location)
- at [Agra](location)
- [American](cuisine)
- [Lesser than Rs. 300](price)
- [Rs. 300 to 700](price)
- [More than 700](price)
- can you give list of restuarants?
- at [Ahmedabad](location)
- list me out few restaurants at [Agra](location)
- [Between Rs. 300 to Rs. 700](price)
- please search few [Italian](cuisine) restaurants for me
- Around [Kolkata](location)
- Find me few [North Indian](cuisine) restaurants at [Durgapur](location)
- [Greater than Rs. 700](price)
- can you find me [Italian](cuisine) restaurants in [Ajmer](location)?
- can you find me [Indian](cuisine) restaurants in [Allahabad](location)?
- can you find me [Indian](cuisine) restaurants at [Durgapur](location)?
- can you find me [Italian](cuisine) restaurants in [Mumbai](location:mumbai)
- at [Bhopal](location)!!
- at [Dehradun](location)
- can you help me find [Indian](cuisine) restuarants?
- at [mumbai](location)
- Im hungry. Looking out for some good restaurants
- [Ajmer](location)
- [South Indian](cuisine)
- [Between Rs. 300 to Rs. 700](price)

## intent:send_email
- [yes](acknowledge), send it to [roy.nabarko@gmail.com](email)
- [yes](acknowledge), send it to [xxxxxxx.xxxxxxx@xxxx.com](email)
- please send it to [xxxxxxxxxx@gmail.com](email)(acknowledge:yes)
- [no](acknowledge), Thanks
- [No](acknowledge:no)
- [Not](acknowledge:no) required
- [yes](acknowledge), please mail at [rony.chillout@gmail.com](email)
- [yes](acknowledge), please send me a mail at [rony.chillout@gmail.com](email)
- [yes](acknowledge), please send it over [rony.chillout@gmail.com](email)
- [no](acknowledge) thanks
- [yes](acknowledge). Please send it to [rony.chillout@gmail.com](email)

## synonym:4
- four

## synonym:Chennai
- Madras

## synonym:Delhi
- New Delhi
- Dilli
- Nai Dilli

## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:kolkata
- Calcutta
- kolkata
- calcutta

## synonym:mexican
- Mexican

## synonym:mid
- moderate
- Rs. 300 to 700

## synonym:mumbai
- Mumbai
- Bombay
- bombay

## synonym:no
- No
- Not

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## regex:send_email
- yes [a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.com$]
