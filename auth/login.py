def authenticate(username, password):

    admin_password = "super-secret-password"

    if password == admin_password:
        return True

    return False