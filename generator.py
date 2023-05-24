# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)

"""
C:\Users\mgobea\Documents\develop\Python\crud_python
(venv) λ py generator.py
This is printed first
1
This is printed second
2
This is printed at last
3
"""