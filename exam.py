def print_string_n_times(string, n):
# Добавим условный оператор для выполнения следующей строки    
    if n > 0:
        print(string)
        print_string_n_times(string, n-1)
# Добавим метод для вывода строки с клавиатуры
user_string = input("Введите строку: ")
# Добавим метод для для количества строк которые нужно вывести
user_n = int(input("Введите количество повторений: "))

print_string_n_times(user_string, user_n)
