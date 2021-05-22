weather = {"city": "Москва", "temperature": "20", "date": "27.05.2019"}
weather ['temperature']=int(weather ['temperature'])
weather ['temperature']= weather ['temperature'] - 5
print(weather)
print(weather.get('country'))
print(weather.get('country', 'Russia'))
print(len(weather))