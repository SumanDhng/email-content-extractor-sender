# Email Content Extractor and Sender

This script provides functionalities to process email files and extract their content (subject and body), and either save the extraction as JSON or convert it to Excel. It also facilitates sending emails using the extracted data or using a pre-existing excel.

## Requirements

Install the required dependencies using the following command:

```
pip install -r requirements.txt
```


## Installation

1. Clone the repository or download the script.

2. Create a file named `credentials.env` and include the following environment variables:

    ```
    DISPLAY_NAME = Your_Display_Name
    EMAIL = Your_Email_Address
    PASSWORD = Your_Email_Password
    RECEIVER_EMAIL = Receiver_Email_Address
    ```
    
3. Run the script using the following command:

    ```
    py main.py
    ```

4. Follow the prompts to choose the desired operation and provide the necessary inputs.

## Functionalities

### Extracting Email Content

The script allows users to extract email content from both .eml and .msg files. The extracted data, including the email subject and body, can be saved as JSON or converted to an Excel file.

### Sending Email

The script enables the sending of emails using pre-existing JSON data or by loading data from JSON or Excel files. With the flexibility to provide the file path for the JSON or Excel file.

## Usage

1. Run the script and choose the operation you want to perform.
2. Follow the prompts for providing the necessary inputs.
3. Check the "Output" directory for the extracted or converted data files.
