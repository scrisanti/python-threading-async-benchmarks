# Threading and Multiprocessing Benchmarks

Exploring who to get around the GIL for CPU intensive tasks.

## CPU Heavy Functions

Finding factorials and prime factors are two of the most common CPU-heavy tasks so they are used here.

With the inputs `main(num_list = [499,499,499,499,499]` inside of main-mp.py the performance improvements are signifigant:

# Benchmarks

Multiprocessing:
    Finds the prime factors five consecuitive times:
    - Input Digit: $499 := 499^11 + 499 = 477645842414670666895611255998$
    
    Then compute factorial of $499^2$ and count the number of digits five times

    Total Time: 71.7277s

For Loop: 232.16s 

Hardware: Macbook Air M1, 8 cores, 8GB RAM