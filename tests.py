import unittest
import base32h

class TestBase32HMethods(unittest.TestCase):

    def test_encode_digit(self):
		with self.assertRaises(Exception):
			base32h.encode_digit(-1)
		with self.assertRaises(Exception):
			base32h.encode_digit('a')
		with self.assertRaises(Exception):
			base32h.encode_digit('foo')
		with self.assertRaises(Exception):
			base32h.encode_digit(32)
		with self.assertRaises(Exception):
			base32h.encode_digit(33)

		
		for n in range(32):
			self.assertEqual(type(base32h.encode_digit(n)), str)
			self.assertEqual(len(base32h.encode_digit(n)), 1)
			#    try:
			#        print encode_digit(n)
			#    except Exception as e:
			#        print (type(e), e)
			#	 self.assertEqual('foo'.upper(), 'FOO')

    def test_encode_number(self):
		for n in [-1,'a','foo']:
			with self.assertRaises(Exception):
				base32h.encode_number(n)

		for n in range(35) + range (0,32**2+1, 16):
			self.assertEqual(type(base32h.encode_number(n)), str)

    def test_decode_(self):
		for m in range(1,32*32):
			self.assertEqual(m, base32h.decode_base32h(base32h.encode_number(m)))
		for m in ['0','o','O']:
			self.assertEqual('0',base32h.encode_number(base32h.decode_base32h(m)))

if __name__ == '__main__':
    unittest.main()

