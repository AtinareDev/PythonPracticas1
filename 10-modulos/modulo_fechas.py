import locale
import datetime

# Configurar el idioma a español (dependiendo de tu sistema operativo, podrías necesitar 'es_ES.UTF-8'')
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


print(datetime.date.today())
fecha_completa = datetime.datetime.now()

print(fecha_completa.month)
print(fecha_completa.day)


# Formatear fechas
# %Y Año
# %m Mes    %B Nombre del mes
# %d Día
# %H Hora
# %M Minutos
# %S Segundos

fecha_personalizada = fecha_completa.strftime('%d-%m-%Y')
print(fecha_personalizada)
fecha_personalizada = fecha_completa.strftime('%d-%B-%Y')
print(fecha_personalizada)
