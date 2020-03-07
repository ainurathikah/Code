import numpy as np
import matplotlib.pyplot as plt

plt.title('Sine Graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
x=np.arange(0,10,0.1)
t=np.sin(x)

plt.xlim(0,10)
plt.plot(x,t,'k-')
plt.savefig('Sin.png')

plt.show()
