import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(1,2000,2000)

y1 = [0.6 * math.sin(3 * value * math.pi/1000) for value in x]
y2 = [-0.6 * math.sin(1.8 * value * math.pi/1000) for value in x]
print("y1", y1)
print("y2", y2)
# sin_joint1 = 0.6 * sin(3*M_PI*sin_count/1000.0)
# sin_joint2 = -0.6 * sin(1.8*M_PI*sin_count/1000.0)

plt.figure()
plt.plot(x,y1, color='orange', linewidth=1.0, linestyle='--')
plt.plot(x,y2,color='red',linewidth=1.0,linestyle='--')

plt.show()







