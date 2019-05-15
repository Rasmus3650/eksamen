from matplotlib import pyplot as plt
import numpy as np

class NeuralNetwork21(object):
    def __init__(self, iter):
        self.iter = iter
        # each point is length, width, type (0, 1)
        self.data = [[3, 1.5, 1],
                     [2, 1, 0],
                     [4, 1.5, 1],
                     [3, 1, 0],
                     [3.5, .5, 1],
                     [2, .5, 0],
                     [5.5, 1, 1],
                     [1, 1, 0]]

        self.mystery_flower = [4.5, 1]
        self.start(self.iter, self.data)
    # network

    #       o  flower type
    #      / \  w1, w2, b
    #     o   o  length, width




    def vis_data(self,data):
        plt.grid()

        for i in range(len(data)):
            c = 'r'
            if data[i][2] == 0:
                c = 'b'
            #plt.scatter([data[i][0]], [data[i][1]], c=c)

        #plt.scatter([mystery_flower[0]], [mystery_flower[1]], c='gray')


    # activation function

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def sigmoid_p(self, x):
        return self.sigmoid(x) * (1-self.sigmoid(x))

    X = np.linspace(-5, 5, 100)

    #plt.plot(X, sigmoid(X), c="b") # sigmoid in blue
    #fig1 = plt.plot(X, sigmoid_p(X), c="r") # sigmoid_p in red



    # train

    def train(self, iter, data):
        # random init of weights
        w1 = np.random.randn()
        w2 = np.random.randn()
        b = np.random.randn()

        iterations = iter
        learning_rate = 0.2
        costs = []  # keep costs during training, see if they go down

        for i in range(iterations):
            # get a random point
            ri = np.random.randint(len(data))
            point = data[ri]

            z = point[0] * w1 + point[1] * w2 + b
            pred = self.sigmoid(z)  # networks prediction

            target = point[2]

            # cost for current random point
            cost = np.square(pred - target)

            # print the cost over all data points every 1k iters
            if i % 100 == 0:
                c = 0
                for j in range(len(data)):
                    p = data[j]
                    p_pred = self.sigmoid(w1 * p[0] + w2 * p[1] + b)
                    c += np.square(p_pred - p[2])
                costs.append(c)
                #print(cost)

            dcost_dpred = 2 * (pred - target)
            dpred_dz = self.sigmoid_p(z)

            dz_dw1 = point[0]
            dz_dw2 = point[1]
            dz_db = 1

            dcost_dz = dcost_dpred * dpred_dz

            dcost_dw1 = dcost_dz * dz_dw1
            dcost_dw2 = dcost_dz * dz_dw2
            dcost_db = dcost_dz * dz_db

            w1 = w1 - learning_rate * dcost_dw1
            w2 = w2 - learning_rate * dcost_dw2
            b = b - learning_rate * dcost_db

        return costs, w1, w2, b


    def start(self, iter, data):
        print("start")
        costs, w1, w2, b = self.train(iter, data)

        fig = plt.plot(costs)
        plt.show(fig)
