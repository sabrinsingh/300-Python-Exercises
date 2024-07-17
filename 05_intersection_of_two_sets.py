a= {1,2,3}
b= {1,3,4}



# Using the intersection() method
c = a.intersection(b)
print(c)  # Output: {1, 3}

# Using the & operator (which also performs union)
d = a & b
print(d)  # Output: {1, 3}