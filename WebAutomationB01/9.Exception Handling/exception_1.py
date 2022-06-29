'''
Exceptions are error.
we should handle exception in our code.
'''

'''
def exception_handling():
    a = 10
    b = 20
    c = 0
    d = (a + b) / c
    print(d)


exception_handling()
'''

def exception_handling_tryExcept():
    try:
        a = 10
        b = 20
        c = 10
        d = (a + b) / c
        print(d)

    except:
        print('We are in except block')

exception_handling_tryExcept()