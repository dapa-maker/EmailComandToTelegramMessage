import imaplib
import email
import telegram as tele

from dotenv import load_dotenv, dotenv_values
import os


def check():
    load_dotenv()
    imap_server = os.getenv("IMAP_SERVER")
    email_address = os.getenv("EMAIL_ADDRESS")
    print("Server: " + imap_server + " // Address: " + email_address)
    password = os.getenv("PASS_EMAIL")

    imap = imaplib.IMAP4_SSL(imap_server)

    imap.login(email_address, password)
    imap.select("Inbox")
    _, data = imap.search(None, "ALL")
    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]

    _, mail = imap.fetch(latest_email_id, "(RFC822)")
    message = email.message_from_bytes(mail[0][1])

    message_str = ""
    for part in message.walk():
        if part.get_content_type() == "text/plain":
            message_str += part.as_string()
    imap.close()

    index = message_str.find("QR")
    num_str = message_str[index + 2: index + 3]

    num = int(num_str)

    if num == 1:
        tele.sendMessage("1. Nachricht")

    elif num == 2:
        tele.sendMessage("2. Nachricht")

    elif num == 3:
        tele.sendMessage("3. Nachricht")

    else:
        tele.sendMessage("4. Nachricht")
