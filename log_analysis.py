# Beta v0.1

from time import sleep

print("\n           📊 Анализатор логов\n")
print('''1. Вывести всю активность\n2. Общее кол-во запросов\n3. Вывод уникальных IP\n4. Кол-во запросов по конкретному IP-адресу\n0. Закрыть''')
print("------------------------")

start_menu = int(input("Выберите пункт меню: "))
requests = []

def add_logs_to_list(file):
	id_num = 0

	for line in file.readlines():
		line = line.strip().split()
		id_num += 1
		requests.append(dict(ID=id_num, ip=line[0], method=line[1], path=line[2], status=int(line[3])))

	file.close()

add_logs_to_list(file=open('log.txt'))

while start_menu != 0:

	# Вывод всей активности (Всего содержимого файла log.txt)
	if start_menu == 1:
		print('---------------------------------------------------------')
		print(f'''ID | IP           | METHOD | PATH      | STATUS''')
		print('---------------------------------------------------------')

		for data in requests:
			print(f'{str(data['ID']).ljust(2)} | {data['ip']}  | {data['method'].ljust(6)} | {data['path'].ljust(9)} | {data['status']}')
			sleep(0.5)
		print('---------------------------------------------------------')

		sleep(1)

	# Сортировка уникальных IP-адресов
	elif start_menu == 3:

		ip_filter = set()

		for data in requests:
			ip_filter.add(data['ip'])

		id_num = 0

		print('---------------------------------------------------------')
		print('ID | IP |')
		print('---------------------------------------------------------')

		for ip in ip_filter:
			id_num += 1
			print(str(id_num).ljust(2) + ' | ' + ip)
			sleep(0.5)

	print("\n           📊 Анализатор логов")
	print('''1. Вывести всю активность\n2. Общее кол-во запросов\n3. Вывод уникальных IP\n4. Кол-во запросов по конкретному IP-адресу\n0. Закрыть''')
	print("------------------------")

	start_menu = int(input("Выберите пункт меню: "))