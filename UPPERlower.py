def solve(s: str) -> str:
    # Подсчитываем количество заглавных и строчных букв
    lower_count = sum(1 for char in s if char.islower())
    upper_count = sum(1 for char in s if char.isupper())

    # Преобразуем строку в зависимости от количества букв
    if upper_count > lower_count:
        return s.upper()
    else:
        return s.lower()

# Примеры использования
print(solve("coDe"))  # Вывод: "code"
print(solve("CODe"))  # Вывод: "CODE"
print(solve("coDE"))  # Вывод: "code"
