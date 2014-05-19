#usr/bin/python

import numpy as np

def computeKDL(A1, A2, A3, Q):
    m_string = ';'.join([' '.join(map(str,x)) for x in [A1, A2, A3, Q]])
    m = np.matrix(m_string, dtype=np.float)
    m_rel = np.transpose((m+1)/(m.sum(axis=1)+5))

    i = 0   # 0 --> KLD(Q,A_1)
            # 1 --> KLD(Q,A_2)
            # 2 --> KLD(Q,A_3)
    logStuff = np.divide(m_rel[:,3], m_rel[:,i])
    logStuff = np.log2(logStuff)


    kullback = np.multiply(m_rel[:,3], logStuff)
    print(kullback)
    print(sum(kullback))

def doA():
    A1 = [20, 36, 90, 75, 12]
    A2 = [21, 100, 100, 3, 57]
    A3 = [3, 23, 12, 67, 34]
    Q = [25, 40, 45, 10, 20]
    computeKDL(A1,A2,A3,Q)


def doB():
    A1 = [2,78,10,11,5]
    A2 = [36,45,30,32,29]
    A3 = [100,5,6,23,0]
    Q = [3,2,5,4,2]
    computeKDL(A1,A2,A3,Q)

doA()