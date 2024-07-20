import requests
import subprocess
import shutil

url = 'https://github.com/ArchipelagoMW/Archipelago/releases/download/0.5.0/Setup.Archipelago.0.5.0.exe'
local_filename = 'archipelago.exe'
properties_location = "C:\ProgramData\Archipelago\Minecraft Forge server\server.properties"

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
    exit(0)
print("Process completed with return code:", result.returncode)
shutil.copy2("./"+local_filename, properties_location)
print("\n\nInstall finished. Press enter to exit.")
input()

