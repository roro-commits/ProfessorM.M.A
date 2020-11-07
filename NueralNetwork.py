import matplotlib.pyplot as mlp
import numpy as np
from numpy.core.defchararray import array

from calc.NN_calc import Nueral_calc as n_calc




class NeuralNetwork:

    def __init__(self,input_node,hidden_node,output_node):
        self.input_node = input_node
        self.hidden_node = hidden_node
        self.output_node = output_node
        ##Bias, the bias is manually computed
        self.bias_one = ( np.random.rand(1,1) -0.5)
        self.bias_two = ( np.random.rand(1,1) -0.5)
        #self.hidden_input_weight = (np.random.rand(hidden_node,input_node) -0.5)
        self.hidden_input_weight = np.array([[0.9,0.3,0.4],[0.2,0.8,0.2],[0.1,0.5,0.6]]) + self.bias_one #test weights
        #self.output_hidden_weight = (np.random.rand(output_node,hidden_node) -0.5)
        self.output_hidden_weight = np.array([[0.3,0.7,0.5],[0.6,0.5,0.2],[0.8,0.1,0.9]]) + self.bias_two#test weight
    
    def train(self):
        print("hidden weght input",(self.hidden_input_weight))
        print("output weght input",(self.output_hidden_weight))
        #
        pass 

    
    def feed_Forward(self, X_input):
    
       # X_input = np.array(X_input,ndmin=2)  #// converting X_input into 2D array
        
        self.InputTOHidden = n_calc()
        ITH = self.InputTOHidden.matrixdot(self.hidden_input_weight,X_input) 
        print(ITH ," reading !!!!!!!!")
        self.InputTOHidden.visual(ITH,"input to hidden/ output of input")
        ## Activation Layer of input l2 weight 
        self.InputToOut = n_calc()
        ITO = self.InputToOut.activation_function(ITH,self.InputToOut.sigmoid)
        ## Out Layer ** l3 
        self.OutPut = n_calc()
        OTIO = self.OutPut.matrixdot(self.output_hidden_weight,ITO) 
        self.OutPut.visual(OTIO,"output of hidden / input of output")
        ###activation of ouput 
        self.out = n_calc()
        OUT = self.out.activation_function(OTIO,self.out.sigmoid)
        
        return OUT


#inputs = np.random.rand(3,1) - 0.5
inputs = np.array([0.9,0.1,0.8])
print()
Nn = NeuralNetwork(3,3,3)
Nn.train()
result = Nn.feed_Forward(inputs)
Nn = NeuralNetwork(3,3,3)
deeplayer = Nn.feed_Forward(result)
print("OUTput", result)
print("more layers", deeplayer)

