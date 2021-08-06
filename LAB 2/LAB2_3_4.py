def get_error_source(four_bit_num1, four_bit_num2, result):
    ''' Fill in docstring
    '''
    vector = []
    total1 = 0
    total2 = 0
    for i in range(0,len(four_bit_num1)):
        first_sum = (four_bit_num1[i]*(2**(3-i)))
        second_sum = (four_bit_num2[i]*(2**(3-i)))
        total1 = total1 + first_sum
        total2 = total2 + second_sum
    sum_v = total1 + total2
    condition = True
    while condition :
        result1 = sum_v%2
        result2 = int(result1)
        vector.append(result2)
        k = (sum_v-result1)
        sum_v = (k)/2
        if k == 0:
            condition = False
    vector.reverse()
    if len(vector) == 1:
        vector.extend([0,0,0])
    elif len(vector) == 2:
        vector.extend([0,0])
    elif len(vector) == 3:
        vector.extend([0])
        
    if len(vector) == len(result):
        return 0
    else:
        result.reverse()
        vector.reverse()
        for j in range(0,len(result)):
            if result[i] == vector[i]:
                return 1
            else:
                return 2

if __name__ == "__main__":
    t = get_error_source([0,0,0,0],[0,0,0,0],[0,0,0,0])
    print(t)
    y = get_error_source([1,0,0,1],[1,0,0,1],[0,0,1,0])
    print(y)
    u = get_error_source([1,0,0,1],[1,0,0,1],[1,0,1,0])
    print(u)
