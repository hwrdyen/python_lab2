from LAB2_3_1 import*
from LAB2_2_2 import*

def check_bit_add(four_bit_num1, four_bit_num2, result):
    ''' Fill in docstring
    '''
    q = add_two_bin_nums(four_bit_num1,four_bit_num2)
    w = error_indices(q, result)
    return w
    

if __name__ == "__main__":
    z = check_bit_add([1,0,1,0],[0,1,0,1],[1,1,1,1])
    print(z)
    x = check_bit_add([1,0,1,0],[0,1,0,1],[0,1,0,1])
    print(x)
    c = check_bit_add([1,1,1,1],[1,1,1,1],[1,1,1,0])
    print(c)
