def delete_user(email, user_emails, users_storage):
    if email in users_storage:
        users_storage.pop(email)
        for i in range(len(user_emails)):
            if user_emails[i] == email:
                user_emails.pop(i)
                break
            else:
                continue
        return None
    else:
        print("Email not found")
