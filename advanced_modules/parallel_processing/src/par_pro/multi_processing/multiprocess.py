from concurrent.futures import ProcessPoolExecutor  # Tool to manage multiple worker processes
from typing import Callable, Iterable, Any, List     # Type hints to clarify input/output types
from multiprocessing import cpu_count               # Detects how many CPU cores are available


def parallel_map(
    fn: Callable[[Any], Any],         # Function to apply to each item in the data list
    data: Iterable[Any],              # List of inputs to process in parallel
    processes: int = None             # Number of parallel processes to use (default: all cores)
) -> List[Any]:
    """
    A simplified parallel map function using ProcessPoolExecutor.
    Runs the given function `fn` on each item in `data` using multiple processes.

    Returns a list of results in the same order as input.
    """

    # If user didn't specify number of processes, use all available CPU cores
    if processes is None:
        processes = cpu_count()

    # Create a pool of worker processes
    with ProcessPoolExecutor(max_workers=processes) as executor:
        # Use executor.map to apply the function to all items in parallel
        results = executor.map(fn, data)

        # Convert the map result (which is an iterator) to a list
        return list(results)
