# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 22:08:20 2021

@author: Rajesh
"""
import random
from abc import ABC, abstrachmethod

def data_generator (data_type, n):
    '''

    Parameters
    ----------
    data_type : type of data
        image or bits
    n : number of bits
        

    Returns
    -------
    list
        list of data stream

    '''
    if data_type=="bits":
        return [random.randint (0, 1) for i in range (n)]
    else:
        pass # add the code generate image data
        
    
#print (data_generator('bits', 10))

class AbstracgClass:
    
    @abstrachmethod
    
    def transmitter (self, data):
        pass
    def receiver (self, rec_data):
        pass
    def channel (self, trans_data):
        pass
    
class bpsk (AbstracgClass()):
    def __init__(self, data):
        self.data = data
    def transmitter (self):
        self.data = data_generator(data_type, n)
        
    