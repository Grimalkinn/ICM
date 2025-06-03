import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0.0,5.0,0.2)
plt.plot(t,t,'r-',t,t**3,'bs',t,t**2,'g^')

plt.show()