def total_salary(path):
    total = 0      # тут будемо накопичувати загальну суму зарплат
    count = 0      # тут будемо рахувати кількість розробників

    try:
        # відкриваємо файл для читання
        with open(path, "r", encoding="utf-8") as file:
            # читаємо файл построково
            for line in file:
                # прибираємо зайві пробіли та розділяємо рядок по комі
                name, salary = line.strip().split(",")

                # додаємо зарплату до загальної суми
                total += int(salary)

                # збільшуємо лічильник розробників
                count += 1

        # якщо файл був порожній
        if count == 0:
            return (0, 0)

        # рахуємо середню зарплату
        average = total / count

        # повертаємо кортеж: (загальна сума, середня)
        return (total, average)

    # якщо файл не знайдено
    except FileNotFoundError:
        print("File not found.")
        return (0, 0)

    # якщо в файлі неправильний формат даних
    except ValueError:
        print("Invalid data format in file.")
        return (0, 0)

total, average = total_salary("salary.txt")
print(f"Загальна сума: {total}, Середня: {average}")
