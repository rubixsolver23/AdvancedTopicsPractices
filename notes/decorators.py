def cough(func):

    def func_wrapper():
        #stuff that happens before the function
        print("*cough*")
        func()
        print("*cough*")
        #stuff that happens after

    return func_wrapper

@cough
def awkward():
    print("Can I get a discount?")


@cough
def answer():
    print("This is a dollar tree. . .")


awkward()
answer()