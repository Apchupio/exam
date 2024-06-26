def print_string_n_times(string, n):
    if n > 0:
        print(string)
        print_string_n_times(string, n-1)

user_string = input("Введите строку: ")
user_n = int(input("Введите количество повторений: "))

print_string_n_times(user_string, user_n)
