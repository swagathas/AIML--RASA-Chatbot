
## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "chennai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chennai"}
    - action_validate_city
    - slot{"location": "chennai"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_validate_budget
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_city
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* budget{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_validate_budget
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_goodbye
    - action_restart

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_city
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* budget{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_validate_budget
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_check_mail
* deny
    - utter_goodbye
    - action_restart

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_city
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* budget{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_validate_budget
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_check_mail
* affirm
    - utter_ask_mail
* send_mail{"mail_id": "swagathas@gmail.com"}
    - slot{"mail_id": "swagathas@gmail.com"}
    - action_send_mail
    - utter_confirm_mail
    - utter_confirm_all
* deny
    - utter_goodbye
    - action_restart

## interactive_story_5
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_validate_city
    - slot{"location": "Chennai"}
    - utter_ask_budget
* budget{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_validate_budget
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_check_mail
* deny
    - utter_confirm_all
* deny
    - utter_goodbye

## interactive_story_6
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_validate_city
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* budget{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_validate_budget
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - utter_check_mail
* affirm
    - utter_ask_mail
* send_mail{"mail_id": "shailu130202@gmail.com"}
    - slot{"mail_id": "shailu130202@gmail.com"}
    - action_send_mail
    - utter_confirm_mail
    - utter_confirm_all
* deny
    - utter_goodbye
    - action_restart

* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_city
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* budget{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_validate_budget
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_check_mail
* affirm
    - utter_ask_mail
* send_mail{"mail_id": "swagathas@gmail.com"}
    - slot{"mail_id": "swagathas@gmail.com"}
    - action_send_mail
    - utter_confirm_mail
    - utter_confirm_all
* deny
    - utter_goodbye
    - action_restart

* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"location": null}
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_validate_city
    - slot{"location": "New Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_validate_budget
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - utter_check_mail
* affirm
    - utter_ask_mail
* send_mail{"mail_id": "swagathas@gmail.com"}
    - slot{"mail_id": "swagathas@gmail.com"}
    - action_send_mail
    - utter_confirm_mail
    - utter_confirm_all
* deny
    - utter_goodbye
