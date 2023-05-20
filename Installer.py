import os
import subprocess
import requests
import webbrowser

# define the GitHub repository URL and the list of files to download
github_repo = "https://github.com/Parahdox/freshstarts"
files_to_download = [
    "4ukeyforandroid.exe",
    "ChromeSetup (2).exe",
    "NordVPNSetup.exe",
    "OfficeSetup.exe",
    "readerdc64_en_ka_cra_mdr_install.exe",
    "winrar-x64-611.exe"
    "VeraCrypt_Setup_x64_1.25.9.zip"
]

# create a temporary directory to store the downloaded files
temp_dir = "temp"
if not os.path.exists(temp_dir):
    os.mkdir(temp_dir)

# download the files from the GitHub repository and save them to the temporary directory
for filename in files_to_download:
    url = f"{github_repo}/raw/main/{filename}"
    print(f"Downloading {url}...")
    response = requests.get(url)
    response.raise_for_status()  # raise an exception if the request fails
    with open(f"{temp_dir}/{filename}", "wb") as f:
        f.write(response.content)
    print(f"Downloaded {filename} to {temp_dir}")

# install the downloaded programs with admin privileges
for filename in files_to_download:
    filepath = f"{temp_dir}/{filename}"
    print(f"Installing {filepath}...")
    try:
        subprocess.call([filepath])  # use the appropriate installation command-line arguments for each program
    except OSError as e:
        print(f"Error installing {filename}: {e}")
    else:
        print(f"Successfully installed {filename}")

#open web browser and navigate to web pages for installers to big to download from repository

url1 = 'https://www.synology.com/en-global/dsm/feature/drive'
url2 = 'https://get.adobe.com/reader/'
webbrowser.open(url1)
webbrowser.open_new_tab(url2)


