# -*- coding: utf-8 -*-
"""
Updated for comprehensive testing of classifyTriangle()

@author: jrr
@author: rk
@updated: March 14, 2025
"""

import unittest

from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    """Unit tests for classifyTriangle function"""

    #Tests for Right Triangle
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 should be a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 should be a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(8, 15, 17), 'Right', '8,15,17 should be a Right triangle')

    def testRightTriangleD(self):
        self.assertEqual(classifyTriangle(7, 24, 25), 'Right', '7,24,25 should be a Right triangle')

    #Test for Equilateral Triangle
    def testEquilateralTriangle(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10,10,10 should be an Equilateral triangle')

    #Tests for Isosceles Triangle 
    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isosceles', '5,5,8 should be an Isosceles triangle')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(7, 7, 10), 'Isosceles', '7,7,10 should be an Isosceles triangle')

    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles', '2,2,3 should be an Isosceles triangle')

    #Tests for Scalene Triangle
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '4,5,6 should be a Scalene triangle')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(10, 15, 20), 'Scalene', '10,15,20 should be a Scalene triangle')

    #Tests for Invalid Input
    def testInvalidInputNegative(self):
        self.assertEqual(classifyTriangle(-1, 5, 6), 'InvalidInput', '-1,5,6 should be InvalidInput')

    def testInvalidInputZero(self):
        self.assertEqual(classifyTriangle(0, 5, 6), 'InvalidInput', '0,5,6 should be InvalidInput')

    def testInvalidInputString(self):
        self.assertEqual(classifyTriangle('a', 5, 6), 'InvalidInput', "'a',5,6 should be InvalidInput")

    def testInvalidInputFloat(self):
        self.assertEqual(classifyTriangle(5.5, 6, 7), 'InvalidInput', '5.5,6,7 should be InvalidInput')

    def testInvalidInputTooLarge(self):
        self.assertEqual(classifyTriangle(201, 150, 100), 'InvalidInput', '201,150,100 should be InvalidInput')

    #Tests for Not a Triangle 
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 should be NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(10, 1, 1), 'NotATriangle', '10,1,1 should be NotATriangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(7, 2, 5), 'NotATriangle', '7,2,5 should be NotATriangle')

    def testNotATriangleD(self):
        self.assertEqual(classifyTriangle(100, 1, 1), 'NotATriangle', '100,1,1 should be NotATriangle')

if __name__ == '__main__':
    print('Running unit tests...')
    unittest.main()
