import threading
import time

def cpu_heavy_task(n: int) -> float:
    number = 2**n + n
    start_time = time.time()
    count_pf = count_prime_factors(number)
    end_time = time.time()
    print(f'Task Time: {end_time - start_time:.4f}s - {number} has {count_pf} prime factors')


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

def main(num_list = [66,72,35]):
    """
    Main Function for testing/benchmarking multithreading and async
    """
    print(f' {"Start of Threading":-^50}')
    start_threading = time.time()
    thread_list = []
    for n in num_list:
        t = threading.Thread(target=cpu_heavy_task, args=(n,))
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()
    end_threading = time.time()
    print(f'Total Threading Time: {end_threading - start_threading:.4f}s')
    print("\n")

    print(f' {"Start of Looping":-^50}')
    start_looping = time.time()
    for n in num_list:
        cpu_heavy_task(n)
    end_looping = time.time()
    print(f'Total Loop Time: {end_looping - start_looping:.4f}s')


if __name__ == "__main__":
    main(num_list = [66,72,35])
