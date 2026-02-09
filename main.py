from pyscript import display, document

def verify_account(e):
    document.getElementById('output').innerHTML = ' '

    username = document.getElementById('username').value
    password = document.getElementById('password').value

    user_count = 0
    user_ok = False

    for char in username:
        user_count += 1

    if user_count >= 7:
        user_ok = True
    else:
        display(f'Username must be at least 7 characters', target='output')
        return
    

    has_letter = False
    has_number = False
    pass_count = 0

    for char in password:
        pass_count += 1
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_number = True

    if pass_count < 10:
        display(f'Password must be at least 10 characters', target='output')
    elif not has_letter:
        display(f'Password must contain at least 1 letter', target='output')
    elif not has_number:
        display(f'Password must contain at least 1 number', target='output')
    else:
        display(f'Account successfully created!', target='output')