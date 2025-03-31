
def string_to_array(input_string):
    # Если строка пустая, возвращаем список с пустой строкой
    if input_string == "":
        return [""]
    # Используем метод split для разделения строки на слова
    words = input_string.split()
    return words
