import math
def angle_between(v, w):
    ''' Fill in docstring
    '''
    variable_control = 0
    total1 = 0
    total2 = 0
    total3 = 0
    
    for i in v:
        dot_product = (v[variable_control])*(w[variable_control])
        first_v = (v[variable_control])**2
        first_w = (w[variable_control])**2
        variable_control += 1
        total1 += dot_product
        total2 += first_v
        total3 += first_w
    abs_v = math.sqrt(total2)
    abs_w = math.sqrt(total3)
    denominator = abs_v * abs_w
    value = (total1)/denominator
    radiance = math.acos(total1/denominator)
    angle = 180 * radiance / math.pi
    return angle
        

if __name__ == "__main__":
    r = angle_between([-1],[2])
    print(r)
    t = angle_between([0,1,0,1], [1,3,4,5])
    print(t)
