import matplotlib.pyplot as mlp
import pandas as pd
import numpy as np
import scipy.special
from calc.NN_calc import Nueral_calc as n_calc



class NeuralNetwork:

    def __init__(self, input_node, hidden_node, output_node, learn_rate):
        self.input_node = input_node
        self.hidden_node = hidden_node
        self.output_node = output_node
        self.lr = learn_rate
        ##Bias, the bias is manually computed
        self.bias_one = (np.random.rand(1, 1) - 0.5)
        self.bias_two = (np.random.rand(1, 1) - 0.5)
        self.hidden_input_weight = np.random.randn (self.hidden_node, self.input_node) * np.sqrt(1 / (self.hidden_node + self.input_node))
        # self.hidden_input_weight = np.array([[0.9,0.3,0.4],[0.2,0.8,0.2],[0.1,0.5,0.6]]) + self.bias_one #test weights
        self.output_hidden_weight = np.random.randn(self.output_node, self.hidden_node)* np.sqrt(1 / (self.output_node + self.hidden_node))
        # self.output_hidden_weight = np.array([[0.3,0.7,0.5],[0.6,0.5,0.2],[0.8,0.1,0.9]]) + self.bias_two#test weight

        mlp.plot(self.hidden_input_weight, self.hidden_input_weight)
        mlp.show()

    def feed_Forward(self, X_input):
        self.X_input = np.array(X_input, ndmin=2).T  # // converting X_input into 2D array
        self.InputTOHidden = n_calc()
        ITH = self.InputTOHidden.matrixdot(self.hidden_input_weight, X_input)
        # print(ITH ," Input x Hidden_weight ")
        self.InputTOHidden.visual(ITH, "input to hidden/ output of input")
        self.calc.visual(X_input, "trail")

        ## Activation Layer of input l2 weight
        self.InputToOut = n_calc()
        ITO = self.InputToOut.activation_function(ITH, self.InputToOut.sigmoid)
        ## Out Layer ** l3
        self.OutPut = n_calc()
        OTIO = self.OutPut.matrixdot(self.output_hidden_weight, ITO)
        self.OutPut.visual(OTIO, "output of hidden / input of output")
        ###activation of ouput
        self.out = n_calc()
        OUT = self.out.activation_function(OTIO, self.out.sigmoid)
        self.OutPut.visual(OUT, "output of Output")
        return OUT

    def train(self, input_array, target_array):
        #self.feed_Forward()
        inputs = np.array(input_array, ndmin=2).T
        targets = np.array(target_array, ndmin=2).T
        self.calc = n_calc()
        # calculate signals into hidden layer
        hidden_inputs = self.calc.matrixdot(self.hidden_input_weight, inputs)  # + self.bias_one
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.calc.activation_function(hidden_inputs, self.calc.sigmoid)
        # calculate signals into final output layer
        final_inputs = np.dot(self.output_hidden_weight, hidden_outputs)  # + self.bias_two
        # calculate the signals emerging from final output layer
        final_outputs = self.calc.activation_function(final_inputs, self.calc.sigmoid)

        # Cost fucntion/ Error (target - actual)
        output_errors = (targets - final_outputs)

        self.calc.visual( final_outputs,"trail")

        # Hidden Error
        hidden_errors = self.calc.matrixdot(self.output_hidden_weight.T, output_errors)

        # update the weights for the links between the hidden and output layers
        self.output_hidden_weight = self.output_hidden_weight - self.lr * self.calc.matrixdot((output_errors * final_outputs * (1.0 - final_outputs)),
                                                      np.transpose(hidden_outputs))

        # update the weights for the links between the input and hidden layers
        self.hidden_input_weight =self.hidden_input_weight - self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),np.transpose(inputs))



        print("weight output", self.output_hidden_weight)
        # print("Wight input H", self.hidden_input_weight)

        return output_errors




# numbers of input, hidden and output nodes & learning rate
input_nodes = 784
hidden_nodes = 100
output_node = 10
learning_rate = 0.001

Nueural_net = NeuralNetwork(input_nodes, hidden_nodes, output_node, learning_rate)

data_file = open("/home/rotimi/Documents/FYP/mnist_train_100.csv", 'r')
data_list = data_file.readlines()
data_file.close()

epoch = 10

for x in range(epoch):

    for data in data_list:
        all_values = data_list[0].split(',')
        #mlp.imshow(all_values, cmap="Greys", interpolation="None")
        ####s##########################scalling inputs #######################
        scaled_input = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        targets = np.zeros(output_node) + 0.01
        targets[int(all_values[0])] = 0.99
        # print(scaled_input)
        # Nueural_net.train(scaled_input,targets)
        acc = Nueural_net.train(scaled_input, targets)
        file = open("/home/rotimi/Documents/FYP/mnist_test copy.csv",'a')
        file.writelines("\n"+str(acc)+"\n")
        file.close()
        # print(Nueural_net.train(scaled_input,targets))
        pass

    pass

# load the mnist test data CSV file into a list
test_data_file = open("/home/rotimi/Documents/FYP/mnist_test copy.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

scorecard = []

# go through all the records in the test data set
for record in test_data_list:
    # split the record by the ',' commas
    all_values = record.split(',')
    # correct answer is first value
    correct_label = int(all_values[0])
    # scale and shift the inputs
    inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    # query the network
    outputs = Nueural_net.feed_Forward(inputs)
    # the index of the highest value corresponds to the label
    label = np.argmax(outputs)
    # append correct or incorrect to list
    if (label == correct_label):
        # network's answer matches correct answer, add 1 to scorecard
        scorecard.append(1)
    else:
        # network's answer doesn't match correct answer, add 0 to scorecard
        scorecard.append(0)
        pass

    pass

# calculate the performance score, the fraction of correct answers
scorecard_array = np.asarray(scorecard)
print("performance = ", scorecard_array.sum() / scorecard_array.size)
