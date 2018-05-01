# On importe le module pigpio et le module time
import pigpio
import time
import os
os.system('pigpiod')
# On instancie un objet nommé my_pi de la classe pigpio
my_pi = pigio.pi()
# On définit une constante correspondant au pin sur lequel est connecté une LED
LED_PIN = 24
# On configure le pin comme étant une sortie
# pigpio.OUTPUT est une constante définie dans le module. Elle vaut 1.
# Cette ligne peut donc également être écrite my_pi.set_mode(24, 1)
my_pi.set_mode(LED_PIN, pigpio.OUTPUT)
# On entre dans une boucle infinie qui met, toutes les secondes, alternativement à l'état haut ou à l'état bas, le pin en question.
led_state = True
while(True):
    my_pi.set(LED_PIN, led_state)
    led_state = not led_state
    time.sleep(1)