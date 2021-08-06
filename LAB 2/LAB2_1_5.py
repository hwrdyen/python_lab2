import math
def unit_vector(v):
    ''' Fill in docstring
    '''
    variable_control = 0
    total1 = 0
    numerator = 0
    vector = []
    if (v != []):
        for i in v:
            first_v = (v[variable_control])**2
            variable_control += 1
            total1 += first_v
        abs_v = math.sqrt(total1)
        for j in range(0,len(v)):
                numerator = v[j]
                a = numerator/abs_v
                vector.append(a)
        return vector
    else:
        return []        
        
if __name__ == "__main__":
    o = unit_vector([2,1])
    print(o)
    p = unit_vector([])
    print(p)
