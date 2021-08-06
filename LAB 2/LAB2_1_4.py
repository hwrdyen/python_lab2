import math
def dot_product(v,w):
    ''' Fill in docstring
    '''
    dot_product = 0
    for variable in range(0, len(v)):
        dot_product += (v[variable] * w[variable])
    return dot_product
        
if __name__ == "__main__":
    y = dot_product([-1],[2])
    print(y)
    u = dot_product([0,1,0,1],[1,3,4,5])
    print(u)
    i = dot_product([0,0],[0,0])
    print(i)
