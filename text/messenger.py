import os
import typer
from dotenv import find_dotenv, load_dotenv
from twilio.rest import Client
from text.persistence import db

# TODO: See if Twilio has efficient group/mass texting.

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

TWILIO_TEST_ACCOUNT_SID = os.getenv('TWILIO_TEST_ACCOUNT_SID')
TWILIO_TEST_AUTH_TOKEN = os.getenv('TWILIO_TEST_AUTH_TOKEN')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_REMINDER_MESSAGING_SERVICE_SID = os.getenv('TWILIO_REMINDER_MESSAGING_SERVICE_SID')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_message(body, to_number):
    typer.echo(typer.style(f"Sending message to {to_number}...", fg=typer.colors.GREEN))
    message = client.messages.create(
        messaging_service_sid=TWILIO_REMINDER_MESSAGING_SERVICE_SID,
        body=body,
        to=to_number
    )
    typer.echo(typer.style(f"Message SID: {message.sid}...", fg=typer.colors.GREEN))


def send_to_all_subscribers(body):
    subscribers = db.retrieve_all_sms_subscribers()
    for subscriber in subscribers:
        to_number = "+1" + subscriber[0]
        send_message(body, to_number)


def get_sms_list():
    db.retrieve_all_sms_subscribers()


def add_subscriber_to_list(phone_number, first_name, last_name):
    db.add_subscriber(phone_number, first_name, last_name)
