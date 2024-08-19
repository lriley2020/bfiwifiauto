echo "Setting wlan0 to down..."
ip link set wlan0 down
macchanger -r  wlan0
echo "Setting wlan0 to up..."
ip link set wlan0 up
echo "Done..."
## Delay to allow network to connect ##
sleep 10
echo "Running captive portal script..."
/home/pi/bfwifiauto/main.py
