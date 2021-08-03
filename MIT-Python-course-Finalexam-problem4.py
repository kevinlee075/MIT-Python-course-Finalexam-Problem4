# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 21:16:02 2021

@author: Lenovo
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    temp_odd = 0
    
    largest_odd = 0
    
    for num in L:
        
        if num % 2 != 0:
            
            temp_odd = num
            
            if temp_odd > largest_odd:
                
                largest_odd = temp_odd
    
    if largest_odd > 0:
        
        return largest_odd
    
    else:
        return None