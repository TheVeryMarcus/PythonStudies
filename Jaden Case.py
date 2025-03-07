def to_jaden_case(quote: str) -> str:
    """
    Преобразует строку в "Jaden Case", где каждое слово начинается с заглавной буквы.

    :param quote: Исходная строка для преобразования.
    :return: Строка в формате "Jaden Case".
    """
    return ' '.join(word.capitalize() for word in quote.split())

# Примеры использования
example_quote_1 = "How can mirrors be real if our eyes aren't real"
example_quote_2 = "If a book store never runs out of a certain book, dose that mean that nobody reads?"
example_quote_3 = "The more time you spend awake the more time you realize how tired you are."

jaden_cased_quote_1 = to_jaden_case(example_quote_1)
jaden_cased_quote_2 = to_jaden_case(example_quote_2)
jaden_cased_quote_3 = to_jaden_case(example_quote_3)

print(jaden_cased_quote_1)  # Вывод: "How Can Mirrors Be Real If Our Eyes Aren't Real"
print(jaden_cased_quote_2)  # Вывод: "If A Book Store Never Runs Out Of A Certain Book Dose That Mean That Nobody Reads?"
print(jaden_cased_quote_3)  # Вывод: "The More Time You Spend Awake The More Time You Realize How Tired You Are."

# Запрашиваем строку у пользователя
input_quote = input("write a quote: ")

# Преобразуем строку в стиль Jaden Smith
jaden_cased_quote = to_jaden_case(input_quote)

# Выводим результат
print("Jaden-Cased:", jaden_cased_quote)