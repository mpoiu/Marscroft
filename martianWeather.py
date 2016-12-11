import requests


class MarsWeather:
    def __init__(self):
        self.data = requests.get("http://marsweather.ingenology.com/v1/latest/").json()['report']
        self.data['wind_direction'] = self.float_or_none(self.data['wind_direction'])

    @staticmethod
    def float_or_none(val):
        try:
            return float(val)
        except ValueError:
            return None

    @staticmethod
    def value_or_empty(val):
        if val != None:
            return val
        else:
            return ''

    def getPressure(self):
        return self.data['pressure']

    def getPressureString(self):
        return self.data['pressure_string']

    def getWindSpeed(self):
        return self.data['wind_speed']

    def getMinTemp(self):
        return self.data['min_temp']

    def getMaxTemp(self):
        return self.data['max_temp']
