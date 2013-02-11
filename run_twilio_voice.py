from flask import Flask, render_template
from twilio.util import TwilioCapability
from twilio_keys import ACCOUNT_SID, AUTH_TOKEN

app = Flask(__name__)

@app.route('/client', methods=['GET','POST'])
def client():
    """Respond to incoming requests."""

    application_sid = "APabe7650f654fc34655fc81ae71caa3ff"
    capability = TwilioCapability(ACCOUNT_SID, AUTH_TOKEN)
    capability.allow_client_outgoing(application_sid)
    token = capability.generate()
    return render_template('client.html', token=token)

if __name__ == "__main__":
    app.run(debug=True)
