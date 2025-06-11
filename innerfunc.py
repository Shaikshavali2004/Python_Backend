"""

def outer():
    print("Outer function started")
    def inner():
        print("Inner function")

    inner()
    inner()

    def login():
        print("Login success")

    login()
    login()

outer()

"""

"""

def outer():
    print("Outer function started")
    def inner():
        print("Inner function")


    def login():
        print("Login success")


outer()
inner() #NameError: name 'inner' is not defined. Did you mean: 'iter'?

"""


#How to invoke inner function from outside?

"""

def outer():
    print("Outer function started")
    def inner():
        print("Inner function")
    
    #return inner

    def login():
        print("Login success")

    return inner
    return login

inner=outer()
inner()
login=outer()
login()

"""

#output:
"""
Outer function started
Inner function
Outer function started
Inner function
"""

def outer():
    print("Outer function started")
    def inner():
        print("Inner function")
    
    

    def login():
        print("Login success")
    
    inner()
    login()
    
outer()

#Output:
"""
Outer function started
Inner function
Login success
"""