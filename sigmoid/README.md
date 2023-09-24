# Sigmoid Approximation Function
### Created in Python and SystemVerilog

This is a sigmoid approximation function that will be used for Logistic Regression with fixed point math. The sigmoid taylor approximation in python was found in the [hyperlinked literature](https://www.researchgate.net/publication/281806053_An_application_of_multilayer_neural_network_on_hepatitis_disease_diagnosis_using_approximations_of_sigmoid_activation_function#pf5), which tests this approxiation.

As noted in the literature, the sigmoid function can be approximated as follows:

$\text{{Taylor Approximation for range }} (-1.5 < x < 1.5) = \frac{1}{2} + \frac{x}{4} - \frac{x^3}{48} + \frac{x^5}{480}$


We note that the range of approximation is only from -1.5 to 1.5. This is useful for Logistic Regression, as the input values to the sigmoid function will only be from 0 to 1. Since the original sigmoid function has the center at 0 where the amplitude = 0.5, I have done some scaling so the x range can work from 0 to 1 with the center at 0.5, rather than the previous range of -1 to 1.
Also, since the range we are working in only requires -1.5 to 1.5, I will not implement the full sigmoid approximation function as it would be redundant in hardware, but I will leave that implementation complete in python.

Another good note is that the max percent error (that I am calculating in my python script) is about 0.85% MAX for this range. Though this is not ideal, this percent error lies at the boundaries of 0 to 1, so most actual calculations will have a much lower percent error.
