#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import zmq

import time

def parse_zmq_config(fn):
    with open(fn, 'r') as fo:
        lines = fo.readlines()

    info_list = []
    for line in lines:
        if line[0] == '#':
            continue
        else:
            try:
                toks = line.split('|')
                title = toks[0].strip()
                ip = toks[1].strip()
                port = int(toks[2])
            except:
                print('Malformed config file %s' % fn)
        info_list.append((title, ip, port))

    return info_list

def main():

    fn = 'zmq_configuration.config'
    cnx_info = parse_zmq_config(fn)
    print(cnx_info)

    context = zmq.Context()

    ip1 = cnx_info[0][1]
    port1 = cnx_info[0][2]
    sub1 = context.socket(zmq.SUB)
    sub1.setsockopt(zmq.RCVTIMEO,0)
    sub1.connect('tcp://%s:%d' % (ip1, port1))
    sub1.setsockopt_string(zmq.SUBSCRIBE, '')

    ip2 = cnx_info[1][1]
    port2 = cnx_info[1][2]
    sub2 = context.socket(zmq.SUB)
    sub2.setsockopt(zmq.RCVTIMEO,0)
    sub2.connect('tcp://%s:%d' % (ip2, port2))
    sub2.setsockopt_string(zmq.SUBSCRIBE, '')

    ip3 = cnx_info[2][1]
    port3 = cnx_info[2][2]
    sub3 = context.socket(zmq.SUB)
    sub3.setsockopt(zmq.RCVTIMEO,0)
    sub3.connect('tcp://%s:%d' % (ip3, port3))
    sub3.setsockopt_string(zmq.SUBSCRIBE, '')

    ip4 = cnx_info[3][1]
    port4 = cnx_info[3][2]
    sub4 = context.socket(zmq.SUB)
    sub4.setsockopt(zmq.RCVTIMEO,0)
    sub4.connect('tcp://%s:%d' % (ip4, port4))
    sub4.setsockopt_string(zmq.SUBSCRIBE, '')
    n_hist = 50

    ip5 = cnx_info[4][1]
    port5 = cnx_info[4][2]
    sub5 = context.socket(zmq.SUB)
    sub5.setsockopt(zmq.RCVTIMEO,0)
    sub5.connect('tcp://%s:%d' % (ip5, port5))
    sub5.setsockopt_string(zmq.SUBSCRIBE, '')

    ip6 = cnx_info[5][1]
    port6 = cnx_info[5][2]
    sub6 = context.socket(zmq.SUB)
    sub6.setsockopt(zmq.RCVTIMEO,0)
    sub6.connect('tcp://%s:%d' % (ip6, port6))
    sub6.setsockopt_string(zmq.SUBSCRIBE, '')

    xdata1 = np.array(list(range(n_hist)))
    ydata1 = np.ones((n_hist, 1)) * np.NaN
    xdata2 = np.array(list(range(n_hist)))
    ydata2 = np.ones((n_hist, 1)) * np.NaN
    xdata3 = np.array(list(range(n_hist)))
    ydata3 = np.ones((n_hist, 1)) * np.NaN
    xdata4 = np.array(list(range(n_hist)))
    ydata4 = np.ones((n_hist, 1)) * np.NaN
    xdata5 = np.array(list(range(n_hist)))
    ydata5 = np.ones((n_hist, 1)) * np.NaN
    xdata6 = np.array(list(range(n_hist)))
    ydata6 = np.ones((n_hist, 1)) * np.NaN
    
    ydata1[0] = 0
    ydata2[0] = 0
    ydata3[0] = 0
    ydata4[0] = 0
    ydata5[0] = 0
    ydata6[0] = 0

    plt.ion()
    fig = plt.figure()

    ax1 = fig.add_subplot(231)
    line1, = ax1.plot(xdata1, ydata1, 'r-')
    ax2 = fig.add_subplot(232)
    line2, = ax2.plot(xdata2, ydata2, 'r-')
    ax3 = fig.add_subplot(233)
    line3, = ax3.plot(xdata3, ydata3, 'r-')
    ax4 = fig.add_subplot(234)
    line4, = ax4.plot(xdata4, ydata4, 'r-')
    ax5 = fig.add_subplot(235)
    line5, = ax5.plot(xdata5, ydata5, 'r-')
    ax6 = fig.add_subplot(236)
    line6, = ax6.plot(xdata6, ydata6, 'r-')

    ax1.set_title(cnx_info[0][0])
    ax2.set_title(cnx_info[1][0])
    ax3.set_title(cnx_info[2][0])
    ax4.set_title(cnx_info[3][0])
    ax5.set_title(cnx_info[4][0])
    ax6.set_title(cnx_info[5][0])

    fig.canvas.draw()
    ix = 0 
    while (1):
        try:
            num1 = float(sub1.recv_string())
        except zmq.Again:
            num1 = np.NaN
        try:
            num2 = float(sub2.recv_string())
        except zmq.Again:
            num2 = np.NaN
        try:
            num3 = float(sub3.recv_string())
        except zmq.Again:
            num3 = np.NaN
        try:
            num4 = float(sub4.recv_string())
        except zmq.Again:
            num4 = np.NaN
        try:
            num5 = float(sub5.recv_string())
        except zmq.Again:
            num5 = np.NaN
        try:
            num6 = float(sub6.recv_string())
        except zmq.Again:
            num6 = np.NaN

        ydata1[0] = num1
        xdata1[0] = ix
        ydata2[0] = num2
        xdata2[0] = ix
        ydata3[0] = num3
        xdata3[0] = ix
        ydata4[0] = num4
        xdata4[0] = ix
        ydata5[0] = num5
        xdata5[0] = ix
        ydata6[0] = num6
        xdata6[0] = ix

        ydata1 = np.roll(ydata1, -1)
        xdata1 = np.roll(xdata1, -1)
        ydata2 = np.roll(ydata2, -1)
        xdata2 = np.roll(xdata2, -1)
        ydata3 = np.roll(ydata3, -1)
        xdata3 = np.roll(xdata3, -1)
        ydata4 = np.roll(ydata4, -1)
        xdata4 = np.roll(xdata4, -1)
        ydata5 = np.roll(ydata5, -1)
        xdata5 = np.roll(xdata5, -1)
        ydata6 = np.roll(ydata6, -1)
        xdata6 = np.roll(xdata6, -1)

        xdata_plot1 = xdata1[np.isfinite(ydata1).squeeze()]
        ydata_plot1 = ydata1[np.isfinite(ydata1).squeeze()]
        xdata_plot2 = xdata2[np.isfinite(ydata2).squeeze()]
        ydata_plot2 = ydata2[np.isfinite(ydata2).squeeze()]
        xdata_plot3 = xdata3[np.isfinite(ydata3).squeeze()]
        ydata_plot3 = ydata3[np.isfinite(ydata3).squeeze()]
        xdata_plot4 = xdata4[np.isfinite(ydata4).squeeze()]
        ydata_plot4 = ydata4[np.isfinite(ydata4).squeeze()]
        xdata_plot5 = xdata5[np.isfinite(ydata5).squeeze()]
        ydata_plot5 = ydata5[np.isfinite(ydata5).squeeze()]
        xdata_plot6 = xdata6[np.isfinite(ydata6).squeeze()]
        ydata_plot6 = ydata6[np.isfinite(ydata6).squeeze()]

# Plot 1
        xmin1 = np.min(xdata_plot1)
        xmax1 = np.max(xdata_plot1)
        ymin1 = np.min(ydata_plot1)
        ymax1 = np.max(ydata_plot1)
        ax1.set_xlim([xmin1, xmax1])
        ax1.set_ylim([ymin1, ymax1])
        line1.set_xdata(xdata_plot1)
        line1.set_ydata(ydata_plot1)

# Plot 2
        xmin2 = np.min(xdata_plot2)
        xmax2 = np.max(xdata_plot2)
        ymin2 = np.min(ydata_plot2)
        ymax2 = np.max(ydata_plot2)
        ax2.set_xlim([xmin2, xmax2])
        ax2.set_ylim([ymin2, ymax2])
        line2.set_xdata(xdata_plot2)
        line2.set_ydata(ydata_plot2)

# Plot 3
        xmin3 = np.min(xdata_plot3)
        xmax3 = np.max(xdata_plot3)
        ymin3 = np.min(ydata_plot3)
        ymax3 = np.max(ydata_plot3)
        ax3.set_xlim([xmin3, xmax3])
        ax3.set_ylim([ymin3, ymax3])
        line3.set_xdata(xdata_plot3)
        line3.set_ydata(ydata_plot3)

# Plot 4
        xmin4 = np.min(xdata_plot4)
        xmax4 = np.max(xdata_plot4)
        ymin4 = np.min(ydata_plot4)
        ymax4 = np.max(ydata_plot4)
        ax4.set_xlim([xmin4, xmax4])
        ax4.set_ylim([ymin4, ymax4])
        line4.set_xdata(xdata_plot4)
        line4.set_ydata(ydata_plot4)

# Plot 5
        xmin5 = np.min(xdata_plot5)
        xmax5 = np.max(xdata_plot5)
        ymin5 = np.min(ydata_plot5)
        ymax5 = np.max(ydata_plot5)
        ax5.set_xlim([xmin5, xmax5])
        ax5.set_ylim([ymin5, ymax5])
        line5.set_xdata(xdata_plot5)
        line5.set_ydata(ydata_plot5)

# Plot 6
        xmin6 = np.min(xdata_plot6)
        xmax6 = np.max(xdata_plot6)
        ymin6 = np.min(ydata_plot6)
        ymax6 = np.max(ydata_plot6)
        ax6.set_xlim([xmin6, xmax6])
        ax6.set_ylim([ymin6, ymax6])
        line6.set_xdata(xdata_plot6)
        line6.set_ydata(ydata_plot6)

        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.05)
        ix += 1
        

if __name__ == '__main__':
    main()
