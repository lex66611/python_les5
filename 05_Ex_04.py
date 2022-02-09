translations = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
    # и так далее ...
}

converted_rows = []

with open("Ex_04.txt") as input_data:
    for row in input_data:
        name, value = row.split(" - ")
        converted_rows.append(f"{translations[name]} - {value}")

with open("Ex_04_ru.txt", "w") as output_data:
    output_data.writelines(converted_rows)