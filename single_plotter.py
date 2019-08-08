#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import zmq

import time

def main():
    ip = 'localhost'
    port = 5560
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
    fig.canvas.draw()
    ix = 0 
    while (1):
        num = float(sub.recv_string())
        print(num)
        ydata[0] = num
        xdata[0] = ix
        ix += 1

        xmin = np.min(xdata)
        xmax = np.max(xdata)
        ymin = np.min(ydata)
        ymax = np.max(ydata)
        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymin, ymax])

        ydata = np.roll(ydata, -1)
        xdata = np.roll(xdata, -1)
        line1.set_xdata(xdata)
        line1.set_ydata(ydata)
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.05)
        

if __name__ == '__main__':
    main()
