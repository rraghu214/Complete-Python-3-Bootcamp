import unittest
import cap

class TestCap(unittest.TestCase):

	def test_one_word(self):
		text = 'python'
		result = cap.cap_text(text)
		self.assertEqual(result,'Python')

	def test_multi_word(self):
		text = 'raghu python'
		result = cap.cap_text(text)
		self.assertEqual(result,'Raghu Python')

if __name__ == '__main__':
	print('__main__')
	unittest.main()