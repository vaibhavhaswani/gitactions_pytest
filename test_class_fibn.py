from fibn import fibn

class TestFibn:

	def setup(self):
		"""runs before each test"""
		print("Test Started!")

	def teardown(self):
		"""runs after each test"""
		print("Test End!")

	def setup_class(cls):
		"""runs before every test class"""
		print("Test Class Start!")

	def teardown_class(cls):
		"""runs after every test class"""
		print("Test Class End!")

	def test_1(self):
	  assert fibn(3,5)==[2, 3, 5, 8, 13]

	def test_2(self):
	  assert fibn(0,3)==[0,1,1]

	# def test_2(self):
	#   assert fibn(0,0)==None