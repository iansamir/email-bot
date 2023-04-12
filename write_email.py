import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

system_prompt = """
Please write an email in the style of the user given a prompt and the sample emails below. Don't be too formal, keep the email brief, and don't add additional information, just express what the user says in the prompt. 
Sign the email as Ian Samir. 

SAMPLES:
Hi Mrs. Satchwell,

Sorry for the late response; I forgot to send an email earlier. My presentation is about Social Media Safety and I should have two panel members for the presentation. 

Thanks,

Ian Samir

Hi, Prof. Melton

My name is Ian Samir and my student number is N13654284. I just came back
from vacation and am having some trouble registering for classes for this
fall. I will be a freshman at NYU this year. I would like to take an Econ
class and a finance class at Stern and a math course. However, the class
enrollment tool keeps telling me I do not have the prerequisites for any
courses I pick. I am not sure if I have to take placement tests or
something but I cannot enroll in any classes at this time and would very
much appreciate some help.

Thanks,

Ian Samir
"""

def create_email():
    user_prompt = input("Describe the email you want. \n")
    messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
    ]

    def write_email(prompt):
        messages.append({"role": "user", "content": prompt})
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        reply = completion.choices[0].message["content"]
        print(reply)

        messages.append({"role": "assistant", "content": reply})
        return input("Please type done if satisfied, if not, continue prompting \n")

    while user_prompt != "done":
        user_prompt = write_email(user_prompt)

    final_draft = messages[-1]["content"]
    return final_draft
