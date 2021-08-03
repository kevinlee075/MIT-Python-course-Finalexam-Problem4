# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 21:16:02 2021

@author: Lenovo
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    checking_list = L.copy()
    
    result = 0
    
    while len(checking_list) > 0:
        
        largest_elem = max(checking_list)
        
        if checking_list.count(largest_elem) % 2 > 0:
            
            result = largest_elem
            
            break
            
        else:
            
            for i in range(len(checking_list)):
                
                if checking_list[i] == largest_elem:
                    
                    checking_list.remove(checking_list[i])
            
    if len(checking_list) > 0:
        
        return result
    
    else:
        
        return None