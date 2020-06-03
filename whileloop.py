num_of_tries = 0
while num_of_tries != 3:
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')
    if username == 'anb' and password == '123':
        print('welcome')
        num_of_tries = 0
        exit()
    else:
        print('error')
        num_of_tries += 1
        print('you have ' + str(3 - num_of_tries) + ' tries left')