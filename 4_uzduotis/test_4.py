import pytest

class Test4:
	link = "http://suninjuly.github.io/registration1.html"
	# link = "http://suninjuly.github.io/registration2.html"

	@pytest.fixture(autouse=True)
	def time(self):
		from datetime import datetime
		print("Test started at: ", datetime.now().strftime("%H:%M:%S"))
		yield
		print("\nTest ended at:   ", datetime.now().strftime("%H:%M:%S"))

	@pytest.fixture(scope="module")
	def chrome_webdriver(self):
		from selenium import webdriver
		browser = webdriver.Chrome()
		browser.get(self.link)
		yield browser
		browser.quit()

	def test_name(self, chrome_webdriver):
		value = "Name"
		field_value = ""
		try:
			field = chrome_webdriver.find_element_by_class_name('first_block').find_element_by_class_name('first')
			field.send_keys(value)
			field_value = field.get_attribute('value')
		except:
			pass
		assert field_value == value

	def test_last_name(self, chrome_webdriver):
		value = "Last Name"
		field_value = ""
		try:
			field = chrome_webdriver.find_element_by_class_name('first_block').find_element_by_class_name('second')
			field.send_keys(value)
			field_value = field.get_attribute('value')
		except:
			pass
		assert field_value == value

	def test_email(self, chrome_webdriver):
		value = "Last Email"
		field_value = ""
		try:
			field = chrome_webdriver.find_element_by_class_name('first_block').find_element_by_class_name('third')
			field.send_keys(value)
			field_value = field.get_attribute('value')
		except:
			pass
		assert field_value == value

	def test_phone(self, chrome_webdriver):
		value = "Phone"
		field_value = ""
		try:
			field = chrome_webdriver.find_element_by_class_name('second_block').find_element_by_class_name('first')
			field.send_keys(value)
			field_value = field.get_attribute('value')
		except:
			pass
		assert field_value == value

	def test_address(self, chrome_webdriver):
		value = "Address"
		field_value = ""
		try:
			field = chrome_webdriver.find_element_by_class_name('second_block').find_element_by_class_name('second')
			field.send_keys(value)
			field_value = field.get_attribute('value')
		except:
			pass
		assert field_value == value
