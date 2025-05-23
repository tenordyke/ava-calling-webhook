# Ava Reid Voicemail Webhook

This Flask app detects whether a call was answered by a human or voicemail and plays Ava's pre-recorded message if it's a voicemail.

## Setup Instructions

1. Make sure your Ava voicemail MP3 is hosted at a public HTTPS URL.

2. Update the `response.play(...)` line in `app.py` with your actual file link.

3. Deploy to Render.com or run locally.

### To Deploy on Render:
- Create a new Web Service
- Use `start command`: `gunicorn app:app`
- Add a build command if needed: `pip install -r requirements.txt`
- Make sure port is set to `10000` or default Render port

### To Run Locally:
```bash
pip install -r requirements.txt
python app.py
```

Then point your Twilio call to:
```
https://your-render-domain.com/answer
```

And add this to your Twilio call setup:
```python
call = client.calls.create(
    to="+1XXXXXXXXXX",
    from_="YourTwilioNumber",
    url="https://your-render-domain.com/answer",
    machine_detection="Enable"
)
```
