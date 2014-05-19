#usr/bin/python

import numpy as np

def computeDelta(A1, A2, A3, Q):
    m_string = ';'.join([' '.join(map(str,x)) for x in [A1, A2, A3, Q]])
    m = np.matrix(m_string, dtype=np.float)
    m_rel = np.transpose(m/m.sum(axis=1))

    mean = np.mean(m_rel[:,0:3],1)
    std = np.std(m_rel[:,0:3],1)

    centered = m_rel - np.kron([1, 1, 1, 1], mean)
    z_score = np.divide(centered, np.kron([1, 1, 1, 1], std))

    delta1 = np.abs(z_score[:,0]- z_score[:,3])
    delta2 = np.abs(z_score[:,1]- z_score[:,3])
    delta3 = np.abs(z_score[:,2]- z_score[:,3])

    n = 5

    delta1 = sum(delta1)/n
    delta2 = sum(delta2)/n
    delta3 = sum(delta3)/n

    print(delta1)
    print(delta2)
    print(delta3)

def doA():
    A1 = [20, 36, 90, 75, 12]
    A2 = [21, 100, 100, 3, 57]
    A3 = [3, 23, 12, 67, 34]
    Q = [25, 40, 45, 10, 20]
    computeDelta(A1,A2,A3,Q)


def doB():
    A1 = [2,78,10,11,5]
    A2 = [36,45,30,32,29]
    A3 = [100,5,6,23,0]
    Q = [3,2,5,4,2]
    computeDelta(A1,A2,A3,Q)

doB()