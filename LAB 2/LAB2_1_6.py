def cross_product(v,w):
    ''' Fill in docstring
    '''  
    s = []
    if len(v)==3 and len(w)==3:
        for i in range(0,len(v)):
            if i == 0:
                j,k = 1,2
                s.append(v[j]*w[k] - v[k]*w[j])
            elif i == 1:
                j,k = 2,0
                s.append(v[j]*w[k] - v[k]*w[j])
            else:
                j,k = 0,1
                s.append(v[j]*w[k] - v[k]*w[j])
        return s
    
    elif len(v) == 2 and len(w) == 3:
        for i in range(0,len(v)):
            if i ==0:
                j,k = 1,2
                s.append(v[j]*w[k] - 0*w[j])
            elif i == 1:
                j,k = 2,0
                s.append(0*w[k] - v[k]*w[j])
        j,k = 0,1
        s.append(v[j]*w[k] - v[k]*w[j])
        return s
    
    elif len(w) == 2 and len(v) == 3:
        for i in range(0,len(w)):
            if i ==0:
                j,k = 1,2
                s.append(v[j]*0 - v[k]*w[j])
            elif i == 1:
                j,k = 2,0
                s.append(v[j]*w[k] - v[k]*0)
        j,k = 0,1
        s.append(v[j]*w[k] - v[k]*w[j])
        return s
    
    elif len(v) == 2 and len(w) ==2:
        for i in range(0,len(v)):
            if i == 0:
                j,k = 1,2
                s.append(v[j]*w[k] - v[k]*w[j])
            elif i == 1:
                j,k = 2,0
                s.append(v[j]*w[k] - v[k]*w[j])
        j,k = 0,1
        s.append(v[j]*w[k] - v[k]*w[j])
        return s
    
    elif len(v) == 1 and len(w) == 3:
        for i in range(0,len(v)):
            if i == 0:
                s.append(0)
        j,k = 2,0
        s.append(0*w[k] - v[k]*w[j])
        j,k = 0,1
        s.append(v[j]*w[k] - 0*w[j])
        return s
    
    elif len(w) == 1 and len(v) ==3:
        for i in range(0,len(w)):
            if i == 0:
                j,k = 1,2
                s.append(0)
        j,k = 2,0
        s.append(v[j]*w[k] - v[k]*0)
        j,k = 0,1
        s.append(v[j]*0 - v[k]*w[j])
        return s

    elif len(v) ==1 and len(w) ==2:
        for i in range(0,len(v)):
            if i == 0:
                j,k = 1,2
                s.append(0)
        j,k = 2,0
        s.append(0)
        j,k = 0,1
        s.append(v[j]*w[k])
        return s
    elif len(v) == 1 and len(w) ==1:
        s.append(0)
        s.append(0)
        s.append(0)
        return s
    
    elif (len(v) < 1) or (len(w) <1):
        s.append(0)
        s.append(0)
        s.append(0)
        return s
    
    elif (len(v) > 3) or (len(w) > 3):
        return []
        
if __name__ == "__main__":
    a = cross_product([],[2])
    print(a)
    s = cross_product([2,8],[1,4,3])
    print(s)
    d = cross_product([1,1,1],[5.5,5.5,5.5])
    print(d)
    f = cross_product([1,1,1,0],[1,5.5])
    print(f)
    
    
    
