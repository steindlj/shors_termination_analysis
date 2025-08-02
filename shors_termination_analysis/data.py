import sympy

prime_factors = list(sympy.primerange(3, 1010))
DEFAULT_TEST_SET = [prime_factors[i] * prime_factors[i+1] for i in range(len(prime_factors)-1)]