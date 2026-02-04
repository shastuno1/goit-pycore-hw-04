import json
def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) != 3:
                    continue

                cat_id, name, age = parts

                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })

    except FileNotFoundError:
        print("Файл не знайдено")
    except Exception as e:
        print(f"Помилка: {e}")

    return cats


cats_info = get_cats_info("cats.txt")
print(json.dumps(cats_info, indent=4, ensure_ascii=False))
