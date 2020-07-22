import matplotlib.pyplot as put 
from dateutil import parser
import json
with open('data.json') as file:
    data = json.load(file)   
time1=parser.parse('2019-01-01')
time2=parser.parse('2019-01-31')
dates=[]
price=[]
for i in data['rates']:
    time3 = parser.parse(i)
    if time3 <= time2 and time3 >= time1:
        dates.append(i)
        price.append(data['rates'][i]['INR'])

map_data=list(zip(dates,price))
result = sorted(map_data, key = lambda x: x[0])
dates,price = zip(*result)
put.figure(figsize=(10,9))
put.plot(dates, price, color='red', linestyle='dashed', linewidth='0.5')
put.scatter(dates, price, label='stars', color='green', marker='*', s=100)
put.xlabel('Dates')
put.xticks(rotation=55)
put.ylabel('RATES OF JAN 2019')
put.title('EXCHANGE RATE OF INR AGAINST EUR')
put.show()