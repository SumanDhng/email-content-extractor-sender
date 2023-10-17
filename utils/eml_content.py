import email
from utils.sanitize_text import sanitize_text

def process_eml(file_path,file_name):
    with open(file_path,'rb') as eml_file:
        message = email.message_from_binary_file(eml_file)

    # Initialize the email_data dictionary with details
    email_data={
        "file_name" : file_name, # Set the file name in the extracted data
        "sender" : sanitize_text(message['from']), # Sanitize and extract the sender information
        "receiver" : sanitize_text(message['to']), # Sanitize and extract the receiver information
        "subject" : sanitize_text(message['subject']), # Sanitize and extract the subject
        "email_body" : '', # Initialize an empty string for the email body
        "type" : 'eml' # Set the type as EML
    }

    # Set the type as EML
    for part in message.walk():
        content_type = part.get_content_type()

        # Check if the content type is plain text
        if content_type == 'text/plain':
            payload = part.get_payload(decode=True) # Extract the payload of the part
            
            try:
                decoded_payload = payload.decode("utf-8") # Try to decode the payload using UTF-8
            except UnicodeDecodeError:
                decoded_payload = payload.decode("latin-1", errors='replace') # If decoding fails, use Latin-1
            email_data['email_body'] += decoded_payload # Append the decoded payload to the email body
            email_data['email_body'] = sanitize_text(email_data['email_body'], True) # Sanitize the email body text

    return email_data