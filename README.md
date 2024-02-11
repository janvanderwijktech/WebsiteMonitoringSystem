# WebsiteMonitoringSystem
Website Monitoring and Email Notification System
Overview:
This Python script is designed to monitor the status of a specified website and send email notifications based on the content retrieved from the site. It leverages the curl command to download the webpage and then searches for specific phrases within the content to determine the website's status. Depending on the identified status, the script sends different email alerts to designated recipients.

Features:
Configurable Monitoring Settings: The monitoring settings such as the URL of the website to monitor and the phrases to search for are stored in a configuration file (config.ini), allowing for easy customization.

Email Notification: The script utilizes the Simple Mail Transfer Protocol (SMTP) to send email notifications to designated recipients when specific conditions are met. It supports sending emails to multiple recipients and includes an option for blind carbon copy (BCC) recipients.

Multiple Alert Levels: The script categorizes the website's status into three levels: error, potential error, and no error. Each level triggers a different email notification with customizable subject and content.

Automated Execution: The script runs indefinitely in a loop, continuously monitoring the website at regular intervals. It gracefully handles interruptions such as KeyboardInterrupt, ensuring smooth operation.

How It Works:
Configuration: The script reads configuration settings from the config.ini file, including the URL of the website to monitor, search phrases for different status levels, email settings, and monitoring interval.

Website Checking: At each interval, the script fetches the content of the specified URL using the curl command. It then searches for predefined phrases within the content to determine the website's status.

Email Notification: Based on the identified status (error, potential error, or no error), the script sends corresponding email notifications to the configured recipients. It ensures that each type of email is sent only once until the website's status changes.

Continuous Monitoring: The script continues to monitor the website indefinitely, repeating the checking and notification process at the specified interval.

Deployment:
To deploy this monitoring system, follow these steps:

Customize the config.ini file with the appropriate settings for your environment, including the URL to monitor, email configuration, and search phrases.
Ensure that the necessary Python packages (smtplib, email.mime.text, configparser) are installed.
Run the Python script (monitor_website.py) on a system with internet access and SMTP server connectivity.
Monitor the email alerts to stay informed about the status of the monitored website.
Dependencies:
Python 3.x
curl command-line tool
Internet connectivity
Access to an SMTP server for sending email notifications
License:
This project is distributed under the MIT License, allowing for free use, modification, and distribution.

Feel free to adjust the description according to your preferences and specific details of the project.
