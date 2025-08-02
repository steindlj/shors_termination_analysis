import numpy as np

def order_finding(a: int, N: int) -> int:
    """Find the order r of a modulo N."""
    for r in range(2, N):
        if pow(a, r, N) == 1:
            return r

def shors_algorithm(N: int) -> list:
    """Simulate Shor's algorithm, collecting statistics."""
    statistic = [
        0, # success: gcd(a, N) > 1
        0, # restart: r is odd
        0, # restart: x+-1 mod N = 0
        0  # success: x+-1 mod N != 0
    ]
    while True:
        a = np.random.default_rng().integers(2, N, dtype=int) # a in [2, N)
        if np.gcd(a, N) > 1:
            f0 = np.gcd(a, N)
            f1 = 1
            statistic[0] += 1 
            break
        else: # gcd(a, N) = 1
            r = order_finding(a, N)
            if r % 2 != 0: # r is odd
                statistic[1] += 1
                continue
            else: # r is even
                x = pow(a, int(r/2), N)
                x_plus_minus = (x+1, x-1)
                if np.mod(x_plus_minus[0], N) == 0 or np.mod(x_plus_minus[1], N) == 0:
                    statistic[2] += 1
                    continue
                else:
                    f0 = np.gcd(x_plus_minus[0], N)
                    f1 = np.gcd(x_plus_minus[1], N)
                    statistic[3] += 1
                    break
    return statistic