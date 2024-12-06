import numpy as np

print(np.arange(0, 10))

print(np.zeros(5))

print(np.zeros((4,6)))


print(np.ones(4)* 100)


print(np.linspace(0, 10, 60))


print(np.random.rand(5)) # Standar norml distribution

print(np.random.randint(5))

arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr_2d)
print(arr_2d.sum(axis=1))
