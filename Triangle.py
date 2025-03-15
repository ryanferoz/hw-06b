# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk

updates dont by Ryan Feroz
"""

def classifyTriangle(a, b, c):
    """Classifies a triangle based on side lengths a, b, and c."""
    
    #Validates input
    if not all(isinstance(i, int) for i in (a, b, c)):
        return "InvalidInput"
    
    #Ensures that side lengths are positive and within a reasonable range
    if a <= 0 or b <= 0 or c <= 0 or a > 200 or b > 200 or c > 200:
        return "InvalidInput"
    
    #Checks to see if the sides satisfy the triangle inequality theorem
    if a + b <= c or a + c <= b or b + c <= a:
        return "NotATriangle"

    #Checks for triangle types
    if a == b == c:
        return "Equilateral"
    
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "Right"
    
    if a == b or b == c or a == c:
        return "Isosceles"
    
    return "Scalene"
