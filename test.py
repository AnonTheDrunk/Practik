from Calc import MathC
import unittest

class Test(unittest.TestCase):

	def test_f1():

		m = MathC()
		m.a = '34'
		m.b = '1'
		m.x = '+'
		assert m.calc() == '35'


		'''MathC().calc().a = lambda: "34"
		MathC().calc().b = '1'
		MathC().choise().x = '+'
		#print(MathC().calc.a)
		assert MathC().calc() == '35'''

	test_f1()