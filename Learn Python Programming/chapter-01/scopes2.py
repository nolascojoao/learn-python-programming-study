# Local versusl Global

def local():
    # m doesn't belong to the scopre defined by the local funcion
    # so Python will keep looking into the next enclosing scopre.
    # m is finally found in the global scopre
    print(m, 'printing from the local scopre')

m = 5
print(m, 'printing from the global scopre')
local()
