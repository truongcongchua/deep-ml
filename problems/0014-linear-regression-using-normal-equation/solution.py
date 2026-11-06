import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
	y = np.array(y)
	
	A = X.T @ X
	b = X.T @ y
	theta = np.linalg.solve(A, b)
	return theta