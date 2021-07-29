
API_key = ''

import requests
import datetime as dt

# город Калуга
try:
    req = 'https://api.openweathermap.org/data/2.5/forecast?id=553915&appid=503407cdb3f1e7f1fe0678dd6ea3689c'
    response = requests.get(req)
    data = response.json()
    max_pressure = 0
    min_delta_temp = 100
    current_date = dt.datetime.today()
    night = 0
    for i in data['list']:
        max_pressure = max(max_pressure, i['main']['pressure'])

        if i['dt_txt'].split()[1] == '00:00:00':
            night = float(i['main']['temp_max'])
        if i['dt_txt'].split()[1] == '09:00:00' and night != 0:
            morn = float(i['main']['temp_max'])
            if abs(morn - night) < min_delta_temp:
                min_delta_temp = abs(morn - night)
                current_date = i['dt_txt'].split()[0]
    print('Парсинг предстоящей погоды для города Калуга:')
    print(f'Максимальное давление за предстоящие 5 дней (включая текущий): {max_pressure}')
    print(
        f'День с минимальной разницей между ночной и утренней температурой ({round(min_delta_temp)} градуса Цельсия) - это {current_date}')
except Exception as e:
    print("Exception (forecast):", e)
    pass
