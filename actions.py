from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from email.message import EmailMessage
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
import json

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

def RestaurantSearch(City,Cuisine):
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

def filter_budget(budget,restaurant):
	    #filtered_list=[]
	    minBudget=0
	    maxBudget=9999
	    budget=budget.lower()

	    if budget=='lesser than rs. 300':
	    	minBudget=0
	    	maxBudget=299
	    elif budget=='rs. 300 to 700':
	        minBudget=300
	        maxBudget=700
	    elif budget=='more than 700':
	        minBudget=701
	        maxBudget=9999
	    filtered_list=restaurant[(restaurant["Average Cost for two"] >= minBudget) & (restaurant["Average Cost for two"]  <= maxBudget)].sort_values(by='Aggregate rating', ascending=False)
	    return filtered_list

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		RestSearch_results = RestaurantSearch(City=loc,Cuisine=cuisine)
		budget= tracker.get_slot('price')
		results=filter_budget(budget,RestSearch_results)

		response=""
		if results.shape[0] == 0:
			response= "Oops, Can't find a "+cuisine+" Restaurant in "+loc+" for a budget "+budget
		else:
			for restaurant in filter_budget(budget,RestSearch_results).iloc[:5].iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Aggregate rating']} with avg cost {restaurant['Average Cost for two']} \n\n"

		dispatcher.utter_message("---"+response+"---")
		return [SlotSet('location',loc)]

	
class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('mail_id')
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		RestSearch_results = RestaurantSearch(City=loc,Cuisine=cuisine)
		budget= tracker.get_slot('price')
		results=filter_budget(budget,RestSearch_results)

		response=""
		if results.shape[0] == 0:
			response= "no results"
		else:
			for restaurant in filter_budget(budget,RestSearch_results).iloc[:10].iterrows():
				restaurant = restaurant[1]
				response=response + F"Restaurant Name:- {restaurant['Restaurant Name']} ,\nAddress:- {restaurant['Address']}\n with an Average Rating of  {restaurant['Aggregate rating']} out of 5.\n(The Average cost for 2 people:- {restaurant['Average Cost for two']} )\n\n"

		print("Sending email to  ", str(MailID),"....")

		try:
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login("chatbotrasa702@gmail.com", "swapnil123")

			message = MIMEMultipart()
			message['From'] = "swagathas.07@gmail.com"
			message['To'] = MailID
			message['Subject'] = 'Your Restaurant Search Details! :)'

			body = "Hello! Thanks for interacting with our FoodBot...Check out the Top 10 restuarants that match you requirements:-\n\n"+response
			message.attach(MIMEText(body,"plain"))
			text = message.as_string()
			server.sendmail("chatbotrasa702@gmail.com", MailID, text)
			print("Mail Sent!")
			server.quit()	      

		except Exception as e:
			print("Email Failed")
			print(e)
		#sendmail(MailID,response)
		#return [SlotSet('mail_id',MailID)]
		#generate_response_msg(restaurants_response, tracker.get_slot('cuisine'), 10)



class ActionValidateLocation(Action):

	def name(self):
		return 'action_validate_city'

	def run(self,dispatcher,tracker,domain):

		city_list= map(lambda x:x.upper(),list(ZomatoData['City'].drop_duplicates().reset_index(drop=True)))
		loc=tracker.get_slot('location')

		if loc.upper() not in city_list:

			loc=None
			dispatcher.utter_message("Sorry, we don’t operate in this city!! Please specify a different location...")

		return [SlotSet('location',loc)]


class ActionValidateCuisine(Action):

	def name(self):
		return 'action_validate_cuisine'

	def run(self,dispatcher,tracker,domain):

		cuisine_list=['chinese','mexican','italian','american','south indian','north indian']
		cuisine=tracker.get_slot('cuisine')

		if cuisine.lower() not in cuisine_list:
			response="Oops! We currently do not have Restaurants for the mentioned Cuisine-"+cuisine+"\n Please choose a cuisine from the given list..."

			cuisine=None
			dispatcher.utter_message("---"+response)

		return [SlotSet('cuisine',cuisine)]

class ActionValidateBudget(Action):
	def name(self):
		return 'action_validate_budget'

	def run(self,dispatcher,tracker,domain):

		budget_list=['lesser than rs. 300','rs. 300 to 700','more than 700']
		budget=tracker.get_slot('price')

		if budget.lower() not in budget_list:

			budget=None
			dispatcher.utter_message("Please select Budget from the list!")

		return [SlotSet('price',budget)]

