
from twilio.rest import TwilioRestClient

TWILIO_PHONE_NUMBER = "twilio number"    #phone number purchased through twilio

DIAL_NUMBERS = ["phone number1", "phone number2"]     #list of phone number(s) to be contacted

TWIML_INSTRUCTIONS_URL = \
    "http://static.fullstackpython.com/phone-calls-python.xml"      #accesses xml files from twilio to contact our phone numbers verified from our twilio account

client = TwilioRestClient("authentication key", "sid key") #Authentication keys from twilio

def contact_numbers(numbers_list):
    for number in numbers_list:
        print("Contacting" + number)
        

        #calls defined phone number. For demonstration purposes, have a cell phone being contacted, 
        #however in real world applicaiton, the program would contact the police.
        client.calls.create(to=DIAL_NUMBERS[0], from_=TWILIO_PHONE_NUMBER, url = TWIML_INSTRUCTIONS_URL, method="GET")


        #demonstrationsg that we can also send threaat alerts, either to the police or to a specified phone number.
        message = client.messages. \
            create(to=DIAL_NUMBERS[1], 
                   from_=TWILIO_PHONE_NUMBER, 
                   url = TWIML_INSTRUCTIONS_URL, 
                   body="THREAT DETECTED! Weapon detected at 1234 Oak Street, 18:16, 11.11.18.",
                   media_url = 'https://media.discordapp.net/attachments/513435983023177739/513739387977203742/frame.jpg?width=1796&height=1010')
        
        print(message.sid)


if __name__ == "__main__":
    contact_numbers(DIAL_NUMBERS)
    