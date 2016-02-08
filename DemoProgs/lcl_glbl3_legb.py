"""
LEGB exercise.  What will be printed?
"""

a_var = 'global value'

def outer():
    a_var = 'enclosed value'

    def inner():
        a_var = 'local value'
        print(a_var)

    inner()
    print(a_var)

outer()
print(a_var)
