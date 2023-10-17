import re

# Sanitize the given text by removing non-printable characters and newlines.
def sanitize_text(text, body=False):
    if text is not None:
        cleaned_text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\x9F]', '', text) # Remove non-printable characters
        
        # Remove newlines only if it's not body content
        if body == False:
            cleaned_text = re.sub(r'[\n\r]','',cleaned_text)
    else:
        cleaned_text = text
    return cleaned_text