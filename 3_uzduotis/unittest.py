from selenium import webdriver
import unittest

class UnitTest(unittest.TestCase):
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_block = browser.find_element_by_class_name('first_block')
    second_block = browser.find_element_by_class_name('second_block')

    def test_name(self):
        value = "Name"
        field_value = ""
        try:
            field = self.first_block.find_element_by_class_name('first')
            field.send_keys(value)
            field_value = field.get_attribute('value')
        except:
            pass
        self.assertEqual(field_value, value)

    def test_last_name(self):
        value = "Last Name"
        field_value = ""
        try:
            field = self.first_block.find_element_by_class_name('second')
            field.send_keys(value)
            field_value = field.get_attribute('value')
        except:
            pass
        self.assertEqual(field_value, value)

    def test_email(self):
        value = "Email"
        field_value = ""
        try:
            field = self.first_block.find_element_by_class_name('third')
            field.send_keys(value)
            field_value = field.get_attribute('value')
        except:
            pass
        self.assertEqual(field_value, value)

    def test_phone(self):
        value = "Phone"
        field_value = ""
        try:
            field = self.second_block.find_element_by_class_name('first')
            field.send_keys(value)
            field_value = field.get_attribute('value')
        except:
            pass
        self.assertEqual(field_value, value)

    def test_address(self):
        value = "Address"
        field_value = ""
        try:
            field = self.second_block.find_element_by_class_name('second')
            field.send_keys(value)
            field_value = field.get_attribute('value')
        except:
            pass
        self.assertEqual(field_value, value)

unittest.main()

