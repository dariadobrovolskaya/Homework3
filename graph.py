import matplotlib.pyplot as pyplot
import numpy as np
import random
#создаю поле
pyplot.figure(figsize = (15, 10))
pyplot.grid(1)

n = 100


x = np.arange(n)
y = np.arange(n)

y[0] = 50
#ввожу рандомные точки, создаю первый график
for i in range(n - 1):
    y[i + 1] = y[i] + random.randint(-3,3)

pyplot.plot(x, y, color = '#C9C0FC', linewidth = 3)


#создаю второй график, усредняющий значения первого - цвет делаю темнее
x_average = np.arange(n // 4)
y_average = np.arange(n // 4)

for i in range(n // 4):
    y_average[i] = (y[4 * i] + y[4 * i + 1] + y[4 * i + 2] + y[4 * i + 3]) // 4
    x_average[i] *= 4

x_average[-1] = x[-1]
y_average[-1] = y[-1]

pyplot.plot(x_average, y_average, color = '#122FAA', linewidth = 3)
#дела. эту странную точку в крайней точке графика
pyplot.scatter(x[-1], y[-1], color = '#122FAA', linewidth = 10)

pyplot.show()
