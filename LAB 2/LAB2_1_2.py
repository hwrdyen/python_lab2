import math
def vector_length(v):
    ''' Fill in docstring
    '''
    variable_control = 0
    total = 0
    if v != []:
        for i in v:
            root2 = (v[variable_control])**2
            variable_control += 1
            total += root2
            length = math.sqrt(total)
        return length
    else:
        return -1

if __name__ == "__main__":
    q = vector_length([2,1])
    print(q)
    w = vector_length([])
    print(w)
