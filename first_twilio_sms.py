from twilio.rest import TwilioRestClient
from twilio import twiml
from twilio_keys import ACCOUNT_SID, AUTH_TOKEN

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
message = client.sms.messages.create(to="+15163170315", from_= "+15162792450",
body="first twilio text!")

