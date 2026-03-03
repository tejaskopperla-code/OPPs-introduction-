class myClass:

    __privateVar = 27

    def __privNeth(self):
        print(" I'm  inside class myClass")

    def hello(self):
        print("private variable value",myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__privateVar