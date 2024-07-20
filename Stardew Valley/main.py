import requests
import subprocess
import zipfile
import shutil
import os
import sys

url = 'https://github.com/ArchipelagoMW/Archipelago/releases/download/0.5.0/Setup.Archipelago.0.5.0.exe'
local_filename = 'archipelago.exe'

with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192): 
            f.write(chunk)

print("!!!! Please finish the Archipelago installation to continue !!!!")
try:
    result = subprocess.run(["./"+local_filename], check=True)
except subprocess.CalledProcessError:
    print("Archipelago install failed! press enter to exit")
    input()
    exit(1)


print("Please go to Steam, from Steam go to Stardew Valley, right click, and sellect Properties. Then go to Betas and select 'legacy_1.5.6' and then come back and press enter")
input()

print("!!!! Please download this file and press enter (May need to login to NexusMods)!!!!")
print("https://www.nexusmods.com/stardewvalley/mods/2400?tab=files&file_id=76802")
input()

print("!!!! Please download this file and press enter (May need to login to NexusMods)!!!!")
print("https://www.nexusmods.com/stardewvalley/mods/16087?tab=files&file_id=104618")
input()

print("Please enter the Stardew Valley game directory location:")
stardew = input("> ")

print("Please copy the downloaded files to the same location of this installer and press enter")
input()

def unpack_zip(zip_path, extract_to='.'):
    """
    Unpacks a zip file to the specified directory.

    :param zip_path: Path to the zip file.
    :param extract_to: Directory to extract files to. Defaults to current directory.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

unpack_zip("StardewArchipelago Mod-16087-5-5-3-1719001186.zip")
unpack_zip("SMAPI 3.18.6-2400-3-18-6-1696545739.zip")

print("!!!! Please finish the Stardew Modding API installation to continue !!!!")
def run_installer():
    installer_dir = os.path.dirname(os.path.abspath(__file__)) + "/SMAPI 3.18.6 installer/"

    # Make sure we're not running within a zip folder
    if "%TEMP%" in installer_dir:
        print("Oops! It looks like you're running the installer from inside a zip file. Make sure you unzip the download first.")
        input("Press Enter to exit...")
        sys.exit()

    # Check if the necessary files exist
    installer_dll_path = os.path.join(installer_dir, "internal", "windows", "SMAPI.Installer.dll")
    installer_exe_path = os.path.join(installer_dir, "internal", "windows", "SMAPI.Installer.exe")

    if not os.path.isfile(installer_dll_path):
        print(f"Oops! SMAPI is missing one of its files. Your antivirus might have deleted it.")
        print(f"Missing file: {installer_dll_path}")
        input("Press Enter to exit...")
        sys.exit()

    if not os.path.isfile(installer_exe_path):
        print(f"Oops! SMAPI is missing one of its files. Your antivirus might have deleted it.")
        print(f"Missing file: {installer_exe_path}")
        input("Press Enter to exit...")
        sys.exit()

    # Start the installer
    try:
        subprocess.run(installer_exe_path, check=True)
    except subprocess.CalledProcessError:
        print()
        print("Oops! The SMAPI installer seems to have failed. The error details may be shown above.")
        print()
        input("Press Enter to exit...")
        sys.exit()

run_installer()


shutil.copy2("./StardewArchipelago", stardew+"/Mods/StardewArchipelago")
print("\n\nInstall finished. Press enter to exit.")
input()
