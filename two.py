def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_dict = {"id": cat_id, "name": name, "age": age}
                cats_info.append(cat_dict)
        return cats_info
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []

def print_cats_info(cats_info):
    print("[")
    for cat in cats_info:
        print("    ", cat)
    print("]")

cats_info = get_cats_info("cats_file.txt")
print_cats_info(cats_info)