# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 22:08:20 2021

@author: Rajesh
"""
import random
import numpy as np
from abc import ABC, abstractmethod
from matplotlib import pyplot as plt

class AbstractClass:
    
    @abstractmethod
    
    def transmitter (self, data):
        pass
    def receiver (self, rec_data):
        pass
    def channel (self, trans_data):
        pass    
    

class bpsk (AbstractClass):
    
    def __init__(self, data_type, n):
        #self.__data = 0  # make the data private
        self.data_type = data_type
        self. n = n
        self.trans_data = 0
        self.snrdb = 0
    
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
            return [random.randint(0, 1) for i in range (n)]
        else:
            pass # add the code generate image data
    

        
    def transmitter (self):
        self.__data = np.array(data_generator(self.data_type, self.n)) 
        self.__data = 2*self.__data-1 # bit mapping
        print (f"Transmitted data : {self.__data}")
        
    def channel (self, snrdb):
        self.snrdb = snrdb
        snr_norm = 10**(self.snrdb/10)
        p = snr_norm**0.5
        self.noise = np.random.randn(len(self.__data)) 
        self.__trans_data = p*self.__data + self.noise
        #return self.trans_data
    
    def receiver (self):
        '''
        mask = (self.trans_data >0)
        detected_data = self.trans_data[mask]
        '''
        self.__detected_data = np.zeros (len(self.__data))
        for i in range (len(self.__trans_data)):
            if (self.__trans_data[i] > 0):
                self.__detected_data[i] = 1
            else:
                self.__detected_data[i] = 0
        print(self.__detected_data)
        
    def plotting (self):
        Tb = 1 # T
        Eb = 1
        fc = 1/Tb
        t = np.linspace (0, 1, 1000)
        
        # plotting the transmitted data
        phi = np.sqrt(2*Eb/Tb)*np.sin(2*np.pi*fc*t)
        trans_wave = np.empty([0, len(self.__trans_data)])
        for i in range (len(self.__trans_data)):
            trans_wave = np.append(trans_wave, self.__data[i]*phi )
            
        
        plt.plot (range(len(t)*len(self.__trans_data)), trans_wave)
        plt.show()
        
        # plotting the detected wave
        phi = np.sqrt(2*Eb/Tb)*np.sin(2*np.pi*fc*t)
        detected_wave = np.empty([0, len(self.__trans_data)])
        self.__detected_data = 2*self.__detected_data-1
        for i in range (len(self.__detected_data)):
            detected_wave = np.append(detected_wave, self.__detected_data[i]*phi )
        print(len(phi))
        plt.plot (range(len(t)*len(self.__detected_data)), detected_wave)
        plt.show()
        
        for i in range (self.n):
            if (self.__data[i] > 0):
                self.__data[i] = 1
            else:
                self.__data[i] = 0
        
        for i in range (self.n):
            if (self.__detected_data[i] > 0):
                self.__detected_data[i] = 1
            else:
                self.__detected_data[i] = 0
            
        self.__detected_data = (self.__detected_data).astype('int')
        error_bits = self.__data^self.__detected_data
        print (error_bits)
        ber = sum(error_bits)/(self.n)
        print (f"Ber : {ber}\tsnr : {self.snrdb}")
        return ber
        
    def ber_vs_snr(self):
        ber = np.zeros(20)
        for i in range (20):
            b.transmitter()
            y = b.channel(i)
            b.receiver()
            ber[i] = b.plotting()
            
        #plt.semilogy(np.arange(20), ber)
        plt.semilogy(np.arange(20),ber,color='r',marker='o',linestyle='-')
        
        