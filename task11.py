with open('04.txt', 'r') as file:
    data=file.readlines()
    integ=[]
    for x in data:

        l=len(x)
        s=x
        integ = []
        i = 0
        while i < l:
            s_int = ''
            a = s[i]
            while '0' <= a <= '9':
                s_int += a
                i += 1
                if i < l:
                    a = s[i]
                else:
                    break
            i += 1
            if s_int != '':
                integ.append(int(s_int))
        
        l = [str(integer) for integer in integ]
        a_string = "".join(l)
        num=int(a_string)
        #print(num)
        #print(data)
        alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        shift= num%26
        
        size=len(x)
        x=''.join([str(elem) for elem in x])
        new_data=x[:size-8]
        #print(new_data)
        
        shifr=new_data.replace('-', ' ')
        #print(shifr

        message = shifr.upper()
        itog = ''

        for i in message:
                mesto = alfavit.find(i)
                new_mesto = mesto + shift
                if i in alfavit:
                    itog += alfavit[new_mesto]
                else:
                    itog += i

        if 'NORTHPOLE OBJECT STORAGE' in itog:
            print(itog)
    