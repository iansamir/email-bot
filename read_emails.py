from simplegmail import Gmail
from simplegmail.query import construct_query

gmail = Gmail()

query_params = {
    "newer_than": (6, "year"),
    "older_than": (4, "year")
}

messages = gmail.get_sent_messages(query=construct_query(query_params))

for message in messages:
    print("To: " + message.recipient)
    print("From: " + message.sender)
    print("Subject: " + message.subject)
    print("Date: " + message.date)
    print("Preview: " + message.snippet)
    
    with open("email_samples.txt", "a") as f:
        if message.plain:
            if len(message.plain) < 1000:
                f.write(message.plain)
    # print("Message Body: " + message.plain)  # or message.html
