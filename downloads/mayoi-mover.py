import os
import zipfile
import json
import requests
import shutil

script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

def get_gallery_data(providerAPI, galID, tokenID):
    galleryQuery = {
        "method": "gdata",
        "gidlist": [[galID, tokenID]],
        "namespace": 1
    }
    payload = json.dumps(galleryQuery)
    headers = {'Content-Type': 'application/json', 'Accept': 'application/jsonrequest'}
    response = requests.post(providerAPI, data=payload, headers=headers)
    result = response.json()
    return result

def get_folders_in_directory():
    folders = [folder for folder in os.listdir('.') if os.path.isdir(folder)]
    return folders

def convert_response(response):
    converted_response = {}
    gmetadata = response.get("gmetadata")
    if gmetadata:
        gmetadata = gmetadata[0]
        converted_response["category"] = gmetadata.get("category")
        converted_response["download"] = f"/archive/{gmetadata['gid']}/download/"
        converted_response["expunged"] = gmetadata.get("expunged", False)
        converted_response["filecount"] = int(gmetadata.get("filecount", 0))
        converted_response["filesize"] = int(gmetadata.get("filesize", 0))
        converted_response["fjord"] = False
        converted_response["gallery"] = gmetadata.get("gid")
        converted_response["posted"] = int(gmetadata.get("posted", 0))
        converted_response["rating"] = float(gmetadata.get("rating", 0))
        converted_response["tags"] = gmetadata.get("tags", [])
        converted_response["title"] = gmetadata.get("title")
        converted_response["title_jpn"] = gmetadata.get("title_jpn")
        converted_response["uploader"] = gmetadata.get("uploader")
    return converted_response

def create_api_json(folder, response):
    zip_file = None
    for file in os.listdir(folder):
        if file.endswith(".zip"):
            if zip_file:
                print(f"Ignoring folder '{folder}' due to multiple zip files.")
                return
            zip_file = os.path.join(folder, file)

    if not zip_file:
        print(f"Ignoring folder '{folder}' as no zip file found.")
        return

    api_data = convert_response(response)

    api_json = json.dumps(api_data)
    api_json_path = os.path.join(folder, "api.json")
    with open(api_json_path, "w") as file:
        file.write(api_json)

    with zipfile.ZipFile(zip_file, "a") as zipf:
        zipf.write(api_json_path, "api.json")

    os.remove(api_json_path)  # Remove the temporary api.json file
    
def move_zips_and_delete_folders():
    # Destination directory to move the zip files
    destination_directory = r"PATH TO YOUR LANRARAGI GALLERY FOLDER"

    # Iterate through all subdirectories in the current directory
    for root, dirs, files in os.walk(os.getcwd()):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)

            # Check if the folder contains only one zip file
            zip_files = [file for file in os.listdir(folder_path) if file.endswith('.zip')]
            if len(zip_files) == 1:
                zip_file_name = zip_files[0]
                zip_file_path = os.path.join(folder_path, zip_file_name)

                # Move the zip file to the destination directory
                new_zip_file_path = os.path.join(destination_directory, zip_file_name)
                shutil.move(zip_file_path, new_zip_file_path)

                # Remove the original folder
                shutil.rmtree(folder_path)

                print(f"Moved '{zip_file_name}' to '{destination_directory}' and deleted '{dir_name}'.")

def process_folders(providerAPI):
    folders = get_folders_in_directory()
    for folder in folders:
        folder_parts = folder.split("-")
        if len(folder_parts) != 2:
            print(f"Ignoring folder '{folder}' due to incorrect format.")
            continue
        galID, tokenID = folder_parts
        response = get_gallery_data(providerAPI, galID, tokenID)
        create_api_json(folder, response)
    move_zips_and_delete_folders()

# Example usage
providerAPI = "https://api.e-hentai.org/api.php"
process_folders(providerAPI)
