def UFO(N, data, octal):
    data1= []
    for el in data:
        el = str(el)
        if octal:
            el = int(el, 8)
        else:
            el = int(el, 16)
        data1.append(el)
    return data1
        
