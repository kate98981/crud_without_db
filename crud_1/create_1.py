def create_user(email, name, password, phone, user_emails, users_storage):
    if email in user_emails:
        print('The user exist')
        return None
    else:
        # вывод, что ввели для добавления
        user_info = [email, name, password, phone]
        user_emails.append(email)
        users_storage[email] = {"name": name,
                                "password": password,
                                "phone": phone}
        print('create_user_f = ', user_info)
        return None
