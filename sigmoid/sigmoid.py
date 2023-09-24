import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x: (float)) -> float:
    '''This is a sigmoid (1 / (1 + e^-x)) approximation function 
    that uses the Taylor expansion to solve the sigmoid equation. 
    The purpose of this function is to find a simpler solution 
    that can be easily ported to an FPGA. 
    Inputs: x == exponential power [float], iters == number of 
    iterations of the Taylor expansion; Output: sum == summation 
    of the Taylor expansion'''

    ## Summation code ##
    if x <= -5.5:
        sum = 0
    elif (x > -5.5) and (x <= -1.5):
        sum = 0.571859 + (0.392773*x) + (0.108706 * (x**2)) + (0.014222 * (x**3)) + (0.000734 * (x**4))
    elif (x > -1.5) and (x < 1.5): # Commented out the last 3 indexes because percent error barely changes after the 6th index
        sum = (1/2) + (x/4) - ((x**3)/48) + ((x**5)/480) - ((x**7)/2688) + ((x**9)/10368) #- ((x**11)/ 248832) + ((x**13)/39739392) - ((x**15)/4479180)
    elif (x >= 1.5) and (x < 5.5):
        sum = 0.428141 + (0.392773*x) - (0.108706 * (x**2)) + (0.014222 * (x**3)) - (0.000734 * (x**4))
    else:
        sum = 1

    return sum

# First test of sigmoid (Checking a single point)
x     = 1
x     = (2 * x) - 1
iters = 10
sig_real = 1 / (1 + np.exp(-x))
sig_appr = sigmoid(x)
print('sig_real = {}'.format(sig_real))
print('sig_appr = {}'.format(sig_appr))

# Second test of sigmoid (Checking multiple points)
max_diff = 0
cur_diff = 0
for i in np.arange(-1, 1, 0.00001):
    sig_real = 1 / (1 + np.exp(-i))
    sig_appr = sigmoid(i)
    cur_diff = np.abs(sig_real - sig_appr) # Check biggest diff and return max error
    if max_diff < cur_diff:
        max_diff = cur_diff
# Print max percent error
print(max_diff * 100)

## Matplotlib Plot of Sigmoid
x = np.linspace(-10, 10, 100)
y = [sigmoid(x[i]) for i in range(100)]
plt.plot(x, y)
plt.title('Sigmoid Function')
plt.xlabel('x')
plt.ylabel('σ(x)')
plt.grid(True)
plt.show()
