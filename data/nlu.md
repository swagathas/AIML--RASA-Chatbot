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
- yup

## intent:deny
- No
- Nope
- Nah
- not required
- no thanks
- i dont need it
- No need
- nope
- no

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
- Hi

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
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
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Mexican](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
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
- hi find me a [chinese](cuisine) restaurant in [chennai](location) restaurant in [chennai](location)
- Find me a Restaurant
- [Mumbai](location)
- find me a restaurant in [Mumbai](location)
- Find me a restaurant in [bengaluru]{"entity": "location", "value": "bangalore"}
- Hi Find me an [Italian](cuisine) restaurant
- [Chennai](location)
- Hi find me a restaurant in [Dilli]{"entity": "location", "value": "New Delhi"}
- find me a restaurant in [chennai](location)
- hi pls find me a restaurant
- [Rishikesh](location)
- [Delhi]{"entity": "location", "value": "New Delhi"}
- [Chinese]{"entity": "cuisine", "value": "chinese"}

## intent:budget
- [lesser than Rs. 300](price)
- [Rs. 300 to 700](price)
- [more than  700](price)
- [Lesser than Rs. 300](price)
- [More than 700](price)
- [Lesser than Rs. 300](price)

## intent:send_mail
- [swapnil123@gmail.com](mail_id)
- [swagathas@outlook.com](mail_id)
- [swagathas@gmail.com](mail_id)
- [shailu130202@gmail.com](mail_id)
- [swagathas@gmail.com](mail_id)

## synonym: mumbai
- bombay

## synonym:4
- four

## synonym:Delhi
- New Delhi

## synonym:Mysore
- Mysuru

## synonym:New Delhi
- Dilli
- Delhi
- dilli

## synonym:Ooty
- Ootacamund

## synonym:Puducherry
- Pondicherry
- Pondy
- Pondi

## synonym:Vizag
- Vishakapatnam

## synonym:bangalore
- bengaluru
- Bengaluru
- bengalore

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex: email
- ^[A-z0-9]+[\._-]?[A-z0-9]+[@]\w+([.]\w{2,3}){1,2}$

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}
