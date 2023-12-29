import config
import re
import random

def update_garage(plate):
    plate = plate.upper()
    mycursor = config.db.cursor()
    vehicule_name_query="SELECT vehicle FROM player_vehicles WHERE plate = (%s)"
    mycursor.execute(vehicule_name_query,(plate,))
    for row in mycursor.fetchall():
        vehicle_name = re.sub('[0-9]', '', row[0])

    try:
        vehicle_name
    except:
        return 'Le véhicule n\'existe pas'
    else:
        garage_update_query="UPDATE player_vehicles SET garage = 'pillboxgarage' WHERE plate = (%s)"
        mycursor.execute(garage_update_query,(plate,))
        config.db.commit()
        return(f"Le vehicule {vehicle_name} {plate} a été déplacé à la fourrière")