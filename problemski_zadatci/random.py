from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np



model = LinearRegression()

N = 20
X = np.random.uniform(1,5,size=(N,2))

X = np.column_stack([X, np.sum(X, axis=1) - np.random.uniform(0,1,size=N)])

s = np.sum(X, axis=1) / 2

print(X)
print(s)
x_minus_s = s[:, np.newaxis] - X
x_minus_s_prod = np.product(x_minus_s, axis=1)
pre_sqrt = s * x_minus_s_prod
areas = np.sqrt(pre_sqrt)

y = areas