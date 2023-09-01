import os
import resend  # make sure the 'resend' package is installed

resend.api_key = "re_6PeVi179_HcrXp45jBArGYrAvVMJQGx6T"

# Use the line below if you set the API key as an environment variable
# resend.api_key = os.environ["re_6PeVi179_HcrXp45jBArGYrAvVMJQGx6T"] #

params = {
    "from": 'cecconig@newaisolutions.com',
    "to": ["giovanni@newaisolutions.com"],
    "subject": "[Insert Subject Here]",
    "text": "[Insert Text Here]",
}

email = resend.Emails.send(params)
print(email)
