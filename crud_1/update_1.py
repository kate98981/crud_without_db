def check_user(email, user_emails, users_storage):
    if email in user_emails:
        return users_storage.get(email)
    else:
        return 0


def update_user(email, name, password, phone, users_storage):
    d = [('name', name), ('password', password), ('phone', phone)]
    users_storage.get(email).update(d)
    return 0
