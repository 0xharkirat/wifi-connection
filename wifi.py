import subprocess
import internet
import time

# your wifi ssid and profile
wifi_ssid = "<your network id"
wifi_profile = "<your wifi profile>"

# check for internet and attempt to connect to wifi
while True:
    connected = internet.checkInternetHttplib()
    if connected:
        break
    else:
        print(f'trying to connect to {wifi_ssid}...')
        subprocess.run(["netsh", "wlan", "connect", f"ssid={wifi_ssid}", f"name={wifi_profile}"], check=True)
        time.sleep(2)




# Replace "your_wifi_ssid" and "your_wifi_password" with your actual wifi details
    



