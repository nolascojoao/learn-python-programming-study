# Local versus Global

# We define a function, called local
def local():
    m = 7
    print(m)

# We define m within the global scope
m = 5

# We call, or 'execute' the function local
local()
print(m)
