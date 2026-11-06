import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	a = np.array(a)
	m = a.shape[0]
	n = a.shape[1]
	if m * n != new_shape[0] * new_shape[1]:
		return []
	return np.reshape(a, new_shape).tolist()
