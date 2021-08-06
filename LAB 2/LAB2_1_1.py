import math
def vector_from_points(p1, p2):
    ''' Fill in docstring
    '''
    if (p1 != []) and (p2 != []):
        variable_control = 0
        vector = []
        for i in p1:
            distance_p1p2 = p2[variable_control] - p1[variable_control]
            variable_control +=1
            vector.append(distance_p1p2)
        return vector
    else:
        return []

if __name__ == "__main__":
    # test your vector operations here
    v1 = [0, -2, 3]
    v2 = [1, 1, 1]
    k = vector_from_points([0,0],[1,2])
    print(k)
    z = vector_from_points([3,-1,0],[10,0,1])
    print(z)

    test = vector_from_points([1,1,2],[])
    print(test)
