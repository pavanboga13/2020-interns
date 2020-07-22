import json
from dateutil import parser
import matplotlib.pyplot as plt 

with open('data.json') as file:
    data = json.load(file)    
time1=parser.parse('2019-01-01')
time2=parser.parse('2019-01-31')
dates=[]
price1 = []
price2 = []
for i in data['rates']:
    time3 = parser.parse(i)
    if time3 <= time2 and time3 >= time1:
        dates.append(i)
        price1.append(data['rates'][i]['INR'])
        price2.append(data['rates'][i]['GBP'])
map_data=list(zip(dates,price1,price2))
result = sorted(map_data, key = lambda x: x[0])
dates, price1, price2 = zip(*result)
plt.figure(figsize=(10,9))
plt.plot(dates,price1, color='red', label='INR')
plt.plot(dates,price2, color='green', label='GBP')
plt.xlabel('Dates In Jan 2019')
plt.xticks(rotation=55)
plt.ylabel('Rates Of JAN 2019')
plt.title('Exchange Rate Of INR AND GBP Against EUR')
plt.legend()
plt.show()