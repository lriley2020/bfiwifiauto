## biwifiauto

I made this script whilst on a Britanny Ferries ferry from Portsmoth, UK to Santander, Spain!

I ran this on a Raspberry Pi 3b, powered off a powerbank.

`main.py` uses Selenium to complete the captive portal that users have to fill in before using the Britanny Ferries free wifi

`ferry_mac_cron.sh` is intended to be triggered every half an hour by a cron job. It brings the WLAN interface down, randomises the wlan0 MAC address, brings the interface back up, and runs `main.py `

Note: the randomised MAC address is needed in order to make raspberry pi appear to be a new client (therefore bypassing the 30 minute limit)

If these two scripts are paired with a second WLAN interface and configured to create a Wifi extender like [here](https://pimylifeup.com/raspberry-pi-wifi-extender/), the result is a free Wifi hotspot that all of your devices can connect to, without being limited to 30 minutes or having to complete a captive portal.

Enjoy! :)
