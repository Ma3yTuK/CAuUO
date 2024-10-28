import numpy as np
from numpy.linalg import inv



###values###
v = np.array([   3,  4,  5,  8,  9   ])
c = np.array([   1,  6,  4,  7,  6   ])
B = 13
ORT = np.zeros((v.size, B))
x = np.zeros(ORT.shape)
###values###


def forward_method():
    for k in range(ORT.shape[0]):
        for b in range(ORT.shape[1]):
            if k == 0:
                if v[k] <= b + 1:
                    ORT[k, b] = c[k]
                    x[k, b] = 1
                else:
                    ORT[k, b] = 0
                    x[k, b] = 0
            else:
                tmp = ORT[k - 1, b]
                if v[k] <= b + 1:
                    tmp1 = c[k]
                    if b >= v[k]:
                        tmp1 += ORT[k - 1, b - v[k]]
                    if tmp1 > tmp:
                        ORT[k, b] = tmp1
                        x[k, b] = 1
                        continue
                ORT[k, b] = tmp
                x[k, b] = 0
    
    return ORT[-1, -1]


def backward_method():
    result = np.zeros(v.size)

    b = B - 1
    for k in reversed(range(v.size)):
        result[k] = x[k, b]
        b -= round(result[k] * v[k])

    return result, B - b - 1


def main():
    print(forward_method(), backward_method())


if __name__ == "__main__":
    main()