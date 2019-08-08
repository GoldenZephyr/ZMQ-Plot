#!/usr/bin/python3
import zmq
import numpy as np
import time
import sys

def main():
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5560
    context = zmq.Context()
    pub = context.socket(zmq.PUB)
    pub.bind('tcp://*:%s' % port)
    while (1):
        num = np.random.random()
        pub.send_string(str(num))
        time.sleep(0.5)


if __name__ == '__main__':
    main()
