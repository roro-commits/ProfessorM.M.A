from numpy.core.defchararray import array
import numpy as np
from calc.NN_calc import Nueral_calc as n_calc
import  matplotlib.pyplot as mlp
import  pandas as pd
from sklearn.preprocessing import LabelEncoder as encoder





class NeuralNetwork:

    def __init__(self,input_node,hidden_node,output_node):
        self.input_node = input_node
        self.hidden_node = hidden_node
        self.output_node = output_node
        self.hidden_input_weight = (np.random.rand(hidden_node,input_node) -0.5)
        #self.hidden_input_weight = np.array([[0.9,0.3,0.4],[0.2,0.8,0.2],[0.1,0.5,0.6]]) #test weights
        self.output_hidden_weight = (np.random.rand(output_node,hidden_node) -0.5)
        #self.output_hidden_weight = np.array([[0.3,0.7,0.5],[0.6,0.5,0.2],[0.8,0.1,0.9]]) #test weight
    
    def train(self):
        print("hidden weght input",(self.hidden_input_weight))
        print("output weght input",(self.output_hidden_weight))
        pass 

    def feed_Forward(self, X_input):
    
       # X_input = np.array(X_input,ndmin=2)  #// converting X_input into 2D array
        
        self.InputTOHidden = n_calc()
        ITH = self.InputTOHidden.matrixdot(self.hidden_input_weight,X_input.T)
        ## Activation Layer of input * l2 weight 
        self.InputToOut = n_calc()
        ITO = self.InputToOut.activation_function(ITH,self.InputToOut.sigmoid)
        ## Out Layer ** l3 
        self.OutPut = n_calc()
        OTIO = self.OutPut.matrixdot(self.output_hidden_weight,ITO)
        ###activation of ouput 
        self.out = n_calc()
        OUT = self.out.activation_function(OTIO,self.out.sigmoid)
        
        return OUT


inputs = np.random.rand(30,1) - 0.5
#inputs = np.array([0.9,0.1,0.8])
print()
Nn = NeuralNetwork(28,28,1)
Nn.train()



UFC_data = pd.read_csv('/home/rotimi/Documents/FYP/UFC_data.csv')
UFC_data['Stance'] = encoder().fit_transform(UFC_data['Stance'])
UFC_data['Stance.1'] = encoder().fit_transform(UFC_data['Stance'])
UFC_data = UFC_data.drop(['Unnamed: 0'], axis=1)
UFC_data = UFC_data.drop(['Name'], axis=1)
UFC_data = UFC_data.drop(['Name.1'], axis=1)
cols_to_norm = ['Height', 'Stance', 'Weight', 'Reach', 'DOB', 'SLpm', 'SAcc',
                'SApm', 'StrDef', 'TDAvg', 'TDAcc', 'TDDef', 'SubAvg', 'AvgTime2Win',
                'Height.1', 'Stance.1', 'Weight.1', 'Reach.1', 'DOB.1',
                'SLpm.1', 'SApm.1', 'StrDef.1', 'TDAvg.1', 'TDAcc.1',
                'TDDef.1', 'SubAvg.1', 'AvgTime2Win.1']
UFC_data[cols_to_norm] = UFC_data[cols_to_norm].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

x_data = UFC_data.drop('Win', axis=1)
labels = UFC_data['Win']

x = x_data.loc[0:8]

print(x)
result = Nn.feed_Forward(x)
print(result)