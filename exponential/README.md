# Exponential Approximation Function
### Created in Python and SystemVerilog

This is a exponential approximation function that was initially planned for use in Logistic Regression with fixed point math. To create this function in SystemVerilog, I used the exponential expansion, which is commonly found [online](https://en.wikipedia.org/wiki/Exponential_function).

$e^x \approx 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \ldots = \sum_{n=0}^{\infty} \frac{x^n}{n!}$

To create this function in SystemVerilog, I "simulated" how it would work by first writting it in python. Essentially, the logic data path/algorithm will perform similar to the python script. I created parameters to change the amount of iterations of the expansion as well as the data width of the function.
As noted, this was planned to be used for sigmoid approximation, but became too complex as I would have to implement fixed point division, meaning a lot of latency through the data path. This implementation may be explored again in future research.
