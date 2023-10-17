import os

# Custom Imports
from utils.eml_content import process_eml
from utils.msg_content import process_msg
from utils.data_conversion import load_json, convert_to_json, convert_to_xls, load_xls
from utils.send_email import send_email

if __name__ == "__main__":
    cwd = os.getcwd() # Get the current working directory
    output_path = os.path.join(cwd, "Output") # Path for Output directory
    json_output = os.path.join(output_path, "content_extraction.json") # Path for Json Output file
    xls_ouput = os.path.join(output_path, "content_extraction.xlsx") # Path for Excel Output file

    # Ask for desired operation
    operation_choice = int(input("Enter 1 to extract from eml/msg or 2 to send email: "))
    
    print("\n\t\t\033[1m\033[4mEmail Body & Subject Extractor\033[0m\n")

    # Check if the user wants to extract data from eml/msg files
    if operation_choice == 1:
        extraction = []

        # Folder Path containing Eml/Msg Files
        folder_path = input("Enter Folder path: ")

        # Traverse through folder
        for root,dirs,files in os.walk(folder_path):
            for file in files:
                # Check if the file is of eml or msg type
                if file.endswith(("eml","msg")):
                    file_path = os.path.join(root, file)
                    file_name = os.path.basename(file_path)
                    # Process eml files
                    if file.endswith("eml"):
                        email_data = process_eml(file_path,file_name)
                        extraction.append(email_data)
                    # Process msg files
                    elif file.endswith("msg"):
                        msg_data = process_msg(file_path,file_name)
                        extraction.append(msg_data)
        if extraction:
            # Create directory if it doesn't exist
            if not os.path.exists("Output"):
                os.mkdir("Output")
            
            # Data Conversions
            convert_to_json(extraction, json_output)
            json_data = load_json(json_output)
            convert_to_xls(json_data, xls_ouput)

            print("Extraction Completed!")
            
    elif operation_choice == 2:
        print("\n\t\t\033[1m\033[4mEmail Sender\033[0m\n")
        
        # Ask the user for the mode of data input
        data_mode = int(input("Enter 1 to use pre-existing json or 2 to give path to json or xlsx: "))

        # Load the pre-existing JSON data
        if data_mode == 1:
            json_data = load_json(json_output)

        # Ask for json or xlsx file path
        elif data_mode == 2:
            file_path = input("\nEnter the file path (json/xlsx):")
            
            # Loop until valid path is provided
            while not (os.path.isfile(file_path)):
                file_path = input("Please enter a valid File Path (json or xlsx): ").strip('"')

            file_name = os.path.basename(file_path)

            # Load json and convert to xlsx
            if file_name.endswith("json"):
                json_data = load_json(file_path)
                convert_to_xls(json_data, xls_ouput)
            
            # Load xlsx and convert to json
            elif file_name.endswith(("xlsx","xls")):
                df = load_xls(file_path)
                df_json = df.to_json(orient="records")
                convert_to_json(df_json, json_output)
                json_data = load_json(json_output)
       
        send_email(json_data) # Send Email using json data

        print("Done!")
        