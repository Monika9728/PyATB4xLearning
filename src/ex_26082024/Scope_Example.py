def outer_func():
    var1=20
    def inner_function():
        print(var1)
    def nested_function2():
            print(var1)
    inner_function()
    nested_function2()