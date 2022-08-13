# --------------------------
# visualization 1/f Chaos movement
# --------------------------

import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#initialization
k = 250
k = int(k) + 1
x = random.random()
chaos = []
chaosy =[]

for i in range(1,k):
    
    y = x
    chaosy.append(y)
    
    if 0.05 <= x < 0.5:
        x = x + 2*x*x
    elif 0.5 <= x < 0.95:
        x = x - 2*(1-x)*(1-x)
    else:
        x = random.random()
    
    chaos.append(x)

#print(chaos)

# visualize
# create dataframe 
df1 = pd.DataFrame(chaos)    
df2 = pd.DataFrame(chaosy,chaos)
pd.set_option('display.max_rows', 1000)
print(df2)

# visualize - set figure
fig, ax = plt.subplots(ncols=2, tight_layout=True, figsize=(10,5))

ax[0].plot(df1, color='dodgerblue',label = r'$1/f$')
ax[0].legend()
ax[0].set_title(label='Chaos Time Line')
ax[0].set_xlabel('t')
ax[0].set_ylabel('f(t)')

ax[1].plot(df2,':', color='mediumseagreen',label = r'$1/f$')
ax[1].set_title(label='Chaos Locus')
ax[1].legend()
ax[1].set_xlabel('x')
ax[1].set_ylabel('f(x)')
ax[1].text(0,1.4,r'$f_1(x) = x + 2x^2 \quad (0.05 \leqq x < 0.5)$')
ax[1].text(0,1.3,r'$f_2(x) = x - 2(1-x)^2 \quad (0.5 \leqq x < 0.95)$')

x = np.linspace(0,1)

y1 = x + 2*x*x
y2 = x - 2*(1-x)*(1-x)
y3 = x
ax[1].set_ylim(-0.5, 1.5)

ax[1].plot(x,y1)
ax[1].plot(x,y2)
ax[1].plot(x,y3, color = 'tomato')

plt.savefig('Chaos Locus '+str(i)+'.png',dpi=300)

plt.show()
