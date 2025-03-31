from concurrent.futures import ThreadPoolExecutor, as_completed  # Threading-based parallelism tools
from typing import Callable, Iterable, Any, List, Optional        # Type hinting for safety and clarity
from tqdm import tqdm                                             # Optional progress bar for async mode


def threaded_map(
    fn: Callable[[Any], Any],           # Function to apply to each element in the data
    data: Iterable[Any],                # Iterable of input data
    max_workers: Optional[int] = None,  # Number of threads to use (defaults to optimal thread count)
    async_mode: bool = False,           # Flag to process tasks asynchronously
    show_progress: bool = False,        # Flag to show tqdm progress bar
    handle_errors: bool = False         # Handle per-task exceptions gracefully if True
) -> List[Any]:
    """
    Threaded parallel map utility using ThreadPoolExecutor.
    Designed for I/O-bound workloads (e.g., API calls, file I/O).

    Args:
        fn: Function to apply to each item.
        data: Iterable input.
        max_workers: Max number of threads (defaults to system optimized).
        async_mode: Use asynchronous (as_completed) execution.
        show_progress: Whether to show progress using tqdm.
        handle_errors: Catch and log errors for individual tasks.

    Returns:
        List of results in the order they are completed.
    """
    results = []  # Output list to collect results

    # Initialize thread pool executor
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        if async_mode:
            # Submit all tasks asynchronously and track future -> input mapping
            futures = {executor.submit(fn, item): item for item in data}

            # Create a progress iterator if enabled, else use standard as_completed
            progress = tqdm(as_completed(futures), total=len(futures)) if show_progress else as_completed(futures)

            # Iterate over tasks as they complete
            for future in progress:
                try:
                    # Append result of each completed future
                    results.append(future.result())
                except Exception as e:
                    if handle_errors:
                        # Log the error and insert None if handling is enabled
                        print(f"[ERROR] Failed to process {futures[future]}: {e}")
                        results.append(None)
                    else:
                        # Raise exception to crash early if not handling
                        raise
        else:
            # Synchronous mode: use map to preserve order
            iterator = executor.map(fn, data)

            # Wrap with tqdm if progress display is enabled
            if show_progress:
                iterator = tqdm(iterator, total=len(data))

            # Convert iterator to list and store results
            results = list(iterator)

    return results  # Return final list of results
