'''
Using NumPy create random vector of size 20 having only float in the range 1-20.
Then reshape the array to 4 by 5
Then replace the max in each row by 0 (axis=1) (you can NOT implement it via for loop)
Evaluation
'''

# Import the NumPy library and alias it as 'np' for brevity and convention.
import numpy as np

# Create a random vector of size 20 with floats in the range 1-20
v1 = np.random.uniform(1, 20, 20)

print("Original Random Vector:\n", v1)
print()

# Reshape the array to 4 by 5 (4 rows and 5 columns)
reshapedArray = v1.reshape(4, 5)

print("Reshaped array ro 4 by 5 :\n", reshapedArray)
print()

# Replace the max in each row by 0 (axis=1)
reshapedArray[np.arange(4), reshapedArray.argmax(axis=1)] = 0

print("Reshaped Array:\n", reshapedArray)