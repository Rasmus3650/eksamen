from matplotlib import pyplot as plt
import numpy as np

class NeuralNetwork21(object):
    def __init__(self, iter):
        self.iter = iter
        #hvert punkt er længde, bredde og type (0, 1)
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

    #       o  blomster type
    #      / \  w1, w2, b
    #     o   o  længde, bredde




    # activation function
    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def sigmoid_p(self, x):
        return self.sigmoid(x) * (1-self.sigmoid(x))


    # train
    def train(self, iter, data):
        # Vi starter ud med tilfældige vægte og bias
        w1 = np.random.randn()
        w2 = np.random.randn()
        b = np.random.randn()

        iterations = iter
        learning_rate = 0.2
        costs = []  # holder styr på cost, så vi kan se om den falder

        for i in range(iterations):
            # får et tilfældigt punkt
            ri = np.random.randint(len(data))
            point = data[ri]

            # Regner vores netværks gæt ud, ud fra det tilfældige punkt
            z = point[0] * w1 + point[1] * w2 + b
            pred = self.sigmoid(z)  # networks prediction

            #Dette er det rigtige svar til punktet
            target = point[2]


            # print the cost over all data points every 100 iters
            if i % 100 == 0:
                c = 0
                for j in range(len(data)):
                    p = data[j]
                    p_pred = self.sigmoid(w1 * p[0] + w2 * p[1] + b)
                    c += np.square(p_pred - p[2])
                costs.append(c)

            # Regner cost ud ud fra den afledte cost-funktion med den afledte sigmoid
            dcost_dpred = 2 * (pred - target)
            dpred_dz = self.sigmoid_p(z)


            dz_dw1 = point[0]
            dz_dw2 = point[1]
            dz_db = 1

            dcost_dz = dcost_dpred * dpred_dz

            dcost_dw1 = dcost_dz * dz_dw1
            dcost_dw2 = dcost_dz * dz_dw2
            dcost_db = dcost_dz * dz_db

            #Ændrer på vægte og bias for at optimere netværket
            w1 = w1 - learning_rate * dcost_dw1
            w2 = w2 - learning_rate * dcost_dw2
            b = b - learning_rate * dcost_db

        return costs, w1, w2, b


    def start(self, iter, data):
        # Kører vores train funktion
        costs, w1, w2, b = self.train(iter, data)

        #Finder ud af hvilken type blomst, vores netværk vil sige "mysteryflower" er
        mystery_pred = self.sigmoid((self.mystery_flower[0] * w1) + (self.mystery_flower[1] * w2) + b)
        print("Mystery: " + str(mystery_pred))

        #Plotter vores cost, for at se om den falder
        fig = plt.plot(costs)
        plt.show(fig)
