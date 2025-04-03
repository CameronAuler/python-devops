import time
import random
from typing import List
import threading  # To show which thread is processing the task
from par_pro.threading.thread import threaded_map  # Threaded parallel utility


# I/O-bound simulated task: pretend to call an API with a delay
def simulated_api_call(delay: float) -> str:
    """
    Simulates an I/O-bound task (like a remote API call) by sleeping for a short duration.
    Logs the thread name to demonstrate how threading parallelizes I/O.
    """
    thread = threading.current_thread().name  # Get the current thread name
    print(f"[{thread}] Calling simulated API with {delay:.2f}s delay")
    time.sleep(delay)  # Simulate the delay (I/O wait)
    return f"Finished API call with {delay:.2f}s delay"


# Utility function to time execution in ms and return the result
def time_it(label: str, func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    elapsed = (end - start) * 1000  # Convert to milliseconds
    print(f"{label} took {elapsed:.2f} ms")
    return elapsed, result


# Main use case comparing sequential vs threaded API calls
def run_network_simulation_use_case():
    print("\n=== NETWORK SIMULATION USE CASE ===")

    # Simulate 30 API calls, each with a random I/O delay between 0.1s and 0.3s
    data = [random.uniform(0.1, 0.3) for _ in range(30)]

    # --- SEQUENTIAL EXECUTION ---
    def run_sequential():
        results = []
        for delay in data:
            results.append(simulated_api_call(delay))  # Run each call in sequence
        return results

    sequential_time, _ = time_it("Sequential processing", run_sequential)

    # --- THREADED EXECUTION ---
    threaded_time, _ = time_it(
    "Threaded processing (threaded_map)",
    threaded_map,
    simulated_api_call,
    data,
    max_workers=10
)


    # --- EXECUTION TIME SUMMARY ---
    print("\n=== EXECUTION TIME COMPARISON ===")
    print(f"Sequential:      {sequential_time:.2f} ms")
    print(f"Threaded:        {threaded_time:.2f} ms")
    speedup = sequential_time / threaded_time if threaded_time > 0 else 0
    print(f"Speedup:         {speedup:.2f}x faster\n")


# Script entry point
if __name__ == "__main__":
    run_network_simulation_use_case()
