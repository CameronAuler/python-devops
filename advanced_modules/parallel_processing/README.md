# Overview
Python provides two primary mechanisms for parallel and concurrent execution: multiprocessing and threading, each suited for different types of workloads. Multiprocessing is ideal for CPU-bound tasks—operations that require heavy computation like data processing, numerical simulations, or machine learning inference—by spawning multiple independent processes that bypass the Global Interpreter Lock (GIL) and fully utilize multiple CPU cores. In contrast, threading is best suited for I/O-bound tasks—operations that spend time waiting on external resources such as file systems, APIs, or databases—by running multiple threads within the same process to overlap these waiting periods and improve throughput.

# Multiprocessing
A production-grade Python utility for executing tasks in parallel using the `multiprocessing` module via `concurrent.futures.ProcessPoolExecutor`. This utility is designed for **CPU-bound** workloads where Python’s Global Interpreter Lock (GIL) becomes a bottleneck.

This module provides a configurable `parallel_map()` function that allows you to distribute work across multiple processes, with support for synchronous and asynchronous execution, error handling, and progress tracking.

## Overview

Python’s Global Interpreter Lock (GIL) prevents multiple native threads from executing Python bytecode simultaneously. While this simplifies memory management, it limits the ability of Python threads to take full advantage of multiple CPU cores for computationally intensive work.

The `multiprocessing` module solves this by spawning **independent system-level processes**—each with its own Python interpreter and memory space. This enables **true parallel execution** on multi-core CPUs. 

Use this utility when you need to accelerate workloads that are compute-heavy, such as:

- Data transformations across large datasets
- Image or video frame processing
- Parallelizing ML model inference across batches
- Mathematical simulations or scoring functions
- NLP pre-processing at scale (e.g., tokenization, cleaning)

## Function Signature

```python
def parallel_map(
    fn: Callable[[Any], Any],
    data: Iterable[Any],
    processes: Optional[int] = None,
    chunk_size: int = 10,
    async_mode: bool = False,
    show_progress: bool = False,
    handle_errors: bool = False
) -> List[Any]
```

## Parameters

| Name            | Type               | Description |
|-----------------|--------------------|-------------|
| `fn`            | `Callable`         | Function to apply to each item in `data`. |
| `data`          | `Iterable[Any]`    | Input data over which `fn` will be mapped. |
| `processes`     | `Optional[int]`    | Number of worker processes. Defaults to `multiprocessing.cpu_count()`. |
| `chunk_size`    | `int`              | Batch size passed to each process in synchronous mode. |
| `async_mode`    | `bool`             | If `True`, tasks are submitted and collected asynchronously using `as_completed()`. |
| `show_progress` | `bool`             | If `True`, a `tqdm` progress bar is shown. |
| `handle_errors` | `bool`             | If `True`, errors are logged and skipped individually. If `False`, the first error will raise and halt execution. |

## Installation

If using the `show_progress=True` option, install the optional `tqdm` dependency:

```bash
poetry add tqdm
```

## How It Works

The `parallel_map` function wraps Python’s `ProcessPoolExecutor` to distribute tasks across multiple processes, leveraging true parallelism.

### Architecture:

- **Process Pool**: A pool of worker processes is created (`max_workers=N`). Each process runs independently with its own interpreter and memory space.
- **Task Submission**:
  - In **synchronous mode**, tasks are batched and distributed using `executor.map()`. Results are returned in order.
  - In **asynchronous mode**, each task is submitted individually via `executor.submit()`. Results are collected using `as_completed()`, allowing you to track which tasks complete first.
- **Chunking**: In sync mode, `chunk_size` controls how many items are sent to each worker at a time. This can help reduce IPC (inter-process communication) overhead.
- **Error Handling**:
  - If `handle_errors=True`, any exceptions are caught and logged per-task.
  - If `handle_errors=False`, the first exception raised will halt execution.
- **Progress Bar**: If `show_progress=True`, results are tracked visually via `tqdm`.

### Why Use Multiprocessing?

Multiprocessing sidesteps the GIL by using OS-level processes, making it ideal for CPU-heavy workloads. It avoids context-switching costs inherent in threading and unlocks all available CPU cores for concurrent execution.

## When to Use Multiprocessing

Multiprocessing is most effective when each task involves **significant computation** or **heavy CPU-bound operations**.

### Strong Candidates:
- Expensive mathematical computations
- Batch processing large files (e.g., PDFs, images)
- Generating embeddings or tokenizing large text corpora
- Batch inference using ML models
- Processing large NumPy/Pandas datasets

### Weak Candidates (better alternatives):
- **I/O-bound work**: Use threading or asyncio for operations like:
  - File I/O
  - Database queries
  - Network/API requests
- **Low-latency or interactive use cases**: Not suitable due to process startup overhead.
- **Small and fast tasks**: Multiprocessing overhead may outweigh performance gains.

## Notes and Limitations

- **Pickling requirement**: Functions and data must be picklable because they are serialized and passed between processes. Avoid:
  - Lambdas
  - Closures (functions defined inside other functions)
  - Open file handles or sockets
- **Startup overhead**: Each process has non-trivial startup time. It’s best to batch tasks or use a reasonable `chunk_size` to amortize this cost.
- **Memory usage**: Each process is independent and maintains its own memory. Large datasets may increase total RAM consumption.
- **Cross-platform quirks**: On Windows, you must protect the multiprocessing call with `if __name__ == "__main__"` to avoid recursive process spawning.
- **No shared state**: Unlike threads, processes do not share memory by default. You must use multiprocessing primitives like `Queue` or `Manager` to coordinate across workers if needed.
- **Not suitable for real-time**: Multiprocessing is optimized for throughput, not latency. For sub-50ms use cases, consider using ONNX Runtime or optimized C/C++ extensions.



# Threading
A flexible and efficient Python utility for running I/O-bound tasks concurrently using `concurrent.futures.ThreadPoolExecutor`. This threading module provides a `threaded_map()` function that is ideal for workloads that spend time waiting on external resources such as file systems, network responses, or databases.

It supports both synchronous and asynchronous execution patterns, optional per-task error handling, and progress tracking using `tqdm`.

## Overview

Python’s threading model does not achieve true parallelism for CPU-bound tasks due to the Global Interpreter Lock (GIL). However, it is extremely effective for **I/O-bound workloads**, where threads spend time waiting on external operations (network, disk, etc.).

By overlapping wait times using threads, the program can execute many tasks “in parallel” from the perspective of I/O throughput, significantly improving performance without spawning multiple processes.

This utility is designed for tasks such as:

- Web scraping and concurrent API requests
- File or disk I/O
- Log ingestion and parsing
- Database read/write operations
- Lightweight async-safe background tasks

## Function Signature

```python
def threaded_map(
    fn: Callable[[Any], Any],
    data: Iterable[Any],
    max_workers: Optional[int] = None,
    async_mode: bool = False,
    show_progress: bool = False,
    handle_errors: bool = False
) -> List[Any]
```

## Parameters

| Name            | Type               | Description |
|-----------------|--------------------|-------------|
| `fn`            | `Callable`         | Function to apply to each item in `data`. |
| `data`          | `Iterable[Any]`    | Input data over which `fn` will be mapped. |
| `max_workers`   | `Optional[int]`    | Number of threads to use. Defaults to a reasonable system-dependent value. |
| `async_mode`    | `bool`             | If `True`, tasks are submitted and collected asynchronously using `as_completed()`. |
| `show_progress` | `bool`             | If `True`, a `tqdm` progress bar is shown. |
| `handle_errors` | `bool`             | If `True`, errors are logged and skipped individually. If `False`, the first error will raise and halt execution. |

---

## Installation

If using the `show_progress=True` option, install the optional `tqdm` dependency:

```bash
poetry add tqdm
```

## How It Works

The `threaded_map` function builds on Python’s `ThreadPoolExecutor`, which manages a pool of native threads that share the same memory space and Python interpreter.

### Architecture:

- **Thread Pool**: A pool of threads is initialized (`max_workers=N`). These threads execute Python functions concurrently, though only one thread executes Python bytecode at a time due to the GIL.
- **I/O Parallelism**: While one thread is waiting (e.g. for a network response), other threads can execute. This is particularly effective for tasks that are I/O-bound and frequently block.
- **Synchronous vs Asynchronous**:
  - In **synchronous mode**, results are collected in input order using `executor.map()`.
  - In **asynchronous mode**, tasks are submitted with `executor.submit()` and collected in order of completion using `as_completed()`.
- **Progress Bar**: If `show_progress=True`, a `tqdm` progress bar wraps the completion iterator.
- **Error Handling**:
  - When `handle_errors=True`, each failed task is logged and skipped.
  - If `False`, the first raised exception will terminate the entire run.

## When to Use Threading

Threading is ideal for tasks that spend time **waiting on I/O** rather than executing CPU-heavy code.

### Strong Candidates:
- Concurrent API calls (e.g. using `requests`, `httpx`)
- File read/write operations across many files
- Logging pipelines or event processing
- Polling remote services
- Lightweight function calls that rely on external systems

### Weak Candidates (better alternatives):
- **CPU-bound computation**: Use multiprocessing instead
- **Heavy ML inference or data transformations**: Use multiprocessing or specialized runtime
- **Tasks requiring shared state between threads**: Consider using locks or thread-safe data structures (e.g., `queue.Queue`)

## Notes and Limitations

- **No true CPU parallelism**: Threads share the same memory and interpreter; only one runs Python bytecode at a time.
- **Best for I/O-bound workloads**: Threading increases throughput by overlapping waiting periods.
- **Thread-safe data**: Python data structures like lists and dictionaries are not thread-safe by default. Avoid shared state or use `threading.Lock` if needed.
- **Memory-efficient**: Threads share memory, so spawning many threads is cheaper than spawning many processes.
- **No pickling required**: Unlike multiprocessing, threading allows any callable (including lambdas and closures) since memory is shared.
