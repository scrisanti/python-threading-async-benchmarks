import multiprocessing
from timeit import default_timer as timer
import math

import sys
sys.set_int_max_str_digits(0)

def cpu_heavy_task(n: int) -> float:
    number = n**11 + n # 2**n + n

    start_time = timer()
    # print(start_time)
    count_pf = count_prime_factors(number)
    print('Computing Factorial')

    fact_start_time = timer()
    # print(fact_start_time)
    fact = math.factorial(n**2)

    end_time = timer()
    # print(end_time)

    print(f'Total Task Time: {end_time - start_time:.4f}s - ({end_time-fact_start_time:.4f}s {fact_start_time-start_time:.4f}s)')
    print(f'{number} has {count_pf} prime factors and ({n}^2)! has {len(str(fact))} digits')


def count_prime_factors(n: int) -> int:
    print(f'Finding prime factors for {n}')
    count = 0
    i = 2

    while i ** 2 <= n: # If this number is less than square root
        if n % i: #If there is a remainder, add one
            i += 1
        else: # No remainder then keep going!
            n //= i
            count += 1

    if n > 1:
        count += 1

    return count

def main(num_list = [66,72,35,43]):
    """
    Main Function for testing/benchmarking multiprocessing and async
    """
    print(f' {"Start of Multiprocessing":-^50}')
    start_mp = timer()

    with multiprocessing.Pool(processes=len(num_list)) as pool:
        res = pool.map(cpu_heavy_task, iter(num_list))
    
    end_mp = timer()

    print(f'Total Multiprocessing Time: {end_mp - start_mp:.4f}s')
    print("\n")

    print(f' {"Start of Looping":-^50}')
    start_looping = timer()

    for n in num_list:
        cpu_heavy_task(n)

    print('Ended Heavy Task')
    end_looping = timer()
    print(f'Total Loop Time: {end_looping - start_looping:.4f}s')


if __name__ == "__main__":
    main(num_list = [499,499,499,499,499]) # [66,72,35,43,66,23,63,77,52,11,43,9,36,27])
