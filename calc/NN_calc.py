import numpy as np 
import math as mp



class Nueral_calc:
    def __init__(self):
            
            pass

    def matrixdot( self,weights, inputs ):
        self.input_x  = weights.dot(inputs)
        return self.input_x


    
    def sigmoid (self,input_x):
        eular = np.exp(1)
        self.sig = 1/(1 + mp.pow(eular,-input_x))

        return self.sig


    def step (self, input_x):
        self.threshold = 0.0
        self.step =0
        if ( input_x >= self.threshold):
            self.step = 1
        else:
            self.step = 0

        return self.step




    def activation_function(self, input_x, func):
        self.out_x =[]

        for x in input_x:
            out = func(x)
            self.out_x.append(out)
        
        return self.out_x

        




    

    

    








