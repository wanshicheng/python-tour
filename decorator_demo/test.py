a_string = "This is a global variable"
def foo():
    print(locals())
print(globals()) # doctest: +ELLIPSIS
foo() #