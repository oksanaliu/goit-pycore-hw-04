def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary_str = line.strip().split(',')
                salary = int(salary_str)
                total_salary += salary
                num_developers += 1

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except ValueError:
        print("Неправильний формат даних у файлі.")
        return None, None


    if num_developers == 0:
        print("У файлі немає даних про розробників.")
        return None, None

    average_salary = total_salary / num_developers
    return total_salary, average_salary

total, average = total_salary("salary.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")