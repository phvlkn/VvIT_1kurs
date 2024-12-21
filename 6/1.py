class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def check_password(self, password):
        if password == self.__password:
            return True
        else:
            return False

    def set_password(self, prev_password, new_password):
        if self.check_password(prev_password):
            self.__password = new_password
            print("Password has been changed")
        else:
            print("Passwords do not match")

user1 = UserAccount("user1", "aboba@mail.ru", "password")
user1.set_password("password", "password1")
user1.set_password("password", "<PASSWORD>")