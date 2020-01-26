user_input = ['']

def ui_and_check(user_input):
    while True:
        try:
            n = int(input("enter a number..."))
        except ValueError:
            print('not an integer')
            continue
        else:
            if n >= 100 or n <= 0:
                print('number is out of range')
                continue
            print(str(n)+' is an integer')
            user_input[0]=n
            break
    # return user_input


ui_and_check(user_input)

print(user_input[0])