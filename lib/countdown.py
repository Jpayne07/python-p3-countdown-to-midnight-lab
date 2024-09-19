import time

def countdown(int):
    while int > 0:
        print (f'{int} SECOND(S)!')
        int -= 1
    print('HAPPY NEW YEAR!')
    return None

def countdown_with_sleep(int):
    while int > 0:
        print (f'{int} SECOND(S)!')
        int -= 1
        time.sleep(1)
    print('HAPPY NEW YEAR!')
    return None

countdown_with_sleep(10)

