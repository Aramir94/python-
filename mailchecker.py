# Delete All aliexpress
import imaplib
import email
# imap 
imap_server = 'imap.gmail.com'
email_address = input('input your gmail ID \n')
password = input('input your password \n')
delete_word = input('input wanna delete\n')

imap = imaplib.IMAP4_SSL(imap_server, port=993)
imap.login(email_address, password)

imap.select("Inbox")
_, msgnums = imap.search(None, "ALL")

print(msgnums)

for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")

    message = email.message_from_bytes(data[0][1])

    print(f"Message Number: {msgnum}")
    print(f"From : {message.get('From')}")
    print(f"To : {message.get('To')}")
    print(f"BCC : {message.get('BCC')}")
    print(f"Date : {message.get('Date')}")
    print(f"Subject : {message.get('Subject')}")

    # print("Content:")
    # for part in message.walk():
    #     if part.get_content_type() == "text/plain":
    #         print(part.as_string())

    if delete_word in message.get('From'):
        imap.store(msgnum, '+FLAGS', '\\Deleted') 
imap.expunge()
imap.close()



