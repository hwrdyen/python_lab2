def packet_diff(packet1, packet2):
    ''' Fill in docstring
    '''
    vector = []
    for i in range(0,len(packet1)):
        if packet1[i] != packet2[i]:
            vector.append(i)
        k = len(vector)
    return k

if __name__ == "__main__":
    z = packet_diff([0,1,0,1],[1,1,0,1])
    print(z)
    x = packet_diff([0,1,1,0],[0,1,1,0])
    print(x)
