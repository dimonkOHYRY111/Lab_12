import json

journals = [
    {"name": "Journal A", "price": 25.50, "circulation": 8000},
    {"name": "Journal B", "price": 35.00, "circulation": 12000},
    {"name": "Journal C", "price": 15.75, "circulation": 5000},
    {"name": "Journal D", "price": 40.20, "circulation": 15000},
    {"name": "Journal E", "price": 18.90, "circulation": 7000}
]


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не знайдений.")
        return []


def print_json(filename):
    data = load_from_json(filename)
    if data:
        print(json.dumps(data, indent=4, ensure_ascii=False))
    else:
        print("Дані відсутні або файл порожній.")


def add_record(filename):
    name = input("Введіть назву журналу: ")
    price = float(input("Введіть ціну журналу: "))
    circulation = int(input("Введіть тираж журналу: "))

    new_record = {"name": name, "price": price, "circulation": circulation}
    data = load_from_json(filename)
    data.append(new_record)
    save_to_json(data, filename)
    print(f"Запис '{name}' додано.")


def delete_record(filename):
    name = input("Введіть назву журналу, який потрібно видалити: ")
    data = load_from_json(filename)

    # Знайти і видалити запис
    new_data = [record for record in data if record["name"] != name]
    if len(new_data) != len(data):
        save_to_json(new_data, filename)
        print(f"Запис '{name}' видалено.")
    else:
        print("Журнал не знайдено.")


def search_by_field(filename):
    field = input("За яким полем хочете шукати (name, price, circulation): ")
    value = input(f"Введіть значення для поля '{field}': ")

    data = load_from_json(filename)

    if field in ["name", "price", "circulation"]:
        if field == "price" or field == "circulation":
            value = float(value) if field == "price" else int(value)
        results = [record for record in data if record[field] == value]
        print(f"Знайдені записи: {json.dumps(results, indent=4, ensure_ascii=False)}")
    else:
        print("Невірне поле для пошуку.")


def calculate_average_price():
    data = journals
    filtered_data = [record for record in data if record["circulation"] < 10000]

    if filtered_data:
        total_price = sum(record["price"] for record in filtered_data)
        average_price = total_price / len(filtered_data)
        print(f"Середня ціна журналів з тиражем менше 10 000: {average_price:.2f} грн")

        result = {"average_price": average_price}
        save_to_json(result, "average_price_result.json")
        print("Результат збережено в файл 'average_price_result.json'")
    else:
        print("Жодного журналу з тиражем менше 10 000 примірників не знайдено.")


def menu():
    print("\nМеню:")
    print("1. Вивести вміст JSON файлу")
    print("2. Додати новий запис до JSON файлу")
    print("3. Видалити запис з JSON файлу")
    print("4. Пошук за полем")
    print("5. Обчислити середню ціну журналів з тиражем менше 10 000")
    print("6. Вийти")

    while True:
        choice = input("\nВиберіть опцію: ")
        if choice == '1':
            print_json('journals.json')
        elif choice == '2':
            add_record('journals.json')
        elif choice == '3':
            delete_record('journals.json')
        elif choice == '4':
            search_by_field('journals.json')
        elif choice == '5':
            calculate_average_price()
        elif choice == '6':
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    save_to_json(journals, 'journals.json')

    menu()
