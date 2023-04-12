from write_email import create_email
from send_email import send_email

final_email = create_email()
subject = input("Subject? \n")
recipient = input("To whom? \n")

send_email(recipient=recipient, subject=subject, message=final_email)