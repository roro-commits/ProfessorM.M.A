import matplotlib.pyplot as mlp
import pandas as pd
import numpy as np
import scipy.special
from calc.NN_calc import Nueral_calc as n_calc


class NeuralNetwork:

    def __init__(self, input_node, output_node, learn_rate):
        self.layer_weights = np.random.randn(output_node, input_node) * np.sqrt(1 / (input_node + output_node))
        self.calc = n_calc()
        self.input_node = input_node
        self.input_node = output_node
        self.lr = learn_rate

    # def dense(self, layer_nodes, input_size):
    #     # self.layer_weights = np.array([[0.9,0.3,0.4],[0.2,0.8,0.2],[0.1,0.5,0.6]])
    #     # print("Weights", self.layer_weights)
    #     self.calc.visual(self.layer_weights, "Weights")
    #     return self.layer_weights

    def feed_forward(self, input_x):
        self.x_input = np.array(input_x, ndmin=2).T
        self.net_input = self.calc.matrixdot(self.layer_weights, self.x_input)
        self.calc.visual(self.net_input, " Input x Weights ")
        final_output = self.calc.activation_function(self.net_input, self.calc.sigmoid)
        self.calc.visual(final_output, "output")
        # final_output = np.squeeze(np.asanyarray(final_output))
        # print("output", out)
        # print("output", len(out))

        return final_output

    def train(self, input_x, targets_y):
        # x_inputs = np.array(input_x, ndmin=2).T
        y_target = np.array(targets_y, ndmin=2).T
        final_out = self.feed_forward(input_x)
        cost_error = (y_target - final_out)
        self.calc.visual(cost_error, "cost error")
        # cost_error = (y_target - outputs)
        eError = np.dot(self.layer_weights.T, cost_error)
        self.layer_weights = self.layer_weights - self.lr * np.dot((cost_error * final_out * (1.0 - final_out)),np.transpose(self.x_input))



        return final_out


input = 784
output_node = 10
inputs = [0.2, 9]
# inputs = [0.2, 1.8, 0.9, 0.7, 0.0, 8.9, 0.5]
# inputs = [0.9, 0.1, 0.8]
N = NeuralNetwork(input, output_node, 0.001)
# layer_one = N.dense(3, len(inputs))
# lay1 = N.feed_forward(inputs, layer_one)
# layer_two = N.dense(2, len(lay1))
# lay2 = N.feed_forward(np.squeeze(np.asanyarray(lay1)), layer_two)
# # layer_three = N.dense(1, len(lay2))
# # lay3 = N.feed_forward(np.squeeze(np.asanyarray(lay2)), layer_three)

data_file = open("/home/rotimi/Documents/FYP/mnist_train.csv", 'r')
data_list = data_file.readlines()
data_file.close()

epoch = 10

for x in range(epoch):

    for data in data_list:
        all_values = data_list[0].split(',')
        # mlp.imshow(all_values, cmap="Greys", interpolation="None")
        ####s##########################scalling inputs #######################
        scaled_input = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        targets = np.zeros(output_node) + 0.01
        targets[int(all_values[0])] = 0.99
        #################l1#########################
        train = N.train(scaled_input, targets)
        file = open("/home/rotimi/Documents/FYP/cost.txt", 'a')
        file.writelines("\n" + str(train) + "\n")
        file.close()
        # print(Nueural_net.train(scaled_input,targets))
        pass

    pass

# load the mnist test data CSV file into a list
test_data_file = open("/home/rotimi/Documents/FYP/mnist_test.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

scorecard = []

for record in test_data_list:
    # split the record by the ',' commas
    all_values = record.split(',')
    # correct answer is first value
    correct_label = int(all_values[0])
    # scale and shift the inputs
    inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    # query the network
    outputs = N.feed_forward(inputs)
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
