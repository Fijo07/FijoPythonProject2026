class User:
    def __init__(self,firsname, lastname):
        print("creating clss user")
        self.firsname = firsname
        self.lastname = lastname

    def print_hello(self):
        print("he {} {}".format(self.firstname, self.lastname))

    def print_bye(self):
            print("bye {} {}".format(self.firstname, self.lastname))