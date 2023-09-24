# from binary_fractions import Binary
import numpy as np

def exp_func (x: float, iters: int) -> float:
   sum  = 1
   fact = 1
   
   for k in range(1, iters):
      fact = fact * k
      sum  = sum + ((x ** k) / (fact))

   return sum


def exp_approx(x: float) -> float:
   """
   This is a sigmoid approximation function where we iterate
   up to only 10 times. This function is written in a way that
   will be easily portable to FPGA code (hence the 'cycle' comments)
   Input: x == the input power of e^x (float); Output: sum == 
   fixed (float in this case) point return value (float)"""

   # Create 1/fact Vector
   fact = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
   fact = [1/fact[i] for i in range(9)]

   # Create x -> x^9 values
   # Cycle 1
   x_vect    = [None] * 10
   x_vect[0] = 1 # When k = 0
   x_vect[1] = x
   x_vect[2] = x_vect[1] * x_vect[1]
   x_vect[3] = x_vect[1] * x_vect[1] * x_vect[1]

   # Cycle 2
   x_vect[4] = x_vect[3] * x_vect[1]
   x_vect[5] = x_vect[3] * x_vect[2]
   x_vect[6] = x_vect[3] * x_vect[3]

   # Cycle 3
   x_vect[7] = x_vect[6] * x_vect[1]
   x_vect[8] = x_vect[6] * x_vect[2]
   x_vect[9] = x_vect[6] * x_vect[3]

   # Mult each x -> x^9 by 1/fact
   # Cycle 4
   k_ind = [x_vect[i+1] * fact[i] for i in range(9)]

   # Summation
   sum = 1
   for i in range(9):
      sum = sum + k_ind[i]

   return sum

## Test approximation function
## Calculate max difference between num_pts
## diff pts from 0 to 1
num_pts = int(1e+6)
e_diff = [None] * num_pts
min    = -1
max    = 1
step   = (max - min) / num_pts
chkpt  = num_pts / 10

i   = 0
chk = 0
for k in np.arange(min, max, step):
   e_real    = np.exp(k)
   e_appr    = exp_approx(k)
   e_diff[i] = (e_real-e_appr) / e_real
   i = i + 1
   if i%(chkpt) == 0:
      print('Current iteration: {}'.format(chk))
      chk = chk + chkpt

max_val  = np.max(e_diff) * 100
print('Percent difference of max: {}'.format(max_val))
