import math
def vector_projection(v,w):
    ''' Fill in docstring
    '''
    total1 = 0
    total2 = 0
    vector = []
    for i in range(0,len(v)):
        dot_product = (v[i]) * (w[i])
        total1 += dot_product
        first_v = (v[i])**2
        total2 += first_v
    q = (total1)/(total2)
    print(q)
    for j in range(0,len(v)):
        h = (v[j])* q
        vector.append(h)
    return vector

if __name__ == "__main__":
    z = vector_projection([-2],[1.5])
    print(z)
    x = vector_projection([0,3],[1.5,2])
    print(x)
