# Twilio-Text
## Lightweight Limited-Purpose SMS Tool

This is the public open source version of Clean Your Shoes' proprietary messaging tool that it uses to send brand updates and notifications via SMS.

This tool is built with Python 3.11.2 and Twilio API. It can be added to a code base as part of a bigger project you may be working on, or can be ran by itself as a CLI program.

This code is free to use and download. Fork, clone, copy, download, whatever with this code. All I ask is that you provide proper credit when using this code in your own work.

### Requirements
- Python 3.11.2
- A Twilio account for SMS services. (Please refer to their API docs)
- Additional Libraries:
  - `os`
  - `typer`
  - `dotenv`
  - `twilio`

As the `dotenv` library suggests, you will need to put your Twilio credentials in an `.env` file where the code can access it. Of course, you may change this to fit whatever configuration/settings file or process you prefer.

### Running the program
This is currently a lightweight tool that runs on the CLI via `typer`. Navigate to the `twilio-text` folder and run:

`python3 -m twilio-text`

From there, an easy-to-use, interactive menu will pop up. If this does not work, you may first need to import this module into your Python path.

### Upcoming Releases
Below are some features that will be added to the open-source version. Since this was originally built for Clean Your Shoes, many of these are coded and built specifically for the needs of the brand and its tech stack, and must be properly refactored and reconfigure for open-source use.
- Persistence object/class to connect your DB of choice to the tool.
  - Adding numbers to the DB
  - Retrieve subscriber list
- Send SMS to multiple numbers.
- GUI