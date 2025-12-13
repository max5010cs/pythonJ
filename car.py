class Car:
	def __init__(self, model, year, manufacturer):
		self.model = model
		self.year = year
		self.manufacturer = manufacturer
		self.odometer = 0
	def get_model(self):
		print(f'Model is {self.model.title()}')
	def get_odometer(self):
		print(f'It is {self.odometer}')
	def get_name(self):
		print(f'{self.year} {self.manufacturer.title()} {self.model.title()}')
	def update_odometer(self):
		message = input('What number: ')
		if int(message) > 0:
			self.odometer = int(message)
			print('Done')
		else:
			print('Nope')
