from concurrent.futures import ThreadPoolExecutor  # High-level threading interface
from typing import Callable, Iterable, Any, List    # Type hints for function inputs and outputs


def threaded_map(
    fn: Callable[[Any], Any],       # Function to apply to each item
    data: Iterable[Any],            # Input data list
    max_workers: int = None         # Number of threads (default: auto)
) -> List[Any]:
    """
    A simplified threaded map function using ThreadPoolExecutor.
    Applies the given function to each item in the data list using multiple threads.

    Designed for I/O-bound tasks such as API calls, web scraping, or file reads.

    Returns a list of results in the same order as the input.
    """

    # Create a thread pool with the given number of threads (or default)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Apply the function to each item using multiple threads
        results = executor.map(fn, data)

        # Convert the results (an iterator) into a list
        return list(results)
