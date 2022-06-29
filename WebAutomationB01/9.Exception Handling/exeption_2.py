def exception_handling_tryEachFinally():
    try:
        a = 10
        b = 20
        c = 0
        d = (a + b) / c
        print(d)

    except:
        print('We are in except block')
    else:
        print('No exception,We are in Else block.')
    finally:
        print('Finally always executed.')


exception_handling_tryEachFinally()
