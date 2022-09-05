import pandas as pd
india_weather = pd.DataFrame({
       'city':['mumbai','delhi','banglore'],
       'temp':[32,45,30],
       'humidity':[80,60,78]
       })

india_weather

us_weather =  pd.DataFrame({
       'city':['new york','chicago','oriando'],
       'temp':[21,14,35],
       'humidity':[68,65,75]
       })

us_weather

df = pd.concat([india_weather,us_weather])
df

df = pd.concat([india_weather,us_weather],ignore_index = True)
df


us_weather
us_weather['temp'][us_weather['city']] = int([us_weather['temp'].mean()])

us_weather['city'][us_weather['temp']==(us_weather['temp'].mean())]---to find average 

df = pd.concat([india_weather,us_weather],keys=['india','us']) ---- keys

us_weather['temp'].mean()                 average finding
us_weather['humidity'].mean() 

df[['city','temp','humidity']] [df['city']=='mumbai']--------simple query

df = pd.concat([india_weather,us_weather],axis=1)------horizontal joins with same index