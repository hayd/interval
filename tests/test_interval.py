import unittest
from interval import *

class TestIntervalSet(unittest.TestCase):

	def setUp(self):
		self.i01c = Interval(0, 1)
		self.i02c = Interval(0, 2)
		self.i13c = Interval(1, 3)
		self.i12c = Interval(1, 2)
		self.i11c = Interval(1, 1)
		self.is01c = IntervalSet([self.i01c])
		self.is02c = IntervalSet([self.i02c])
		self.is13c = IntervalSet([self.i13c])
		self.is12c = IntervalSet([self.i12c])
		self.is11c = IntervalSet([self.i11c])

	def test_or(self):
		self.assertEqual(self.is02c, self.is01c + self.is12c)
		self.assertEqual(self.is02c, self.is01c | self.is12c)
		self.assertEqual(self.is02c, self.is01c.union(self.is12c))
		# TODO self.assertEqual(self.is02c, self.is01c or self.is12c)

	def test_and(self):
		self.assertEqual(self.is11c, self.is01c & self.is12c)
		self.assertEqual(self.is11c, self.is01c.intersection(self.is12c))
		# TODO self.assertEqual(self.is11c, self.is01c and self.is12c)

	def test_difference(self):
		expected = IntervalSet([Interval(1, 2, lower_closed=False, upper_closed=True)])
		self.assertEqual(expected, self.is02c - self.is01c)
		self.assertEqual(expected, self.is02c.difference(self.is01c))

	def test_symmetric_difference(self):
		expected = IntervalSet([Interval(0, 1, lower_closed=True, upper_closed=False),
			                  Interval(2, 3, lower_closed=False, upper_closed=True)])
		self.assertEqual(expected, self.is13c.symmetric_difference(self.is02c))

	def test_subset(self):
		self.assertFalse(self.is02c.issubset(self.is01c))
		self.assertTrue(self.is12c.issubset(self.is02c))
		self.assertTrue(self.is01c.issubset(self.is01c))

	def test_superset(self):
		self.assertTrue(self.is01c.issubset(self.is02c))
		self.assertFalse(self.is02c.issubset(self.is12c))
		self.assertTrue(self.is01c.issubset(self.is01c))