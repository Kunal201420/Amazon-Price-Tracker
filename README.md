# Amazon Price Tracker with Email Alerts

This Python project tracks the price of a product on Amazon and sends an email notification when the price drops below a target threshold. It securely uses environment variables to manage sensitive information like credentials and URLs.

---

## Features
- Scrapes live product name and price data from Amazon.
- Automatically calculates a price threshold for alerts.
- Sends email notifications when the price falls below the threshold.
- Uses environment variables for security and configuration.

---

## Technologies Used
- Python 3
- BeautifulSoup4 (for HTML parsing)
- Requests (for web scraping)
- smtplib (for sending email alerts)
- os (for environment variable management)

---

## Prerequisites
You need:
- Python 3 installed on your system.
- A Gmail account (App Password required if 2FA is enabled).
- The Amazon product URL to monitor.
- Installed dependencies.
