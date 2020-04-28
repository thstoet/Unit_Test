class Validator:

    def username_is_valid(self, username):
        if len(username) > 10:
            return False

        if " " in username:
            return False

        if username.islower():
            return False

        return True

if __name__ == "__main__":

    myValidator = Validator()

    if myValidator.username_is_valid("mario"):
        print("OK")
    else:
        print("NOK")
