import csv


def write_data_csv(file_name, data):
    with open(file_name, 'w') as f:
        writer = csv.DictWriter(
            f, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in data:
            writer.writerow(d)


def get_department_info(raw_data):
    departments = {}
    for row in raw_data:
        if row['department'] not in departments:
            departments[row['department']] = {
                'total_workers': 0,
                'total_salary': 0,
                'min_salary': int(row['salary']),
                'max_salary': int(row['salary'])
            }
        departments[row['department']]['total_workers'] += 1
        departments[row['department']]['total_salary'] += int(row['salary'])
        if departments[row['department']]['min_salary'] > int(row['salary']):
            departments[row['department']]['min_salary'] = int(row['salary'])
        if departments[row['department']]['max_salary'] < int(row['salary']):
            departments[row['department']]['max_salary'] = int(row['salary'])
    return [{'department': dep,
             'total_workers': info['total_workers'],
             'avg_salary': info['total_salary'] / info['total_workers'],
             'min_salary': info['min_salary'],
             'max_salary': info['max_salary']} for dep, info in departments.items()]


def read_data_csv(file_name):
    with open(file_name) as f:
        reader = csv.DictReader(f)
        return list(reader)


if __name__ == '__main__':
    raw_data = read_data_csv('data.csv')
    department_info = get_department_info(raw_data)
    write_data_csv('out.csv', department_info)
