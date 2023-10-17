import extract_msg
import re
from utils.sanitize_text import sanitize_text

def process_msg(file_path,file_name):
    msg = extract_msg.Message(file_path)

    headers = str(msg.header).splitlines() # Extract and split the headers
    sender_name = ""
    sender_email = ""
    
    # Iterate through the headers
    for header in headers: 
        if header.startswith("From:"): # Check for the sender information
            sender_match = re.search(r'From:\s+"?(.*?)"?\s*(<.*?>)', header) # Extract sender name and email
            
            # Extract and clean the sender's name and email
            if sender_match:
                sender_name = sender_match.group(1).strip(' "')
                sender_email = sender_match.group(2).strip(' "')
    
    # Combine the sender's name and email
    sender = sender_name + " " + sender_email
    
    # Initialize the msg_data dictionary with details
    msg_data = {
        "file_name" : file_name,
        "sender" : sanitize_text(sender.strip()), # Sanitize and extract the sender information
        "receiver" : sanitize_text(msg.to), # Sanitize and extract the receiver information
        "subject" : sanitize_text(msg.subject), # Sanitize and extract the subject
        "email_body" : sanitize_text(msg.body, True), # Sanitize and extract the email body
        "type": 'msg'  # Set the type as MSG
    }
    msg.close() # Close the MSG file
    return msg_data