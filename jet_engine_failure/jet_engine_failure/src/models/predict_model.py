
X = result[['sensor2', 'sensor3', 'sensor7', 'sensor14',
       'sensor16']]
X = sm.add_constant(X)
y = result[['FailureCycle']]
model = sm.OLS(y, X)
results = model.fit()
print(results.summary2())