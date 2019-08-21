import Update_Codes

def read_file(station=False, buses=False):
	with open('bus_codes.txt', 'r') as f:
		content = f.readlines()
		station_name = content[0]
		bus_codes = content[1]
	
	if (station):
		return station_name
	elif (buses):
		return bus_codes
	else:
		return False

def main(bus, update=False, url=''):
	
	if (update):
		Update_Codes.update_bus_codes(url)
		print('Bus codes updated..\n')
		print('Checking buses for: ' + read_file(station=True))

		return True

	if (bus == 'EXIT'):
		exit()

	bus_codes = eval(read_file(buses=True))

	for i in bus_codes:
		if (i == bus):
			print('Geçer..\n')
			return True
	
	print('Geçmez..\n')
	return False

if __name__ == '__main__':

	print('Checking buses for: ' + read_file(station=True))

	while True:
		update = False
		url = ''
		bus = input('[+] Enter bus code: ')
		bus = bus.split(' ')
		if (bus[0].upper() == 'UPDATE'):
			update = True
			try:
				url = bus[1]
			except Exception as e:
				pass
		main(bus[0].upper(), update, url)
