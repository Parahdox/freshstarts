import os
import subprocess
import requests

# define the GitHub repository URL and the list of files to download
github_repo = "https://github.com/Parahdox/freshstarts"
files_to_download = ["4ukeyforandroid.exe", "ChromeSetup (2).exe", "NordVPNSetup.exe", "OfficeSetup.exe", "readerdc64_en_ka_cra_mdr_install.exe", "winrar-x64-611.exe"]

# create a temporary directory to store the downloaded files
temp_dir = "temp"
if not os.path.exists(temp_dir):
    os.mkdir(temp_dir)

# download the files from the GitHub repository and save them to the temporary directory
for filename in files_to_download:
    url = f"{github_repo}/raw/main/{filename}"
    response = requests.get(url)
    with open(f"{temp_dir}/{filename}", "wb") as f:
        f.write(response.content)

# install the downloaded programs
for filename in files_to_download:
    filepath = f"{temp_dir}/{filename}"
    subprocess.call([filepath, "/SILENT"])  # use the appropriate installation command-line arguments for each program