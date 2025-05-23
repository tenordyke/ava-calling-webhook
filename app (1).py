from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/answer", methods=['POST'])
def answer_call():
    answered_by = request.form.get("AnsweredBy", "")
    response = VoiceResponse()

    if "machine" in answered_by.lower():
        # Voicemail detected — play Ava's recording from static path
        response.play("https://ava-calling-service.onrender.com/static/audio/ava-voicemail.mp3")
    else:
        # Live person — brief message or routing
        response.say("Hi there! This call was intended for voicemail. We’ll follow up again soon.")

    return Response(str(response), mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True)
