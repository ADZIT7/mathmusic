import matplotlib.pyplot as plt
import numpy as np

class Graph:
    def __init__(self,e):
        self.function = e 
    def getYInt(self):
        x = 0
        return eval(self.function)
    def getY(self,x):
        return eval(self.function)
    def graph(self,raw = "null",fromx = -10,tox = 10, amount = 40):
        # define variables
        x = np.linspace(fromx, tox, num = amount)
        # format graph
        fig, ax = plt.subplots()
        ax.set_title(raw + ' (close window to continue)')
        ax.spines["left"].set_position(("data", 0))
        ax.spines["bottom"].set_position(("data", 0))
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        # arrows!
        ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
        ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
        ax.plot(0, 0, "<k", transform=ax.get_yaxis_transform(), clip_on=False)
        ax.plot(0, 0, "vk", transform=ax.get_xaxis_transform(), clip_on=False)

        # check if valid
        try:
            y = eval(self.function)  
        except:
            print("Function is not valid")
        else:
            # graph the function
            plt.plot(x,y, 'g')
            plt.plot(0, self.getYInt(), marker="o", markersize=5, markerfacecolor="gray")
            # show the graph
            plt.show()