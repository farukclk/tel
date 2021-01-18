read -p "mac address: " mac
read -p "cap file   : " cap

python3 set.py | aircrack-ng -w - -b $mac $cap

