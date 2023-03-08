import imaplib
import email

# Login to your Daum.net email account
mail = imaplib.IMAP4_SSL('imap.daum.net')
mail.login('coadrnd@daum.net', 'devicemart!@')

# Select the mailbox you want to download emails from
mail.select('inbox')

# Search for emails based on sender email address
status, email_ids = mail.search(None, 'FROM "telecs@telecs.co.kr"')

# Loop through each email id and download attachments
for id in email_ids[0].split():
    status, email_data = mail.fetch(id, '(RFC822)')
    raw_email = email_data[0][1]
    email_message = email.message_from_bytes(raw_email)
    if email.utils.parseaddr(email_message['From'])[1] == 'specific_sender':
        for part in email_message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            filename = part.get_filename()
            if not filename:
                continue
            with open(filename, 'wb') as f:
                f.write(part.get_payload(decode=True))

# Logout of your email account
mail.logout()
