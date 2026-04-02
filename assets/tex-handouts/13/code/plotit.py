import matplotlib.pyplot as plt
import numpy as np

# 1. Generate 100 points between -5 and 5
x = np.linspace(0,1,2)

# 2. Define the function y = x^2
ysat = np.array([7,17])
ysabct = np.array([20,8])
ysadt = np.array([6,15])
ysbt = np.array([17,10])

# 3. Create the plot
plt.plot(x, ysat, label='sat', color='blue', linestyle='-')
plt.plot(x, ysabct, label='sbcdt', color='purple', linestyle='--')
plt.plot(x, ysadt, label='sadt', color='brown', linestyle='-.')
plt.plot(x, ysbt, label='sbcdt', color='green', linestyle=':')

# 4. Add labels and title
plt.xlabel("parameter (t)")
plt.ylabel("path length")
plt.legend()

# 5. Display the result
plt.show()
