from crud_1.create_1 import create_user
from crud_1.delete_1 import delete_user
from crud_1.read_1 import user_info, all_users_info
# список почт, ключи для словаря
from crud_1.update_1 import check_user, update_user

user_emails = []
users_storage = {}

while True:
    action = input('enter action ')
    if action == 'create':
        print('action =', action)
        email = input('Email: ')
        name = input('Name: ')
        password = input('Password: ')
        phone = input('Phone: ')
        # пересохраняем то, что вернет функция create_user
        # будем постоянно добавлять email-ы
        create_user(email,
                    name,
                    password,
                    phone,
                    user_emails,
                    users_storage)
        print('user_emails = ', user_emails)
        print('users_storage= ', users_storage)
    elif action == 'read_all':
        print('action =', action)
        all_users_info(users_storage)

    elif action == 'read_user':
        user_e = input('Enter user email ')
        message = user_info(user_e, user_emails, users_storage)
        print('action =', action)
        print('User =', message)
    elif action == 'update':
        print('action =', action)
        email = input('Email: ')
        if check_user(email, user_emails, users_storage) == 0:
            print('Пользователя не существует')
        else:
            message = check_user(email, user_emails, users_storage)
            print(message)
            name = input('Name: ')
            password = input('Password: ')
            phone = input('Phone: ')
            update_user(email, name, password, phone, users_storage)
            print('users_storage= ', users_storage)
    elif action == 'delete':
        print('action =', action)
        email = input('Email: ')
        delete_user(email, user_emails, users_storage)
        print('user_emails = ', user_emails)
        print('users_storage= ', users_storage)
    elif action == "--help":
        print("create: create user \n"
              "read_all: view the list of users \n"
              "read_user: view user with email \n"
              "update: update user \n"
              "delete: delete user")
