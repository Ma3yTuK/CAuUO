import numpy as np
from numpy.linalg import inv



###values###
v = np.array([  [   1,  2,  3   ]   ])
c = np.array([  [   1,  2,  3   ]   ])
B = 3
ORT = np.zeros((v.size, B))
x = np.zeros(ORT.shape)
###values###


def forward_method():
    for k in range(ORT.shape[0]):
        for b in range(ORT.shape[1]):
            if K == 0:
                if v[k] <= b:
                    ORT[k, b] = c[k]
                    x[k, b] = 1
                else:
                    ORT[k, b] = 0
                    x[k, b] = 0
            else:
                tmp = ORT[k - 1, b]
                if v[k] <= b:
                    tmp1 = ORT[k - 1, b - b[k]] + c[k]
                    if tmp1 > tmp:
                        ORT[k, b] = tmp1
                        x[k, b] = 1
                        continue
                ORT[k, b] = tmp
                x[k, b] = 0
    
    return ORT[-1, -1]


def backward_method():
    result = np.zeros(v.size)

    b = ORT[-1, -1]
    for k in reversed(range(v.size)):
        result[k] = x[k, b]
        b -= result[k] * v[k]

    return result


def main():
    print(forward_method(), backward_method())


if __name__ == "__main__":
    main()