from flask import Flask, request, render_template
from twilio.util import TwilioCapability
import twilio.twiml
from twilio_keys import ACCOUNT_SID, AUTH_TOKEN, my_twilio_num, CALLERS 
import re

app = Flask(__name__)

# my Twilio phone number
caller_id = "+%s" %(my_twilio_num)
default_client = "Moon"

@app.route("/", methods=['GET','POST'])
def hello_monkey():
    # Get the caller's phone number from the incoming Twilio request
    from_number = request.values.get('From', None)
    resp = twilio.twiml.Response()

    # if the caller is someone we know:
    if from_number in CALLERS: # Greet the caller by name
        resp.say("Hello " + CALLERS[from_number])
    else:
        resp.say("Hello Monkey")

    return str(resp)


@app.route('/voice', methods=['GET','POST'])
def voice():
    from_number = request.values.get('PhoneNumber', None)

    resp = twilio.twiml.Response()

    with resp.dial(callerId=caller_id) as r:
        if from_number and re.search('^[\d\(\)\- \+]+$', from_number):
            r.number(from_number)
        else:
            r.client(default_client)

    return str(resp)


@app.route('/client', methods=['GET','POST'])
def client():
    """Respond to incoming requests."""

    capability = TwilioCapability(ACCOUNT_SID, AUTH_TOKEN)
    application_sid = "APabe7650f654fc34655fc81ae71caa3ff"
    application_sid2 = "AP123"

    capability.allow_client_outgoing(application_sid2)
    capability.allow_client_incoming(default_client)

    token = capability.generate()
    return render_template('client.html', token=token, client_name=default_client)

if __name__ == "__main__":
    app.run(debug=True)
