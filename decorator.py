def my_shiny_new_decorator(function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("я код до вызова функции")
        function_to_decorate()
        print("а я код, срабатывающий после")
    return the_wrapper_around_the_original_function

def stand_alone_function():
    print("я простая однокая функция")

stand_alone_function()
stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
stand_alone_function_decorated()