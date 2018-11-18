
from twilio.rest import TwilioRestClient

TWILIO_PHONE_NUMBER = "+13239225253"    #phone number purchased through twilio

DIAL_NUMBERS = ["+18058133733", "+18054099434"]     #list of phone number(s) to be contacted

TWIML_INSTRUCTIONS_URL = \
    "http://static.fullstackpython.com/phone-calls-python.xml"      #accesses xml files from twilio to contact our phone numbers verified from our twilio account

client = TwilioRestClient("ACb164f149b0bd171c91b77ca00e96fa58", "642adfa9333d686beb7e5c223ffaaa6f") #Authentication keys from twilio

def contact_numbers(numbers_list):
    for number in numbers_list:
        print("Contacting" + number)
        

        #calls defined phone number. For demonstration purposes, have a cell phone being contacted, 
        #however in real world applicaiton, the program would contact the police.
        client.calls.create(to=DIAL_NUMBERS[0], from_=TWILIO_PHONE_NUMBER, url = TWIML_INSTRUCTIONS_URL, method="GET")


        #demonstrationg that we can also send threaat alerts, either to the police or to a specified phone number.
        message = client.messages. \
            create(to=DIAL_NUMBERS[1], 
                   from_=TWILIO_PHONE_NUMBER, 
                   url = TWIML_INSTRUCTIONS_URL, 
                   body="THREAT DETECTED! Weapon detected at 1234 Oak Street, 18:16, 11.11.18.",
                   media_url = 'https://media.discordapp.net/attachments/513435983023177739/513739387977203742/frame.jpg?width=1796&height=1010')
        
        print(message.sid)


if __name__ == "__main__":
    contact_numbers(DIAL_NUMBERS)
    