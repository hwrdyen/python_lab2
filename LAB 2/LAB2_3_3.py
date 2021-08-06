def check_dec_add(four_bit_num1, four_bit_num2):
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
    if len(vector)>4:
        return 0
    else:
        return 1
    

if __name__ == "__main__":
    v = check_dec_add([0,0,1,1],[0,1,0,1])
    print(v)
    b = check_dec_add([1,0,0,0],[1,0,0,0])
    print(b)
