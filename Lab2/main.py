import numpy as np
from numpy.linalg import inv



###values###
A = np.array([  [   0,  1,  2,  3   ],
                [   0,  0,  1,  2   ],
                [   0,  2,  2,  3   ]   ])
B = np.zeros(A.shape)
C = np.zeros(A.shape)
###values###


def forward_method():
    for p in range(A.shape[0]):
        for q in range(A.shape[1]):
            if p == 0:
                B[p, q] = A[p, q]
                C[p, q] = q
            else:
                tmp = A[p,:q + 1] + np.flip(B[p-1,:q + 1])
                C[p, q] = np.argmax(tmp)
                B[p, q] = tmp[int(C[p, q])]
    
    return B[-1, -1]


def backward_method():
    result = np.zeros(A.shape[0])
    q = A.shape[1] - 1

    for i, c_row in enumerate(np.flip(C, 0)):
        result[-i-1] = c_row[int(q)]
        q = q - c_row[int(q)]

    return result


def main():
    print(forward_method(), backward_method())


if __name__ == "__main__":
    main()