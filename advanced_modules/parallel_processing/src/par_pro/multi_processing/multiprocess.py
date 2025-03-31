from concurrent.futures import ProcessPoolExecutor, as_completed  # High-level multiprocessing interface
from typing import Callable, Iterable, Any, List, Optional        # Type hints for better clarity and editor support
from multiprocessing import cpu_count                             # Used to get the number of available CPU cores
from tqdm import tqdm                                             # Progress bar for iterables


def parallel_map(
    fn: Callable[[Any], Any],          # Function to apply to each element of the data
    data: Iterable[Any],               # Input data as an iterable
    processes: Optional[int] = None,   # Number of processes to use (defaults to all CPU cores)
    chunk_size: int = 10,              # Size of chunks passed to each process (for sync mode only)
    async_mode: bool = False,          # Flag to enable asynchronous processing
    show_progress: bool = False,       # Flag to show progress bar
    handle_errors: bool = False        # Flag to handle task-level errors without crashing
) -> List[Any]:
    """
    A robust, reusable parallel processing utility using ProcessPoolExecutor.
    Applies `fn` to each item in `data` using multiprocessing with optional async, error handling, and progress bar.
    """
    if processes is None:
        processes = cpu_count()  # Use all available CPU cores if not specified

    results = []  # List to collect results

    # Create a pool of worker processes
    with ProcessPoolExecutor(max_workers=processes) as executor:
        if async_mode:
            # Submit all tasks to the pool and keep a mapping of future -> item
            futures = {executor.submit(fn, item): item for item in data}

            # Create a progress iterator if enabled, otherwise just use as_completed
            progress = tqdm(as_completed(futures), total=len(futures)) if show_progress else as_completed(futures)

            # Iterate over each completed future
            for future in progress:
                try:
                    # Append the result to the results list
                    results.append(future.result())
                except Exception as e:
                    if handle_errors:
                        # Log the error and append None if error handling is enabled
                        print(f"[ERROR] Failed to process {futures[future]}: {e}")
                        results.append(None)
                    else:
                        # Raise the error if error handling is disabled
                        raise
        else:
            # Use executor.map for synchronous mapping (applies chunking)
            iterator = executor.map(fn, data, chunksize=chunk_size)

            # Wrap the iterator in tqdm if progress bar is enabled
            if show_progress:
                iterator = tqdm(iterator, total=len(data))

            # Convert the iterator to a list to get all results
            results = list(iterator)

    return results  # Return all collected results
