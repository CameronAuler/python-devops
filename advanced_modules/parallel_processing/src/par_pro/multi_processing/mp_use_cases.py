import time
import random
import math
from typing import List, Tuple
from multiprocessing import current_process, cpu_count  # To show which process runs what
from par_pro import parallel_map


# CPU-intensive task: Factor a large semi-prime number
def factor_semi_prime(n: int) -> Tuple[int, int]:
    """
    Factor a semi-prime number — a product of two large prime numbers — into its original prime components.
    This brute-force factorization simulates a cryptographic-style CPU-intensive task, commonly found in number theory and RSA encryption.
    Logs the process ID to demonstrate how the task is distributed across multiple processes.
    """
    proc = current_process().name  # Get current process name (e.g., 'ForkProcess-1')
    print(f"[{proc}] Starting factorization of {n}")

    # Brute-force factorization
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return (i, n // i)  # Return both factors

    return (n, 1)  # Return fallback if no factors found


# Utility function to time execution in ms and return the elapsed time
def time_it(label: str, func, *args, **kwargs) -> Tuple[float, any]:
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    elapsed_ms = (end - start) * 1000
    print(f"{label} took {elapsed_ms:.2f} ms")
    return elapsed_ms, result


# Main use case: sequential vs multiprocessing factorization
def run_prime_computation_use_case():
    print("\n=== SEMI-PRIME FACTORIZATION USE CASE ===")

    # Generate a list of semi-primes by multiplying two random primes
    primes = [
        15485867, 15485917, 15485933, 15485941, 15485959,
        15485977, 15485981, 15485987, 15485989, 15486011
    ]
    data = [random.choice(primes) * random.choice(primes) for _ in range(30)]

    print(f"Using {cpu_count()} CPU cores")

    # --- SEQUENTIAL EXECUTION ---
    def run_sequential():
        results = []
        for num in data:
            results.append(factor_semi_prime(num))
        return results

    sequential_time, _ = time_it("Sequential processing", run_sequential)

    # --- MULTIPROCESSING EXECUTION ---
    parallel_time, _ = time_it(
        "Multiprocessing (parallel_map)",
        parallel_map,
        factor_semi_prime,
        data,
        processes=cpu_count(),
        chunk_size=5,
        async_mode=False,
        show_progress=False,
        handle_errors=True
    )

    # --- TIME COMPARISON SUMMARY ---
    print("\n=== EXECUTION TIME COMPARISON ===")
    print(f"Sequential:       {sequential_time:.2f} ms")
    print(f"Multiprocessing:  {parallel_time:.2f} ms")
    improvement = sequential_time / parallel_time if parallel_time > 0 else 0
    print(f"Speedup:          {improvement:.2f}x faster\n")


# Run the test directly
if __name__ == "__main__":
    run_prime_computation_use_case()
