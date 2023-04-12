from simplegmail import Gmail

gmail = Gmail() # will open a browser window to ask you to log in and authenticate

# sample_email = """
# Hi, Prof. Melton

# My name is Ian Samir and my student number is N13654284. I just came back
# from vacation and am having some trouble registering for classes for this
# fall. I will be a freshman at NYU this year. I would like to take an Econ
# class and a finance class at Stern and a math course. However, the class
# enrollment tool keeps telling me I do not have the prerequisites for any
# courses I pick. I am not sure if I have to take placement tests or
# something but I cannot enroll in any classes at this time and would very
# much appreciate some help.

# Thanks,

# Ian
# """

# sample_email = sample_email.replace("\n", "<br>")
sender_email = ""
def send_email(recipient, subject, message):
    message = message.replace("\n", "<br>")
    params = {
        "to": recipient,
        "sender": sender_email,
        "subject": subject,
        "msg_html": message,
        "signature": True  # use my account signature
    }

    message = gmail.send_message(**params)  # equivalent to send_message(to="you@youremail.com", sender=...)
    
    print("Message sent successfully")
