with open('Ex_03.txt') as f:
    lines_worker = f.readlines()
    f.close()

salary_threshold = 20000
total_salary = 0
num_worker = len(lines_worker)
poor_worker_list = []
for line in lines_worker:
    split_line = line.split()
    salary = float(split_line[1])
    total_salary += salary
    if salary < salary_threshold:
        poor_worker_list.append(split_line[0])
print(f"Работников с зарплатой меньше 20000: {poor_worker_list}")
print(f"Средняя зарплата: {total_salary / num_worker}")