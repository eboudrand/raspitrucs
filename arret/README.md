# Bouton d'arrêt

## Câblage du bouton poussoir 4 points
- brancher la borne + sur le PIN 2
- brancher la borne - sur le PIN 39
- brancher la borne LED - sur le PIN 9 (GROUND)
- brancher la borne LED + sur le PIN 7 (GPIO 4)

## Scripts
- copier bouton_arret.py dans /etc/scripts (répertoire à créer)
- ajouter dans /etc/rc.local la ligne ```python3 /etc/scripts/bouton_arret.py &```

Le script bouton_arret.py utilise [lcd_setup](https://github.com/eboudrand/raspitrucs/blob/master/lcd/lcd_setup). Vérifier sa présence dans /usr/local/bin
