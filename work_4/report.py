import csv
from work_4.static import KZ_LETTERS

if __name__ == '__main__':
    with open('./work_4/out/data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        with open('./work_4/README.md', 'a+') as file:
            next(reader)
            for (i, letter), row in zip(enumerate(KZ_LETTERS), reader):
                file.write(
                    f"""
### Буква {letter}

<img src="./alphabet/{i+1}.png" width="150"> <img src="out/profile/x/{i+1}.png" width="300"> <img src="out/profile/y/{i+1}.png" width="300">
"""
                )

                file.write(
                    f"""
Признаки:
- Вес чёрного = {row[1]}
- Нормированный вес чёрного = {row[2]}
- Центр масс = {row[3]}
- Нормированный центр масс = {row[4]}
- Моменты инерции = {row[5]}
- Нормированные моменты инерции = {row[6]}
"""
                )
