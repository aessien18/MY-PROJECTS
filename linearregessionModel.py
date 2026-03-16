X = [[98,65,95],
     [67,17,95], 
     [78,82,85], 
     [90,95,48],
     [88,90,92]
     ]
y = [92, 12, 80, 67, 85]

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)
mse = mean_squared_error(y, predictions)
print("Predictions:", predictions)
print("Mean Squared Error:", mse)
