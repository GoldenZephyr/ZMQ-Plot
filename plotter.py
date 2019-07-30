#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import zmq

def main():
    context = zmq.Context()
    sub = context.socket(zmq.SUB)
    sub.connect('tcp://%s:%d' % (ip, port))
    sub.setsockopt_string(zmq.SUBSCRIBE, '')
    n_hist = 50
    xdata = np.array(list(range(50)))
    ydata = np.zeros((50, 1))
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1, = ax.plot(xdata, ydata, 'r-')
    ix = 0 
    while (1):
        num = float(sub.recv_string())
        ydata[ix % n_hist] = num
        xdata[ix % n_hist] = ix
        line1.
        

if __name__ == '__main__':
    main()
