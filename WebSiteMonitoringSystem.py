import time
import smtplib
from email.mime.text import MIMEText
import configparser
import subprocess
import sys

# Lees instellingen uit de config.ini
config = configparser.ConfigParser()
config.read('config.ini')

monitoring_settings = config['MonitoringSettings']
email_settings = config['EmailSettings']
email_error_settings = config['EmailWhenError']
email_no_error_settings = config['EmailNoError']
interval = int(config['IntervalInSeconds']['time'])

url = monitoring_settings['url']
search_phrase_error = monitoring_settings['foutzoekzin']
search_phrase_maybe_error = monitoring_settings['mogelijkfoutzin']
search_phrase_no_error = monitoring_settings['goedzoekzin']

recipients = email_settings['ontvangers'].split(',')
bcc_recipients = email_settings.get('bcc_ontvangers', '').split(',')
sender = email_settings['afzender']
smtp_server = email_settings['smtp_server']
smtp_port = int(email_settings['smtp_port'])
smtp_auth = email_settings.getboolean('smtp_auth')

# Variabelen om bij te houden of een e-mail al is verstuurd
error_email_sent = False
maybe_error_email_sent = False
no_error_email_sent = False

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    
    # Voeg BCC-ontvangers toe aan de e-mail
    if bcc_recipients:
        msg['Bcc'] = ', '.join(bcc_recipients)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        if smtp_auth:
            server.login(sender, email_settings['smtp_password'])
        server.sendmail(sender, recipients + bcc_recipients, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_website():
    global error_email_sent, maybe_error_email_sent, no_error_email_sent

    try:
        # Gebruik curl om de website te downloaden naar tmp.txt
        subprocess.run(['curl', '-o', 'tmp.txt', url], check=True)

        with open('tmp.txt', 'r', encoding='utf-8') as f:
            content = f.read()

        if search_phrase_error in content and not error_email_sent:
            send_email(email_error_settings['onderwerp'], email_error_settings['inhoud'])
            error_email_sent = True
            maybe_error_email_sent = False
            no_error_email_sent = False
        elif search_phrase_maybe_error in content and not maybe_error_email_sent:
            send_email(email_error_settings['onderwerp'], email_error_settings['inhoud'])
            maybe_error_email_sent = True
            error_email_sent = False
            no_error_email_sent = False
        elif search_phrase_no_error in content and not no_error_email_sent:
            send_email(email_no_error_settings['onderwerp'], email_no_error_settings['inhoud'])
            no_error_email_sent = True
            error_email_sent = False
            maybe_error_email_sent = False

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        while True:
            check_website()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Script stopped by user")
        sys.exit(0)
