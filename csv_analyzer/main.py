import csv

FIELD_SALARY = 'salary'
FIELD_DEPARTMENT = 'department'
FIELD_TOTAL_WORKERS = 'total_workers'
FIELD_TOTAL_SALARY = 'total_salary'
FIELD_MIN_SALARY = 'min_salary'
FIELD_MAX_SALARY = 'max_salary'
FIELD_AVG_SALARY = 'avg_salary'


def write_data_csv(file_name: str, data: list):
    """write data to csv file with file_name"""
    with open(file_name, 'w') as f:
        writer = csv.DictWriter(
            f, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in data:
            writer.writerow(d)


def get_department_info(raw_data: list):
    """get department info from input raw data"""
    departments = {}
    for row in raw_data:
        department_name = row[FIELD_DEPARTMENT]
        if department_name not in departments:
            departments[department_name] = {
                FIELD_TOTAL_WORKERS: 0,
                FIELD_TOTAL_SALARY: 0,
                FIELD_MIN_SALARY: int(row[FIELD_SALARY]),
                FIELD_MAX_SALARY: int(row[FIELD_SALARY])
            }
        departments[department_name][FIELD_TOTAL_WORKERS] += 1
        departments[department_name][FIELD_TOTAL_SALARY] += int(row[FIELD_SALARY])
        if departments[department_name][FIELD_MIN_SALARY] > int(row[FIELD_SALARY]):
            departments[department_name][FIELD_MIN_SALARY] = int(row[FIELD_SALARY])
        if departments[department_name][FIELD_MAX_SALARY] < int(row[FIELD_SALARY]):
            departments[department_name][FIELD_MAX_SALARY] = int(row[FIELD_SALARY])
    return [{FIELD_DEPARTMENT: dep,
             FIELD_TOTAL_WORKERS: info[FIELD_TOTAL_WORKERS],
             FIELD_AVG_SALARY: "%.2f" % (info[FIELD_TOTAL_SALARY] / info[FIELD_TOTAL_WORKERS]),
             FIELD_MIN_SALARY: info[FIELD_MIN_SALARY],
             FIELD_MAX_SALARY: info[FIELD_MAX_SALARY]} for dep, info in departments.items()]


def read_data_csv(file_name: str):
    """read data from csv file with file_name"""
    with open(file_name) as f:
        reader = csv.DictReader(f)
        return list(reader)


def print_all_departments():
    """print department names"""
    raw_data = read_data_csv('data.csv')
    department_info = get_department_info(raw_data)
    print([dep[FIELD_DEPARTMENT] for dep in department_info])


def print_departments_info():
    """print departments info"""
    raw_data = read_data_csv('data.csv')
    department_info = get_department_info(raw_data)
    print(department_info)


def save_departments_info_to_csv():
    """print departments info"""
    raw_data = read_data_csv('data.csv')
    department_info = get_department_info(raw_data)
    write_data_csv('out.csv', department_info)


def menu():
    """write menu info to stdout"""
    choice = input("""
                      1: Вывести все отделы
                      2: Вывести сводный отчёт по отделам
                      3: Сохранить сводный отчёт в виде csv
                      4: Выход

                      Please enter your choice: """)

    if choice == "1":
        print_all_departments()
    elif choice == "2":
        print_departments_info()
    elif choice == "3":
        save_departments_info_to_csv()
    elif choice == "4":
        exit(0)
    else:
        menu()


if __name__ == '__main__':
    menu()
