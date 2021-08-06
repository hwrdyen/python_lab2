def error_indices(packet1, packet2):
    ''' Fill in docstring
    '''
    vector = []
    for i in range(0,len(packet1)):
        if packet1[i] != packet2[i]:
            vector.append(i)
    return vector

if __name__ == "__main__":
    e = error_indices([0,1,1,1],[1,1,0,1])
    print(e)
    r = error_indices([1,1,0,1],[1,1,0,1])
    print(r)
