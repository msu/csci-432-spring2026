import matplotlib.pyplot as plt
import numpy as np

# 1. Generate 100 points between -5 and 5
x = np.linspace(0,1,2)

# 2. Define the function y = x^2
ysabt = np.array([7,12])
yscbt = np.array([12,7])
ysct = np.array([8,9])
yscdt = np.array([13,7])

# 3. Create the plot
plt.plot(x, ysabt, label=' ', color='blue', linestyle='-')
plt.plot(x, yscbt, label=' ', color='purple', linestyle='--')
plt.plot(x, ysct, label=' ', color='brown', linestyle='-.')
plt.plot(x, yscdt, label=' ', color='green', linestyle=':')

# 4. Add labels and title
plt.xlabel("parameter (t)")
plt.ylabel("path length")
plt.legend()

# 5. Display the result
plt.show()
