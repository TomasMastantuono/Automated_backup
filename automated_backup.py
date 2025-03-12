from datetime import datetime
from time import sleep
import shutil
import os.path

def dt(date1:dir, date2:dir):
    """
    date1: referencia a la fecha mas antigua
    date2: referencia a la fecha mas actual
    """
    dyear = float(date2['year']) - float(date1['year'])
    dmonth = float(date2['month']) - float(date1['month'])
    dday = float(date2['day']) - float(date1['day'])
    dhour = float(date2['hour']) - float(date1['hour'])
    dminute = float(date2['minute']) - float(date1['minute'])
    dseconds = float(date2['seconds']) - float(date1['seconds'])
    
    return abs(dyear), abs(dmonth), abs(dday), abs(dhour), abs(dminute), abs(dseconds)


def copyfolder(dir1:str, dir2:str):
    
    """
    dir1: dirección cuyos archivos se quieren copiar
    dir2: dirreción a la cual se quieren pegar los archivos
    """
    
    try:
        shutil.copytree(dir1, dir2, dirs_exist_ok = True)
    except Exception as e:
        print(f'Error: {e}')


def last_modification(dir:str):
    date = os.path.getmtime(dir)
    total_date = str(datetime.fromtimestamp(date))
    
    last_date = {
        'year': total_date[:4],
        'month': total_date[5:7],
        'day': total_date[8:10],
        'hour': total_date[11:13],
        'minute': total_date[14:16],
        'seconds': total_date[17:]
    }
    return last_date
    

# Ubicaciones de las carpetas
dir1 = 'fold1'
dir2 = 'fold1_copy'

# Último backup realizado
try:

    Ldate = last_modification(dir2)

except Exception as e:

    print(f'Error: {e} \n La carpeta no existía')

    Ldate = {
        'year': 0,
        'month': 0,
        'day': 0,
        'hour': 0,
        'minute': 0,
        'seconds': 0
    }

while True:
    Adate = datetime.today().strftime('%Y-%m-%d  %H:%M:%S')

    today = {
        'year': Adate[:4],
        'month': Adate[5:7],
        'day': Adate[8:10],
        'hour': Adate[12:14],
        'minute': Adate[15:17],
        'seconds': Adate[18:]
    }

    dyears, dmonths, ddays, dhours, dminutes, dseconds = dt(Ldate, today)
    
    # Solo realizo un backup cada cambio de mes
    if dmonths != 0:
        copyfolder(dir1, dir2)
        Ldate = today
        print('Se realizó una copia con éxito')
        sleep(24*60*60) # Realiza verificaciones todos los días
    else:
        print(f'Vuelvo a probar en 1 minuto, la carpeta tuvo como última modificación \n {Ldate}')
        sleep(24*60*60) # Realiza verificaciones todos los días
