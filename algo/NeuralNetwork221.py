import numpy as np
from matplotlib import pyplot as plt




class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        # Weight inputs, add bias, then use the activation function
        total = np.dot(self.weights, inputs) + self.bias
        return OurNeuralNetwork.sigmoid(total)

    def mse_loss(self, y_true, y_pred):
        # y_true and y_pred are numpy arrays of the same length.
        return ((y_true - y_pred) ** 2).mean()


weights = np.array([0, 1]) # w1 = 0, w2 = 1
bias = 4                   # b = 4


class OurNeuralNetwork(object):
    '''
    Et neuralt netværk med:
    - 2 inputs
    - et "hidden layer" med 2 neuroner (h1, h2)
    - et "output layer" med 1 neuron (o1)
    '''

    def __init__(self, iter):
        self.iter = iter

        # Definer dataset
        self.data = np.array([
            [-2, -1],  # Alice
            [25, 6],  # Bob
            [17, 4],  # Charlie
            [-15, -6],  # Diana
        ])
        self.all_y_trues = np.array([
            1,  # Alice
            0,  # Bob
            0,  # Charlie
            1,  # Diana
        ])
        # Weights
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()

        # Biases
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()
        #print("w1: " + str(self.w1))
        #print("w2: " + str(self.w2))
        #print("w3: " + str(self.w3))
        #print("w4: " + str(self.w4))
        #print("w5: " + str(self.w5))
        #print("w6: " + str(self.w6))

        #print("b1: " + str(self.b1))
        #print("b2: " + str(self.b2))
        #print("b3: " + str(self.b3))

        #"svarene" på vores træningsdata
        self.y_true = np.array([1, 0, 0, 1])

        #Vores inputs
        self.x = np.array([2, 3])  # x1 = 2, x2 = 3

        #Vores predictions
        self.y_pred = np.array([0, 0, 0, 0])
        self.start(self.iter, self.data, self.all_y_trues, self.y_true, self.x, self.y_pred)

    def sigmoid(self, x):
        # Vores "activation function": f(x) = 1 / (1 + e^(-x))
        return 1 / (1 + np.exp(-x))

    def deriv_sigmoid(self, x):
        # Den afledte af sigmoid: f'(x) = f(x) * (1 - f(x))
        fx = self.sigmoid(x)
        return fx * (1 - fx)

    def feedforward(self, x_pre):
        # x er et numpy array med 2 elementer.
        x = [-1, -1]
        x[0] = (x_pre[0])# - 135)
        x[1] = (x_pre[1])# - 66)

        h1 = self.sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        h2 = self.sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        o1 = self.sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)
        return o1

    def train(self, data, all_y_trues, iter, y_true, x, y_pred):

        '''
        - data er et (n x 2) numpy array, n = antallet af data i datasættet.
        - all_y_trues er et numpy array med n elementer.
        Elementer i all_y_trues er det samme som dem i data.
        '''
        learn_rate = 0.2
        epochs = iter  # number of times to loop through the entire dataset
        losses = []
        for epoch in range(epochs):

            for self.x, self.y_true in zip(data, all_y_trues):

                # --- Laver et feedforward (Vi får brug for værdierne senere)
                sum_h1 = self.w1 * self.x[0] + self.w2 * self.x[1] + self.b1
                h1 = self.sigmoid(sum_h1)

                sum_h2 = self.w3 * self.x[0] + self.w4 * self.x[1] + self.b2
                h2 = self.sigmoid(sum_h2)

                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = self.sigmoid(sum_o1)
                self.y_pred = o1

                # --- Beregner den dummen af den afledte funktion
                # --- Navngivning: d_L_d_w1 er "afledt L / afledt w1"
                d_L_d_ypred = -2 * (self.y_true - self.y_pred)

                # Neuron o1
                d_ypred_d_w5 = h1 * self.deriv_sigmoid(sum_o1)
                d_ypred_d_w6 = h2 * self.deriv_sigmoid(sum_o1)
                d_ypred_d_b3 = self.deriv_sigmoid(sum_o1)

                d_ypred_d_h1 = self.w5 * self.deriv_sigmoid(sum_o1)
                d_ypred_d_h2 = self.w6 * self.deriv_sigmoid(sum_o1)

                # Neuron h1
                d_h1_d_w1 = x[0] * self.deriv_sigmoid(sum_h1)
                d_h1_d_w2 = x[1] * self.deriv_sigmoid(sum_h1)
                d_h1_d_b1 = self.deriv_sigmoid(sum_h1)

                # Neuron h2
                d_h2_d_w3 = x[0] * self.deriv_sigmoid(sum_h2)
                d_h2_d_w4 = x[1] * self.deriv_sigmoid(sum_h2)
                d_h2_d_b2 = self.deriv_sigmoid(sum_h2)

                # --- Updaterer vægte og biases
                # Neuron h1
                self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1

                # Neuron h2
                self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
                self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2

                # Neuron o1
                self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
                self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
                self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3

            # --- Berenger hele loss i slutningen af hver iteration
            if epoch % 100 == 0:
                y_preds = np.apply_along_axis(self.feedforward, 1, data)
                loss = float(Neuron(2,1).mse_loss(all_y_trues, y_preds))
                print("Epoch %d loss: %.3f" % (epoch, loss))
                losses.append(loss)

        plt.plot(losses)
        plt.show()

    def start(self, iter, data, all_y_trues, y_true, x, y_pred):
        # Træner vores neurale netværk!
        OurNeuralNetwork.train(self, data, all_y_trues, iter, y_true, x, y_pred)

        emily = np.array([-7, -3])  # 128 pund, 63 inches
        frank = np.array([20, 9])  # 155 pund, 75 inches
        print("Emily: %.3f" % OurNeuralNetwork.feedforward(self, emily))  # - F
        print("Frank: %.3f" % OurNeuralNetwork.feedforward(self, frank))  # - M

