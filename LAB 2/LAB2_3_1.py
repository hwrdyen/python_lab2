def add_two_bin_nums(four_bit_num1, four_bit_num2):
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

    count = 0
    max_count = 3
    while count <= 3 :
        result1 = sum_v%2
        result2 = int(result1)
        vector.append(result2)
        k = (sum_v-result1)
        sum_v = (k)/2
        count+=1
        if count > 3:
            condition = False
    vector.reverse()
    return (vector)
        

if __name__ == "__main__":
    q = add_two_bin_nums([0,0,1,1],[0,1,0,1])
    print(q)
    w = add_two_bin_nums([0,1,1,0],[1,1,0,0])
    print(w)
    e = add_two_bin_nums([1,1,1,0],[1,1,0,0])
    print(e)
