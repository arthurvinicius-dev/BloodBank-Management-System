import os
import smtplib

# Credentials are read from environment variables instead of being hard-coded.
EMAIL_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')

content = "Hello "
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login(EMAIL_USER, EMAIL_PASSWORD)
mail.sendmail('helpafriend.bloodbank@gmail.com', 'divyashah.qa@gmail.com', content)
