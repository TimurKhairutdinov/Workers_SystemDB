import json
import control as c
import menu as mn

status = True
while status != False:
    mn.menu_user()
    status = mn.stop_prog()