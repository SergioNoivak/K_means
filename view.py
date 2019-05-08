
import numpy as np
import matplotlib.pyplot as plt


def show_function(xelement,yelement):
    ax = plt.subplot(111)
    x = np.arange(0.0, 5.0, 0.09)
    #sin(X^2)/(3-cos(e)-x)
    s = x* np.sin(x*x)/(3-np.cos(np.e)-x)
    line, = plt.plot(x, s, lw=2)
    plt.ylim(-150,150)
    
    plt.plot(xelement, yelement, marker='o', markersize=3, color="red")

    plt.show()



        
        