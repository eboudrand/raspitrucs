# Affichage de l'adresse IP sur un LCD 2 lignes

- Installer pip3 : sudo apt-get install python3-pip
- Installer la librairie "board" : sudo pip3 install adafruit-blinka
- Installer la librairie "adafruit_character_lcd.character_lcd" : sudo pip3 install adafruit-circuitpython-charlcd
- Copier lcd_setup dans /usr/local/bin
- changer les droits d'exécution de lcd_setup : sudo chmod +x /usr/local/bin/lcd_setup
- copier 60-lcd dans /lib/dhcpcd/dhcpcd-hooks/
