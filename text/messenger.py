import os
import typer
from dotenv import find_dotenv, load_dotenv
from twilio.rest import Client

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

TWILIO_TEST_ACCOUNT_SID = os.getenv('TWILIO_TEST_ACCOUNT_SID')
TWILIO_TEST_AUTH_TOKEN = os.getenv('TWILIO_TEST_AUTH_TOKEN')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_MESSAGING_SERVICE_SID = os.getenv('TWILIO_MESSAGING_SERVICE_SID')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_message(body, to_number):
    typer.echo(typer.style(f"Sending message to {to_number}...", fg=typer.colors.GREEN))
    message = client.messages.create(
        messaging_service_sid=TWILIO_MESSAGING_SERVICE_SID,
        body=body,
        to=to_number
    )
    typer.echo(typer.style(f"Message SID: {message.sid}...", fg=typer.colors.GREEN))
