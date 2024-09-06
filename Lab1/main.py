import time
from multiprocessing import Process, current_process
from threading import Thread, current_thread

# Function to compute sum of squares
def sum_of_squares(n):
    return sum(i * i for i in range(n))

# Function for processing with multiprocessing
def sum_of_squares_process(n):
    print(f"Process {current_process().name} is running...")
    # TODO: Implement the logic to compute sum of squares using processes

def compute_in_processes(n, num_processes):
    # TODO: Create multiple processes to perform the task
    pass

# Function for threading
def sum_of_squares_threaded(n):
    print(f"Thread {current_thread().name} is running...")
    # TODO: Implement the logic to compute sum of squares using threads

def compute_in_threads(n, num_threads):
    # TODO: Create multiple threads to perform the task
    pass

# Function for async I/O simulation (optional for advanced students)
async def async_sum_of_squares(n):
    # TODO: Implement the logic to compute sum of squares asynchronously
    pass

def main():
    n = 10**6

    # Sequential Execution
    start_time = time.time()
    result = sum_of_squares(n)
    print(f"Sequential Result: {result}")
    print(f"Time taken (sequential): {time.time() - start_time:.2f} seconds\n")

    # Parallel Execution with Processes
    num_processes = 4
    start_time = time.time()
    compute_in_processes(n, num_processes)
    print(f"Time taken with processes: {time.time() - start_time:.2f} seconds\n")

    # Parallel Execution with Threads
    num_threads = 4
    start_time = time.time()
    compute_in_threads(n, num_threads)
    print(f"Time taken with threads: {time.time() - start_time:.2f} seconds\n")

    # Advanced Concurrency with Asyncio (optional)
    # Uncomment below to use asyncio if needed
    # import asyncio
    # start_time = time.time()
    # asyncio.run(async_sum_of_squares(n))
    # print(f"Time taken with asyncio: {time.time() - start_time:.2f} seconds\n")

if __name__ == "__main__":
    main()
