from prophet import Prophet
from pandas import read_csv, to_datetime
from matplotlib import pyplot

filepath='test.csv'

df = read_csv(filepath)
df.columns = ['ds', 'y']
df['ds'] = to_datetime(df.ds, format='%Y-%m-%d')
    
pyplot.figure(figsize = (16, 9))
pyplot.plot(df.ds, df.y)
pyplot.show()

model = Prophet(interval_width=0.95, yearly_seasonality=True)
model.fit(df)

future = m.make_future_dataframe(periods=50, freq='MS')
forecast = m.predict(future)
preds = forecast['yhat'][:-50]

pyplot.figure(figsize=(15, 6))
pyplot.plot(df.ds, preds, color='red', label='Predictions')
pyplot.plot(df.ds, df.y, color='blue',label='Actual')
pyplot.legend()
pyplot.show()

figure = m.plot(forecast, xlabel='Date', ylabel='Price')
figure.set_size_inches(15, 6)
model.plot_components(forecast)
