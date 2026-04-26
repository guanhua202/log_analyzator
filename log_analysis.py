# Beta v0.2

from time import sleep

requests = []

# ----------------------------------------FUNCTIONS----------------------------------------

def menu_rendering():
	print("\n           📊 Анализатор логов\n")
	print('''1. Вывести всю активность\n2. Общее кол-во запросов\n3. Фильтрация по IP\n0. Закрыть''')
	print("------------------------")

def add_logs_to_list(file):
	request_id = 0

	for line in file.readlines():
		line = line.strip().split()
		request_id += 1
		requests.append(dict(ID=request_id, ip=line[0], method=line[1], path=line[2], status=int(line[3])))

	file.close()

add_logs_to_list(file=open('log.txt'))
menu_rendering()

def ip_filter():
	ip_filter = {data['ip'] for data in requests}

	return ip_filter

def all_ip_output(request_id):
	for ip in ip_filter():
		request_id += 1
		print(f'{str(request_id).ljust(2)} | {ip}')
		sleep(0.5)

def rendering_table_of_ip():
	print('---------------------------------------------------------')
	print(f'''ID | IP           | METHOD | PATH      | STATUS''')
	print('---------------------------------------------------------')

# -------------------------------------------------------------------------------------------

start_menu = int(input("Выберите пункт меню: "))

while start_menu != 0:

	# Вывод всей активности (Всего содержимого файла log.txt)
	if start_menu == 1:
		rendering_table_of_ip()

		for data in requests:
			print(f'{str(data['ID']).ljust(2)} | {data['ip']}  | {data['method'].ljust(6)} | {data['path'].ljust(9)} | {data['status']}')
			sleep(0.5)
		print('---------------------------------------------------------')

		sleep(1)

	elif start_menu == 2:

		succs_request = 0
		refer_request = 0
		err_request = 0

		for data in requests:
			if data['status'] // 100 == 2:
				succs_request += 1
			elif data['status'] // 100 == 3:
				refer_request += 1
			elif data['status'] // 100 == 4:
				err_request += 1

		sleep(1)
		print('------------------------')
		print(f'Успешных: {succs_request}, Ошибок: {err_request}, Перенаправлений: {refer_request}')
		print('------------------------')
		sleep(1)

	# Сортировка уникальных IP-адресов
	elif start_menu == 3:
		print('------------------------')
		print('1. Все IP адреса (без повторений)')
		print('2. Активность конкретного IP (Фильтрация)')
		print('------------------------')

		choice = int(input("Выберите опцию: "))

		if choice == 1:
			request_id = 0

			print('-----------------')
			print('ID | IP |')
			print('-----------------')

			all_ip_output(request_id)

		elif choice == 2:
			
			request_id = 0
			
			print('-----------------')
			print("\nНиже IP которые есть в логах: ")
			print('-----------------')
			print('ID | IP |')
			print('-----------------')

			all_ip_output(request_id)

			select_ip = int(input("Выберите IP адрес для фильтрации: "))

			request_id = 0
			found_ip = 0

			for ip in ip_filter():
				request_id += 1
				
				if select_ip == request_id:
					found_ip = ip
					break

			rendering_table_of_ip()

			for data in requests:
				if data['ip'] == found_ip:
					print(f'{str(data['ID']).ljust(2)} | {data['ip']}  | {data['method'].ljust(6)} | {data['path'].ljust(9)} | {data['status']}')
					sleep(0.5)

			print('---------------------------------------------------------')

	menu_rendering()

	start_menu = int(input("Выберите пункт меню: "))
