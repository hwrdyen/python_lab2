import math

def scalar_projection(v,w):
    ''' Fill in docstring
    '''
    total1 = 0
    total2 = 0
    for i in range(0,len(v)):
        dot_product = (v[i])*(w[i])
        total1 += dot_product
        first_v = (v[i])**2
        total2 += first_v
    total = math.sqrt(total2)
    q = (total1)/(total)
    return q
    
if __name__ == "__main__":
    f = scalar_projection([-2],[1.5])
    print(f)
    g = scalar_projection([0,3],[1.5,2])
    print(g)
