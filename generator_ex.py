#!/usr/bin/python3
import zmq
import numpy as np
import time

def main():
    port = 5560
    context = zmq.Context()
    pub = context.socket(zmq.PUB)
    pub.bind('tcp://*:%s' % p.FOCUS_ROI_PORT)
    while (1):
        num = np.random.random()
        pub.send_string(str(num))
        time.sleep(0.5)


if __name__ == '__main__':
    main()
